"""Named simplic.ox cloud environments and their base URLs."""

from enum import StrEnum


class SimplicOxEnvironment(StrEnum):
    """Enumeration of supported simplic.ox cloud environments."""

    STAGING = "staging"
    PRODUCTION = "production"


#: Central mapping from environment to HTTPS base URL.
#: All URLs use HTTPS and end with a trailing slash.
SIMPLIC_OX_ENVIRONMENT_URLS: dict[SimplicOxEnvironment, str] = {
    SimplicOxEnvironment.STAGING: "https://dev-oxs.simplic.io/",
    SimplicOxEnvironment.PRODUCTION: "https://oxs.simplic.io/",
}


def get_base_url(environment: SimplicOxEnvironment) -> str:
    """Return the HTTPS base URL for the given environment."""
    return SIMPLIC_OX_ENVIRONMENT_URLS[environment]
