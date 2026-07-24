"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class AdditionalTechnicalDataModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    empty_weight: float | None = Field(None, alias="emptyWeight")
    total_weight: float | None = Field(None, alias="totalWeight")
    tire_amount: int | None = Field(None, alias="tireAmount")
    tire_size_steering_axle: float | None = Field(None, alias="tireSizeSteeringAxle")
    tire_size_lift_axle: float | None = Field(None, alias="tireSizeLiftAxle")
    tire_size_drive_axle: float | None = Field(None, alias="tireSizeDriveAxle")
    payload: float | None = None
    fuel_amount: float | None = Field(None, alias="fuelAmount")
    rim_size_axle1: str | None = Field(None, alias="rimSizeAxle1")
    rim_size_axle2: str | None = Field(None, alias="rimSizeAxle2")
    rim_size_axle3: str | None = Field(None, alias="rimSizeAxle3")
    frame_color: str | None = Field(None, alias="frameColor")
    vehicle_execution: str | None = Field(None, alias="vehicleExecution")
    has_fixed_superstructure: bool | None = Field(None, alias="hasFixedSuperstructure")
    superstructure_parking_spaces: int | None = Field(None, alias="superstructureParkingSpaces")
    superstructure_volume: float | None = Field(None, alias="superstructureVolume")
    superstructure_inside_length: float | None = Field(None, alias="superstructureInsideLength")
    superstructure_inside_width: float | None = Field(None, alias="superstructureInsideWidth")
    superstructure_inside_height: float | None = Field(None, alias="superstructureInsideHeight")
    superstructure_loading_height_back: float | None = Field(None, alias="superstructureLoadingHeightBack")
    superstructure_loading_height_front: float | None = Field(None, alias="superstructureLoadingHeightFront")
    superstructure_tire_amount: int | None = Field(None, alias="superstructureTireAmount")
    superstructure_tire_size_normal_axis: float | None = Field(None, alias="superstructureTireSizeNormalAxis")
    superstructure_tire_size_lift_axle: float | None = Field(None, alias="superstructureTireSizeLiftAxle")

class AddonFieldResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class Address(BaseModel):
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

class AggregatedTollResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle: VehicleSubSet | None = None
    start: VehicleLocation | None = None
    end: VehicleLocation | None = None
    total_distance: float | None = Field(None, alias="totalDistance")
    total_costs: float | None = Field(None, alias="totalCosts")
    locations: list[VehicleLocation] | None = None

class AppointmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    due_date: datetime | None = Field(None, alias="dueDate")
    due_value: int | None = Field(None, alias="dueValue")
    execution_value: int | None = Field(None, alias="executionValue")
    planned_date: datetime | None = Field(None, alias="plannedDate")
    execution_date: datetime | None = Field(None, alias="executionDate")
    type: AppointmentTypeResponse | None = None
    vehicle: VehicleSubSet | None = None
    remark: str | None = None
    state: str | None = None

class AppointmentTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    interval_type: str | None = Field(None, alias="intervalType")
    interval: int | None = None

class CalculateTollRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    start_calculation_from: datetime | None = Field(None, alias="startCalculationFrom")

class CarrierContact(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_id: UUID | None = Field(None, alias="contactId")
    address: Address | None = None

class CreateAddonFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class CreateAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    due_date: datetime = Field(alias="dueDate")
    type_id: UUID = Field(alias="typeId")
    vehicle_id: UUID = Field(alias="vehicleId")
    planned_date: datetime | None = Field(None, alias="plannedDate")
    execution_date: datetime | None = Field(None, alias="executionDate")
    remark: str | None = None

class CreateAppointmentTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    interval: int | None = None
    interval_type: str | None = Field(None, alias="intervalType")

class CreateDepartmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    is_selectable: bool | None = Field(None, alias="isSelectable")
    color: str | None = None

class CreateEmissionClassRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_toll_emission_class: bool | None = Field(None, alias="isTollEmissionClass")

class CreateEquipmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    equipment_type_id: UUID | None = Field(None, alias="equipmentTypeId")
    vehicle_id: UUID | None = Field(None, alias="vehicleId")

class CreateEquipmentTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class CreateFinancialSupportStateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateFuelTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    code: str
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateInsuranceTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateLoadingSlotRequest(BaseModel):
    name: str | None = None
    description: str | None = None

class CreateTrafficTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateTransmissionTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str = Field(alias="displayName")
    code: str
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateVehicleApiKeyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID = Field(alias="vehicleId")

class CreateVehicleAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    appointment_type_id: UUID = Field(alias="appointmentTypeId")
    last_date: datetime | None = Field(None, alias="lastDate")
    next_date: datetime | None = Field(None, alias="nextDate")
    remark: str | None = None
    supplier_guid: UUID | None = Field(None, alias="supplierGuid")
    last_value: int | None = Field(None, alias="lastValue")
    next_value: int | None = Field(None, alias="nextValue")
    check_type: int | None = Field(None, alias="checkType")

class CreateVehicleRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_type_id: UUID = Field(alias="vehicleTypeId")
    vehicle_sub_type_id: UUID = Field(alias="vehicleSubTypeId")
    location: str | None = None
    match_code: str | None = Field(None, alias="matchCode")
    status_id: UUID | None = Field(None, alias="statusId")
    mileage: float | None = None
    mileage_date: datetime | None = Field(None, alias="mileageDate")
    operating_hours: float | None = Field(None, alias="operatingHours")
    fuel_tank_capacity: int | None = Field(None, alias="fuelTankCapacity")
    remark: str | None = None
    disposition_sorting_key: str | None = Field(None, alias="dispositionSortingKey")
    year_of_manufacturing: datetime | None = Field(None, alias="yearOfManufacturing")
    registration_document: str | None = Field(None, alias="registrationDocument")
    vehicle_registration: str | None = Field(None, alias="vehicleRegistration")
    is_system_vehicle: bool | None = Field(None, alias="isSystemVehicle")
    department_id: UUID | None = Field(None, alias="departmentId")
    carrier_id: UUID | None = Field(None, alias="carrierId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    e_mail_address: str | None = Field(None, alias="eMailAddress")
    financial_support_state_id: UUID | None = Field(None, alias="financialSupportStateId")
    traffic_type_id: UUID | None = Field(None, alias="trafficTypeId")
    fuel_type_id: UUID | None = Field(None, alias="fuelTypeId")
    transmission_type_id: UUID | None = Field(None, alias="transmissionTypeId")
    insurance_type_id: UUID | None = Field(None, alias="insuranceTypeId")
    emission_class_id: UUID | None = Field(None, alias="emissionClassId")
    additional_technical_data: AdditionalTechnicalDataModel | None = Field(None, alias="additionalTechnicalData")
    registration_certificate: RegistrationCertificateModel | None = Field(None, alias="registrationCertificate")
    registration_plate: RegistrationPlateModel | None = Field(None, alias="registrationPlate")
    registration_document_location: str | None = Field(None, alias="registrationDocumentLocation")
    toll: TollModel | None = None
    appointments: list[CreateVehicleAppointmentRequest] | None = None
    usable_until: datetime | None = Field(None, alias="usableUntil")
    loading_slots: list[CreateLoadingSlotRequest] | None = Field(None, alias="loadingSlots")
    qr_code: str | None = Field(None, alias="qrCode")
    addon: dict[str, dict[str, object]] | None = None

class CreateVehicleStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    hex_color: str | None = Field(None, alias="hexColor")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class CreateVehicleSubTypeDeploymentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    alias: list[str] | None = None
    item_deployment_id: str | None = Field(None, alias="itemDeploymentId")

class CreateVehicleSubTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    alias: list[str] | None = None

class CreateVehicleTypeDeploymentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    vehicle_sub_type: list[CreateVehicleSubTypeDeploymentRequest] | None = Field(None, alias="vehicleSubType")

class CreateVehicleTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    vehicle_sub_type: list[CreateVehicleSubTypeRequest] | None = Field(None, alias="vehicleSubType")

class DailyVehicleLocationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    date: datetime | None = None
    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None
    vehicle_match_code: str | None = Field(None, alias="vehicleMatchCode")
    vehicle_registration_plate: str | None = Field(None, alias="vehicleRegistrationPlate")
    vehicle_addon_data: dict[str, dict[str, object]] | None = Field(None, alias="vehicleAddonData")

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    is_selectable: bool | None = Field(None, alias="isSelectable")
    color: str | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class DeploymentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    item_deployment_responses: list[IItemDeploymentResponse] | None = Field(None, alias="itemDeploymentResponses")

class DeviceLoginRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    api_key: str = Field(alias="apiKey")
    device_id: str = Field(alias="deviceId")

class DeviceLoginResponse(BaseModel):
    token: str | None = None
    scheme: str | None = None

class DeviceLogoutRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID = Field(alias="vehicleId")

class DeviceModel(BaseModel):
    vehicles: list[DeviceVehicleModel] | None = None

class DeviceVehicleModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    match_code: str | None = Field(None, alias="matchCode")
    registration_plate: str | None = Field(None, alias="registrationPlate")
    type: str | None = None

class EmissionClassResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_toll_emission_class: bool | None = Field(None, alias="isTollEmissionClass")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class EndpointContract(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    name: str | None = None
    endpoint: str | None = None
    provider_name: str | None = Field(None, alias="providerName")

class EndpointContractDefinition(BaseModel):
    name: str | None = None
    endpoint: str | None = None

class EquipmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: str | None = None
    equipment_type: EquipmentTypeResponse | None = Field(None, alias="equipmentType")

class EquipmentTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class FinancialSupportStateResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class FuelTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    code: str | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class GetFuelDataResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    fuel_level_percent: float | None = Field(None, alias="fuelLevelPercent")
    date_time: datetime | None = Field(None, alias="dateTime")

class GrpcDefinitions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    package: str | None = None
    service: str | None = None
    proto_file: str | None = Field(None, alias="protoFile")

class IItemDeploymentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    item_deployment_id: str | None = Field(None, alias="itemDeploymentId")

class InsuranceTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class LoadingSlotModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    description: str | None = None

class MonthlyLocationSnapshotModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date: datetime | None = None
    milage: float | None = None
    latitude: float | None = None
    longitude: float | None = None
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    city: str | None = None
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")

class MonthlyMileageReportResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    year: int | None = None
    month: int | None = None
    start_location: MonthlyLocationSnapshotModel | None = Field(None, alias="startLocation")
    end_location: MonthlyLocationSnapshotModel | None = Field(None, alias="endLocation")
    driven_mileage: float | None = Field(None, alias="drivenMileage")
    vehicle_match_code: str | None = Field(None, alias="vehicleMatchCode")
    vehicle_registration_plate: str | None = Field(None, alias="vehicleRegistrationPlate")
    vehicle_addon_data: dict[str, dict[str, object]] | None = Field(None, alias="vehicleAddonData")

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
    group_key: str | None = Field(None, alias="groupKey")
    group_display_key: str | None = Field(None, alias="groupDisplayKey")
    group_display_name: str | None = Field(None, alias="groupDisplayName")

class PatchAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    due_date: datetime | None = Field(None, alias="dueDate")
    planned_date: datetime | None = Field(None, alias="plannedDate")
    execution_date: datetime | None = Field(None, alias="executionDate")
    type_id: UUID | None = Field(None, alias="typeId")
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    remark: str | None = None

class PatchAppointmentTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    interval: int | None = None
    interval_type: str | None = Field(None, alias="intervalType")

class PatchDailyVehicleLocationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None

class PatchDepartmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    is_selectable: bool | None = Field(None, alias="isSelectable")
    color: str | None = None

class PatchEmissionClassRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_toll_emission_class: bool | None = Field(None, alias="isTollEmissionClass")

class PatchEquipmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    equipment_type_id: UUID | None = Field(None, alias="equipmentTypeId")
    vehicle_id: UUID | None = Field(None, alias="vehicleId")

class PatchEquipmentTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class PatchFinancialSupportStateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class PatchFuelTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    code: str | None = None

class PatchInsuranceTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class PatchLoadingSlotRequest(BaseModel):
    id: UUID | None = None
    name: str | None = None
    description: str | None = None
    _remove: bool | None = None

class PatchTrafficTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class PatchTransmissionTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    code: str | None = None

class PatchVehicleAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    appointment_type_id: UUID | None = Field(None, alias="appointmentTypeId")
    last_date: datetime | None = Field(None, alias="lastDate")
    next_date: datetime | None = Field(None, alias="nextDate")
    remark: str | None = None
    supplier_guid: UUID | None = Field(None, alias="supplierGuid")
    last_value: int | None = Field(None, alias="lastValue")
    next_value: int | None = Field(None, alias="nextValue")
    check_type: int | None = Field(None, alias="checkType")
    _remove: bool | None = None

class PatchVehicleRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    location: str | None = None
    match_code: str | None = Field(None, alias="matchCode")
    status_id: UUID | None = Field(None, alias="statusId")
    mileage: float | None = None
    mileage_date: datetime | None = Field(None, alias="mileageDate")
    operating_hours: float | None = Field(None, alias="operatingHours")
    fuel_tank_capacity: int | None = Field(None, alias="fuelTankCapacity")
    remark: str | None = None
    disposition_sorting_key: str | None = Field(None, alias="dispositionSortingKey")
    year_of_manufacturing: datetime | None = Field(None, alias="yearOfManufacturing")
    registration_document: str | None = Field(None, alias="registrationDocument")
    vehicle_registration: str | None = Field(None, alias="vehicleRegistration")
    is_system_vehicle: bool | None = Field(None, alias="isSystemVehicle")
    department_id: UUID | None = Field(None, alias="departmentId")
    carrier_id: UUID | None = Field(None, alias="carrierId")
    phone_number: str | None = Field(None, alias="phoneNumber")
    e_mail_address: str | None = Field(None, alias="eMailAddress")
    financial_support_state_id: UUID | None = Field(None, alias="financialSupportStateId")
    traffic_type_id: UUID | None = Field(None, alias="trafficTypeId")
    fuel_type_id: UUID | None = Field(None, alias="fuelTypeId")
    transmission_type_id: UUID | None = Field(None, alias="transmissionTypeId")
    insurance_type_id: UUID | None = Field(None, alias="insuranceTypeId")
    emission_class_id: UUID | None = Field(None, alias="emissionClassId")
    vehicle_type_id: UUID | None = Field(None, alias="vehicleTypeId")
    vehicle_sub_type_id: UUID | None = Field(None, alias="vehicleSubTypeId")
    additional_technical_data: AdditionalTechnicalDataModel | None = Field(None, alias="additionalTechnicalData")
    registration_certificate: RegistrationCertificateModel | None = Field(None, alias="registrationCertificate")
    registration_plate: RegistrationPlateModel | None = Field(None, alias="registrationPlate")
    registration_document_location: str | None = Field(None, alias="registrationDocumentLocation")
    toll: TollModel | None = None
    usable_until: datetime | None = Field(None, alias="usableUntil")
    loading_slots: list[PatchLoadingSlotRequest] | None = Field(None, alias="loadingSlots")
    appointments: list[PatchVehicleAppointmentRequest] | None = None
    qr_code: str | None = Field(None, alias="qrCode")
    addon: dict[str, object] | None = None

class PatchVehicleStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    hex_color: str | None = Field(None, alias="hexColor")
    is_selectable: bool | None = Field(None, alias="isSelectable")

class PatchVehicleSubTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    alias: list[str] | None = None

class PatchVehicleTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    vehicle_sub_type: list[PatchVehicleSubTypeRequest] | None = Field(None, alias="vehicleSubType")

class RefreshTokenRequest(BaseModel):
    token: str

class RegistrationCertificateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    registrator_id: UUID | None = Field(None, alias="registratorId")
    remarks: str | None = None
    first_registration_date: datetime | None = Field(None, alias="firstRegistrationDate")
    manufacturer: str | None = None
    type: str | None = None
    commercial_designation: str | None = Field(None, alias="commercialDesignation")
    vehicle_identification_number: str | None = Field(None, alias="vehicleIdentificationNumber")
    permissable_total_weight: int | None = Field(None, alias="permissableTotalWeight")
    permissable_total_weight_in_registration_state: int | None = Field(None, alias="permissableTotalWeightInRegistrationState")
    empty_weight: int | None = Field(None, alias="emptyWeight")
    registration_validity_period: datetime | None = Field(None, alias="registrationValidityPeriod")
    registration_date: datetime | None = Field(None, alias="registrationDate")
    vehicle_class: str | None = Field(None, alias="vehicleClass")
    eg_type_approval_number: str | None = Field(None, alias="egTypeApprovalNumber")
    axle_amount: int | None = Field(None, alias="axleAmount")
    permissable_braked_trailer_load: int | None = Field(None, alias="permissableBrakedTrailerLoad")
    permissable_unbraked_trailer_load: int | None = Field(None, alias="permissableUnbrakedTrailerLoad")
    displacement: int | None = None
    rated_power: int | None = Field(None, alias="ratedPower")
    rated_rpm: int | None = Field(None, alias="ratedRPM")
    fuel_type: str | None = Field(None, alias="fuelType")
    power_to_weight_ratio: float | None = Field(None, alias="powerToWeightRatio")
    vehicle_color: str | None = Field(None, alias="vehicleColor")
    seats_including_driver_seat: int | None = Field(None, alias="seatsIncludingDriverSeat")
    standing_places: int | None = Field(None, alias="standingPlaces")
    top_speed: int | None = Field(None, alias="topSpeed")
    standing_noise: int | None = Field(None, alias="standingNoise")
    standing_noise_rpm: int | None = Field(None, alias="standingNoiseRPM")
    driving_noise: int | None = Field(None, alias="drivingNoise")
    emissions: int | None = None
    eg_type_emission_class: str | None = Field(None, alias="egTypeEmissionClass")
    manufacturer_short_name: str | None = Field(None, alias="manufacturerShortName")
    manufacturer_code: int | None = Field(None, alias="manufacturerCode")
    type_code_with_check_digit: str | None = Field(None, alias="typeCodeWithCheckDigit")
    vehicle_identification_check_digit: int | None = Field(None, alias="vehicleIdentificationCheckDigit")
    super_structure_type: str | None = Field(None, alias="superStructureType")
    vehicle_class_designation: str | None = Field(None, alias="vehicleClassDesignation")
    eg_type_approval_date: datetime | None = Field(None, alias="egTypeApprovalDate")
    permissable_maximum_load_axle1: int | None = Field(None, alias="permissableMaximumLoadAxle1")
    permissable_maximum_load_axle2: int | None = Field(None, alias="permissableMaximumLoadAxle2")
    permissable_maximum_load_axle3: int | None = Field(None, alias="permissableMaximumLoadAxle3")
    permissable_maximum_load_axle1_in_registration_state: int | None = Field(None, alias="permissableMaximumLoadAxle1InRegistrationState")
    permissable_maximum_load_axle2_in_registration_state: int | None = Field(None, alias="permissableMaximumLoadAxle2InRegistrationState")
    permissable_maximum_load_axle3_in_registration_state: int | None = Field(None, alias="permissableMaximumLoadAxle3InRegistrationState")
    drive_axle_amount: int | None = Field(None, alias="driveAxleAmount")
    fuel_type_code: str | None = Field(None, alias="fuelTypeCode")
    color_code: str | None = Field(None, alias="colorCode")
    tanker_tank_capacity: int | None = Field(None, alias="tankerTankCapacity")
    trailer_nose_weight: int | None = Field(None, alias="trailerNoseWeight")
    national_emission_class: str | None = Field(None, alias="nationalEmissionClass")
    emission_class_code: str | None = Field(None, alias="emissionClassCode")
    tires_axle1: str | None = Field(None, alias="tiresAxle1")
    tires_axle2: str | None = Field(None, alias="tiresAxle2")
    tires_axle3: str | None = Field(None, alias="tiresAxle3")
    registration_certificate_number_part2: str | None = Field(None, alias="registrationCertificateNumberPart2")
    operating_permit_feature: str | None = Field(None, alias="operatingPermitFeature")
    length: int | None = None
    width: int | None = None
    height: int | None = None
    other_notes: str | None = Field(None, alias="otherNotes")
    remarks_and_exeptions: str | None = Field(None, alias="remarksAndExeptions")
    zlbi_iat_id: UUID | None = Field(None, alias="zlbiIatId")

class RegistrationPlateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    country_iso: str | None = Field(None, alias="countryIso")
    is_seasonal: bool | None = Field(None, alias="isSeasonal")
    registration_identifier: str | None = Field(None, alias="registrationIdentifier")
    remark: str | None = None

class RequiredEndpointContractDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    allow_multiple: bool | None = Field(None, alias="allowMultiple")

class ServiceContract(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")
    endpoint_contracts: list[EndpointContractDefinition] | None = Field(None, alias="endpointContracts")
    required_endpoint_contracts: list[RequiredEndpointContractDefinition] | None = Field(None, alias="requiredEndpointContracts")

class ServiceObject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    version: str | None = None
    base_url: str | None = Field(None, alias="baseUrl")
    swagger_json_url: str | None = Field(None, alias="swaggerJsonUrl")
    model_definition_url: str | None = Field(None, alias="modelDefinitionUrl")
    grpc_definitions: list[GrpcDefinitions] | None = Field(None, alias="grpcDefinitions")
    type: str | None = None
    contracts: list[ServiceContract] | None = None
    graph_ql_schema: str | None = Field(None, alias="graphQLSchema")

class SetDailyVehicleLocationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID = Field(alias="vehicleId")
    date: datetime
    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None

class SetEndpointContractRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contract_name: str = Field(alias="contractName")
    endpoint: str
    provider_name: str | None = Field(None, alias="providerName")

class SetFuelDataRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID = Field(alias="vehicleId")
    fuel_level_percent: float = Field(alias="fuelLevelPercent")

class SetVehicleLocationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None

class SettingOption(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: dict[str, object] | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class TollModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    toll_registration_date: datetime | None = Field(None, alias="tollRegistrationDate")
    axle_count: int | None = Field(None, alias="axleCount")
    emission_class_id: UUID | None = Field(None, alias="emissionClassId")
    permissable_total_weight: float | None = Field(None, alias="permissableTotalWeight")
    toll_emission_class_id: UUID | None = Field(None, alias="tollEmissionClassId")
    order_number: str | None = Field(None, alias="orderNumber")

class TrafficTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class TransmissionTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    code: str | None = None

class UpdateAddonFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class UpdateSettingRequest(BaseModel):
    value: dict[str, object] | None = None

class VehicleApiKeyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    api_key: str | None = Field(None, alias="apiKey")

class VehicleAppointmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    appointment_type: AppointmentTypeResponse | None = Field(None, alias="appointmentType")
    last_date: datetime | None = Field(None, alias="lastDate")
    next_date: datetime | None = Field(None, alias="nextDate")
    remark: str | None = None
    supplier_guid: UUID | None = Field(None, alias="supplierGuid")
    last_value: int | None = Field(None, alias="lastValue")
    next_value: int | None = Field(None, alias="nextValue")
    check_type: int | None = Field(None, alias="checkType")

class VehicleDepartmentResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None
    color: str | None = None

class VehicleEmissionClassResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    is_toll_emission_class: bool | None = Field(None, alias="isTollEmissionClass")

class VehicleFinancialSupportStateResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None

class VehicleFuelTypeResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None
    code: str | None = None

class VehicleInsuranceTypeResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None

class VehicleLocation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    toll_distance: float | None = Field(None, alias="tollDistance")
    toll_costs: float | None = Field(None, alias="tollCosts")
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None

class VehicleLocationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    latitude: float | None = None
    longitude: float | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    fuel_level: float | None = Field(None, alias="fuelLevel")
    milage: float | None = None

class VehicleResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    location: str | None = None
    match_code: str | None = Field(None, alias="matchCode")
    status: VehicleStatusResponse | None = None
    mileage: float | None = None
    mileage_date: datetime | None = Field(None, alias="mileageDate")
    operating_hours: float | None = Field(None, alias="operatingHours")
    fuel_tank_capacity: int | None = Field(None, alias="fuelTankCapacity")
    remark: str | None = None
    disposition_sorting_key: str | None = Field(None, alias="dispositionSortingKey")
    year_of_manufacturing: datetime | None = Field(None, alias="yearOfManufacturing")
    registration_document: str | None = Field(None, alias="registrationDocument")
    vehicle_registration: str | None = Field(None, alias="vehicleRegistration")
    is_system_vehicle: bool | None = Field(None, alias="isSystemVehicle")
    department: VehicleDepartmentResponse | None = None
    emission_class: VehicleEmissionClassResponse | None = Field(None, alias="emissionClass")
    financial_support_state: VehicleFinancialSupportStateResponse | None = Field(None, alias="financialSupportState")
    fuel_type: VehicleFuelTypeResponse | None = Field(None, alias="fuelType")
    transmission_type: VehicleTransmissionTypeResponse | None = Field(None, alias="transmissionType")
    insurance_type: VehicleInsuranceTypeResponse | None = Field(None, alias="insuranceType")
    traffic_type: VehicleTrafficTypeResponse | None = Field(None, alias="trafficType")
    carrier: CarrierContact | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")
    e_mail_address: str | None = Field(None, alias="eMailAddress")
    vehicle_type_sub_type: VehicleTypeSubTypeModel | None = Field(None, alias="vehicleTypeSubType")
    additional_technical_data: AdditionalTechnicalDataModel | None = Field(None, alias="additionalTechnicalData")
    registration_certificate: RegistrationCertificateModel | None = Field(None, alias="registrationCertificate")
    registration_plate: RegistrationPlateModel | None = Field(None, alias="registrationPlate")
    registration_document_location: str | None = Field(None, alias="registrationDocumentLocation")
    toll: TollModel | None = None
    usable_until: datetime | None = Field(None, alias="usableUntil")
    loading_slots: list[LoadingSlotModel] | None = Field(None, alias="loadingSlots")
    appointments: list[VehicleAppointmentResponse] | None = None
    qr_code: str | None = Field(None, alias="qrCode")
    addon: dict[str, dict[str, object]] | None = None

class VehicleStatusResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    hex_color: str | None = Field(None, alias="hexColor")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class VehicleSubSet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    registration_plate: str | None = Field(None, alias="registrationPlate")
    match_code: str | None = Field(None, alias="matchCode")

class VehicleSubTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    alias: list[str] | None = None

class VehicleTrafficTypeResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None

class VehicleTransmissionTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    code: str | None = None

class VehicleTypeGetByAliasResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    vehicle_sub_type: VehicleSubTypeResponse | None = Field(None, alias="vehicleSubType")

class VehicleTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    vehicle_sub_type: list[VehicleSubTypeResponse] | None = Field(None, alias="vehicleSubType")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class VehicleTypeSubTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    sub_type: str | None = Field(None, alias="subType")
    sub_type_id: UUID | None = Field(None, alias="subTypeId")
