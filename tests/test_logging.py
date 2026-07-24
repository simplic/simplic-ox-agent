"""Tests: structured log output includes environment context."""

from __future__ import annotations

import json
import logging

import pytest

from simplic_ox_agent.core.environment import SimplicOxEnvironment
from simplic_ox_agent.core.logging_setup import _JsonFormatter, log_startup


class TestJsonFormatter:
    def _format(self, msg: str, **extra: object) -> dict:
        formatter = _JsonFormatter()
        record = logging.LogRecord(
            name="test.logger",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg=msg,
            args=(),
            exc_info=None,
        )
        for key, value in extra.items():
            setattr(record, key, value)
        raw = formatter.format(record)
        return json.loads(raw)

    def test_message_present(self) -> None:
        entry = self._format("hello world")
        assert entry["message"] == "hello world"

    def test_level_present(self) -> None:
        entry = self._format("test")
        assert entry["level"] == "INFO"

    def test_logger_name_present(self) -> None:
        entry = self._format("test")
        assert entry["logger"] == "test.logger"

    def test_extra_fields_included(self) -> None:
        entry = self._format("msg", simplic_ox_environment="staging")
        assert entry["simplic_ox_environment"] == "staging"

    def test_job_context_includes_environment(self) -> None:
        entry = self._format(
            "job running",
            module_id="my-module",
            simplic_ox_environment="production",
            instance_name="inst-1",
        )
        assert entry["module_id"] == "my-module"
        assert entry["simplic_ox_environment"] == "production"
        assert entry["instance_name"] == "inst-1"


class TestLogStartup:
    def test_logs_staging_environment(self, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("simplic_ox_agent.test_startup")
        with caplog.at_level(logging.INFO, logger="simplic_ox_agent.test_startup"):
            log_startup(
                logger,
                instance_name="inst",
                simplic_ox_environment=SimplicOxEnvironment.STAGING,
                base_url="https://dev-oxs.simplic.io/",
            )
        messages = [r.message for r in caplog.records]
        assert any("starting" in m for m in messages)

    def test_logs_production_warning(self, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("simplic_ox_agent.test_startup_prod")
        with caplog.at_level(logging.WARNING, logger="simplic_ox_agent.test_startup_prod"):
            log_startup(
                logger,
                instance_name="inst",
                simplic_ox_environment=SimplicOxEnvironment.PRODUCTION,
                base_url="https://oxs.simplic.io/",
            )
        warning_messages = [
            r.message for r in caplog.records if r.levelno == logging.WARNING
        ]
        assert any("WARNING" in m and "production" in m for m in warning_messages)

    def test_no_production_warning_for_staging(self, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("simplic_ox_agent.test_no_warn")
        with caplog.at_level(logging.WARNING, logger="simplic_ox_agent.test_no_warn"):
            log_startup(
                logger,
                instance_name="inst",
                simplic_ox_environment=SimplicOxEnvironment.STAGING,
                base_url="https://dev-oxs.simplic.io/",
            )
        warning_messages = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warning_messages) == 0
