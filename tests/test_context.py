"""Tests: ModuleContext properties and immutability."""

from __future__ import annotations

import logging
from unittest.mock import MagicMock

import pytest

from simplic_ox_agent.core.context import ModuleContext
from simplic_ox_agent.core.environment import SimplicOxEnvironment


@pytest.fixture
def staging_context() -> ModuleContext:
    return ModuleContext(
        module_id="test-module",
        module_settings={"batch_size": 50, "endpoint": "/api/test"},
        global_settings={"customer_id": "cust-001", "site_id": "berlin"},
        http=MagicMock(),
        logger=logging.getLogger("test"),
        instance_name="test-instance",
        application_environment="development",
        simplic_ox_environment=SimplicOxEnvironment.STAGING,
    )


class TestModuleContextProperties:
    def test_module_id(self, staging_context: ModuleContext) -> None:
        assert staging_context.module_id == "test-module"

    def test_module_settings(self, staging_context: ModuleContext) -> None:
        assert staging_context.module_settings["batch_size"] == 50

    def test_global_settings(self, staging_context: ModuleContext) -> None:
        assert staging_context.global_settings["customer_id"] == "cust-001"

    def test_instance_name(self, staging_context: ModuleContext) -> None:
        assert staging_context.instance_name == "test-instance"

    def test_application_environment(self, staging_context: ModuleContext) -> None:
        assert staging_context.application_environment == "development"

    def test_simplic_ox_environment_staging(self, staging_context: ModuleContext) -> None:
        assert staging_context.simplic_ox_environment == SimplicOxEnvironment.STAGING

    def test_logger_present(self, staging_context: ModuleContext) -> None:
        assert isinstance(staging_context.logger, logging.Logger)


class TestEnvironmentDistinction:
    def test_application_and_simplic_ox_environments_are_independent(
        self, staging_context: ModuleContext
    ) -> None:
        """application_environment and simplic_ox_environment are distinct fields."""
        # "development" (local) vs "staging" (remote API)
        assert staging_context.application_environment == "development"
        assert staging_context.simplic_ox_environment == SimplicOxEnvironment.STAGING

    def test_environments_carry_different_values(self) -> None:
        ctx = ModuleContext(
            module_id="m",
            module_settings={},
            global_settings={},
            http=MagicMock(),
            logger=logging.getLogger("t"),
            instance_name="inst",
            application_environment="production",  # local deployment is "production"
            simplic_ox_environment=SimplicOxEnvironment.STAGING,  # but API is staging
        )
        assert ctx.application_environment == "production"
        assert ctx.simplic_ox_environment == SimplicOxEnvironment.STAGING
        assert ctx.application_environment != str(ctx.simplic_ox_environment)


class TestModuleContextImmutability:
    def test_http_is_read_only(self, staging_context: ModuleContext) -> None:
        """Modules must not be able to replace the HTTP client."""
        with pytest.raises(AttributeError):
            staging_context.http = MagicMock()  # type: ignore[misc]

    def test_environment_is_read_only(self, staging_context: ModuleContext) -> None:
        """Modules must not be able to change the simplic.ox environment."""
        with pytest.raises(AttributeError):
            staging_context.simplic_ox_environment = SimplicOxEnvironment.PRODUCTION  # type: ignore[misc]

    def test_module_id_is_read_only(self, staging_context: ModuleContext) -> None:
        with pytest.raises(AttributeError):
            staging_context.module_id = "hacked"  # type: ignore[misc]

    def test_instance_name_is_read_only(self, staging_context: ModuleContext) -> None:
        with pytest.raises(AttributeError):
            staging_context.instance_name = "other"  # type: ignore[misc]
