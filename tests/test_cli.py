"""Tests: CLI commands — validate, show-config, and environment output."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from typer.testing import CliRunner

from simplic_ox_agent.cli.main import app

REPO_ROOT = Path(__file__).parent.parent

runner = CliRunner()


def _invoke(*args: str) -> object:
    return runner.invoke(app, list(args))


class TestValidateCommand:
    def test_valid_staging_config(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert result.exit_code == 0
        assert "Configuration valid" in result.output

    def test_shows_instance_name(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert "customer-site-01" in result.output

    def test_shows_simplic_ox_environment(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert "simplic.ox environment: staging" in result.output

    def test_shows_simplic_ox_base_url(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert "https://dev-oxs.simplic.io/" in result.output

    def test_shows_enabled_module_count(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert "Enabled modules: 1" in result.output

    def test_missing_config_exits_nonzero(self, tmp_path: Path) -> None:
        result = _invoke("validate", "--config", str(tmp_path / "nonexistent.json"))
        assert result.exit_code != 0

    def test_invalid_config_exits_nonzero(self, tmp_path: Path) -> None:
        bad = tmp_path / "bad.json"
        bad.write_text('{"application": {"instance_name": "x", "environment": "t"}, "simplic.ox": {"environment": "bogus"}}')
        result = _invoke("validate", "--config", str(bad))
        assert result.exit_code != 0


class TestShowConfigCommand:
    def test_shows_resolved_environment(self) -> None:
        result = _invoke("show-config", "--config", str(REPO_ROOT / "config.example.json"))
        assert result.exit_code == 0
        assert "simplic.ox environment" in result.output
        assert "staging" in result.output

    def test_shows_base_url(self) -> None:
        result = _invoke("show-config", "--config", str(REPO_ROOT / "config.example.json"))
        assert "https://dev-oxs.simplic.io/" in result.output

    def test_shows_application_environment(self) -> None:
        result = _invoke("show-config", "--config", str(REPO_ROOT / "config.example.json"))
        assert "Application environment" in result.output

    def test_shows_instance_name(self) -> None:
        result = _invoke("show-config", "--config", str(REPO_ROOT / "config.example.json"))
        assert "customer-site-01" in result.output


class TestProductionWarning:
    def _make_prod_config(self, tmp_path: Path) -> Path:
        import json

        data: dict[str, Any] = {
            "application": {"instance_name": "prod-inst", "environment": "production"},
            "simplic.ox": {
                "environment": "production",
                "authentication": {"type": "bearer", "token": "tok"},
            },
            "modules": [],
        }
        path = tmp_path / "prod.json"
        path.write_text(json.dumps(data))
        return path

    def test_validate_emits_production_warning(self, tmp_path: Path) -> None:
        cfg_path = self._make_prod_config(tmp_path)
        result = _invoke("validate", "--config", str(cfg_path))
        # Warning goes to stderr, captured together in CliRunner output
        combined = (result.output or "") + (result.stderr if hasattr(result, "stderr") else "")
        assert "WARNING" in combined
        assert "production" in combined

    def test_show_config_emits_production_warning(self, tmp_path: Path) -> None:
        cfg_path = self._make_prod_config(tmp_path)
        result = _invoke("show-config", "--config", str(cfg_path))
        combined = (result.output or "") + (result.stderr if hasattr(result, "stderr") else "")
        assert "WARNING" in combined
        assert "production" in combined

    def test_staging_has_no_production_warning(self) -> None:
        result = _invoke("validate", "--config", str(REPO_ROOT / "config.example.json"))
        assert "WARNING" not in result.output


class TestRunCommand:
    def test_unknown_module_id_exits_nonzero(self) -> None:
        result = _invoke(
            "run", "no-such-module", "--config", str(REPO_ROOT / "config.example.json")
        )
        assert result.exit_code != 0

    def test_shows_target_environment(self) -> None:
        # Even on failure, environment should be echoed before the error
        result = _invoke(
            "run", "no-such-module", "--config", str(REPO_ROOT / "config.example.json")
        )
        assert "staging" in result.output or "staging" in (
            result.stderr if hasattr(result, "stderr") else ""
        )
