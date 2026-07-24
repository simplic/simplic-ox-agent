"""Tests: configuration loading, validation, and field mapping."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from simplic_ox_agent.core.config import (
    ApplicationConfig,
    Config,
    SimplicOxConfig,
    load_config,
)
from simplic_ox_agent.core.environment import SimplicOxEnvironment

REPO_ROOT = Path(__file__).parent.parent


class TestSimplicOxEnvironmentResolution:
    def test_staging_resolves_staging_url(self) -> None:
        cfg = SimplicOxConfig(environment=SimplicOxEnvironment.STAGING)
        assert cfg.get_base_url() == "https://dev-oxs.simplic.io/"

    def test_production_resolves_production_url(self) -> None:
        cfg = SimplicOxConfig(environment=SimplicOxEnvironment.PRODUCTION)
        assert cfg.get_base_url() == "https://oxs.simplic.io/"

    def test_staging_string_accepted(self) -> None:
        cfg = SimplicOxConfig.model_validate({"environment": "staging"})
        assert cfg.environment == SimplicOxEnvironment.STAGING

    def test_production_string_accepted(self) -> None:
        cfg = SimplicOxConfig.model_validate({"environment": "production"})
        assert cfg.environment == SimplicOxEnvironment.PRODUCTION

    def test_unknown_environment_rejected(self) -> None:
        with pytest.raises(ValidationError, match="Unknown simplic.ox environment"):
            SimplicOxConfig.model_validate({"environment": "invalid_env"})

    def test_default_is_staging(self) -> None:
        """Default must be staging to avoid accidental production requests."""
        cfg = SimplicOxConfig()
        assert cfg.environment == SimplicOxEnvironment.STAGING

    def test_production_only_when_explicit(self) -> None:
        """Production must be set explicitly — it is never the implicit default."""
        cfg = SimplicOxConfig.model_validate({"environment": "production"})
        assert cfg.environment == SimplicOxEnvironment.PRODUCTION


class TestApplicationConfig:
    def test_environment_json_key_maps_to_application_environment(self) -> None:
        cfg = ApplicationConfig.model_validate(
            {"instance_name": "inst", "environment": "development"}
        )
        assert cfg.application_environment == "development"

    def test_populate_by_python_name(self) -> None:
        cfg = ApplicationConfig(
            instance_name="inst",
            application_environment="test",
        )
        assert cfg.application_environment == "test"


class TestRootConfig:
    def test_simplic_ox_dot_key_parsed(self, minimal_config_data: dict[str, Any]) -> None:
        cfg = Config.model_validate(minimal_config_data)
        assert cfg.simplic_ox.environment == SimplicOxEnvironment.STAGING

    def test_staging_base_url_from_root_config(self, minimal_config_data: dict[str, Any]) -> None:
        cfg = Config.model_validate(minimal_config_data)
        assert cfg.simplic_ox.get_base_url() == "https://dev-oxs.simplic.io/"

    def test_production_base_url_from_root_config(self) -> None:
        data: dict[str, Any] = {
            "application": {"instance_name": "p", "environment": "prod"},
            "simplic.ox": {"environment": "production"},
        }
        cfg = Config.model_validate(data)
        assert cfg.simplic_ox.environment == SimplicOxEnvironment.PRODUCTION
        assert cfg.simplic_ox.get_base_url() == "https://oxs.simplic.io/"

    def test_unknown_simplic_ox_environment_rejected(self) -> None:
        data: dict[str, Any] = {
            "application": {"instance_name": "t", "environment": "test"},
            "simplic.ox": {"environment": "nope"},
        }
        with pytest.raises(ValidationError, match="Unknown simplic.ox environment"):
            Config.model_validate(data)

    def test_application_environment_distinct_from_simplic_ox_environment(
        self, minimal_config_data: dict[str, Any]
    ) -> None:
        cfg = Config.model_validate(minimal_config_data)
        # "test" (application) vs "staging" (simplic.ox) must be independent
        assert cfg.application.application_environment == "test"
        assert cfg.simplic_ox.environment == SimplicOxEnvironment.STAGING

    def test_settings_accessible(self, staging_config: Config) -> None:
        assert staging_config.settings["customer_id"] == "test-001"


class TestExampleConfig:
    def test_example_config_uses_staging(self) -> None:
        """config.example.json must always target the staging environment."""
        cfg = load_config(REPO_ROOT / "config.example.json")
        assert cfg.simplic_ox.environment == SimplicOxEnvironment.STAGING

    def test_example_config_valid(self) -> None:
        cfg = load_config(REPO_ROOT / "config.example.json")
        assert cfg.application.instance_name == "customer-site-01"

    def test_example_config_has_module(self) -> None:
        cfg = load_config(REPO_ROOT / "config.example.json")
        assert len(cfg.modules) > 0
        assert cfg.modules[0].enabled is True
