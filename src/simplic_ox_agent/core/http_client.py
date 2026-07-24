"""Shared HTTP client bound to a single simplic.ox environment.

Key design decisions
--------------------
* One client is created per application startup (requirement 8).
* The base URL is resolved from ``simplic.ox.environment``; modules only
  supply relative paths (requirement: modules must not hard-code hostnames).
* URL joining is handled manually so that leading or trailing slashes in
  caller-supplied paths never produce malformed URLs (requirement 10).
* Authentication headers are set once at construction; modules cannot
  override them (requirement: prevent module-level auth overrides).
* The environment is read-only after construction (requirement 9).
"""

from __future__ import annotations

import httpx

from .config import SimplicOxConfig
from .environment import SimplicOxEnvironment


def _join_url(base: str, path: str) -> str:
    """Join *base* and *path*, normalising slashes so both sides are safe.

    >>> _join_url("https://example.com/", "/api/foo")
    'https://example.com/api/foo'
    >>> _join_url("https://example.com", "api/foo")
    'https://example.com/api/foo'
    """
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


class SimplicOxHttpClient:
    """Async HTTP client bound to a specific simplic.ox environment.

    Construct via :func:`create_http_client` to ensure credentials are
    resolved from environment variables before the client is built.
    """

    def __init__(
        self,
        environment: SimplicOxEnvironment,
        base_url: str,
        *,
        timeout: int,
        verify_tls: bool,
        headers: dict[str, str],
    ) -> None:
        self._environment = environment
        self._base_url = base_url
        self._client = httpx.AsyncClient(
            timeout=timeout,
            verify=verify_tls,
            headers=headers,
        )

    # ------------------------------------------------------------------
    # Read-only environment properties
    # ------------------------------------------------------------------

    @property
    def environment(self) -> SimplicOxEnvironment:
        """The environment this client is bound to."""
        return self._environment

    @property
    def base_url(self) -> str:
        """The HTTPS base URL for the configured environment."""
        return self._base_url

    # ------------------------------------------------------------------
    # HTTP verbs — modules supply only relative paths
    # ------------------------------------------------------------------

    def _url(self, path: str) -> str:
        return _join_url(self._base_url, path)

    async def get(self, path: str, **kwargs: object) -> httpx.Response:
        return await self._client.get(self._url(path), **kwargs)

    async def post(self, path: str, **kwargs: object) -> httpx.Response:
        return await self._client.post(self._url(path), **kwargs)

    async def put(self, path: str, **kwargs: object) -> httpx.Response:
        return await self._client.put(self._url(path), **kwargs)

    async def patch(self, path: str, **kwargs: object) -> httpx.Response:
        return await self._client.patch(self._url(path), **kwargs)

    async def delete(self, path: str, **kwargs: object) -> httpx.Response:
        return await self._client.delete(self._url(path), **kwargs)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> SimplicOxHttpClient:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()


def create_http_client(config: SimplicOxConfig) -> SimplicOxHttpClient:
    """Build a :class:`SimplicOxHttpClient` from validated configuration.

    Credentials are resolved from environment variables at this point.
    Raises ``ValueError`` if a required environment variable is missing.
    """
    base_url = config.get_base_url()

    headers: dict[str, str] = {}
    auth = config.authentication
    if auth.type == "bearer":
        token = auth.resolve_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
    elif auth.type == "api_key":
        api_key = auth.resolve_api_key()
        if api_key:
            headers["X-Api-Key"] = api_key

    return SimplicOxHttpClient(
        environment=config.environment,
        base_url=base_url,
        timeout=config.timeout_seconds,
        verify_tls=config.verify_tls,
        headers=headers,
    )
