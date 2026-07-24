"""Configuration models for the simplic.ox agent.

JSON key          Python attribute
──────────────────────────────────────────────────
application.environment  →  application.application_environment
simplic.ox               →  config.simplic_ox
simplic.ox.environment   →  config.simplic_ox.environment
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .environment import SIMPLIC_OX_ENVIRONMENT_URLS, SimplicOxEnvironment

_ENV_VAR_RE = re.compile(r"\$\{([^}]+)\}")


def _resolve_env_var(value: str) -> str:
    """Expand ``${VAR}`` placeholders from process environment variables.

    Raises ``ValueError`` if a referenced variable is not set.
    """

    def _replace(match: re.Match[str]) -> str:
        name = match.group(1)
        resolved = os.environ.get(name)
        if resolved is None:
            raise ValueError(f"Environment variable {name!r} is not set")
        return resolved

    return _ENV_VAR_RE.sub(_replace, value)


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------


class RetryConfig(BaseModel):
    max_attempts: int = 3
    initial_delay_seconds: float = 1.0
    maximum_delay_seconds: float = 30.0


class AuthenticationConfig(BaseModel):
    """Credentials for simplic.ox API requests.

    ``${VAR}`` placeholders in *token* and *api_key* are resolved lazily
    at HTTP-client creation time, not during configuration loading.  This
    allows ``config.example.json`` to be loaded without the token being
    set in the environment.
    """

    type: Literal["bearer", "api_key"] = "bearer"
    token: str | None = None
    api_key: str | None = None

    def resolve_token(self) -> str | None:
        """Return the bearer token with ``${VAR}`` placeholders expanded."""
        return _resolve_env_var(self.token) if self.token else None

    def resolve_api_key(self) -> str | None:
        """Return the API key with ``${VAR}`` placeholders expanded."""
        return _resolve_env_var(self.api_key) if self.api_key else None


class SimplicOxConfig(BaseModel):
    """Connection settings for the remote simplic.ox API.

    The ``environment`` field selects the target cloud endpoint.  Only
    ``staging`` and ``production`` are accepted; unknown values are
    rejected during validation.  Defaults to ``staging`` so that a
    misconfigured deployment never silently hits the production API.
    """

    environment: SimplicOxEnvironment = SimplicOxEnvironment.STAGING
    timeout_seconds: int = 30
    verify_tls: bool = True
    authentication: AuthenticationConfig = Field(default_factory=AuthenticationConfig)
    retry: RetryConfig = Field(default_factory=RetryConfig)

    @field_validator("environment", mode="before")
    @classmethod
    def _validate_environment(cls, v: Any) -> SimplicOxEnvironment:
        try:
            return SimplicOxEnvironment(v)
        except ValueError:
            valid = sorted(e.value for e in SimplicOxEnvironment)
            raise ValueError(
                f"Unknown simplic.ox environment {v!r}. "
                f"Supported environments: {valid}"
            )

    def get_base_url(self) -> str:
        """Return the HTTPS base URL for the configured environment."""
        return SIMPLIC_OX_ENVIRONMENT_URLS[self.environment]


class ApplicationConfig(BaseModel):
    """Configuration describing the local agent installation.

    The ``environment`` JSON key is stored internally as
    ``application_environment`` to prevent ambiguity with
    ``simplic.ox.environment``.
    """

    model_config = ConfigDict(populate_by_name=True)

    instance_name: str
    # JSON key is "environment"; Python attribute is "application_environment"
    application_environment: str = Field(default="production", alias="environment")
    log_level: str = "INFO"
    log_format: Literal["json", "text"] = "json"
    log_file: str | None = None
    module_directory: str = "src/simplic_ox_agent/modules"
    shutdown_timeout_seconds: int = 30


class ScheduleConfig(BaseModel):
    type: Literal["interval", "cron"] = "interval"
    seconds: int | None = None
    cron: str | None = None


class ModuleConfig(BaseModel):
    id: str
    module: str
    enabled: bool = True
    schedule: ScheduleConfig = Field(default_factory=ScheduleConfig)
    settings: dict[str, Any] = Field(default_factory=dict)


class Config(BaseModel):
    """Root configuration model.

    The JSON key ``"simplic.ox"`` maps to the Python attribute
    ``simplic_ox`` to avoid attribute-access issues with dots.
    """

    model_config = ConfigDict(populate_by_name=True)

    application: ApplicationConfig
    simplic_ox: SimplicOxConfig = Field(
        alias="simplic.ox",
        default_factory=SimplicOxConfig,
    )
    settings: dict[str, Any] = Field(default_factory=dict)
    modules: list[ModuleConfig] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------


def load_config(path: Path) -> Config:
    """Load and validate a JSON configuration file.

    Raises ``pydantic.ValidationError`` if the file is invalid.
    Environment-variable placeholders in credentials are *not* expanded
    here; they are resolved when the HTTP client is created.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    return Config.model_validate(data)
