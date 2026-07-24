"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    ContactModel,
    OrganizationSettingResult,
)

_PREFIX = "contact-api/v1"


class ContactClient:
    """Typed client for ``contact-api/v1``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.contact import ContactClient

        client = ContactClient(context.http)
    """

    def __init__(self, http: SimplicOxHttpClient) -> None:
        self._http = http
    async def get_contact_by_id(
        self,
        id: UUID,
    ) -> ContactModel:
        response = await self._http.get(
            f"{_PREFIX}/Contact/{id}",
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def contact_update_contact_by_id(
        self,
        id: UUID,
        address: AddressModel | None = None,
        primary_email_address: EmailAddressModel | None = None,
        primary_phone_number: PhoneNumber | None = None,
        email_addresses: list[EmailAddressModel] | None = None,
        phone_numbers: list[PhoneNumberModel] | None = None,
        match_code: str | None = None,
        functions: list[str] | None = None,
        opening_hours: list[OpeningHoursModel] | None = None,
        closed_days: list[ClosedDayModel] | None = None,
        addon: dict[str, dict[str, object]] | None = None,
    ) -> ContactModel:
        _body: dict[str, object] = {
        }
        if address is not None:
            _body["address"] = address
        if primary_email_address is not None:
            _body["primaryEmailAddress"] = primary_email_address
        if primary_phone_number is not None:
            _body["primaryPhoneNumber"] = primary_phone_number
        if email_addresses is not None:
            _body["emailAddresses"] = email_addresses
        if phone_numbers is not None:
            _body["phoneNumbers"] = phone_numbers
        if match_code is not None:
            _body["matchCode"] = match_code
        if functions is not None:
            _body["functions"] = functions
        if opening_hours is not None:
            _body["openingHours"] = opening_hours
        if closed_days is not None:
            _body["closedDays"] = closed_days
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.put(
            f"{_PREFIX}/Contact/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def contact_update_contact_by_id_1(
        self,
        id: UUID,
        address: AddressModel | None = None,
        primary_email_address: EmailAddressModel | None = None,
        primary_phone_number: PhoneNumber | None = None,
        email_addresses: list[EmailAddressModel] | None = None,
        phone_numbers: list[PhoneNumberModel] | None = None,
        match_code: str | None = None,
        functions: list[str] | None = None,
        opening_hours: list[OpeningHoursModel] | None = None,
        closed_days: list[ClosedDayModel] | None = None,
        addon: dict[str, dict[str, object]] | None = None,
    ) -> ContactModel:
        _body: dict[str, object] = {
        }
        if address is not None:
            _body["address"] = address
        if primary_email_address is not None:
            _body["primaryEmailAddress"] = primary_email_address
        if primary_phone_number is not None:
            _body["primaryPhoneNumber"] = primary_phone_number
        if email_addresses is not None:
            _body["emailAddresses"] = email_addresses
        if phone_numbers is not None:
            _body["phoneNumbers"] = phone_numbers
        if match_code is not None:
            _body["matchCode"] = match_code
        if functions is not None:
            _body["functions"] = functions
        if opening_hours is not None:
            _body["openingHours"] = opening_hours
        if closed_days is not None:
            _body["closedDays"] = closed_days
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.patch(
            f"{_PREFIX}/Contact/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def delete_contact_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/Contact/{id}",
        )
        response.raise_for_status()

    async def search(
        self,
        text: str | None = None,
        skip: int | None = None,
        limit: int | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if text is not None:
            _params["text"] = text
        if skip is not None:
            _params["skip"] = skip
        if limit is not None:
            _params["limit"] = limit
        response = await self._http.get(
            f"{_PREFIX}/Contact/search",
            params=_params,
        )
        response.raise_for_status()

    async def get_by_function(
        self,
        function: str | None = None,
        limit: int | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if function is not None:
            _params["function"] = function
        if limit is not None:
            _params["limit"] = limit
        response = await self._http.get(
            f"{_PREFIX}/Contact/get-by-function",
            params=_params,
        )
        response.raise_for_status()

    async def create_contact(
        self,
        address: AddressModel | None = None,
        primary_email_address: EmailAddressModel | None = None,
        primary_phone_number: PhoneNumber | None = None,
        email_addresses: list[EmailAddressModel] | None = None,
        phone_numbers: list[PhoneNumberModel] | None = None,
        match_code: str | None = None,
        functions: list[str] | None = None,
        opening_hours: list[OpeningHoursModel] | None = None,
        closed_days: list[ClosedDayModel] | None = None,
        addon: dict[str, dict[str, object]] | None = None,
    ) -> ContactModel:
        _body: dict[str, object] = {
        }
        if address is not None:
            _body["address"] = address
        if primary_email_address is not None:
            _body["primaryEmailAddress"] = primary_email_address
        if primary_phone_number is not None:
            _body["primaryPhoneNumber"] = primary_phone_number
        if email_addresses is not None:
            _body["emailAddresses"] = email_addresses
        if phone_numbers is not None:
            _body["phoneNumbers"] = phone_numbers
        if match_code is not None:
            _body["matchCode"] = match_code
        if functions is not None:
            _body["functions"] = functions
        if opening_hours is not None:
            _body["openingHours"] = opening_hours
        if closed_days is not None:
            _body["closedDays"] = closed_days
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.post(
            f"{_PREFIX}/Contact",
            json=_body,
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def contact_get_by_location(
        self,
        longitude: float | None = None,
        latitude: float | None = None,
        max_distance_meter: float | None = None,
        min_distance_meter: float | None = None,
        function: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if longitude is not None:
            _params["longitude"] = longitude
        if latitude is not None:
            _params["latitude"] = latitude
        if max_distance_meter is not None:
            _params["maxDistanceMeter"] = max_distance_meter
        if min_distance_meter is not None:
            _params["minDistanceMeter"] = min_distance_meter
        if function is not None:
            _params["function"] = function
        response = await self._http.get(
            f"{_PREFIX}/Contact/get-by-location",
            params=_params,
        )
        response.raise_for_status()

    async def resolve_geo_locations(
        self,
        reset_geo_coordinates: bool | None = None,
    ) -> ContactModel:
        _body: dict[str, object] = {
        }
        if reset_geo_coordinates is not None:
            _body["resetGeoCoordinates"] = reset_geo_coordinates
        response = await self._http.post(
            f"{_PREFIX}/Contact/resolve-geo-locations",
            json=_body,
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def contact_map_get_by_location(
        self,
        longitude: float | None = None,
        latitude: float | None = None,
        max_distance_meter: float | None = None,
        min_distance_meter: float | None = None,
        group: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if longitude is not None:
            _params["longitude"] = longitude
        if latitude is not None:
            _params["latitude"] = latitude
        if max_distance_meter is not None:
            _params["maxDistanceMeter"] = max_distance_meter
        if min_distance_meter is not None:
            _params["minDistanceMeter"] = min_distance_meter
        if group is not None:
            _params["group"] = group
        response = await self._http.get(
            f"{_PREFIX}/ContactMap/get-by-location",
            params=_params,
        )
        response.raise_for_status()

    async def get_by_id(
        self,
        id: UUID | None = None,
    ) -> ContactModel:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalContact/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return ContactModel.model_validate(response.json())

    async def get_organization_settings(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/OrganizationSettings",
        )
        response.raise_for_status()

    async def get_organization_settings_by_internal_name(
        self,
        internal_name: str,
    ) -> OrganizationSettingResult:
        response = await self._http.get(
            f"{_PREFIX}/OrganizationSettings/{internal_name}",
        )
        response.raise_for_status()
        return OrganizationSettingResult.model_validate(response.json())

    async def update_organization_settings_by_internal_name(
        self,
        internal_name: str,
        value: dict[str, object] | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if value is not None:
            _body["value"] = value
        response = await self._http.put(
            f"{_PREFIX}/OrganizationSettings/{internal_name}",
            json=_body,
        )
        response.raise_for_status()
