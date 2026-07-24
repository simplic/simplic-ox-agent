"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

class ChangePasswordRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    new_password: str = Field(alias="newPassword")

class ChangePasswordResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token_id: UUID | None = Field(None, alias="tokenId")

class HookDefinitionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    operation: str | None = None
    data_type: str | None = Field(None, alias="dataType")
    description: str | None = None
    payload: str | None = None

class HookDefinitionResponse(BaseModel):
    definitions: list[HookDefinitionModel] | None = None

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token: str | None = None
    error_state: str | None = Field(None, alias="errorState")
    token_type: str | None = Field(None, alias="tokenType")
    user_id: UUID | None = Field(None, alias="userId")

class RegisterRequest(BaseModel):
    email: str
    password: str

class RegisterResponse(BaseModel):
    email: str | None = None

class RequestUserResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    e_mail: str | None = Field(None, alias="eMail")
    user_name: str | None = Field(None, alias="userName")

class ResetPasswordRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: str
    new_password: str = Field(alias="newPassword")

class ResetPasswordResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token_id: UUID | None = Field(None, alias="tokenId")

class SelectOrganizationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    organization_id: UUID = Field(alias="organizationId")

class SendVerificationCodeRequest(BaseModel):
    email: str

class TwoFactorRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    token_id: UUID | None = Field(None, alias="tokenId")
    code: str | None = None

class TwoFactorResponse(BaseModel):
    payload: dict[str, str] | None = None

class VerifyMailRequest(BaseModel):
    email: str
    code: str
