"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    AddonFieldResponse,
    AggregatedTollResponse,
    AppointmentResponse,
    AppointmentTypeResponse,
    DailyVehicleLocationResponse,
    DepartmentResponse,
    DeploymentResponse,
    DeviceLoginResponse,
    DeviceModel,
    EmissionClassResponse,
    EndpointContract,
    EquipmentResponse,
    EquipmentTypeResponse,
    FinancialSupportStateResponse,
    FuelTypeResponse,
    GetFuelDataResponse,
    InsuranceTypeResponse,
    MonthlyMileageReportResponse,
    OrganizationSettingResult,
    ServiceObject,
    TrafficTypeResponse,
    TransmissionTypeResponse,
    VehicleApiKeyModel,
    VehicleLocationResponse,
    VehicleResponse,
    VehicleStatusResponse,
    VehicleTypeGetByAliasResponse,
    VehicleTypeResponse,
)

_PREFIX = "vehicle-api/v2"


class VehicleClient:
    """Typed client for ``vehicle-api/v2``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.vehicle import VehicleClient

        client = VehicleClient(context.http)
    """

    def __init__(self, http: SimplicOxHttpClient) -> None:
        self._http = http
    async def get_addon_field(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/AddonField",
        )
        response.raise_for_status()

    async def create_addon_field(
        self,
        object_name: str | None = None,
        property_name: str | None = None,
        property_type: str | None = None,
        description: str | None = None,
    ) -> AddonFieldResponse:
        _body: dict[str, object] = {
        }
        if object_name is not None:
            _body["objectName"] = object_name
        if property_name is not None:
            _body["propertyName"] = property_name
        if property_type is not None:
            _body["propertyType"] = property_type
        if description is not None:
            _body["description"] = description
        response = await self._http.post(
            f"{_PREFIX}/AddonField",
            json=_body,
        )
        response.raise_for_status()
        return AddonFieldResponse.model_validate(response.json())

    async def get_addon_field_by_object_name(
        self,
        object_name: str,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/AddonField/{object_name}",
        )
        response.raise_for_status()

    async def get_by_id(
        self,
        id: UUID,
    ) -> AddonFieldResponse:
        response = await self._http.get(
            f"{_PREFIX}/AddonField/by-id/{id}",
        )
        response.raise_for_status()
        return AddonFieldResponse.model_validate(response.json())

    async def update_addon_field_by_id(
        self,
        id: UUID,
        property_name: str | None = None,
        property_type: str | None = None,
        description: str | None = None,
    ) -> AddonFieldResponse:
        _body: dict[str, object] = {
        }
        if property_name is not None:
            _body["propertyName"] = property_name
        if property_type is not None:
            _body["propertyType"] = property_type
        if description is not None:
            _body["description"] = description
        response = await self._http.put(
            f"{_PREFIX}/AddonField/{id}",
            json=_body,
        )
        response.raise_for_status()
        return AddonFieldResponse.model_validate(response.json())

    async def delete_addon_field_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/AddonField/{id}",
        )
        response.raise_for_status()

    async def create(
        self,
        vehicle_id: UUID,
    ) -> VehicleApiKeyModel:
        response = await self._http.post(
            f"{_PREFIX}/ApiKey/create",
            json={"vehicleId": str(vehicle_id)},
        )
        response.raise_for_status()
        return VehicleApiKeyModel.model_validate(response.json())

    async def delete(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/ApiKey/delete/{id}",
        )
        response.raise_for_status()

    async def api_key_get_by_vehicle(
        self,
        vehicle_id: UUID,
    ) -> VehicleApiKeyModel:
        response = await self._http.get(
            f"{_PREFIX}/ApiKey/get-by-vehicle/{vehicle_id}",
        )
        response.raise_for_status()
        return VehicleApiKeyModel.model_validate(response.json())

    async def get_appointment_by_id(
        self,
        id: UUID,
    ) -> AppointmentResponse:
        response = await self._http.get(
            f"{_PREFIX}/Appointment/{id}",
        )
        response.raise_for_status()
        return AppointmentResponse.model_validate(response.json())

    async def update_appointment_by_id(
        self,
        id: UUID,
        due_date: str | None = None,
        planned_date: str | None = None,
        execution_date: str | None = None,
        type_id: UUID | None = None,
        vehicle_id: UUID | None = None,
        remark: str | None = None,
    ) -> AppointmentResponse:
        _body: dict[str, object] = {
        }
        if due_date is not None:
            _body["dueDate"] = due_date
        if planned_date is not None:
            _body["plannedDate"] = planned_date
        if execution_date is not None:
            _body["executionDate"] = execution_date
        if type_id is not None:
            _body["typeId"] = str(type_id)
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if remark is not None:
            _body["remark"] = remark
        response = await self._http.patch(
            f"{_PREFIX}/Appointment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentResponse.model_validate(response.json())

    async def delete_appointment_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/Appointment/{id}",
        )
        response.raise_for_status()

    async def create_appointment(
        self,
        due_date: str,
        type_id: UUID,
        vehicle_id: UUID,
        planned_date: str | None = None,
        execution_date: str | None = None,
        remark: str | None = None,
    ) -> AppointmentResponse:
        _body: dict[str, object] = {
            "dueDate": due_date,
            "typeId": str(type_id),
            "vehicleId": str(vehicle_id),
        }
        if planned_date is not None:
            _body["plannedDate"] = planned_date
        if execution_date is not None:
            _body["executionDate"] = execution_date
        if remark is not None:
            _body["remark"] = remark
        response = await self._http.post(
            f"{_PREFIX}/Appointment",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentResponse.model_validate(response.json())

    async def get_appointment_type_by_id(
        self,
        id: UUID,
    ) -> AppointmentTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/AppointmentType/{id}",
        )
        response.raise_for_status()
        return AppointmentTypeResponse.model_validate(response.json())

    async def update_appointment_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        interval: int | None = None,
        interval_type: str | None = None,
    ) -> AppointmentTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if interval is not None:
            _body["interval"] = interval
        if interval_type is not None:
            _body["intervalType"] = interval_type
        response = await self._http.patch(
            f"{_PREFIX}/AppointmentType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentTypeResponse.model_validate(response.json())

    async def delete_appointment_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/AppointmentType/{id}",
        )
        response.raise_for_status()

    async def get_by_interval(
        self,
        interval_type: str | None = None,
    ) -> AppointmentTypeResponse:
        _params: dict[str, object] = {}
        if interval_type is not None:
            _params["intervalType"] = interval_type
        response = await self._http.get(
            f"{_PREFIX}/AppointmentType/get-by-interval",
            params=_params,
        )
        response.raise_for_status()
        return AppointmentTypeResponse.model_validate(response.json())

    async def create_appointment_type(
        self,
        display_name: str | None = None,
        display_key: str | None = None,
        interval: int | None = None,
        interval_type: str | None = None,
    ) -> AppointmentTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if interval is not None:
            _body["interval"] = interval
        if interval_type is not None:
            _body["intervalType"] = interval_type
        response = await self._http.post(
            f"{_PREFIX}/AppointmentType",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentTypeResponse.model_validate(response.json())

    async def create_appointment_type_deployment(
        self,
        display_name: str | None = None,
        display_key: str | None = None,
        interval: int | None = None,
        interval_type: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if interval is not None:
            _body["interval"] = interval
        if interval_type is not None:
            _body["intervalType"] = interval_type
        response = await self._http.post(
            f"{_PREFIX}/AppointmentTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_appointment_type_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        interval: int | None = None,
        interval_type: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if interval is not None:
            _body["interval"] = interval
        if interval_type is not None:
            _body["intervalType"] = interval_type
        response = await self._http.patch(
            f"{_PREFIX}/AppointmentTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def create_daily_vehicle_location(
        self,
        vehicle_id: UUID,
        date: str,
        latitude: float | None = None,
        longitude: float | None = None,
        date_time: str | None = None,
        street: str | None = None,
        house_number: str | None = None,
        zipcode: str | None = None,
        district: str | None = None,
        federal_state: str | None = None,
        country: str | None = None,
        country_iso: str | None = None,
        city: str | None = None,
        fuel_level: float | None = None,
        milage: float | None = None,
    ) -> DailyVehicleLocationResponse:
        _body: dict[str, object] = {
            "vehicleId": str(vehicle_id),
            "date": date,
        }
        if latitude is not None:
            _body["latitude"] = latitude
        if longitude is not None:
            _body["longitude"] = longitude
        if date_time is not None:
            _body["dateTime"] = date_time
        if street is not None:
            _body["street"] = street
        if house_number is not None:
            _body["houseNumber"] = house_number
        if zipcode is not None:
            _body["zipcode"] = zipcode
        if district is not None:
            _body["district"] = district
        if federal_state is not None:
            _body["federalState"] = federal_state
        if country is not None:
            _body["country"] = country
        if country_iso is not None:
            _body["countryIso"] = country_iso
        if city is not None:
            _body["city"] = city
        if fuel_level is not None:
            _body["fuelLevel"] = fuel_level
        if milage is not None:
            _body["milage"] = milage
        response = await self._http.post(
            f"{_PREFIX}/DailyVehicleLocation",
            json=_body,
        )
        response.raise_for_status()
        return DailyVehicleLocationResponse.model_validate(response.json())

    async def update_daily_vehicle_location_by_vehicle_id_date(
        self,
        vehicle_id: UUID,
        date: str,
        latitude: float | None = None,
        longitude: float | None = None,
        date_time: str | None = None,
        street: str | None = None,
        house_number: str | None = None,
        zipcode: str | None = None,
        district: str | None = None,
        federal_state: str | None = None,
        country: str | None = None,
        country_iso: str | None = None,
        city: str | None = None,
        fuel_level: float | None = None,
        milage: float | None = None,
    ) -> DailyVehicleLocationResponse:
        _body: dict[str, object] = {
        }
        if latitude is not None:
            _body["latitude"] = latitude
        if longitude is not None:
            _body["longitude"] = longitude
        if date_time is not None:
            _body["dateTime"] = date_time
        if street is not None:
            _body["street"] = street
        if house_number is not None:
            _body["houseNumber"] = house_number
        if zipcode is not None:
            _body["zipcode"] = zipcode
        if district is not None:
            _body["district"] = district
        if federal_state is not None:
            _body["federalState"] = federal_state
        if country is not None:
            _body["country"] = country
        if country_iso is not None:
            _body["countryIso"] = country_iso
        if city is not None:
            _body["city"] = city
        if fuel_level is not None:
            _body["fuelLevel"] = fuel_level
        if milage is not None:
            _body["milage"] = milage
        response = await self._http.patch(
            f"{_PREFIX}/DailyVehicleLocation/{vehicle_id}/{date}",
            json=_body,
        )
        response.raise_for_status()
        return DailyVehicleLocationResponse.model_validate(response.json())

    async def get_daily_vehicle_location_by_id(
        self,
        id: UUID,
    ) -> DailyVehicleLocationResponse:
        response = await self._http.get(
            f"{_PREFIX}/DailyVehicleLocation/{id}",
        )
        response.raise_for_status()
        return DailyVehicleLocationResponse.model_validate(response.json())

    async def daily_vehicle_location_get_by_vehicle(
        self,
        vehicle_id: UUID,
        date: str,
    ) -> DailyVehicleLocationResponse:
        response = await self._http.get(
            f"{_PREFIX}/DailyVehicleLocation/by-vehicle/{vehicle_id}/{date}",
        )
        response.raise_for_status()
        return DailyVehicleLocationResponse.model_validate(response.json())

    async def daily_vehicle_location_get_by_vehicle_1(
        self,
        vehicle_id: UUID,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if date_from is not None:
            _params["dateFrom"] = date_from
        if date_to is not None:
            _params["dateTo"] = date_to
        response = await self._http.get(
            f"{_PREFIX}/DailyVehicleLocation/by-vehicle/{vehicle_id}",
            params=_params,
        )
        response.raise_for_status()

    async def recalculate(
        self,
        vehicle_id: UUID,
        from_: str | None = None,
        to: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if from_ is not None:
            _params["from"] = from_
        if to is not None:
            _params["to"] = to
        response = await self._http.post(
            f"{_PREFIX}/DailyVehicleLocation/recalculate/{vehicle_id}",
            params=_params,
        )
        response.raise_for_status()

    async def get_department_by_id(
        self,
        id: UUID,
    ) -> DepartmentResponse:
        response = await self._http.get(
            f"{_PREFIX}/Department/{id}",
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def update_department_by_id(
        self,
        id: UUID,
        name: str | None = None,
        is_selectable: bool | None = None,
        color: str | None = None,
    ) -> DepartmentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if color is not None:
            _body["color"] = color
        response = await self._http.patch(
            f"{_PREFIX}/Department/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def delete_department_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/Department/{id}",
        )
        response.raise_for_status()

    async def create_department(
        self,
        name: str,
        is_selectable: bool | None = None,
        color: str | None = None,
    ) -> DepartmentResponse:
        _body: dict[str, object] = {
            "name": name,
        }
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if color is not None:
            _body["color"] = color
        response = await self._http.post(
            f"{_PREFIX}/Department",
            json=_body,
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def create_department_deployment(
        self,
        name: str,
        is_selectable: bool | None = None,
        color: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "name": name,
        }
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if color is not None:
            _body["color"] = color
        response = await self._http.post(
            f"{_PREFIX}/DepartmentDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_department_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        is_selectable: bool | None = None,
        color: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if color is not None:
            _body["color"] = color
        response = await self._http.patch(
            f"{_PREFIX}/DepartmentDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_device_auth(
        self,
    ) -> DeviceModel:
        response = await self._http.get(
            f"{_PREFIX}/DeviceAuth",
        )
        response.raise_for_status()
        return DeviceModel.model_validate(response.json())

    async def login(
        self,
        api_key: str,
        device_id: str,
    ) -> DeviceLoginResponse:
        response = await self._http.post(
            f"{_PREFIX}/DeviceAuth/login",
            json={"apiKey": api_key, "deviceId": device_id},
        )
        response.raise_for_status()
        return DeviceLoginResponse.model_validate(response.json())

    async def refresh_token(
        self,
        token: str,
    ) -> DeviceLoginResponse:
        response = await self._http.post(
            f"{_PREFIX}/DeviceAuth/refresh-token",
            json={"token": token},
        )
        response.raise_for_status()
        return DeviceLoginResponse.model_validate(response.json())

    async def logout(
        self,
        vehicle_id: UUID,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/DeviceAuth/logout",
            json={"vehicleId": str(vehicle_id)},
        )
        response.raise_for_status()

    async def get_emission_class_by_id(
        self,
        id: UUID,
    ) -> EmissionClassResponse:
        response = await self._http.get(
            f"{_PREFIX}/EmissionClass/{id}",
        )
        response.raise_for_status()
        return EmissionClassResponse.model_validate(response.json())

    async def update_emission_class_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        is_toll_emission_class: bool | None = None,
    ) -> EmissionClassResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if is_toll_emission_class is not None:
            _body["isTollEmissionClass"] = is_toll_emission_class
        response = await self._http.patch(
            f"{_PREFIX}/EmissionClass/{id}",
            json=_body,
        )
        response.raise_for_status()
        return EmissionClassResponse.model_validate(response.json())

    async def delete_emission_class_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/EmissionClass/{id}",
        )
        response.raise_for_status()

    async def create_emission_class(
        self,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        is_toll_emission_class: bool | None = None,
    ) -> EmissionClassResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if is_toll_emission_class is not None:
            _body["isTollEmissionClass"] = is_toll_emission_class
        response = await self._http.post(
            f"{_PREFIX}/EmissionClass",
            json=_body,
        )
        response.raise_for_status()
        return EmissionClassResponse.model_validate(response.json())

    async def create_emission_class_deployment(
        self,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        is_toll_emission_class: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if is_toll_emission_class is not None:
            _body["isTollEmissionClass"] = is_toll_emission_class
        response = await self._http.post(
            f"{_PREFIX}/EmissionClassDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_emission_class_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        is_toll_emission_class: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if is_toll_emission_class is not None:
            _body["isTollEmissionClass"] = is_toll_emission_class
        response = await self._http.patch(
            f"{_PREFIX}/EmissionClassDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_equipment_by_id(
        self,
        id: UUID,
    ) -> EquipmentResponse:
        response = await self._http.get(
            f"{_PREFIX}/Equipment/{id}",
        )
        response.raise_for_status()
        return EquipmentResponse.model_validate(response.json())

    async def update_equipment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        equipment_type_id: UUID | None = None,
        vehicle_id: UUID | None = None,
    ) -> EquipmentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if equipment_type_id is not None:
            _body["equipmentTypeId"] = str(equipment_type_id)
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        response = await self._http.patch(
            f"{_PREFIX}/Equipment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return EquipmentResponse.model_validate(response.json())

    async def delete_equipment_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/Equipment/{id}",
        )
        response.raise_for_status()

    async def create_equipment(
        self,
        name: str | None = None,
        number: str | None = None,
        equipment_type_id: UUID | None = None,
        vehicle_id: UUID | None = None,
    ) -> EquipmentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if equipment_type_id is not None:
            _body["equipmentTypeId"] = str(equipment_type_id)
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        response = await self._http.post(
            f"{_PREFIX}/Equipment",
            json=_body,
        )
        response.raise_for_status()
        return EquipmentResponse.model_validate(response.json())

    async def get_equipment_type_by_id(
        self,
        id: UUID,
    ) -> EquipmentTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/EquipmentType/{id}",
        )
        response.raise_for_status()
        return EquipmentTypeResponse.model_validate(response.json())

    async def update_equipment_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
    ) -> EquipmentTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        response = await self._http.patch(
            f"{_PREFIX}/EquipmentType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return EquipmentTypeResponse.model_validate(response.json())

    async def delete_equipment_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/EquipmentType/{id}",
        )
        response.raise_for_status()

    async def create_equipment_type(
        self,
        display_name: str | None = None,
        display_key: str | None = None,
    ) -> EquipmentTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        response = await self._http.post(
            f"{_PREFIX}/EquipmentType",
            json=_body,
        )
        response.raise_for_status()
        return EquipmentTypeResponse.model_validate(response.json())

    async def get_financial_support_state_by_id(
        self,
        id: UUID,
    ) -> FinancialSupportStateResponse:
        response = await self._http.get(
            f"{_PREFIX}/FinancialSupportState/{id}",
        )
        response.raise_for_status()
        return FinancialSupportStateResponse.model_validate(response.json())

    async def update_financial_support_state_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> FinancialSupportStateResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/FinancialSupportState/{id}",
            json=_body,
        )
        response.raise_for_status()
        return FinancialSupportStateResponse.model_validate(response.json())

    async def delete_financial_support_state_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/FinancialSupportState/{id}",
        )
        response.raise_for_status()

    async def create_financial_support_state(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> FinancialSupportStateResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/FinancialSupportState",
            json=_body,
        )
        response.raise_for_status()
        return FinancialSupportStateResponse.model_validate(response.json())

    async def create_financial_support_state_deployment(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/FinancialSupportStateDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_financial_support_state_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/FinancialSupportStateDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def create_fuel_data(
        self,
        vehicle_id: UUID,
        fuel_level_percent: float,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/FuelData",
            json={"vehicleId": str(vehicle_id), "fuelLevelPercent": fuel_level_percent},
        )
        response.raise_for_status()

    async def get_fuel_data_by_vehicle_id(
        self,
        vehicle_id: UUID,
    ) -> GetFuelDataResponse:
        response = await self._http.get(
            f"{_PREFIX}/FuelData/{vehicle_id}",
        )
        response.raise_for_status()
        return GetFuelDataResponse.model_validate(response.json())

    async def get_fuel_type_by_id(
        self,
        id: UUID,
    ) -> FuelTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/FuelType/{id}",
        )
        response.raise_for_status()
        return FuelTypeResponse.model_validate(response.json())

    async def update_fuel_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        code: str | None = None,
    ) -> FuelTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/FuelType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return FuelTypeResponse.model_validate(response.json())

    async def delete_fuel_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/FuelType/{id}",
        )
        response.raise_for_status()

    async def create_fuel_type(
        self,
        display_name: str,
        code: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> FuelTypeResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
            "code": code,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/FuelType",
            json=_body,
        )
        response.raise_for_status()
        return FuelTypeResponse.model_validate(response.json())

    async def create_fuel_type_deployment(
        self,
        display_name: str,
        code: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
            "code": code,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/FuelTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_fuel_type_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        code: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/FuelTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_insurance_type_by_id(
        self,
        id: UUID,
    ) -> InsuranceTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/InsuranceType/{id}",
        )
        response.raise_for_status()
        return InsuranceTypeResponse.model_validate(response.json())

    async def update_insurance_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> InsuranceTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/InsuranceType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return InsuranceTypeResponse.model_validate(response.json())

    async def delete_insurance_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/InsuranceType/{id}",
        )
        response.raise_for_status()

    async def create_insurance_type(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> InsuranceTypeResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/InsuranceType",
            json=_body,
        )
        response.raise_for_status()
        return InsuranceTypeResponse.model_validate(response.json())

    async def create_insurance_type_deployment(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/InsuranceTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_insurance_type_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/InsuranceTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_internal_vehicle(
        self,
        id: UUID | None = None,
    ) -> VehicleResponse:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalVehicle",
            params=_params,
        )
        response.raise_for_status()
        return VehicleResponse.model_validate(response.json())

    async def get_internal_vehicle_type_by_id(
        self,
        id: UUID,
    ) -> VehicleTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalVehicleType/{id}",
        )
        response.raise_for_status()
        return VehicleTypeResponse.model_validate(response.json())

    async def internal_vehicle_type_get_by_alias(
        self,
        alias: str,
    ) -> VehicleTypeGetByAliasResponse:
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalVehicleType/get-by-alias/{alias}",
        )
        response.raise_for_status()
        return VehicleTypeGetByAliasResponse.model_validate(response.json())

    async def get_id(
        self,
        id: UUID,
    ) -> MonthlyMileageReportResponse:
        response = await self._http.get(
            f"{_PREFIX}/MonthlyMileageReport/id/{id}",
        )
        response.raise_for_status()
        return MonthlyMileageReportResponse.model_validate(response.json())

    async def get_monthly_mileage_report_by_vehicle_id_year_month(
        self,
        vehicle_id: UUID,
        year: int,
        month: int,
    ) -> MonthlyMileageReportResponse:
        response = await self._http.get(
            f"{_PREFIX}/MonthlyMileageReport/{vehicle_id}/{year}/{month}",
        )
        response.raise_for_status()
        return MonthlyMileageReportResponse.model_validate(response.json())

    async def get_monthly_mileage_report_by_vehicle_id(
        self,
        vehicle_id: UUID,
        year: int | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if year is not None:
            _params["year"] = year
        response = await self._http.get(
            f"{_PREFIX}/MonthlyMileageReport/{vehicle_id}",
            params=_params,
        )
        response.raise_for_status()

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

    async def get_endpoint_contracts(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/ServiceContract/endpoint-contracts",
        )
        response.raise_for_status()

    async def get_endpoint_contract(
        self,
        contract_name: str,
    ) -> EndpointContract:
        response = await self._http.get(
            f"{_PREFIX}/ServiceContract/{contract_name}/endpoint-contract",
        )
        response.raise_for_status()
        return EndpointContract.model_validate(response.json())

    async def endpoint_contract(
        self,
        contract_name: str,
        endpoint: str,
        provider_name: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
            "contractName": contract_name,
            "endpoint": endpoint,
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        response = await self._http.post(
            f"{_PREFIX}/ServiceContract/endpoint-contract",
            json=_body,
        )
        response.raise_for_status()

    async def get_service_definition(
        self,
    ) -> ServiceObject:
        response = await self._http.get(
            f"{_PREFIX}/ServiceDefinition",
        )
        response.raise_for_status()
        return ServiceObject.model_validate(response.json())

    async def get_graphql_sdl(
        self,
    ) -> ServiceObject:
        response = await self._http.get(
            f"{_PREFIX}/ServiceDefinition/graphql/sdl",
        )
        response.raise_for_status()
        return ServiceObject.model_validate(response.json())

    async def register_service(
        self,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/ServiceDefinition/register-service",
        )
        response.raise_for_status()

    async def get_traffic_type_by_id(
        self,
        id: UUID,
    ) -> TrafficTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/TrafficType/{id}",
        )
        response.raise_for_status()
        return TrafficTypeResponse.model_validate(response.json())

    async def update_traffic_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> TrafficTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/TrafficType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TrafficTypeResponse.model_validate(response.json())

    async def delete_traffic_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/TrafficType/{id}",
        )
        response.raise_for_status()

    async def create_traffic_type(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> TrafficTypeResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/TrafficType",
            json=_body,
        )
        response.raise_for_status()
        return TrafficTypeResponse.model_validate(response.json())

    async def create_traffic_type_deployment(
        self,
        display_name: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/TrafficTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_traffic_type_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/TrafficTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_transmission_type_by_id(
        self,
        id: UUID,
    ) -> TransmissionTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/TransmissionType/{id}",
        )
        response.raise_for_status()
        return TransmissionTypeResponse.model_validate(response.json())

    async def update_transmission_type_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        code: str | None = None,
    ) -> TransmissionTypeResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/TransmissionType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TransmissionTypeResponse.model_validate(response.json())

    async def delete_transmission_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/TransmissionType/{id}",
        )
        response.raise_for_status()

    async def create_transmission_type(
        self,
        display_name: str,
        code: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> TransmissionTypeResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
            "code": code,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/TransmissionType",
            json=_body,
        )
        response.raise_for_status()
        return TransmissionTypeResponse.model_validate(response.json())

    async def create_transmission_type_deployment(
        self,
        display_name: str,
        code: str,
        display_key: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
            "displayName": display_name,
            "code": code,
        }
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/TransmissionTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_transmission_type_deployment_by_id(
        self,
        id: UUID,
        display_name: str | None = None,
        display_key: str | None = None,
        is_selectable: bool | None = None,
        code: str | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/TransmissionTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_vehicle_by_id(
        self,
        id: UUID,
    ) -> VehicleResponse:
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/{id}",
        )
        response.raise_for_status()
        return VehicleResponse.model_validate(response.json())

    async def update_vehicle_by_id(
        self,
        id: UUID,
        location: str | None = None,
        match_code: str | None = None,
        status_id: UUID | None = None,
        mileage: float | None = None,
        mileage_date: str | None = None,
        operating_hours: float | None = None,
        fuel_tank_capacity: int | None = None,
        remark: str | None = None,
        disposition_sorting_key: str | None = None,
        year_of_manufacturing: str | None = None,
        registration_document: str | None = None,
        vehicle_registration: str | None = None,
        is_system_vehicle: bool | None = None,
        department_id: UUID | None = None,
        carrier_id: UUID | None = None,
        phone_number: str | None = None,
        e_mail_address: str | None = None,
        financial_support_state_id: UUID | None = None,
        traffic_type_id: UUID | None = None,
        fuel_type_id: UUID | None = None,
        transmission_type_id: UUID | None = None,
        insurance_type_id: UUID | None = None,
        emission_class_id: UUID | None = None,
        vehicle_type_id: UUID | None = None,
        vehicle_sub_type_id: UUID | None = None,
        additional_technical_data: AdditionalTechnicalDataModel | None = None,
        registration_certificate: RegistrationCertificateModel | None = None,
        registration_plate: RegistrationPlateModel | None = None,
        registration_document_location: str | None = None,
        toll: TollModel | None = None,
        usable_until: str | None = None,
        loading_slots: list[PatchLoadingSlotRequest] | None = None,
        appointments: list[PatchVehicleAppointmentRequest] | None = None,
        qr_code: str | None = None,
        addon: dict[str, object] | None = None,
    ) -> VehicleResponse:
        _body: dict[str, object] = {
        }
        if location is not None:
            _body["location"] = location
        if match_code is not None:
            _body["matchCode"] = match_code
        if status_id is not None:
            _body["statusId"] = str(status_id)
        if mileage is not None:
            _body["mileage"] = mileage
        if mileage_date is not None:
            _body["mileageDate"] = mileage_date
        if operating_hours is not None:
            _body["operatingHours"] = operating_hours
        if fuel_tank_capacity is not None:
            _body["fuelTankCapacity"] = fuel_tank_capacity
        if remark is not None:
            _body["remark"] = remark
        if disposition_sorting_key is not None:
            _body["dispositionSortingKey"] = disposition_sorting_key
        if year_of_manufacturing is not None:
            _body["yearOfManufacturing"] = year_of_manufacturing
        if registration_document is not None:
            _body["registrationDocument"] = registration_document
        if vehicle_registration is not None:
            _body["vehicleRegistration"] = vehicle_registration
        if is_system_vehicle is not None:
            _body["isSystemVehicle"] = is_system_vehicle
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if carrier_id is not None:
            _body["carrierId"] = str(carrier_id)
        if phone_number is not None:
            _body["phoneNumber"] = phone_number
        if e_mail_address is not None:
            _body["eMailAddress"] = e_mail_address
        if financial_support_state_id is not None:
            _body["financialSupportStateId"] = str(financial_support_state_id)
        if traffic_type_id is not None:
            _body["trafficTypeId"] = str(traffic_type_id)
        if fuel_type_id is not None:
            _body["fuelTypeId"] = str(fuel_type_id)
        if transmission_type_id is not None:
            _body["transmissionTypeId"] = str(transmission_type_id)
        if insurance_type_id is not None:
            _body["insuranceTypeId"] = str(insurance_type_id)
        if emission_class_id is not None:
            _body["emissionClassId"] = str(emission_class_id)
        if vehicle_type_id is not None:
            _body["vehicleTypeId"] = str(vehicle_type_id)
        if vehicle_sub_type_id is not None:
            _body["vehicleSubTypeId"] = str(vehicle_sub_type_id)
        if additional_technical_data is not None:
            _body["additionalTechnicalData"] = additional_technical_data
        if registration_certificate is not None:
            _body["registrationCertificate"] = registration_certificate
        if registration_plate is not None:
            _body["registrationPlate"] = registration_plate
        if registration_document_location is not None:
            _body["registrationDocumentLocation"] = registration_document_location
        if toll is not None:
            _body["toll"] = toll
        if usable_until is not None:
            _body["usableUntil"] = usable_until
        if loading_slots is not None:
            _body["loadingSlots"] = loading_slots
        if appointments is not None:
            _body["appointments"] = appointments
        if qr_code is not None:
            _body["qrCode"] = qr_code
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.patch(
            f"{_PREFIX}/Vehicle/{id}",
            json=_body,
        )
        response.raise_for_status()
        return VehicleResponse.model_validate(response.json())

    async def delete_vehicle_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/Vehicle/{id}",
        )
        response.raise_for_status()

    async def create_vehicle(
        self,
        vehicle_type_id: UUID,
        vehicle_sub_type_id: UUID,
        location: str | None = None,
        match_code: str | None = None,
        status_id: UUID | None = None,
        mileage: float | None = None,
        mileage_date: str | None = None,
        operating_hours: float | None = None,
        fuel_tank_capacity: int | None = None,
        remark: str | None = None,
        disposition_sorting_key: str | None = None,
        year_of_manufacturing: str | None = None,
        registration_document: str | None = None,
        vehicle_registration: str | None = None,
        is_system_vehicle: bool | None = None,
        department_id: UUID | None = None,
        carrier_id: UUID | None = None,
        phone_number: str | None = None,
        e_mail_address: str | None = None,
        financial_support_state_id: UUID | None = None,
        traffic_type_id: UUID | None = None,
        fuel_type_id: UUID | None = None,
        transmission_type_id: UUID | None = None,
        insurance_type_id: UUID | None = None,
        emission_class_id: UUID | None = None,
        additional_technical_data: AdditionalTechnicalDataModel | None = None,
        registration_certificate: RegistrationCertificateModel | None = None,
        registration_plate: RegistrationPlateModel | None = None,
        registration_document_location: str | None = None,
        toll: TollModel | None = None,
        appointments: list[CreateVehicleAppointmentRequest] | None = None,
        usable_until: str | None = None,
        loading_slots: list[CreateLoadingSlotRequest] | None = None,
        qr_code: str | None = None,
        addon: dict[str, dict[str, object]] | None = None,
    ) -> VehicleResponse:
        _body: dict[str, object] = {
            "vehicleTypeId": str(vehicle_type_id),
            "vehicleSubTypeId": str(vehicle_sub_type_id),
        }
        if location is not None:
            _body["location"] = location
        if match_code is not None:
            _body["matchCode"] = match_code
        if status_id is not None:
            _body["statusId"] = str(status_id)
        if mileage is not None:
            _body["mileage"] = mileage
        if mileage_date is not None:
            _body["mileageDate"] = mileage_date
        if operating_hours is not None:
            _body["operatingHours"] = operating_hours
        if fuel_tank_capacity is not None:
            _body["fuelTankCapacity"] = fuel_tank_capacity
        if remark is not None:
            _body["remark"] = remark
        if disposition_sorting_key is not None:
            _body["dispositionSortingKey"] = disposition_sorting_key
        if year_of_manufacturing is not None:
            _body["yearOfManufacturing"] = year_of_manufacturing
        if registration_document is not None:
            _body["registrationDocument"] = registration_document
        if vehicle_registration is not None:
            _body["vehicleRegistration"] = vehicle_registration
        if is_system_vehicle is not None:
            _body["isSystemVehicle"] = is_system_vehicle
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if carrier_id is not None:
            _body["carrierId"] = str(carrier_id)
        if phone_number is not None:
            _body["phoneNumber"] = phone_number
        if e_mail_address is not None:
            _body["eMailAddress"] = e_mail_address
        if financial_support_state_id is not None:
            _body["financialSupportStateId"] = str(financial_support_state_id)
        if traffic_type_id is not None:
            _body["trafficTypeId"] = str(traffic_type_id)
        if fuel_type_id is not None:
            _body["fuelTypeId"] = str(fuel_type_id)
        if transmission_type_id is not None:
            _body["transmissionTypeId"] = str(transmission_type_id)
        if insurance_type_id is not None:
            _body["insuranceTypeId"] = str(insurance_type_id)
        if emission_class_id is not None:
            _body["emissionClassId"] = str(emission_class_id)
        if additional_technical_data is not None:
            _body["additionalTechnicalData"] = additional_technical_data
        if registration_certificate is not None:
            _body["registrationCertificate"] = registration_certificate
        if registration_plate is not None:
            _body["registrationPlate"] = registration_plate
        if registration_document_location is not None:
            _body["registrationDocumentLocation"] = registration_document_location
        if toll is not None:
            _body["toll"] = toll
        if appointments is not None:
            _body["appointments"] = appointments
        if usable_until is not None:
            _body["usableUntil"] = usable_until
        if loading_slots is not None:
            _body["loadingSlots"] = loading_slots
        if qr_code is not None:
            _body["qrCode"] = qr_code
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.post(
            f"{_PREFIX}/Vehicle",
            json=_body,
        )
        response.raise_for_status()
        return VehicleResponse.model_validate(response.json())

    async def get_filtered_with_paging(
        self,
        search_text: str | None = None,
        skip: int | None = None,
        limit: int | None = None,
        is_deleted: bool | None = None,
        registration_plate_required: bool | None = None,
        only_registered: bool | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if search_text is not None:
            _params["searchText"] = search_text
        if skip is not None:
            _params["skip"] = skip
        if limit is not None:
            _params["limit"] = limit
        if is_deleted is not None:
            _params["isDeleted"] = is_deleted
        if registration_plate_required is not None:
            _params["registrationPlateRequired"] = registration_plate_required
        if only_registered is not None:
            _params["onlyRegistered"] = only_registered
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/get-filtered-with-paging",
            params=_params,
        )
        response.raise_for_status()

    async def get_count_of_vehicles(
        self,
        search_text: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if search_text is not None:
            _params["searchText"] = search_text
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/get-count-of-vehicles",
            params=_params,
        )
        response.raise_for_status()

    async def get_fleet_age(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/get-fleet-age",
        )
        response.raise_for_status()

    async def get_by_qrcode(
        self,
        q_r_code: str | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if q_r_code is not None:
            _params["qRCode"] = q_r_code
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/get-by-qrcode",
            params=_params,
        )
        response.raise_for_status()

    async def calculate_toll(
        self,
        vehicle_id: UUID | None = None,
        start_calculation_from: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if start_calculation_from is not None:
            _body["startCalculationFrom"] = start_calculation_from
        response = await self._http.post(
            f"{_PREFIX}/Vehicle/calculate-toll",
            json=_body,
        )
        response.raise_for_status()

    async def get_aggregated_toll(
        self,
        vehicle_id: UUID,
        start_date_time: str,
        end_date_time: str,
        include_locations: bool | None = None,
    ) -> AggregatedTollResponse:
        _params: dict[str, object] = {}
        _params["startDateTime"] = start_date_time
        _params["endDateTime"] = end_date_time
        if include_locations is not None:
            _params["includeLocations"] = include_locations
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/{vehicle_id}/aggregated-toll",
            params=_params,
        )
        response.raise_for_status()
        return AggregatedTollResponse.model_validate(response.json())

    async def get_toll_gpx_file(
        self,
        vehicle_id: UUID,
        start_date_time: str,
        end_date_time: str,
    ) -> AggregatedTollResponse:
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/{vehicle_id}/toll-gpx-file",
            params={"startDateTime": start_date_time, "endDateTime": end_date_time},
        )
        response.raise_for_status()
        return AggregatedTollResponse.model_validate(response.json())

    async def get_appointments(
        self,
        vehicle_id: UUID,
        states: str | None = None,
        type_id: UUID | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if states is not None:
            _params["states"] = states
        if type_id is not None:
            _params["typeId"] = str(type_id)
        response = await self._http.get(
            f"{_PREFIX}/Vehicle/{vehicle_id}/appointments",
            params=_params,
        )
        response.raise_for_status()

    async def create_vehicle_location(
        self,
        vehicle_id: UUID | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        date_time: str | None = None,
        street: str | None = None,
        house_number: str | None = None,
        zipcode: str | None = None,
        district: str | None = None,
        federal_state: str | None = None,
        country: str | None = None,
        country_iso: str | None = None,
        city: str | None = None,
        fuel_level: float | None = None,
        milage: float | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if latitude is not None:
            _body["latitude"] = latitude
        if longitude is not None:
            _body["longitude"] = longitude
        if date_time is not None:
            _body["dateTime"] = date_time
        if street is not None:
            _body["street"] = street
        if house_number is not None:
            _body["houseNumber"] = house_number
        if zipcode is not None:
            _body["zipcode"] = zipcode
        if district is not None:
            _body["district"] = district
        if federal_state is not None:
            _body["federalState"] = federal_state
        if country is not None:
            _body["country"] = country
        if country_iso is not None:
            _body["countryIso"] = country_iso
        if city is not None:
            _body["city"] = city
        if fuel_level is not None:
            _body["fuelLevel"] = fuel_level
        if milage is not None:
            _body["milage"] = milage
        response = await self._http.post(
            f"{_PREFIX}/VehicleLocation",
            json=_body,
        )
        response.raise_for_status()

    async def get_vehicle_location_by_vehicle_id(
        self,
        vehicle_id: UUID,
    ) -> VehicleLocationResponse:
        response = await self._http.get(
            f"{_PREFIX}/VehicleLocation/{vehicle_id}",
        )
        response.raise_for_status()
        return VehicleLocationResponse.model_validate(response.json())

    async def get_vehicle_status_by_id(
        self,
        id: UUID,
    ) -> VehicleStatusResponse:
        response = await self._http.get(
            f"{_PREFIX}/VehicleStatus/{id}",
        )
        response.raise_for_status()
        return VehicleStatusResponse.model_validate(response.json())

    async def update_vehicle_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        hex_color: str | None = None,
        is_selectable: bool | None = None,
    ) -> VehicleStatusResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/VehicleStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return VehicleStatusResponse.model_validate(response.json())

    async def delete_vehicle_status_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/VehicleStatus/{id}",
        )
        response.raise_for_status()

    async def create_vehicle_status(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        hex_color: str | None = None,
        is_selectable: bool | None = None,
    ) -> VehicleStatusResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/VehicleStatus",
            json=_body,
        )
        response.raise_for_status()
        return VehicleStatusResponse.model_validate(response.json())

    async def vehicle_status_get_all(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/VehicleStatus/get-all",
        )
        response.raise_for_status()

    async def create_vehicle_status_deployment(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        hex_color: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.post(
            f"{_PREFIX}/VehicleStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_vehicle_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        hex_color: str | None = None,
        is_selectable: bool | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        response = await self._http.patch(
            f"{_PREFIX}/VehicleStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def get_vehicle_type_by_id(
        self,
        id: UUID,
    ) -> VehicleTypeResponse:
        response = await self._http.get(
            f"{_PREFIX}/VehicleType/{id}",
        )
        response.raise_for_status()
        return VehicleTypeResponse.model_validate(response.json())

    async def update_vehicle_type_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        vehicle_sub_type: list[PatchVehicleSubTypeRequest] | None = None,
    ) -> VehicleTypeResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if vehicle_sub_type is not None:
            _body["vehicleSubType"] = vehicle_sub_type
        response = await self._http.patch(
            f"{_PREFIX}/VehicleType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return VehicleTypeResponse.model_validate(response.json())

    async def delete_vehicle_type_by_id(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.delete(
            f"{_PREFIX}/VehicleType/{id}",
        )
        response.raise_for_status()

    async def create_vehicle_type(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        vehicle_sub_type: list[CreateVehicleSubTypeRequest] | None = None,
    ) -> VehicleTypeResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if vehicle_sub_type is not None:
            _body["vehicleSubType"] = vehicle_sub_type
        response = await self._http.post(
            f"{_PREFIX}/VehicleType",
            json=_body,
        )
        response.raise_for_status()
        return VehicleTypeResponse.model_validate(response.json())

    async def vehicle_type_get_all(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/VehicleType/get-all",
        )
        response.raise_for_status()

    async def vehicle_type_get_by_alias(
        self,
        alias: str,
    ) -> VehicleTypeGetByAliasResponse:
        response = await self._http.get(
            f"{_PREFIX}/VehicleType/get-by-alias/{alias}",
        )
        response.raise_for_status()
        return VehicleTypeGetByAliasResponse.model_validate(response.json())

    async def create_vehicle_type_deployment(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        vehicle_sub_type: list[CreateVehicleSubTypeDeploymentRequest] | None = None,
    ) -> DeploymentResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if vehicle_sub_type is not None:
            _body["vehicleSubType"] = vehicle_sub_type
        response = await self._http.post(
            f"{_PREFIX}/VehicleTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return DeploymentResponse.model_validate(response.json())

    async def update_vehicle_type_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        vehicle_sub_type: list[PatchVehicleSubTypeRequest] | None = None,
    ) -> VehicleTypeResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if vehicle_sub_type is not None:
            _body["vehicleSubType"] = vehicle_sub_type
        response = await self._http.patch(
            f"{_PREFIX}/VehicleTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return VehicleTypeResponse.model_validate(response.json())
