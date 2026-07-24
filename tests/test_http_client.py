"""Tests: HTTP client URL joining and environment binding."""

from __future__ import annotations

import pytest
import httpx
import respx

from simplic_ox_agent.core.config import AuthenticationConfig, SimplicOxConfig
from simplic_ox_agent.core.environment import SimplicOxEnvironment
from simplic_ox_agent.core.http_client import SimplicOxHttpClient, _join_url, create_http_client


# ---------------------------------------------------------------------------
# URL joining helper
# ---------------------------------------------------------------------------


class TestJoinUrl:
    def test_leading_slash_in_path(self) -> None:
        assert _join_url("https://example.com/", "/api/foo") == "https://example.com/api/foo"

    def test_no_leading_slash_in_path(self) -> None:
        assert _join_url("https://example.com/", "api/foo") == "https://example.com/api/foo"

    def test_base_without_trailing_slash(self) -> None:
        assert _join_url("https://example.com", "/api/foo") == "https://example.com/api/foo"

    def test_both_no_slash(self) -> None:
        assert _join_url("https://example.com", "api/foo") == "https://example.com/api/foo"

    def test_staging_base_with_path(self) -> None:
        base = "https://dev-oxs.simplic.io/"
        result = _join_url(base, "/api/integrations/logistics")
        assert result == "https://dev-oxs.simplic.io/api/integrations/logistics"

    def test_production_base_with_path(self) -> None:
        base = "https://oxs.simplic.io/"
        result = _join_url(base, "/api/integrations/logistics")
        assert result == "https://oxs.simplic.io/api/integrations/logistics"


# ---------------------------------------------------------------------------
# Client properties
# ---------------------------------------------------------------------------


class TestClientProperties:
    def test_staging_environment(self, staging_simplic_ox_config: SimplicOxConfig) -> None:
        client = create_http_client(staging_simplic_ox_config)
        assert client.environment == SimplicOxEnvironment.STAGING

    def test_staging_base_url(self, staging_simplic_ox_config: SimplicOxConfig) -> None:
        client = create_http_client(staging_simplic_ox_config)
        assert client.base_url == "https://dev-oxs.simplic.io/"

    def test_production_environment(self, production_simplic_ox_config: SimplicOxConfig) -> None:
        client = create_http_client(production_simplic_ox_config)
        assert client.environment == SimplicOxEnvironment.PRODUCTION

    def test_production_base_url(self, production_simplic_ox_config: SimplicOxConfig) -> None:
        client = create_http_client(production_simplic_ox_config)
        assert client.base_url == "https://oxs.simplic.io/"

    def test_environment_is_read_only(self, staging_simplic_ox_config: SimplicOxConfig) -> None:
        client = create_http_client(staging_simplic_ox_config)
        with pytest.raises(AttributeError):
            client.environment = SimplicOxEnvironment.PRODUCTION  # type: ignore[misc]


# ---------------------------------------------------------------------------
# HTTP requests (mocked)
# ---------------------------------------------------------------------------


class TestHttpRequests:
    @pytest.mark.asyncio
    async def test_post_with_leading_slash(
        self, staging_simplic_ox_config: SimplicOxConfig
    ) -> None:
        with respx.mock:
            respx.post("https://dev-oxs.simplic.io/api/integrations/logistics").mock(
                return_value=httpx.Response(200, json={"ok": True})
            )
            async with create_http_client(staging_simplic_ox_config) as client:
                response = await client.post("/api/integrations/logistics", json={})
            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_post_without_leading_slash(
        self, staging_simplic_ox_config: SimplicOxConfig
    ) -> None:
        with respx.mock:
            respx.post("https://dev-oxs.simplic.io/api/integrations/logistics").mock(
                return_value=httpx.Response(200)
            )
            async with create_http_client(staging_simplic_ox_config) as client:
                response = await client.post("api/integrations/logistics", json={})
            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_get_request(self, staging_simplic_ox_config: SimplicOxConfig) -> None:
        with respx.mock:
            respx.get("https://dev-oxs.simplic.io/api/health").mock(
                return_value=httpx.Response(200, json={"status": "ok"})
            )
            async with create_http_client(staging_simplic_ox_config) as client:
                response = await client.get("/api/health")
            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_staging_does_not_reach_production(
        self, staging_simplic_ox_config: SimplicOxConfig
    ) -> None:
        """A staging client must never send requests to the production URL."""
        with respx.mock:
            prod_route = respx.post("https://oxs.simplic.io/api/integrations/logistics")
            staging_route = respx.post(
                "https://dev-oxs.simplic.io/api/integrations/logistics"
            ).mock(return_value=httpx.Response(200))

            async with create_http_client(staging_simplic_ox_config) as client:
                await client.post("/api/integrations/logistics", json={})

            assert staging_route.called
            assert not prod_route.called

    @pytest.mark.asyncio
    async def test_production_does_not_reach_staging(
        self, production_simplic_ox_config: SimplicOxConfig
    ) -> None:
        """A production client must never send requests to the staging URL."""
        with respx.mock:
            staging_route = respx.post(
                "https://dev-oxs.simplic.io/api/integrations/logistics"
            )
            prod_route = respx.post("https://oxs.simplic.io/api/integrations/logistics").mock(
                return_value=httpx.Response(200)
            )

            async with create_http_client(production_simplic_ox_config) as client:
                await client.post("/api/integrations/logistics", json={})

            assert prod_route.called
            assert not staging_route.called
