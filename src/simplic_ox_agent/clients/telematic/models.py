"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

class AddressResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    street: str | None = None
    city: str | None = None
    zip_code: str | None = Field(None, alias="zipCode")
    country: str | None = None
    country_code: str | None = Field(None, alias="countryCode")

class AutomaticVehicleConfigurationCreationSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_type: str | None = Field(None, alias="vehicleType")
    external_vehicle_identifier_template: str | None = Field(None, alias="externalVehicleIdentifierTemplate")
    create_in_telematic_system: bool | None = Field(None, alias="createInTelematicSystem")

class AvailableServices(BaseModel):
    spedion: list[str] | None = None
    transics: list[str] | None = None
    webfleet: list[str] | None = None
    sms: list[str] | None = None
    generic: list[str] | None = None
    none: list[str] | None = None

class CheckCredentialsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    credentials: ProviderConfigurationModel | None = None
    provider_name: str | None = Field(None, alias="providerName")

class CompleteWorkflowStepRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workflow_step_id: UUID = Field(alias="workflowStepId")
    data_fields: list[DataFieldValueRequest] | None = Field(None, alias="dataFields")

class CreateDataFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    localizations: list[DataFieldLocalizationModel] | None = None
    data_type: DataFieldTypeModel | None = Field(None, alias="dataType")
    default_value: str | None = Field(None, alias="defaultValue")
    set_definition: list[str] | None = Field(None, alias="setDefinition")
    format: str | None = None

class CreateDtcoReadJobRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")
    cron: str | None = None

class CreateEmploymentConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    employment_id: UUID | None = Field(None, alias="employmentId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_driver_identifier: str | None = Field(None, alias="externalDriverIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")

class CreateMessageQueueRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    flows: list[str] | None = None
    type_filter: list[IncomingMessageType] | None = Field(None, alias="typeFilter")

class CreateReadJobRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")
    cron: str | None = None

class CreateTelematicConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str = Field(alias="providerName")
    provider_configuration: ProviderConfigurationModel | None = Field(None, alias="providerConfiguration")
    auto_creation_settings: list[AutomaticVehicleConfigurationCreationSettings] | None = Field(None, alias="autoCreationSettings")

class CreateVehicleConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_vehicle_identifier: str | None = Field(None, alias="externalVehicleIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")

class CreateWorkflowRequest(BaseModel):
    name: str | None = None
    value: str | None = None
    description: str | None = None
    steps: list[WorkflowStepAssignmentSet] | None = None

class CreateWorkflowStepRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    localizations: list[WorkflowStepLocalizationModel] | None = None
    data_fields: list[WorkflowStepDataFieldSet] | None = Field(None, alias="dataFields")
    step_order: int | None = Field(None, alias="stepOrder")
    roles: list[str] | None = None

class DataFieldLocalizationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    language_code: str | None = Field(None, alias="languageCode")
    value: str | None = None

class DataFieldLocalizationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    language_code: str | None = Field(None, alias="languageCode")
    value: str | None = None

class DataFieldResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    localizations: list[DataFieldLocalizationModel] | None = None
    data_type: DataFieldTypeModel | None = Field(None, alias="dataType")
    default_value: str | None = Field(None, alias="defaultValue")
    set_definition: list[str] | None = Field(None, alias="setDefinition")
    format: str | None = None

class DataFieldTypeModel(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class DataFieldValueRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_field_id: UUID = Field(alias="dataFieldId")
    value: str | None = None

class DeleteDtcoReadJobRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")

class DeleteReadJobRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")

class EmploymentConfigurationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    employment_id: UUID | None = Field(None, alias="employmentId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_driver_identifier: str | None = Field(None, alias="externalDriverIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")

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

class GrpcDefinitions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    package: str | None = None
    service: str | None = None
    proto_file: str | None = Field(None, alias="protoFile")

class IActionResult(BaseModel):
    pass

class ImportVehiclesRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_name: str | None = Field(None, alias="providerName")

class IncomingMessageType(IntEnum):
    VALUE_0 = 0
    VALUE_100 = 100
    VALUE_199 = 199
    VALUE_200 = 200
    VALUE_299 = 299
    VALUE_300 = 300
    VALUE_399 = 399
    VALUE_400 = 400
    VALUE_999 = 999

class MessageQueueResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    flows: list[str] | None = None
    type_filter: list[IncomingMessageType] | None = Field(None, alias="typeFilter")

class OpeningHoursResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_: str | None = Field(None, alias="from")
    to: str | None = None

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

class OutMessageLogResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    message_type: str | None = Field(None, alias="messageType")
    provider: str | None = None
    source_message_json: str | None = Field(None, alias="sourceMessageJson")
    destination_message_json: str | None = Field(None, alias="destinationMessageJson")
    response_json: str | None = Field(None, alias="responseJson")
    internal_vehicle_id: UUID | None = Field(None, alias="internalVehicleId")
    internal_driver_id: UUID | None = Field(None, alias="internalDriverId")
    internal_tour_id: UUID | None = Field(None, alias="internalTourId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    success: bool | None = None

class OutgoingAttachmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    blob_id: UUID | None = Field(None, alias="blobId")

class PatchDataFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    localizations: list[DataFieldLocalizationModel] | None = None
    data_type: DataFieldTypeModel | None = Field(None, alias="dataType")
    default_value: str | None = Field(None, alias="defaultValue")
    set_definition: list[str] | None = Field(None, alias="setDefinition")
    format: str | None = None

class PatchEmploymentConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    employment_id: UUID | None = Field(None, alias="employmentId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_driver_identifier: str | None = Field(None, alias="externalDriverIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")

class PatchMessageQueueRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    flows: list[str] | None = None
    type_filter: list[IncomingMessageType] | None = Field(None, alias="typeFilter")

class PatchProviderConfiguration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: str | None = None
    password: str | None = None
    account_name: str | None = Field(None, alias="accountName")
    api_key: str | None = Field(None, alias="apiKey")
    system_nr: int | None = Field(None, alias="systemNr")
    integrator: str | None = None

class PatchTelematicConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    provider_configuration: PatchProviderConfiguration | None = Field(None, alias="providerConfiguration")
    auto_creation_settings: list[AutomaticVehicleConfigurationCreationSettings] | None = Field(None, alias="autoCreationSettings")

class PatchVehicleConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_vehicle_identifier: str | None = Field(None, alias="externalVehicleIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")

class PatchWorkflowRequest(BaseModel):
    name: str | None = None
    value: str | None = None
    description: str | None = None
    steps: list[WorkflowStepAssignmentSet] | None = None

class PatchWorkflowStepRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    localizations: list[WorkflowStepLocalizationModel] | None = None
    data_fields: list[WorkflowStepDataFieldSet] | None = Field(None, alias="dataFields")
    step_order: int | None = Field(None, alias="stepOrder")
    roles: list[str] | None = None

class ProviderConfigurationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: str | None = None
    password: str | None = None
    account_name: str | None = Field(None, alias="accountName")
    api_key: str | None = Field(None, alias="apiKey")
    system_nr: int | None = Field(None, alias="systemNr")
    integrator: str | None = None

class RequiredEndpointContractDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    allow_multiple: bool | None = Field(None, alias="allowMultiple")

class SendTextMessageRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    driver_id: UUID | None = Field(None, alias="driverId")
    message: str | None = None

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

class SetEndpointContractRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contract_name: str = Field(alias="contractName")
    endpoint: str
    provider_name: str | None = Field(None, alias="providerName")

class SettingOption(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: dict[str, object] | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class TelematicConfigurationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    provider_name: str | None = Field(None, alias="providerName")
    provider_configuration: ProviderConfigurationModel | None = Field(None, alias="providerConfiguration")
    auto_creation_settings: list[AutomaticVehicleConfigurationCreationSettings] | None = Field(None, alias="autoCreationSettings")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TelematicDataFieldResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_field_id: UUID | None = Field(None, alias="dataFieldId")
    is_required: bool | None = Field(None, alias="isRequired")
    name: str | None = None
    localizations: list[DataFieldLocalizationResponse] | None = None
    type: str | None = None
    value: str | None = None
    collected_at_utc: datetime | None = Field(None, alias="collectedAtUtc")

class TelematicOrderResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    internal_id: UUID | None = Field(None, alias="internalId")
    order_number: str | None = Field(None, alias="orderNumber")
    article_name: str | None = Field(None, alias="articleName")
    order_type: str | None = Field(None, alias="orderType")
    quantity: float | None = None
    quantity_unit: str | None = Field(None, alias="quantityUnit")
    weight: float | None = None
    loading_meter: float | None = Field(None, alias="loadingMeter")
    reference: str | None = None
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    attached_resources: list[TelematicResourceResponse] | None = Field(None, alias="attachedResources")
    external_notes: str | None = Field(None, alias="externalNotes")
    opening_hours: list[OpeningHoursResponse] | None = Field(None, alias="openingHours")
    attachments: list[OutgoingAttachmentResponse] | None = None
    workflow: TelematicWorkflowResponse | None = None

class TelematicPlaceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    internal_id: UUID | None = Field(None, alias="internalId")
    name: str | None = None
    address: AddressResponse | None = None
    start_date_time_utc: datetime | None = Field(None, alias="startDateTimeUtc")
    end_date_time_utc: datetime | None = Field(None, alias="endDateTimeUtc")
    latitude: float | None = None
    longitude: float | None = None
    reference: str | None = None
    orders: list[TelematicOrderResponse] | None = None
    notes: str | None = None
    workflow: TelematicWorkflowResponse | None = None

class TelematicResourceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    match_code: str | None = Field(None, alias="matchCode")

class TelematicTourResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    internal_id: UUID | None = Field(None, alias="internalId")
    tour_number: str | None = Field(None, alias="tourNumber")
    reference: str | None = None
    internal_vehicle_id: UUID | None = Field(None, alias="internalVehicleId")
    internal_driver_id: UUID | None = Field(None, alias="internalDriverId")
    start_date_time_utc: datetime | None = Field(None, alias="startDateTimeUtc")
    end_date_time_utc: datetime | None = Field(None, alias="endDateTimeUtc")
    places: list[TelematicPlaceResponse] | None = None
    public_key: str | None = Field(None, alias="publicKey")

class TelematicWorkflowResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None
    value: str | None = None
    description: str | None = None
    steps: list[TelematicWorkflowStepResponse] | None = None

class TelematicWorkflowStepResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workflow_step_id: UUID | None = Field(None, alias="workflowStepId")
    order: int | None = None
    name: str | None = None
    localizations: list[WorkflowStepLocalizationResponse] | None = None
    data_fields: list[TelematicDataFieldResponse] | None = Field(None, alias="dataFields")
    is_completed: bool | None = Field(None, alias="isCompleted")
    completed_at_utc: datetime | None = Field(None, alias="completedAtUtc")
    roles: list[str] | None = None

class UpdateSettingRequest(BaseModel):
    value: dict[str, object] | None = None

class UploadBlobResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    blob_id: UUID | None = Field(None, alias="blobId")
    name: str | None = None
    content_type: str | None = Field(None, alias="contentType")

class VehicleConfigurationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    vehicle_id: UUID | None = Field(None, alias="vehicleId")
    match_code: str | None = Field(None, alias="matchCode")
    provider_name: str | None = Field(None, alias="providerName")
    external_vehicle_identifier: str | None = Field(None, alias="externalVehicleIdentifier")
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    active_services: list[str] | None = Field(None, alias="activeServices")
    load_workflow: WorkflowResponse | None = Field(None, alias="loadWorkflow")
    delivery_workflow: WorkflowResponse | None = Field(None, alias="deliveryWorkflow")

class WorkflowResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None
    value: str | None = None
    description: str | None = None
    steps: list[WorkflowStepAssignmentModel] | None = None

class WorkflowStepAssignmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workflow_step_id: UUID | None = Field(None, alias="workflowStepId")
    order: int | None = None
    step: WorkflowStepResponse | None = None

class WorkflowStepAssignmentSet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workflow_step_id: UUID | None = Field(None, alias="workflowStepId")
    order: int | None = None

class WorkflowStepDataFieldModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_field_id: UUID | None = Field(None, alias="dataFieldId")
    is_required: bool | None = Field(None, alias="isRequired")
    field: DataFieldResponse | None = None

class WorkflowStepDataFieldSet(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    data_field_id: UUID | None = Field(None, alias="dataFieldId")
    is_required: bool | None = Field(None, alias="isRequired")

class WorkflowStepLocalizationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    language_code: str | None = Field(None, alias="languageCode")
    value: str | None = None

class WorkflowStepLocalizationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    language_code: str | None = Field(None, alias="languageCode")
    value: str | None = None

class WorkflowStepResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    localizations: list[WorkflowStepLocalizationModel] | None = None
    data_fields: list[WorkflowStepDataFieldModel] | None = Field(None, alias="dataFields")
    step_order: int | None = Field(None, alias="stepOrder")
    roles: list[str] | None = None
