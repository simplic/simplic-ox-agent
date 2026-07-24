"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    CertificateModel,
    EntraConnectResponse,
    EntraRequestAdminConsentResponse,
    InternalCertificateModel,
    OrganizationLinkInvitationAcceptedResponse,
    OrganizationLinkInvitationModel,
    OrganizationModel,
    OrganizationSiteModel,
    TeamModel,
)

_PREFIX = "organization-api/v1"


class OrganizationClient:
    """Typed client for ``organization-api/v1``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.organization import OrganizationClient

        client = OrganizationClient(context.http)
    """

    def __init__(self, http: SimplicOxHttpClient) -> None:
        self._http = http
    async def get_certificate_by_id(
        self,
        id: UUID,
    ) -> CertificateModel:
        """Gets a certificate with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Certificate/{id}",
        )
        response.raise_for_status()
        return CertificateModel.model_validate(response.json())

    async def update_certificate_by_id(
        self,
        id: UUID,
        cert_file: str | None = None,
        pfx_file: str | None = None,
        pfx_password: str | None = None,
    ) -> CertificateModel:
        """Updates the given certificate."""
        _body: dict[str, object] = {
        }
        if cert_file is not None:
            _body["certFile"] = cert_file
        if pfx_file is not None:
            _body["pfxFile"] = pfx_file
        if pfx_password is not None:
            _body["pfxPassword"] = pfx_password
        response = await self._http.patch(
            f"{_PREFIX}/Certificate/{id}",
            json=_body,
        )
        response.raise_for_status()
        return CertificateModel.model_validate(response.json())

    async def delete_certificate_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a certificate with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Certificate/{id}",
        )
        response.raise_for_status()

    async def create_certificate(
        self,
        cert_file: str,
        pfx_file: str | None = None,
        pfx_password: str | None = None,
    ) -> CertificateModel:
        """Creates a new certificate."""
        _body: dict[str, object] = {
            "certFile": cert_file,
        }
        if pfx_file is not None:
            _body["pfxFile"] = pfx_file
        if pfx_password is not None:
            _body["pfxPassword"] = pfx_password
        response = await self._http.post(
            f"{_PREFIX}/Certificate",
            json=_body,
        )
        response.raise_for_status()
        return CertificateModel.model_validate(response.json())

    async def create_pfx_file(
        self,
        id: UUID,
        key_file: str,
        pfx_password: str | None = None,
    ) -> CertificateModel:
        """Create pfx file"""
        _body: dict[str, object] = {
            "id": str(id),
            "keyFile": key_file,
        }
        if pfx_password is not None:
            _body["pfxPassword"] = pfx_password
        response = await self._http.post(
            f"{_PREFIX}/Certificate/create-pfx-file",
            json=_body,
        )
        response.raise_for_status()
        return CertificateModel.model_validate(response.json())

    async def connect(
        self,
        code: str | None = None,
        state: dict[str, object] | None = None,
        redirect_uri: str | None = None,
    ) -> EntraConnectResponse:
        _body: dict[str, object] = {
        }
        if code is not None:
            _body["code"] = code
        if state is not None:
            _body["state"] = state
        if redirect_uri is not None:
            _body["redirectUri"] = redirect_uri
        response = await self._http.post(
            f"{_PREFIX}/Entra/connect",
            json=_body,
        )
        response.raise_for_status()
        return EntraConnectResponse.model_validate(response.json())

    async def admin_consent_request(
        self,
        redirect_uri: str | None = None,
    ) -> EntraRequestAdminConsentResponse:
        _params: dict[str, object] = {}
        if redirect_uri is not None:
            _params["RedirectUri"] = redirect_uri
        response = await self._http.post(
            f"{_PREFIX}/Entra/admin-consent-request",
            params=_params,
        )
        response.raise_for_status()
        return EntraRequestAdminConsentResponse.model_validate(response.json())

    async def admin_consent_callback(
        self,
        admin_consent: str | None = None,
        tenant: str | None = None,
        state: str | None = None,
        error: str | None = None,
        error_description: str | None = None,
    ) -> EntraConnectResponse:
        _body: dict[str, object] = {
        }
        if admin_consent is not None:
            _body["adminConsent"] = admin_consent
        if tenant is not None:
            _body["tenant"] = tenant
        if state is not None:
            _body["state"] = state
        if error is not None:
            _body["error"] = error
        if error_description is not None:
            _body["errorDescription"] = error_description
        response = await self._http.post(
            f"{_PREFIX}/Entra/admin-consent-callback",
            json=_body,
        )
        response.raise_for_status()
        return EntraConnectResponse.model_validate(response.json())

    async def get_internal_certificate_by_id(
        self,
        id: UUID,
    ) -> InternalCertificateModel:
        """Gets a list of all users of an organization."""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalCertificate/{id}",
        )
        response.raise_for_status()
        return InternalCertificateModel.model_validate(response.json())

    async def get_all_ids(
        self,
    ) -> None:
        """Gets a list of all organization ids."""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganization/get-all-ids",
        )
        response.raise_for_status()

    async def internal_organization_get_all(
        self,
    ) -> None:
        """Gets a list of organizations that belongs to the current user"""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganization/get-all",
        )
        response.raise_for_status()

    async def get_users(
        self,
    ) -> None:
        """Gets a list of all users of an organization."""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganization/get-users",
        )
        response.raise_for_status()

    async def get_current(
        self,
    ) -> OrganizationModel:
        """Gets a list of all users of an organization."""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganization/get-current",
        )
        response.raise_for_status()
        return OrganizationModel.model_validate(response.json())

    async def get_internal_organization_site_by_id(
        self,
        id: UUID,
    ) -> OrganizationSiteModel:
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganizationSite/{id}",
        )
        response.raise_for_status()
        return OrganizationSiteModel.model_validate(response.json())

    async def internal_organization_site_get_all_by_organization(
        self,
        id: UUID | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalOrganizationSite/get-all-by-organization",
            params=_params,
        )
        response.raise_for_status()

    async def get_internal_team_by_id(
        self,
        id: UUID,
    ) -> TeamModel:
        """Gets a team with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalTeam/{id}",
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def get_all_by_user(
        self,
        id: UUID | None = None,
    ) -> None:
        """Retrives all teams with the given user id."""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalTeam/get-all-by-user",
            params=_params,
        )
        response.raise_for_status()

    async def member_get_all(
        self,
    ) -> None:
        """Returns all memberships"""
        response = await self._http.get(
            f"{_PREFIX}/Member/get-all",
        )
        response.raise_for_status()

    async def get_pending_invitations(
        self,
    ) -> None:
        """Returns all memberships pending invitations"""
        response = await self._http.get(
            f"{_PREFIX}/Member/get-pending-invitations",
        )
        response.raise_for_status()

    async def invite(
        self,
        email_address: str,
        custom_invitation_text: str | None = None,
    ) -> None:
        """Invites a user by their mail address."""
        _body: dict[str, object] = {
            "emailAddress": email_address,
        }
        if custom_invitation_text is not None:
            _body["customInvitationText"] = custom_invitation_text
        response = await self._http.post(
            f"{_PREFIX}/Member/invite",
            json=_body,
        )
        response.raise_for_status()

    async def delete_invite(
        self,
        id: UUID,
    ) -> None:
        """Deletes a member invite by id."""
        response = await self._http.post(
            f"{_PREFIX}/Member/delete-invite",
            json={"id": str(id)},
        )
        response.raise_for_status()

    async def accept(
        self,
        organization_id: UUID,
    ) -> None:
        """Accept an invitation from an organization"""
        response = await self._http.post(
            f"{_PREFIX}/Member/accept",
            json={"organizationId": str(organization_id)},
        )
        response.raise_for_status()

    async def decline(
        self,
        organization_id: UUID,
    ) -> None:
        """Decline an invitation from an organization"""
        response = await self._http.post(
            f"{_PREFIX}/Member/decline",
            json={"organizationId": str(organization_id)},
        )
        response.raise_for_status()

    async def leave(
        self,
        id: UUID,
    ) -> None:
        """Removes a member from an organization by the id of the membership."""
        response = await self._http.post(
            f"{_PREFIX}/Member/leave",
            json={"id": str(id)},
        )
        response.raise_for_status()

    async def update(
        self,
        id: UUID,
        roles: list[str],
    ) -> None:
        """Update user membership in organization"""
        response = await self._http.put(
            f"{_PREFIX}/Member/update/{id}",
            json={"roles": roles},
        )
        response.raise_for_status()

    async def remove(
        self,
        id: UUID,
    ) -> None:
        """Removes a member from an organization by the id of the membership."""
        response = await self._http.post(
            f"{_PREFIX}/Member/remove",
            json={"id": str(id)},
        )
        response.raise_for_status()

    async def get_organization(
        self,
    ) -> OrganizationModel:
        """Returns the actual organization, from "OId"-claim in the jwt token"""
        response = await self._http.get(
            f"{_PREFIX}/Organization",
        )
        response.raise_for_status()
        return OrganizationModel.model_validate(response.json())

    async def create_organization(
        self,
        address: AddressModelRequest,
        name: str,
        dummy: bool | None = None,
    ) -> OrganizationModel:
        """Creates a new organization and connects it with the currently logged in user"""
        _body: dict[str, object] = {
            "address": address,
            "name": name,
        }
        if dummy is not None:
            _body["dummy"] = dummy
        response = await self._http.post(
            f"{_PREFIX}/Organization",
            json=_body,
        )
        response.raise_for_status()
        return OrganizationModel.model_validate(response.json())

    async def update_organization(
        self,
        address: AddressModelRequest,
        name: str,
    ) -> OrganizationModel:
        """Change the actual organization information"""
        response = await self._http.put(
            f"{_PREFIX}/Organization",
            json={"address": address, "name": name},
        )
        response.raise_for_status()
        return OrganizationModel.model_validate(response.json())

    async def get_for_user(
        self,
    ) -> None:
        """Returns a list of organizations that belongs to the current user"""
        response = await self._http.get(
            f"{_PREFIX}/Organization/get-for-user",
        )
        response.raise_for_status()

    async def get_member_invitations(
        self,
    ) -> None:
        """Returns a list of member invitations for the organization that belongs to the current user"""
        response = await self._http.get(
            f"{_PREFIX}/Organization/get-member-invitations",
        )
        response.raise_for_status()

    async def get_member_list(
        self,
    ) -> None:
        """Returns all member that belongs to the current organization"""
        response = await self._http.get(
            f"{_PREFIX}/Organization/get-member-list",
        )
        response.raise_for_status()

    async def delete_organization_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes testing organization (only works if it was created with dummy set to true)"""
        response = await self._http.delete(
            f"{_PREFIX}/Organization/{id}",
        )
        response.raise_for_status()

    async def get_linked(
        self,
        module: str | None = None,
        search_contains: str | None = None,
    ) -> None:
        """Returns a list of organizations that belongs to the current user"""
        _params: dict[str, object] = {}
        if module is not None:
            _params["module"] = module
        if search_contains is not None:
            _params["searchContains"] = search_contains
        response = await self._http.get(
            f"{_PREFIX}/OrganizationLink/get-linked",
            params=_params,
        )
        response.raise_for_status()

    async def get_my_invitations(
        self,
    ) -> None:
        """Gets a list of all pending invitations"""
        response = await self._http.get(
            f"{_PREFIX}/OrganizationLinkInvitation/get-my-invitations",
        )
        response.raise_for_status()

    async def get_organization_link_invitation(
        self,
    ) -> None:
        """Get static invitation links"""
        response = await self._http.get(
            f"{_PREFIX}/OrganizationLinkInvitation",
        )
        response.raise_for_status()

    async def create_one_time(
        self,
        target_organization: str,
        email: str,
        send_as_mail: bool | None = None,
        modules: list[str] | None = None,
    ) -> OrganizationLinkInvitationModel:
        """Creates a new invitation for linking with another organization"""
        _body: dict[str, object] = {
            "targetOrganization": target_organization,
            "email": email,
        }
        if send_as_mail is not None:
            _body["sendAsMail"] = send_as_mail
        if modules is not None:
            _body["modules"] = modules
        response = await self._http.post(
            f"{_PREFIX}/OrganizationLinkInvitation/create-one-time",
            json=_body,
        )
        response.raise_for_status()
        return OrganizationLinkInvitationModel.model_validate(response.json())

    async def accept_one_time(
        self,
        id: UUID,
    ) -> OrganizationLinkInvitationAcceptedResponse:
        """Accept a pending invitation"""
        response = await self._http.put(
            f"{_PREFIX}/OrganizationLinkInvitation/accept-one-time/{id}",
        )
        response.raise_for_status()
        return OrganizationLinkInvitationAcceptedResponse.model_validate(response.json())

    async def decline_one_time(
        self,
        id: UUID,
    ) -> None:
        """Decline a pending invitation"""
        response = await self._http.put(
            f"{_PREFIX}/OrganizationLinkInvitation/decline-one-time/{id}",
        )
        response.raise_for_status()

    async def create_static(
        self,
        expire_date: str | None = None,
        modules: list[str] | None = None,
    ) -> OrganizationLinkInvitationModel:
        """Creates a new invitation for linking with another organization"""
        _body: dict[str, object] = {
        }
        if expire_date is not None:
            _body["expireDate"] = expire_date
        if modules is not None:
            _body["modules"] = modules
        response = await self._http.post(
            f"{_PREFIX}/OrganizationLinkInvitation/create-static",
            json=_body,
        )
        response.raise_for_status()
        return OrganizationLinkInvitationModel.model_validate(response.json())

    async def join_static(
        self,
        token: str,
    ) -> OrganizationLinkInvitationAcceptedResponse:
        """Create an orgainzation link by using a static token"""
        response = await self._http.put(
            f"{_PREFIX}/OrganizationLinkInvitation/join-static/{token}",
        )
        response.raise_for_status()
        return OrganizationLinkInvitationAcceptedResponse.model_validate(response.json())

    async def get_by_token(
        self,
        token: str,
    ) -> OrganizationLinkInvitationModel:
        """Get invitation by token"""
        response = await self._http.get(
            f"{_PREFIX}/OrganizationLinkInvitation/get-by-token/{token}",
        )
        response.raise_for_status()
        return OrganizationLinkInvitationModel.model_validate(response.json())

    async def delete_organization_link_invitation_by_id(
        self,
        id: UUID,
    ) -> None:
        """Delete an invitation"""
        response = await self._http.delete(
            f"{_PREFIX}/OrganizationLinkInvitation/{id}",
        )
        response.raise_for_status()

    async def get_organization_site_by_id(
        self,
        id: UUID,
    ) -> OrganizationSiteModel:
        response = await self._http.get(
            f"{_PREFIX}/OrganizationSite/{id}",
        )
        response.raise_for_status()
        return OrganizationSiteModel.model_validate(response.json())

    async def update_organization_site_by_id(
        self,
        id: UUID,
        name: str | None = None,
        address: AddressModelRequest | None = None,
    ) -> OrganizationSiteModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if address is not None:
            _body["address"] = address
        response = await self._http.patch(
            f"{_PREFIX}/OrganizationSite/{id}",
            json=_body,
        )
        response.raise_for_status()
        return OrganizationSiteModel.model_validate(response.json())

    async def delete_organization_site_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/OrganizationSite/{id}",
        )
        response.raise_for_status()

    async def organization_site_get_all(
        self,
    ) -> OrganizationSiteModel:
        response = await self._http.get(
            f"{_PREFIX}/OrganizationSite/get-all",
        )
        response.raise_for_status()
        return OrganizationSiteModel.model_validate(response.json())

    async def create_organization_site(
        self,
        name: str | None = None,
        address: AddressModelRequest | None = None,
    ) -> OrganizationSiteModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if address is not None:
            _body["address"] = address
        response = await self._http.post(
            f"{_PREFIX}/OrganizationSite",
            json=_body,
        )
        response.raise_for_status()
        return OrganizationSiteModel.model_validate(response.json())

    async def role_get_all(
        self,
    ) -> None:
        """Returns a list of available roles"""
        response = await self._http.get(
            f"{_PREFIX}/Role/get-all",
        )
        response.raise_for_status()

    async def get_team_by_id(
        self,
        id: UUID,
    ) -> TeamModel:
        """Gets a team with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Team/{id}",
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def update_team_by_id(
        self,
        id: UUID,
        name: str | None = None,
    ) -> TeamModel:
        """Updates the given team."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        response = await self._http.put(
            f"{_PREFIX}/Team/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def delete_team_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a team with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Team/{id}",
        )
        response.raise_for_status()

    async def team_get_all(
        self,
    ) -> None:
        """Retrives all teams."""
        response = await self._http.get(
            f"{_PREFIX}/Team/get-all",
        )
        response.raise_for_status()

    async def create_team(
        self,
        name: str | None = None,
    ) -> TeamModel:
        """Creates a new team."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        response = await self._http.post(
            f"{_PREFIX}/Team",
            json=_body,
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def add_member(
        self,
        id: UUID,
        user_id: UUID | None = None,
    ) -> TeamModel:
        """Adds a user to a team."""
        _body: dict[str, object] = {
        }
        if user_id is not None:
            _body["userId"] = str(user_id)
        response = await self._http.put(
            f"{_PREFIX}/Team/add-member/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def remove_member(
        self,
        id: UUID,
        user_id: UUID | None = None,
    ) -> TeamModel:
        """Removes a user from a team."""
        _body: dict[str, object] = {
        }
        if user_id is not None:
            _body["userId"] = str(user_id)
        response = await self._http.put(
            f"{_PREFIX}/Team/remove-member/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TeamModel.model_validate(response.json())

    async def get_all_by_currentuser(
        self,
    ) -> None:
        """Retrives all teams from the current user."""
        response = await self._http.get(
            f"{_PREFIX}/Team/get-all-by-currentuser",
        )
        response.raise_for_status()

    async def team_get_all_by_organization(
        self,
    ) -> None:
        """Retrives all teams from the current organization."""
        response = await self._http.get(
            f"{_PREFIX}/Team/get-all-by-organization",
        )
        response.raise_for_status()
