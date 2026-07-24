"""simplic.ox agent CLI.

Commands
--------
validate     Validate the configuration file and print a summary.
show-config  Display the full resolved configuration.
run          Manually execute a single module once.
"""

from __future__ import annotations

import asyncio
import importlib
import logging
import sys
from pathlib import Path
from typing import Optional

import typer
from pydantic import ValidationError

from ..core.config import Config, load_config
from ..core.context import ModuleContext
from ..core.environment import SimplicOxEnvironment
from ..core.http_client import create_http_client
from ..core.logging_setup import log_startup, setup_logging

app = typer.Typer(
    name="simplic-ox-agent",
    help="simplic.ox agent — manages scheduled API integrations.",
    no_args_is_help=True,
)

_CONFIG_OPTION = typer.Option(
    "config.json",
    "--config",
    "-c",
    help="Path to the JSON configuration file.",
    show_default=True,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_or_exit(config_path: Path) -> Config:
    if not config_path.exists():
        typer.echo(f"Configuration file not found: {config_path}", err=True)
        raise typer.Exit(1)
    try:
        return load_config(config_path)
    except ValidationError as exc:
        typer.echo(f"Configuration is invalid:\n{exc}", err=True)
        raise typer.Exit(1)
    except Exception as exc:  # noqa: BLE001
        typer.echo(f"Failed to load configuration: {exc}", err=True)
        raise typer.Exit(1)


def _production_warning(environment: SimplicOxEnvironment, base_url: str) -> None:
    typer.echo(
        f"\nWARNING: simplic.ox-agent is connected to the production "
        f"simplic.ox environment at {base_url}",
        err=True,
    )


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------


@app.command("validate")
def validate(
    config_path: Path = _CONFIG_OPTION,
) -> None:
    """Validate the configuration file and print a summary."""
    cfg = _load_or_exit(config_path)

    ox_env = cfg.simplic_ox.environment
    base_url = cfg.simplic_ox.get_base_url()
    enabled_modules = sum(1 for m in cfg.modules if m.enabled)

    typer.echo("Configuration valid")
    typer.echo(f"Instance: {cfg.application.instance_name}")
    typer.echo(f"simplic.ox environment: {ox_env}")
    typer.echo(f"simplic.ox base URL: {base_url}")
    typer.echo(f"Enabled modules: {enabled_modules}")

    if ox_env == SimplicOxEnvironment.PRODUCTION:
        _production_warning(ox_env, base_url)


# ---------------------------------------------------------------------------
# show-config
# ---------------------------------------------------------------------------


@app.command("show-config")
def show_config(
    config_path: Path = _CONFIG_OPTION,
) -> None:
    """Display the resolved configuration (secrets are not shown)."""
    cfg = _load_or_exit(config_path)

    ox_env = cfg.simplic_ox.environment
    base_url = cfg.simplic_ox.get_base_url()
    enabled_modules = sum(1 for m in cfg.modules if m.enabled)
    total_modules = len(cfg.modules)

    typer.echo("─" * 60)
    typer.echo("simplic.ox Agent — Resolved Configuration")
    typer.echo("─" * 60)
    typer.echo(f"Instance:                   {cfg.application.instance_name}")
    typer.echo(f"Application environment:    {cfg.application.application_environment}")
    typer.echo(f"simplic.ox environment:     {ox_env}")
    typer.echo(f"simplic.ox base URL:        {base_url}")
    typer.echo(f"Log level:                  {cfg.application.log_level}")
    typer.echo(f"Log format:                 {cfg.application.log_format}")
    if cfg.application.log_file:
        typer.echo(f"Log file:                   {cfg.application.log_file}")
    typer.echo(f"Shutdown timeout:           {cfg.application.shutdown_timeout_seconds}s")
    typer.echo(f"Modules (enabled/total):    {enabled_modules}/{total_modules}")
    typer.echo(f"TLS verification:           {cfg.simplic_ox.verify_tls}")
    typer.echo(f"Request timeout:            {cfg.simplic_ox.timeout_seconds}s")
    typer.echo(f"Retry max attempts:         {cfg.simplic_ox.retry.max_attempts}")

    if cfg.modules:
        typer.echo("\nModules:")
        for mod in cfg.modules:
            status = "enabled" if mod.enabled else "disabled"
            typer.echo(f"  [{status:8}]  {mod.id}  ({mod.module})")

    if ox_env == SimplicOxEnvironment.PRODUCTION:
        _production_warning(ox_env, base_url)


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------


@app.command("run")
def run_module(
    module_id: str = typer.Argument(..., help="ID of the module to run."),
    config_path: Path = _CONFIG_OPTION,
) -> None:
    """Manually execute a single module once."""
    cfg = _load_or_exit(config_path)

    ox_env = cfg.simplic_ox.environment
    base_url = cfg.simplic_ox.get_base_url()

    typer.echo(f"Target environment: {ox_env} ({base_url})")

    if ox_env == SimplicOxEnvironment.PRODUCTION:
        _production_warning(ox_env, base_url)

    module_cfg = next((m for m in cfg.modules if m.id == module_id), None)
    if module_cfg is None:
        typer.echo(f"Module {module_id!r} not found in configuration.", err=True)
        raise typer.Exit(1)

    if not module_cfg.enabled:
        typer.echo(f"Module {module_id!r} is disabled.", err=True)
        raise typer.Exit(1)

    typer.echo(f"Running module: {module_id}")
    asyncio.run(_run_module_async(cfg, module_cfg, ox_env, base_url))
    typer.echo(f"Module {module_id!r} completed.")


async def _run_module_async(
    cfg: Config,
    module_cfg,  # ModuleConfig
    ox_env: SimplicOxEnvironment,
    base_url: str,
) -> None:
    setup_logging(
        level=cfg.application.log_level,
        fmt=cfg.application.log_format,
        log_file=cfg.application.log_file,
    )
    logger = logging.getLogger(f"simplic_ox_agent.{module_cfg.id}")

    log_startup(
        logger,
        instance_name=cfg.application.instance_name,
        simplic_ox_environment=ox_env,
        base_url=base_url,
    )

    try:
        mod = importlib.import_module(module_cfg.module)
    except ImportError as exc:
        typer.echo(f"Cannot import module {module_cfg.module!r}: {exc}", err=True)
        raise typer.Exit(1) from exc

    run_fn = getattr(mod, "run", None)
    if run_fn is None:
        typer.echo(
            f"Module {module_cfg.module!r} does not expose a 'run' function.",
            err=True,
        )
        raise typer.Exit(1)

    async with create_http_client(cfg.simplic_ox) as http_client:
        context = ModuleContext(
            module_id=module_cfg.id,
            module_settings=module_cfg.settings,
            global_settings=cfg.settings,
            http=http_client,
            logger=logger,
            instance_name=cfg.application.instance_name,
            application_environment=cfg.application.application_environment,
            simplic_ox_environment=ox_env,
        )
        await run_fn(context)
