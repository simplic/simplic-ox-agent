"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

class AddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    company_name: str | None = Field(None, alias="companyName")
    additional01: str | None = None
    additional02: str | None = None
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    city: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country_iso: str | None = Field(None, alias="countryIso")
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    match_code: str | None = Field(None, alias="matchCode")
    manual_coordinates: bool | None = Field(None, alias="manualCoordinates")
    geo_score: float | None = Field(None, alias="geoScore")

class ClosedDayModel(BaseModel):
    date: datetime | None = None
    reason: str | None = None

class ContactModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address: AddressModel | None = None
    primary_email_address: EmailAddressModel | None = Field(None, alias="primaryEmailAddress")
    primary_phone_number: PhoneNumber | None = Field(None, alias="primaryPhoneNumber")
    email_addresses: list[EmailAddressModel] | None = Field(None, alias="emailAddresses")
    phone_numbers: list[PhoneNumberModel] | None = Field(None, alias="phoneNumbers")
    match_code: str | None = Field(None, alias="matchCode")
    functions: list[str] | None = None
    opening_hours: list[OpeningHoursModel] | None = Field(None, alias="openingHours")
    closed_days: list[ClosedDayModel] | None = Field(None, alias="closedDays")
    addon: dict[str, dict[str, object]] | None = None
    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    organization_id: UUID | None = Field(None, alias="organizationId")

class CreateContactRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address: AddressModel | None = None
    primary_email_address: EmailAddressModel | None = Field(None, alias="primaryEmailAddress")
    primary_phone_number: PhoneNumber | None = Field(None, alias="primaryPhoneNumber")
    email_addresses: list[EmailAddressModel] | None = Field(None, alias="emailAddresses")
    phone_numbers: list[PhoneNumberModel] | None = Field(None, alias="phoneNumbers")
    match_code: str | None = Field(None, alias="matchCode")
    functions: list[str] | None = None
    opening_hours: list[OpeningHoursModel] | None = Field(None, alias="openingHours")
    closed_days: list[ClosedDayModel] | None = Field(None, alias="closedDays")
    addon: dict[str, dict[str, object]] | None = None

class DayOfWeek(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class EmailAddressModel(BaseModel):
    email: str | None = None
    type: str | None = None

class OpeningHoursModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    day_of_week: DayOfWeek | None = Field(None, alias="dayOfWeek")
    open_time: str | None = Field(None, alias="openTime")
    close_time: str | None = Field(None, alias="closeTime")
    is_closed: bool | None = Field(None, alias="isClosed")

class OrganizationSettingResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    internal_name: str | None = Field(None, alias="internalName")
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    value: dict[str, object] | None = None
    default_value: dict[str, object] | None = Field(None, alias="defaultValue")
    value_type_name: str | None = Field(None, alias="valueTypeName")
    options: list[SettingOption] | None = None
    has_options: bool | None = Field(None, alias="hasOptions")

class PhoneNumber(BaseModel):
    number: str | None = None
    type: str | None = None

class PhoneNumberModel(BaseModel):
    number: str | None = None
    type: str | None = None

class ResolveLocationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    reset_geo_coordinates: bool | None = Field(None, alias="resetGeoCoordinates")

class SettingOption(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: dict[str, object] | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class UpdateContactRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address: AddressModel | None = None
    primary_email_address: EmailAddressModel | None = Field(None, alias="primaryEmailAddress")
    primary_phone_number: PhoneNumber | None = Field(None, alias="primaryPhoneNumber")
    email_addresses: list[EmailAddressModel] | None = Field(None, alias="emailAddresses")
    phone_numbers: list[PhoneNumberModel] | None = Field(None, alias="phoneNumbers")
    match_code: str | None = Field(None, alias="matchCode")
    functions: list[str] | None = None
    opening_hours: list[OpeningHoursModel] | None = Field(None, alias="openingHours")
    closed_days: list[ClosedDayModel] | None = Field(None, alias="closedDays")
    addon: dict[str, dict[str, object]] | None = None

class UpdateSettingRequest(BaseModel):
    value: dict[str, object] | None = None
