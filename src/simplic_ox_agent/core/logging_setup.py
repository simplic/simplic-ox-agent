"""Logging configuration for the simplic.ox agent."""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

from .environment import SimplicOxEnvironment

_SKIP_LOG_ATTRS = frozenset(
    {
        "args",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "levelname",
        "levelno",
        "lineno",
        "message",
        "module",
        "msecs",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "taskName",
        "thread",
        "threadName",
    }
)


class _JsonFormatter(logging.Formatter):
    """Minimal structured JSON log formatter (no third-party dependency)."""

    def format(self, record: logging.LogRecord) -> str:
        record.message = record.getMessage()
        entry: dict = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.message,
        }
        if record.exc_info:
            entry["exc_info"] = self.formatException(record.exc_info)
        # Merge caller-supplied ``extra`` fields
        for key, value in record.__dict__.items():
            if key not in _SKIP_LOG_ATTRS and not key.startswith("_"):
                entry[key] = value
        return json.dumps(entry, default=str)


def setup_logging(
    level: str = "INFO",
    fmt: str = "json",
    log_file: str | None = None,
) -> None:
    """Configure the ``simplic_ox_agent`` logger.

    Must be called once during application startup before any log
    messages are emitted.
    """
    root = logging.getLogger("simplic_ox_agent")
    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    root.handlers.clear()

    if fmt == "json":
        formatter: logging.Formatter = _JsonFormatter()
    else:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)

    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)


def log_startup(
    logger: logging.Logger,
    *,
    instance_name: str,
    simplic_ox_environment: SimplicOxEnvironment,
    base_url: str,
) -> None:
    """Emit startup log entries including the resolved environment and URL.

    Emits a prominent WARNING when the agent targets the production
    simplic.ox environment.
    """
    logger.info(
        "simplic.ox-agent starting",
        extra={
            "instance_name": instance_name,
            "simplic_ox_environment": str(simplic_ox_environment),
            "simplic_ox_base_url": base_url,
        },
    )

    if simplic_ox_environment == SimplicOxEnvironment.PRODUCTION:
        logger.warning(
            f"WARNING: simplic.ox-agent is connected to the production "
            f"simplic.ox environment at {base_url}"
        )
