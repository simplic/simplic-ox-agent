"""Runtime context supplied to every module execution."""

from __future__ import annotations

import logging
from typing import Any

from .environment import SimplicOxEnvironment
from .http_client import SimplicOxHttpClient
from .local_store import LocalDataStore


class ModuleContext:
    """Immutable runtime context provided to each module invocation.

    All properties are read-only.  Modules cannot replace the HTTP
    client, change the environment, or mutate shared configuration.

    Attributes
    ----------
    module_id:
        Identifier of the currently executing module.
    module_settings:
        Per-module ``settings`` block from the configuration file.
    global_settings:
        The top-level ``settings`` block shared across all modules.
    http:
        Shared HTTP client bound to the configured simplic.ox environment.
        Modules use only relative paths, e.g. ``/api/integrations/foo``.
    logger:
        Structured logger scoped to this module.
    instance_name:
        Human-readable name of the local agent installation.
    application_environment:
        Label describing the local deployment (e.g. ``"development"``,
        ``"production"``).  Distinct from ``simplic_ox_environment``.
    simplic_ox_environment:
        The remote simplic.ox API environment (``staging`` or
        ``production``) that the HTTP client targets.
    data:
        Persistent local key-value store scoped to this module.  Data
        is saved as JSON on disk and survives between runs.
    """

    __slots__ = (
        "_module_id",
        "_module_settings",
        "_global_settings",
        "_http",
        "_logger",
        "_instance_name",
        "_application_environment",
        "_simplic_ox_environment",
        "_data_store",
    )

    def __init__(
        self,
        *,
        module_id: str,
        module_settings: dict[str, Any],
        global_settings: dict[str, Any],
        http: SimplicOxHttpClient,
        logger: logging.Logger,
        instance_name: str,
        application_environment: str,
        simplic_ox_environment: SimplicOxEnvironment,
        data_store: LocalDataStore,
    ) -> None:
        self._module_id = module_id
        self._module_settings = module_settings
        self._global_settings = global_settings
        self._http = http
        self._logger = logger
        self._instance_name = instance_name
        self._application_environment = application_environment
        self._simplic_ox_environment = simplic_ox_environment
        self._data_store = data_store

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def module_id(self) -> str:
        return self._module_id

    @property
    def module_settings(self) -> dict[str, Any]:
        return self._module_settings

    @property
    def global_settings(self) -> dict[str, Any]:
        return self._global_settings

    @property
    def http(self) -> SimplicOxHttpClient:
        """Shared HTTP client.  Modules must not replace this."""
        return self._http

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def instance_name(self) -> str:
        return self._instance_name

    @property
    def application_environment(self) -> str:
        """Local deployment label (e.g. ``development``, ``production``)."""
        return self._application_environment

    @property
    def simplic_ox_environment(self) -> SimplicOxEnvironment:
        """Remote simplic.ox API environment (``staging`` or ``production``)."""
        return self._simplic_ox_environment

    @property
    def data(self) -> LocalDataStore:
        """Persistent local key-value store scoped to this module."""
        return self._data_store
