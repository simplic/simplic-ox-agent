"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    ChangePasswordResponse,
    HookDefinitionResponse,
    LoginResponse,
    RegisterResponse,
    RequestUserResponse,
    ResetPasswordResponse,
    TwoFactorResponse,
)

_PREFIX = "auth-api/v1"


class AuthClient:
    """Typed client for ``auth-api/v1``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.auth import AuthClient

        client = AuthClient(context.http)
    """

    def __init__(self, http: SimplicOxHttpClient) -> None:
        self._http = http
    async def login(
        self,
        email: str,
        password: str,
    ) -> LoginResponse:
        """Login using username and password. Will return a JWT when logging in was successful."""
        response = await self._http.post(
            f"{_PREFIX}/Auth/login",
            json={"email": email, "password": password},
        )
        response.raise_for_status()
        return LoginResponse.model_validate(response.json())

    async def select_organization(
        self,
        organization_id: UUID,
    ) -> LoginResponse:
        response = await self._http.post(
            f"{_PREFIX}/Auth/select-organization",
            json={"organizationId": str(organization_id)},
        )
        response.raise_for_status()
        return LoginResponse.model_validate(response.json())

    async def register(
        self,
        email: str,
        password: str,
    ) -> RegisterResponse:
        response = await self._http.post(
            f"{_PREFIX}/Auth/register",
            json={"email": email, "password": password},
        )
        response.raise_for_status()
        return RegisterResponse.model_validate(response.json())

    async def send_verification_code(
        self,
        email: str,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/Auth/send-verification-code",
            json={"email": email},
        )
        response.raise_for_status()

    async def verify_mail(
        self,
        email: str,
        code: str,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/Auth/verify-mail",
            json={"email": email, "code": code},
        )
        response.raise_for_status()

    async def restore_password(
        self,
        email: str,
        new_password: str,
    ) -> ResetPasswordResponse:
        response = await self._http.post(
            f"{_PREFIX}/Auth/restore-password",
            json={"email": email, "newPassword": new_password},
        )
        response.raise_for_status()
        return ResetPasswordResponse.model_validate(response.json())

    async def change_password(
        self,
        new_password: str,
    ) -> ChangePasswordResponse:
        response = await self._http.post(
            f"{_PREFIX}/Auth/change-password",
            json={"newPassword": new_password},
        )
        response.raise_for_status()
        return ChangePasswordResponse.model_validate(response.json())

    async def verify_two_factor(
        self,
        token_id: UUID | None = None,
        code: str | None = None,
    ) -> TwoFactorResponse:
        _body: dict[str, object] = {
        }
        if token_id is not None:
            _body["tokenId"] = str(token_id)
        if code is not None:
            _body["code"] = code
        response = await self._http.post(
            f"{_PREFIX}/Auth/verify-two-factor",
            json=_body,
        )
        response.raise_for_status()
        return TwoFactorResponse.model_validate(response.json())

    async def get_hook_definition(
        self,
    ) -> HookDefinitionResponse:
        response = await self._http.get(
            f"{_PREFIX}/HookDefinition",
        )
        response.raise_for_status()
        return HookDefinitionResponse.model_validate(response.json())

    async def get_by_email(
        self,
        email: str | None = None,
    ) -> RequestUserResponse:
        """Get a user by its e-mail address"""
        _params: dict[str, object] = {}
        if email is not None:
            _params["email"] = email
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalUser/get-by-email",
            params=_params,
        )
        response.raise_for_status()
        return RequestUserResponse.model_validate(response.json())

    async def get_by_id(
        self,
        id: UUID | None = None,
    ) -> RequestUserResponse:
        """Get a user by its id"""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalUser/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return RequestUserResponse.model_validate(response.json())
