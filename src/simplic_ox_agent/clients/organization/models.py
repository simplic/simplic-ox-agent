"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

class AcceptJoinMemberRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    organization_id: UUID = Field(alias="organizationId")

class AddTeamMemberRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: UUID | None = Field(None, alias="userId")

class AddressModelRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    additional01: str | None = None
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zip_code: str | None = Field(None, alias="zipCode")
    city: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    federal_state_iso: str | None = Field(None, alias="federalStateIso")

class AddressModelResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    additional01: str | None = None
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zip_code: str | None = Field(None, alias="zipCode")
    city: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    federal_state: FederalStateModel | None = Field(None, alias="federalState")

class BillingAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    additional01: str | None = None
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zip_code: str | None = Field(None, alias="zipCode")
    city: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    vat_id: str | None = Field(None, alias="vatId")
    invoice_recipient: list[str] | None = Field(None, alias="invoiceRecipient")

class CertificateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cert_file: str | None = Field(None, alias="certFile")
    issuer: str | None = None
    subject: str | None = None
    not_before: datetime | None = Field(None, alias="notBefore")
    not_after: datetime | None = Field(None, alias="notAfter")
    serial_number: str | None = Field(None, alias="serialNumber")
    thumbprint: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    pfx_file: str | None = Field(None, alias="pfxFile")

class CreateOrganizationRequest(BaseModel):
    address: AddressModelRequest
    name: str
    dummy: bool | None = None

class CreateOrganizationSiteRequest(BaseModel):
    name: str | None = None
    address: AddressModelRequest | None = None

class CreatePfxFileRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID
    key_file: str = Field(alias="keyFile")
    pfx_password: str | None = Field(None, alias="pfxPassword")

class CreateTeamRequest(BaseModel):
    name: str | None = None

class DeclineJoinMemberRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    organization_id: UUID = Field(alias="organizationId")

class DeleteInviteMemberRequest(BaseModel):
    id: UUID

class EntraAdminConsentCallbackRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    admin_consent: str | None = Field(None, alias="adminConsent")
    tenant: str | None = None
    state: str | None = None
    error: str | None = None
    error_description: str | None = Field(None, alias="errorDescription")

class EntraConnectRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    code: str | None = None
    state: dict[str, object] | None = None
    redirect_uri: str | None = Field(None, alias="redirectUri")

class EntraConnectResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    entra_tenant_id: str | None = Field(None, alias="entraTenantId")

class EntraRequestAdminConsentResponse(BaseModel):
    url: str | None = None

class FederalStateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    name: str | None = None
    federal_state_iso: str | None = Field(None, alias="federalStateIso")
    country_iso: str | None = Field(None, alias="countryIso")

class InternalCertificateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cert_file: str | None = Field(None, alias="certFile")
    issuer: str | None = None
    subject: str | None = None
    not_before: datetime | None = Field(None, alias="notBefore")
    not_after: datetime | None = Field(None, alias="notAfter")
    serial_number: str | None = Field(None, alias="serialNumber")
    thumbprint: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    pfx_file: str | None = Field(None, alias="pfxFile")
    pfx_password: str | None = Field(None, alias="pfxPassword")

class InviteMemberRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email_address: str = Field(alias="emailAddress")
    custom_invitation_text: str | None = Field(None, alias="customInvitationText")

class LeaveOrganizationRequest(BaseModel):
    id: UUID

class OrganizationInvitaitonType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class OrganizationLinkInvitationAcceptedResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    foreign_organization_id: UUID | None = Field(None, alias="foreignOrganizationId")
    modules: list[str] | None = None
    state: OrganizationLinkState | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    originator: str | None = None
    accepted_by: str | None = Field(None, alias="acceptedBy")
    invitation_id: UUID | None = Field(None, alias="invitationId")

class OrganizationLinkInvitationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    email: str | None = None
    domain: str | None = None
    token: str | None = None
    state: OrganizationLinkState | None = None
    modules: list[str] | None = None
    expire_date: datetime | None = Field(None, alias="expireDate")
    organization_name: str | None = Field(None, alias="organizationName")
    originator: str | None = None
    type: OrganizationInvitaitonType | None = None

class OrganizationLinkInvitationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    target_organization: str = Field(alias="targetOrganization")
    email: str
    send_as_mail: bool | None = Field(None, alias="sendAsMail")
    modules: list[str] | None = None

class OrganizationLinkState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class OrganizationLinkStaticInvitationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    expire_date: datetime | None = Field(None, alias="expireDate")
    modules: list[str] | None = None

class OrganizationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    address: AddressModelResponse | None = None
    billing_address_model: BillingAddressModel | None = Field(None, alias="billingAddressModel")
    is_dummy: bool | None = Field(None, alias="isDummy")
    entra_tenant_id: str | None = Field(None, alias="entraTenantId")
    entra_id_admin_consent: bool | None = Field(None, alias="entraIdAdminConsent")

class OrganizationSiteModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    address: AddressModelResponse | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class PatchOrganizationSiteRequest(BaseModel):
    name: str | None = None
    address: AddressModelRequest | None = None

class RemoveMemberRequest(BaseModel):
    id: UUID

class RemoveTeamMemberRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: UUID | None = Field(None, alias="userId")

class TeamMember(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: UUID | None = Field(None, alias="userId")
    e_mail: str | None = Field(None, alias="eMail")

class TeamModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    name: str | None = None
    team_member: list[TeamMember] | None = Field(None, alias="teamMember")

class UpdateMemberRequest(BaseModel):
    roles: list[str]

class UpdateOrganizationRequest(BaseModel):
    address: AddressModelRequest
    name: str

class UpdateTeamRequest(BaseModel):
    name: str | None = None

class UploadCertificateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    cert_file: str = Field(alias="certFile")
    pfx_file: str | None = Field(None, alias="pfxFile")
    pfx_password: str | None = Field(None, alias="pfxPassword")
