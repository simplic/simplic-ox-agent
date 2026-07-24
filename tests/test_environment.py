"""Tests: environment enum, URL mapping, and HTTPS enforcement."""

from __future__ import annotations

import pytest

from simplic_ox_agent.core.environment import (
    SIMPLIC_OX_ENVIRONMENT_URLS,
    SimplicOxEnvironment,
    get_base_url,
)


class TestEnvironmentValues:
    def test_staging_value(self) -> None:
        assert SimplicOxEnvironment.STAGING == "staging"

    def test_production_value(self) -> None:
        assert SimplicOxEnvironment.PRODUCTION == "production"

    def test_enum_is_str(self) -> None:
        assert isinstance(SimplicOxEnvironment.STAGING, str)
        assert isinstance(SimplicOxEnvironment.PRODUCTION, str)

    def test_str_round_trip(self) -> None:
        assert SimplicOxEnvironment("staging") is SimplicOxEnvironment.STAGING
        assert SimplicOxEnvironment("production") is SimplicOxEnvironment.PRODUCTION


class TestEnvironmentURLs:
    def test_staging_url(self) -> None:
        assert get_base_url(SimplicOxEnvironment.STAGING) == "https://dev-oxs.simplic.io/"

    def test_production_url(self) -> None:
        assert get_base_url(SimplicOxEnvironment.PRODUCTION) == "https://oxs.simplic.io/"

    def test_all_environments_have_urls(self) -> None:
        for env in SimplicOxEnvironment:
            assert env in SIMPLIC_OX_ENVIRONMENT_URLS, f"{env} has no URL entry"

    def test_all_urls_use_https(self) -> None:
        for env, url in SIMPLIC_OX_ENVIRONMENT_URLS.items():
            assert url.startswith("https://"), f"{env} URL must use HTTPS, got: {url}"

    def test_urls_have_trailing_slash(self) -> None:
        for env, url in SIMPLIC_OX_ENVIRONMENT_URLS.items():
            assert url.endswith("/"), f"{env} URL should end with '/': {url}"

    def test_staging_and_production_are_different_urls(self) -> None:
        staging = get_base_url(SimplicOxEnvironment.STAGING)
        production = get_base_url(SimplicOxEnvironment.PRODUCTION)
        assert staging != production

    def test_unknown_environment_raises(self) -> None:
        with pytest.raises(ValueError):
            SimplicOxEnvironment("unknown_env")
