#!/usr/bin/env python3
"""Generate a typed Python client from an OpenAPI 3.x JSON spec.

The generated code follows the same style as the hand-written clients in
``src/simplic_ox_agent/clients/``.

Usage
-----
    python scripts/generate_client.py --url URL --name NAME

Options
-------
    --url      OpenAPI JSON URL
    --name     Client module name, e.g. ``auth``, ``user-profile``
    --out-dir  Path to the ``clients/`` package root (auto-detected by default)
    --dry-run  Print generated code without writing files
    --force    Overwrite existing files without prompting

Examples
--------
    python scripts/generate_client.py \\
        --url https://oxs.simplic.io/auth-api/v1/swagger/v1/swagger.json \\
        --name auth

    python scripts/generate_client.py \\
        --url https://oxs.simplic.io/user-api/v1/swagger/v1/swagger.json \\
        --name user \\
        --dry-run
"""
from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


# ── text helpers ──────────────────────────────────────────────────────────────


def to_snake(s: str) -> str:
    """camelCase / PascalCase / kebab-case → snake_case."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.replace("-", "_").lower()


def to_pascal(s: str) -> str:
    """kebab-case / snake_case → PascalCase."""
    return "".join(w.capitalize() for w in re.split(r"[-_]", s) if w)


def safe_name(name: str) -> str:
    """Append ``_`` to names that clash with Python keywords (e.g. ``from_``)."""
    return f"{name}_" if keyword.iskeyword(name) else name


# ── OpenAPI type helpers ───────────────────────────────────────────────────────


def schema_name(ref: str) -> str:
    """Extract the bare schema name from a ``$ref`` path."""
    return ref.rsplit("/", 1)[-1]


def py_type(schema: dict[str, Any]) -> tuple[str, bool]:
    """Return ``(python_type_annotation, needs_uuid_import)``.

    Nullability (``| None``) is NOT applied here; callers handle it.
    """
    if not schema:
        return "object", False
    if "$ref" in schema:
        return schema_name(schema["$ref"]), False
    kind = schema.get("type", "object")
    fmt = schema.get("format", "")
    if kind == "string":
        return ("UUID", True) if fmt == "uuid" else ("str", False)
    if kind == "integer":
        return "int", False
    if kind == "number":
        return "float", False
    if kind == "boolean":
        return "bool", False
    if kind == "array":
        inner, u = py_type(schema.get("items") or {})
        return f"list[{inner}]", u
    if kind == "object":
        add = schema.get("additionalProperties")
        if add and isinstance(add, dict):
            inner, u = py_type(add)
            return f"dict[str, {inner}]", u
        return "dict[str, object]", False
    return "object", False


def pick_ref(content: dict[str, Any]) -> str | None:
    """Extract the schema ``$ref`` name from a request/response content dict."""
    for mime in ("application/json", "text/json", "text/plain"):
        s = content.get(mime, {}).get("schema", {})
        if "$ref" in s:
            return schema_name(s["$ref"])
    return None


def response_schema(op: dict[str, Any]) -> str | None:
    """Return the response body schema name for a 200/201 response, or None."""
    for status in ("200", "201"):
        content = op.get("responses", {}).get(status, {}).get("content", {})
        if content:
            return pick_ref(content)
    return None


def request_schema(op: dict[str, Any]) -> str | None:
    """Return the request body schema name, or None."""
    content = op.get("requestBody", {}).get("content", {})
    return pick_ref(content) if content else None


# ── method name derivation ────────────────────────────────────────────────────


def derive_method_name(http_verb: str, path: str) -> str:
    """Derive a Python method name from ``HTTP_VERB /some/path``."""
    _VERB_PREFIX = {
        "get": "get",
        "post": "create",
        "put": "update",
        "patch": "update",
        "delete": "delete",
    }
    _GET_VERBS = frozenset(("get", "list", "find", "search", "fetch"))

    all_segs = [s for s in path.split("/") if s and s.lower() != "internal"]
    if not all_segs:
        return http_verb

    controller = to_snake(all_segs[0])
    rest = all_segs[1:]
    # Separate plain action words from path-parameter placeholders ({...}).
    # Parameters appear in the function signature, not the method name.
    action_segs = [s for s in rest if not (s.startswith("{") and s.endswith("}"))]
    param_names = [s[1:-1] for s in rest if s.startswith("{") and s.endswith("}")]
    prefix = _VERB_PREFIX.get(http_verb, http_verb)

    if action_segs:
        name = "_".join(to_snake(s) for s in action_segs)
        # GET: add prefix only when action doesn't already start with a fetch verb
        if http_verb == "get" and not any(name.startswith(v) for v in _GET_VERBS):
            name = f"get_{name}"
        # Non-GET: keep action words as-is (e.g. login, calculate_toll)
    elif param_names:
        # No action words but path has params → qualify to avoid collision with
        # the no-param variant (GET /Resource vs GET /Resource/{id})
        param_suffix = "_".join(to_snake(p) for p in param_names)
        name = f"{prefix}_{controller}_by_{param_suffix}"
    else:
        # Plain resource path: GET /Resource, POST /Resource
        name = f"{prefix}_{controller}"

    return name


# ── model code builder ────────────────────────────────────────────────────────


def _enum_member_name(value: object) -> str:
    """Convert an enum value to a SCREAMING_SNAKE_CASE Python identifier."""
    s = to_snake(str(value)).upper()
    # Identifiers must not start with a digit
    if s and s[0].isdigit():
        s = f"VALUE_{s}"
    return s or "UNKNOWN"


def build_models(
    schemas: dict[str, Any],
    response_names: set[str],
) -> tuple[str, list[str]]:
    """Generate ``models.py`` source and return ``(source, exported_names)``."""
    exported: list[str] = []
    blocks: list[str] = []
    needs_uuid = False
    needs_enum = False  # StrEnum / IntEnum
    needs_datetime = False
    needs_date = False

    for cls_name, schema in schemas.items():
        if cls_name not in response_names:
            continue
        properties: dict[str, Any] = schema.get("properties") or {}
        required: set[str] = set(schema.get("required") or [])
        enum_values: list[Any] = schema.get("enum") or []

        # ── enum schema ───────────────────────────────────────────────────────
        if enum_values:
            needs_enum = True
            kind = schema.get("type", "string")
            base_cls = "IntEnum" if kind == "integer" else "StrEnum"
            members: list[str] = []
            seen_names: set[str] = set()
            for v in enum_values:
                if v is None:
                    continue
                name = _enum_member_name(v)
                # Deduplicate member names that map to the same identifier
                if name in seen_names:
                    name = f"{name}_{v}"
                    name = re.sub(r"[^A-Z0-9_]", "_", name.upper())
                seen_names.add(name)
                members.append(f'    {name} = {v!r}')
            block = [f"class {cls_name}({base_cls}):"] + (members or ["    pass"])
            blocks.append("\n".join(block))
            exported.append(cls_name)
            continue

        # ── skip non-object, non-enum schemas (aliases, raw types, etc.) ─────
        if not properties and schema.get("type") != "object":
            continue

        # ── object / BaseModel schema ─────────────────────────────────────────
        fields: list[str] = []
        has_alias = False

        # Required fields first so Pydantic sees them before optionals
        ordered = [(k, v) for k, v in properties.items() if k in required] + [
            (k, v) for k, v in properties.items() if k not in required
        ]

        for json_key, prop in ordered:
            snake = safe_name(to_snake(json_key))
            # An alias is needed when the Python name differs from the JSON key
            # (camelCase mapping) OR when safe_name had to rename a keyword.
            alias = snake != json_key
            if alias:
                has_alias = True
            base, u = py_type(prop)
            if u:
                needs_uuid = True
            # Map date-time / date string formats to proper Python types in
            # model fields; Pydantic v2 handles the ISO 8601 parsing.
            if prop.get("type") == "string":
                fmt = prop.get("format", "")
                if fmt == "date-time":
                    base = "datetime"
                    needs_datetime = True
                elif fmt == "date":
                    base = "date"
                    needs_date = True
            is_req = json_key in required
            nullable = prop.get("nullable", False)
            ann = f"{base} | None" if (not is_req or nullable) else base

            if alias:
                default = "" if is_req else "None, "
                fields.append(
                    f'    {snake}: {ann} = Field({default}alias="{json_key}")'
                )
            else:
                suffix = "" if is_req else " = None"
                fields.append(f"    {snake}: {ann}{suffix}")

        block = [f"class {cls_name}(BaseModel):"]
        if has_alias:
            block += ["    model_config = ConfigDict(populate_by_name=True)", ""]
        block += fields if fields else ["    pass"]
        blocks.append("\n".join(block))
        exported.append(cls_name)

    header = [
        '"""Pydantic models generated from the OpenAPI spec."""',
        "",
        "from __future__ import annotations",
        "",
    ]
    if needs_uuid:
        header += ["from uuid import UUID", ""]
    if needs_date or needs_datetime:
        parts = ", ".join(filter(None, [
            "date" if needs_date else "",
            "datetime" if needs_datetime else "",
        ]))
        header += [f"from datetime import {parts}", ""]
    if needs_enum:
        header += ["from enum import IntEnum, StrEnum", ""]
    header += ["from pydantic import BaseModel, ConfigDict, Field", "", ""]

    src = "\n".join(header) + "\n\n".join(blocks) + "\n"
    return src, exported


# ── per-method code builder ───────────────────────────────────────────────────


def render_method(
    verb: str,
    path: str,
    name: str,
    op: dict[str, Any],
    schemas: dict[str, Any],
    response_names: set[str],
) -> tuple[str, list[str], bool]:
    """Return ``(method_source, used_return_types, needs_uuid)``.

    ``method_source`` is already indented for a class body (4 spaces).
    """
    lines: list[str] = []
    used_types: list[str] = []
    needs_uuid = False

    docstring = op.get("summary", "").strip()
    params = op.get("parameters") or []
    path_params = [p for p in params if p.get("in") == "path"]
    query_params = [p for p in params if p.get("in") == "query"]

    # ── request body fields ───────────────────────────────────────────────────
    # (py_name, json_key, base_type, is_uuid, is_required)
    body_fields: list[tuple[str, str, str, bool, bool]] = []
    req_schema = request_schema(op)
    if req_schema and req_schema in schemas:
        s = schemas[req_schema]
        props = s.get("properties") or {}
        req_set: set[str] = set(s.get("required") or [])
        ordered = [(k, v) for k, v in props.items() if k in req_set] + [
            (k, v) for k, v in props.items() if k not in req_set
        ]
        for jk, prop in ordered:
            base, u = py_type(prop)
            if u:
                needs_uuid = True
            # PATCH semantics: every field is optional; only set fields are sent
            is_req = (jk in req_set) and verb != "patch"
            body_fields.append((safe_name(to_snake(jk)), jk, base, u, is_req))

    # ── return type ───────────────────────────────────────────────────────────
    resp = response_schema(op)
    ret_type = resp if (resp and resp in response_names) else "None"
    if ret_type != "None":
        used_types.append(ret_type)

    # ── signature parts ───────────────────────────────────────────────────────
    sig: list[str] = ["self"]

    for p in path_params:
        pn = safe_name(to_snake(p["name"]))
        pt, u = py_type(p.get("schema") or {})
        if u:
            needs_uuid = True
        sig.append(f"{pn}: {pt}")

    for py_name, _, base, u, is_req in body_fields:
        if u:
            needs_uuid = True
        sig.append(f"{py_name}: {base}" if is_req else f"{py_name}: {base} | None = None")

    for p in query_params:
        pn = safe_name(to_snake(p["name"]))
        pt, u = py_type(p.get("schema") or {})
        if u:
            needs_uuid = True
        req = p.get("required", False)
        sig.append(f"{pn}: {pt}" if req else f"{pn}: {pt} | None = None")

    # ── URL expression (f-string literal for the generated file) ─────────────
    # Substitute {pathParam} → {snake_param} in the path first
    call_path = path
    for p in path_params:
        call_path = call_path.replace(
            f"{{{p['name']}}}", f"{{{safe_name(to_snake(p['name']))}}}"
        )
    # Build the f-string: {{_PREFIX}} becomes {_PREFIX} in the output file
    url_expr = f'f"{{_PREFIX}}{call_path}"'

    # ── method header ─────────────────────────────────────────────────────────
    lines += [
        f"    async def {name}(",
        *[f"        {p}," for p in sig],
        f"    ) -> {ret_type}:",
    ]
    if docstring:
        lines.append(f'        """{docstring}"""')

    # ── method body ───────────────────────────────────────────────────────────
    if body_fields:
        all_required = all(bf[4] for bf in body_fields) and verb != "patch"
        if all_required:
            # Simple inline JSON dict
            items = ", ".join(
                f'"{jk}": str({py})' if is_uuid else f'"{jk}": {py}'
                for py, jk, _, is_uuid, _ in body_fields
            )
            lines += [
                f"        response = await self._http.{verb}(",
                f"            {url_expr},",
                f"            json={{{items}}},",
                "        )",
            ]
        else:
            # Build payload dict; omit optional fields when None
            lines.append("        _body: dict[str, object] = {")
            for py, jk, _, is_uuid, is_req in body_fields:
                if is_req:
                    val = f"str({py})" if is_uuid else py
                    lines.append(f'            "{jk}": {val},')
            lines.append("        }")
            for py, jk, _, is_uuid, is_req in body_fields:
                if not is_req:
                    val = f"str({py})" if is_uuid else py
                    lines += [
                        f"        if {py} is not None:",
                        f'            _body["{jk}"] = {val}',
                    ]
            lines += [
                f"        response = await self._http.{verb}(",
                f"            {url_expr},",
                "            json=_body,",
                "        )",
            ]
    elif query_params:
        req_qp = [p for p in query_params if p.get("required", False)]
        opt_qp = [p for p in query_params if not p.get("required", False)]
        if not opt_qp:
            # Simple inline params dict
            items = ", ".join(
                f'"{p["name"]}": str({safe_name(to_snake(p["name"]))})'  
                if py_type(p.get("schema") or {})[1]
                else f'"{p["name"]}": {safe_name(to_snake(p["name"]))}'
                for p in query_params
            )
            lines += [
                f"        response = await self._http.{verb}(",
                f"            {url_expr},",
                f"            params={{{items}}},",
                "        )",
            ]
        else:
            # Conditional params dict
            lines.append("        _params: dict[str, object] = {}")
            for p in req_qp:
                pn = safe_name(to_snake(p["name"]))
                _, is_uuid = py_type(p.get("schema") or {})
                val = f"str({pn})" if is_uuid else pn
                lines.append(f'        _params["{p["name"]}"] = {val}')
            for p in opt_qp:
                pn = safe_name(to_snake(p["name"]))
                _, is_uuid = py_type(p.get("schema") or {})
                val = f"str({pn})" if is_uuid else pn
                lines += [
                    f"        if {pn} is not None:",
                    f'            _params["{p["name"]}"] = {val}',
                ]
            lines += [
                f"        response = await self._http.{verb}(",
                f"            {url_expr},",
                "            params=_params,",
                "        )",
            ]
    else:
        lines += [
            f"        response = await self._http.{verb}(",
            f"            {url_expr},",
            "        )",
        ]

    lines.append("        response.raise_for_status()")
    if ret_type != "None":
        lines.append(f"        return {ret_type}.model_validate(response.json())")

    return "\n".join(lines), used_types, needs_uuid


# ── client code builder ───────────────────────────────────────────────────────


def build_client(
    cls_name: str,
    prefix: str,
    operations: list[dict[str, Any]],
    schemas: dict[str, Any],
    response_names: set[str],
) -> str:
    """Generate ``client.py`` source."""
    method_blocks: list[str] = []
    all_ret_types: set[str] = set()
    needs_uuid = False

    for op in operations:
        src, used, u = render_method(
            op["verb"], op["path"], op["name"],
            op["operation"], schemas, response_names,
        )
        method_blocks.append(src)
        all_ret_types.update(used)
        if u:
            needs_uuid = True

    imports = [
        '"""Typed client generated from the OpenAPI spec."""',
        "",
        "from __future__ import annotations",
        "",
    ]
    if needs_uuid:
        imports += ["from uuid import UUID", ""]
    imports += ["from ...core.http_client import SimplicOxHttpClient"]
    if all_ret_types:
        imports += [
            "from .models import (",
            *[f"    {t}," for t in sorted(all_ret_types)],
            ")",
        ]
    imports += ["", f'_PREFIX = "{prefix}"', "", ""]

    class_header = [
        f"class {cls_name}:",
        f'    """Typed client for ``{prefix}``.',
        "",
        "    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`",
        "    and exposes one async method per endpoint.  Responses are parsed into",
        "    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.",
        "",
        "    Example::",
        "",
        f"        from simplic_ox_agent.clients.{cls_name.lower().removesuffix('client')} import {cls_name}",
        "",
        f"        client = {cls_name}(context.http)",
        '    """',
        "",
        "    def __init__(self, http: SimplicOxHttpClient) -> None:",
        "        self._http = http",
        "",
    ]

    return (
        "\n".join(imports)
        + "\n"
        + "\n".join(class_header)
        + "\n\n".join(method_blocks)
        + "\n"
    )


# ── __init__.py builder ───────────────────────────────────────────────────────


def build_init(cls_name: str, exported_models: list[str]) -> str:
    """Generate ``__init__.py`` source."""
    lines = [f"from .client import {cls_name}"]
    if exported_models:
        lines += [
            "from .models import (",
            *[f"    {m}," for m in sorted(exported_models)],
            ")",
        ]
    lines += [
        "",
        "__all__ = [",
        f'    "{cls_name}",',
        *[f'    "{m}",' for m in sorted(exported_models)],
        "]",
        "",
    ]
    return "\n".join(lines)


def collect_refs(schema: dict[str, Any], schemas: dict[str, Any], seen: set[str]) -> None:
    """Recursively collect all ``$ref`` schema names reachable from *schema*."""
    if not schema:
        return
    if "$ref" in schema:
        name = schema_name(schema["$ref"])
        if name not in seen and name in schemas:
            seen.add(name)
            collect_refs(schemas[name], schemas, seen)
        return
    # object properties
    for prop in (schema.get("properties") or {}).values():
        collect_refs(prop, schemas, seen)
    # array items
    if "items" in schema:
        collect_refs(schema["items"], schemas, seen)
    # additionalProperties
    add = schema.get("additionalProperties")
    if isinstance(add, dict):
        collect_refs(add, schemas, seen)
    # allOf / anyOf / oneOf
    for key in ("allOf", "anyOf", "oneOf"):
        for sub in schema.get(key) or []:
            collect_refs(sub, schemas, seen)



def fetch_spec(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(url) as r:  # noqa: S310 — URL comes from CLI
        return json.loads(r.read())


def find_clients_dir(script_file: Path) -> Path:
    """Walk up from the script location to find ``src/*/clients/``."""
    for ancestor in [script_file.resolve().parent, *script_file.resolve().parents]:
        if (ancestor / "pyproject.toml").exists():
            hits = list(ancestor.glob("src/*/clients"))
            if hits:
                return hits[0]
            break
    raise FileNotFoundError(
        "Could not auto-detect the clients/ package directory.  "
        "Pass --out-dir to specify it explicitly."
    )


def patch_clients_init(clients_root: Path, module: str, cls_name: str) -> None:
    """Add the new client import to ``clients/__init__.py``."""
    init_path = clients_root / "__init__.py"
    if not init_path.exists():
        return
    text = init_path.read_text(encoding="utf-8")
    import_line = f"from .{module} import {cls_name}"
    if import_line in text:
        return  # already present

    # Insert import; add before __all__ when present, else append
    if "__all__" in text:
        text = text.replace("\n__all__", f"\n{import_line}\n\n__all__", 1)
    else:
        text = text.rstrip("\n") + f"\n{import_line}\n"

    # Add to __all__ list
    text = re.sub(
        r'(__all__\s*=\s*\[)(.*?)(\])',
        lambda m: m.group(1) + m.group(2) + f'    "{cls_name}",\n' + m.group(3),
        text,
        flags=re.DOTALL,
    )
    init_path.write_text(text, encoding="utf-8")
    print(f"  updated {init_path}")


# ── main ──────────────────────────────────────────────────────────────────────


def find_project_root(script_file: Path) -> Path:
    """Walk up from *script_file* until we find a directory with pyproject.toml."""
    for p in [script_file.resolve().parent, *script_file.resolve().parents]:
        if (p / "pyproject.toml").exists():
            return p
    return script_file.resolve().parent


def generate_one(
    url: str,
    name: str,
    clients_root: Path,
    *,
    dry_run: bool,
    force: bool,
) -> None:
    """Fetch *url*, generate client *name*, write into *clients_root*."""
    out_dir = clients_root / name

    print(f"Fetching {url} …", file=sys.stderr)
    spec = fetch_spec(url)

    servers = spec.get("servers") or []
    prefix = urlparse(servers[0]["url"]).path.strip("/") if servers else name

    schemas: dict[str, Any] = (spec.get("components") or {}).get("schemas") or {}
    paths: dict[str, Any] = spec.get("paths") or {}

    response_names: set[str] = set()
    operations: list[dict[str, Any]] = []

    for path, path_item in paths.items():
        for verb in ("get", "post", "put", "patch", "delete"):
            op = path_item.get(verb)
            if not op:
                continue
            rn = response_schema(op)
            if rn:
                response_names.add(rn)
            req = request_schema(op)
            if req:
                response_names.add(req)
            operations.append({
                "verb": verb,
                "path": path,
                "name": derive_method_name(verb, path),
                "operation": op,
            })

    expanded: set[str] = set()
    for root in list(response_names):
        if root in schemas:
            expanded.add(root)
            collect_refs(schemas[root], schemas, expanded)
    response_names = expanded

    name_count = Counter(op["name"] for op in operations)
    for op in operations:
        if name_count[op["name"]] > 1:
            ctrl = to_snake(
                next(s for s in op["path"].split("/") if s and s.lower() != "internal")
            )
            if not op["name"].startswith(ctrl + "_"):
                op["name"] = f"{ctrl}_{op['name']}"
    name_seq: dict[str, int] = {}
    for op in operations:
        n = op["name"]
        if n in name_seq:
            name_seq[n] += 1
            op["name"] = f"{n}_{name_seq[n]}"
        else:
            name_seq[n] = 0

    cls_name = f"{to_pascal(name)}Client"

    models_src, exported_models = build_models(schemas, response_names)
    client_src = build_client(cls_name, prefix, operations, schemas, response_names)
    init_src = build_init(cls_name, exported_models)

    files: dict[Path, str] = {
        out_dir / "models.py": models_src,
        out_dir / "client.py": client_src,
        out_dir / "__init__.py": init_src,
    }

    if dry_run:
        for file_path, src in files.items():
            sep = "=" * 68
            print(f"\n{sep}\n# {file_path}\n{sep}\n{src}")
        return

    existing = [p for p in files if p.exists()]
    if existing and not force:
        print("The following files already exist:", file=sys.stderr)
        for p in existing:
            print(f"  {p}", file=sys.stderr)
        answer = input("Overwrite? [y/N] ").strip().lower()
        if answer != "y":
            sys.exit("Aborted.")

    out_dir.mkdir(parents=True, exist_ok=True)
    for file_path, src in files.items():
        file_path.write_text(src, encoding="utf-8")
        print(f"  wrote {file_path}")

    patch_clients_init(clients_root, name, cls_name)

    module_path = (
        ".".join(clients_root.parts[clients_root.parts.index("src") + 1:])
        if "src" in clients_root.parts
        else f"clients.{name}"
    )
    print(f"\nDone.  Import with:")
    print(f"  from {module_path}.{name} import {cls_name}")


# ── main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate a typed Python client from an OpenAPI 3.x spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--url", metavar="URL",
                    help="OpenAPI JSON spec URL (single-client mode)")
    ap.add_argument("--name", metavar="NAME",
                    help="Client module name, e.g. 'auth' (single-client mode)")
    ap.add_argument("--all", action="store_true",
                    help="Generate all clients listed in the config file")
    ap.add_argument("--config", metavar="FILE",
                    help="Path to clients.json (default: <project-root>/clients.json)")
    ap.add_argument("--out-dir", metavar="DIR",
                    help="Path to the clients/ package root (auto-detected by default)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print generated code without writing files")
    ap.add_argument("--force", action="store_true",
                    help="Overwrite existing files without prompting")
    args = ap.parse_args()

    if not args.all and not (args.url and args.name):
        ap.error("Provide either --all or both --url and --name.")

    clients_root = (
        Path(args.out_dir).resolve()
        if args.out_dir
        else find_clients_dir(Path(__file__))
    )

    if args.all:
        config_path = (
            Path(args.config).resolve()
            if args.config
            else find_project_root(Path(__file__)) / "clients.json"
        )
        if not config_path.exists():
            sys.exit(f"Config file not found: {config_path}")
        config = json.loads(config_path.read_text(encoding="utf-8"))
        entries: list[dict[str, str]] = config.get("clients") or []
        if not entries:
            sys.exit("No clients defined in config file.")
        for entry in entries:
            print(f"\n── {entry['name']} ──", file=sys.stderr)
            generate_one(
                entry["url"],
                entry["name"],
                clients_root,
                dry_run=args.dry_run,
                force=args.force,
            )
    else:
        generate_one(
            args.url,
            args.name,
            clients_root,
            dry_run=args.dry_run,
            force=args.force,
        )


if __name__ == "__main__":
    main()
