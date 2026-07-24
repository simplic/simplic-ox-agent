"""Per-module local data store.

Provides a simple JSON-backed key-value store that is scoped to a single
module.  Each module gets its own file under the configured data directory:

    <data_directory>/<module_id>.json

Usage inside a module::

    async def run(context: ModuleContext) -> None:
        last_run = context.data.get("last_processed_id")
        context.data.set("last_processed_id", 42)
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

_log = logging.getLogger(__name__)


class LocalDataStore:
    """Persistent JSON key-value store for a single module.

    Data is loaded lazily on first access and written back to disk after
    every mutating operation.  All values must be JSON-serialisable.

    Parameters
    ----------
    data_dir:
        Directory that holds the per-module JSON files.  Created
        automatically if it does not exist.
    module_id:
        The module's unique identifier; used as the file name stem.
    """

    __slots__ = ("_path", "_data", "_loaded")

    def __init__(self, data_dir: Path, module_id: str) -> None:
        # Sanitise module_id so it is safe as a file-name component.
        safe_id = module_id.replace("/", "_").replace("\\", "_")
        self._path: Path = data_dir / f"{safe_id}.json"
        self._data: dict[str, Any] = {}
        self._loaded: bool = False

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _ensure_loaded(self) -> None:
        if self._loaded:
            return
        self._loaded = True
        if self._path.exists():
            try:
                text = self._path.read_text(encoding="utf-8")
                parsed = json.loads(text)
                if isinstance(parsed, dict):
                    self._data = parsed
                else:
                    _log.warning(
                        "Local data store at %s contained non-dict JSON; resetting.",
                        self._path,
                    )
                    self._data = {}
            except (OSError, json.JSONDecodeError) as exc:
                _log.warning(
                    "Could not read local data store at %s: %s; starting empty.",
                    self._path,
                    exc,
                )
                self._data = {}

    def _persist(self) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.write_text(
                json.dumps(self._data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        except OSError as exc:
            _log.error("Failed to persist local data store at %s: %s", self._path, exc)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for *key*, or *default* if the key is absent."""
        self._ensure_loaded()
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Store *value* under *key* and persist to disk immediately."""
        self._ensure_loaded()
        self._data[key] = value
        self._persist()

    def delete(self, key: str) -> None:
        """Remove *key* from the store.  No-op if the key does not exist."""
        self._ensure_loaded()
        if key in self._data:
            del self._data[key]
            self._persist()

    def clear(self) -> None:
        """Remove all keys from the store and persist the empty state."""
        self._ensure_loaded()
        self._data = {}
        self._persist()

    def all(self) -> dict[str, Any]:
        """Return a shallow copy of all stored key-value pairs."""
        self._ensure_loaded()
        return dict(self._data)

    def __contains__(self, key: str) -> bool:
        self._ensure_loaded()
        return key in self._data

    def __repr__(self) -> str:
        return f"LocalDataStore(path={self._path!r}, loaded={self._loaded})"
