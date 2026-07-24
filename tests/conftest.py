"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from simplic_ox_agent.core.config import (
    ApplicationConfig,
    AuthenticationConfig,
    Config,
    ModuleConfig,
    ScheduleConfig,
    SimplicOxConfig,
)
from simplic_ox_agent.core.environment import SimplicOxEnvironment

REPO_ROOT = Path(__file__).parent.parent


@pytest.fixture
def staging_simplic_ox_config() -> SimplicOxConfig:
    return SimplicOxConfig(
        environment=SimplicOxEnvironment.STAGING,
        authentication=AuthenticationConfig(type="bearer", token="test-token"),
    )


@pytest.fixture
def production_simplic_ox_config() -> SimplicOxConfig:
    return SimplicOxConfig(
        environment=SimplicOxEnvironment.PRODUCTION,
        authentication=AuthenticationConfig(type="bearer", token="prod-token"),
    )


@pytest.fixture
def minimal_config_data() -> dict[str, Any]:
    return {
        "application": {
            "instance_name": "test-instance",
            "environment": "test",
        },
        "simplic.ox": {
            "environment": "staging",
            "authentication": {"type": "bearer", "token": "test-token"},
        },
        "settings": {"customer_id": "test-001"},
        "modules": [
            {
                "id": "test-module",
                "module": "simplic_ox_agent.modules.example_module",
                "enabled": True,
                "schedule": {"type": "interval", "seconds": 300},
                "settings": {"batch_size": 50},
            }
        ],
    }


@pytest.fixture
def staging_config(minimal_config_data) -> Config:
    return Config.model_validate(minimal_config_data)
