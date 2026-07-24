"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    AvailableServices,
    DataFieldResponse,
    EmploymentConfigurationModel,
    EndpointContract,
    IActionResult,
    MessageQueueResponse,
    OrganizationSettingResult,
    OutMessageLogResponse,
    ServiceObject,
    TelematicConfigurationResponse,
    TelematicTourResponse,
    UploadBlobResponse,
    VehicleConfigurationModel,
    WorkflowResponse,
    WorkflowStepResponse,
)

_PREFIX = "telematic-api/v1"


class TelematicClient:
    """Typed client for ``telematic-api/v1``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.telematic import TelematicClient

        client = TelematicClient(context.http)
    """

    def __init__(self, http: SimplicOxHttpClient) -> None:
        self._http = http
    async def get_data_field_by_id(
        self,
        id: UUID,
    ) -> DataFieldResponse:
        response = await self._http.get(
            f"{_PREFIX}/DataField/{id}",
        )
        response.raise_for_status()
        return DataFieldResponse.model_validate(response.json())

    async def update_data_field_by_id(
        self,
        id: UUID,
        name: str | None = None,
        localizations: list[DataFieldLocalizationModel] | None = None,
        data_type: DataFieldTypeModel | None = None,
        default_value: str | None = None,
        set_definition: list[str] | None = None,
        format: str | None = None,
    ) -> DataFieldResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if localizations is not None:
            _body["localizations"] = localizations
        if data_type is not None:
            _body["dataType"] = data_type
        if default_value is not None:
            _body["defaultValue"] = default_value
        if set_definition is not None:
            _body["setDefinition"] = set_definition
        if format is not None:
            _body["format"] = format
        response = await self._http.patch(
            f"{_PREFIX}/DataField/{id}",
            json=_body,
        )
        response.raise_for_status()
        return DataFieldResponse.model_validate(response.json())

    async def delete_data_field_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/DataField/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_data_field(
        self,
        name: str | None = None,
        localizations: list[DataFieldLocalizationModel] | None = None,
        data_type: DataFieldTypeModel | None = None,
        default_value: str | None = None,
        set_definition: list[str] | None = None,
        format: str | None = None,
    ) -> DataFieldResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if localizations is not None:
            _body["localizations"] = localizations
        if data_type is not None:
            _body["dataType"] = data_type
        if default_value is not None:
            _body["defaultValue"] = default_value
        if set_definition is not None:
            _body["setDefinition"] = set_definition
        if format is not None:
            _body["format"] = format
        response = await self._http.post(
            f"{_PREFIX}/DataField",
            json=_body,
        )
        response.raise_for_status()
        return DataFieldResponse.model_validate(response.json())

    async def get_employment_configuration_by_id(
        self,
        id: UUID,
    ) -> EmploymentConfigurationModel:
        response = await self._http.get(
            f"{_PREFIX}/EmploymentConfiguration/{id}",
        )
        response.raise_for_status()
        return EmploymentConfigurationModel.model_validate(response.json())

    async def update_employment_configuration_by_id(
        self,
        id: UUID,
        employment_id: UUID | None = None,
        match_code: str | None = None,
        provider_name: str | None = None,
        external_driver_identifier: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        active_services: list[str] | None = None,
    ) -> EmploymentConfigurationModel:
        _body: dict[str, object] = {
        }
        if employment_id is not None:
            _body["employmentId"] = str(employment_id)
        if match_code is not None:
            _body["matchCode"] = match_code
        if provider_name is not None:
            _body["providerName"] = provider_name
        if external_driver_identifier is not None:
            _body["externalDriverIdentifier"] = external_driver_identifier
        if valid_from is not None:
            _body["validFrom"] = valid_from
        if valid_to is not None:
            _body["validTo"] = valid_to
        if active_services is not None:
            _body["activeServices"] = active_services
        response = await self._http.patch(
            f"{_PREFIX}/EmploymentConfiguration/{id}",
            json=_body,
        )
        response.raise_for_status()
        return EmploymentConfigurationModel.model_validate(response.json())

    async def delete_employment_configuration_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/EmploymentConfiguration/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_employment_configuration(
        self,
        employment_id: UUID | None = None,
        match_code: str | None = None,
        provider_name: str | None = None,
        external_driver_identifier: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        active_services: list[str] | None = None,
    ) -> EmploymentConfigurationModel:
        _body: dict[str, object] = {
        }
        if employment_id is not None:
            _body["employmentId"] = str(employment_id)
        if match_code is not None:
            _body["matchCode"] = match_code
        if provider_name is not None:
            _body["providerName"] = provider_name
        if external_driver_identifier is not None:
            _body["externalDriverIdentifier"] = external_driver_identifier
        if valid_from is not None:
            _body["validFrom"] = valid_from
        if valid_to is not None:
            _body["validTo"] = valid_to
        if active_services is not None:
            _body["activeServices"] = active_services
        response = await self._http.post(
            f"{_PREFIX}/EmploymentConfiguration",
            json=_body,
        )
        response.raise_for_status()
        return EmploymentConfigurationModel.model_validate(response.json())

    async def get_for_employment(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/EmploymentConfiguration/get-for-employment/{id}",
        )
        response.raise_for_status()

    async def get_generic_telematic_tours(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/generic-telematic-tours",
        )
        response.raise_for_status()

    async def get_download_blob(
        self,
        tour_id: UUID,
        blob_id: UUID,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/generic-telematic-tours/download-blob/{tour_id}/{blob_id}",
        )
        response.raise_for_status()

    async def upload_blob(
        self,
        tour_id: UUID,
        place_id: UUID,
        order_id: UUID,
    ) -> UploadBlobResponse:
        response = await self._http.post(
            f"{_PREFIX}/generic-telematic-tours/upload-blob/{tour_id}/{place_id}/{order_id}",
        )
        response.raise_for_status()
        return UploadBlobResponse.model_validate(response.json())

    async def places_complete_step(
        self,
        tour_id: UUID,
        place_id: UUID,
        workflow_step_id: UUID,
        data_fields: list[DataFieldValueRequest] | None = None,
    ) -> TelematicTourResponse:
        _body: dict[str, object] = {
            "workflowStepId": str(workflow_step_id),
        }
        if data_fields is not None:
            _body["dataFields"] = data_fields
        response = await self._http.post(
            f"{_PREFIX}/generic-telematic-tours/{tour_id}/places/{place_id}/complete-step",
            json=_body,
        )
        response.raise_for_status()
        return TelematicTourResponse.model_validate(response.json())

    async def orders_complete_step(
        self,
        tour_id: UUID,
        order_id: UUID,
        workflow_step_id: UUID,
        data_fields: list[DataFieldValueRequest] | None = None,
    ) -> TelematicTourResponse:
        _body: dict[str, object] = {
            "workflowStepId": str(workflow_step_id),
        }
        if data_fields is not None:
            _body["dataFields"] = data_fields
        response = await self._http.post(
            f"{_PREFIX}/generic-telematic-tours/{tour_id}/orders/{order_id}/complete-step",
            json=_body,
        )
        response.raise_for_status()
        return TelematicTourResponse.model_validate(response.json())

    async def get_generic_telematic_tours_by_tour_id(
        self,
        tour_id: UUID,
    ) -> TelematicTourResponse:
        response = await self._http.get(
            f"{_PREFIX}/generic-telematic-tours/{tour_id}",
        )
        response.raise_for_status()
        return TelematicTourResponse.model_validate(response.json())

    async def get_internal_workflow_by_id(
        self,
        id: UUID,
    ) -> WorkflowResponse:
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalWorkflow/{id}",
        )
        response.raise_for_status()
        return WorkflowResponse.model_validate(response.json())

    async def get_message_queue_by_id(
        self,
        id: UUID,
    ) -> MessageQueueResponse:
        response = await self._http.get(
            f"{_PREFIX}/MessageQueue/{id}",
        )
        response.raise_for_status()
        return MessageQueueResponse.model_validate(response.json())

    async def update_message_queue_by_id(
        self,
        id: UUID,
        name: str | None = None,
        flows: list[str] | None = None,
        type_filter: list[IncomingMessageType] | None = None,
    ) -> MessageQueueResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if flows is not None:
            _body["flows"] = flows
        if type_filter is not None:
            _body["typeFilter"] = type_filter
        response = await self._http.patch(
            f"{_PREFIX}/MessageQueue/{id}",
            json=_body,
        )
        response.raise_for_status()
        return MessageQueueResponse.model_validate(response.json())

    async def delete_message_queue_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/MessageQueue/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_message_queue(
        self,
        name: str | None = None,
        flows: list[str] | None = None,
        type_filter: list[IncomingMessageType] | None = None,
    ) -> MessageQueueResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if flows is not None:
            _body["flows"] = flows
        if type_filter is not None:
            _body["typeFilter"] = type_filter
        response = await self._http.post(
            f"{_PREFIX}/MessageQueue",
            json=_body,
        )
        response.raise_for_status()
        return MessageQueueResponse.model_validate(response.json())

    async def get_read_messages(
        self,
        queue_id: UUID,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/MessageQueue/{queue_id}/read-messages",
        )
        response.raise_for_status()

    async def commit_message(
        self,
        message_id: UUID,
    ) -> None:
        response = await self._http.put(
            f"{_PREFIX}/MessageQueue/{message_id}/commit-message",
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

    async def get_out_message_log_by_id(
        self,
        id: UUID,
    ) -> OutMessageLogResponse:
        response = await self._http.get(
            f"{_PREFIX}/OutMessageLog/{id}",
        )
        response.raise_for_status()
        return OutMessageLogResponse.model_validate(response.json())

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

    async def create_read_job(
        self,
        provider_name: str | None = None,
        cron: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        if cron is not None:
            _body["cron"] = cron
        response = await self._http.post(
            f"{_PREFIX}/Telematic/create-read-job",
            json=_body,
        )
        response.raise_for_status()

    async def delete_read_job(
        self,
        provider_name: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        response = await self._http.delete(
            f"{_PREFIX}/Telematic/delete-read-job",
            json=_body,
        )
        response.raise_for_status()

    async def create_dtco_read_job(
        self,
        provider_name: str | None = None,
        cron: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        if cron is not None:
            _body["cron"] = cron
        response = await self._http.post(
            f"{_PREFIX}/Telematic/create-dtco-read-job",
            json=_body,
        )
        response.raise_for_status()

    async def delete_dtco_read_job(
        self,
        provider_name: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        response = await self._http.delete(
            f"{_PREFIX}/Telematic/delete-dtco-read-job",
            json=_body,
        )
        response.raise_for_status()

    async def get_available_services(
        self,
    ) -> AvailableServices:
        response = await self._http.get(
            f"{_PREFIX}/Telematic/get-available-services",
        )
        response.raise_for_status()
        return AvailableServices.model_validate(response.json())

    async def send_text_message(
        self,
        vehicle_id: UUID | None = None,
        driver_id: UUID | None = None,
        message: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if driver_id is not None:
            _body["driverId"] = str(driver_id)
        if message is not None:
            _body["message"] = message
        response = await self._http.post(
            f"{_PREFIX}/Telematic/send-text-message",
            json=_body,
        )
        response.raise_for_status()

    async def check_credentials(
        self,
        credentials: ProviderConfigurationModel | None = None,
        provider_name: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if credentials is not None:
            _body["credentials"] = credentials
        if provider_name is not None:
            _body["providerName"] = provider_name
        response = await self._http.post(
            f"{_PREFIX}/Telematic/check-credentials",
            json=_body,
        )
        response.raise_for_status()

    async def get_import_vehicle(
        self,
        provider_name: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if provider_name is not None:
            _body["providerName"] = provider_name
        response = await self._http.post(
            f"{_PREFIX}/Telematic/get-import-vehicle",
            json=_body,
        )
        response.raise_for_status()

    async def get_telematic_configuration_by_id(
        self,
        id: UUID,
    ) -> TelematicConfigurationResponse:
        response = await self._http.get(
            f"{_PREFIX}/TelematicConfiguration/{id}",
        )
        response.raise_for_status()
        return TelematicConfigurationResponse.model_validate(response.json())

    async def delete_telematic_configuration_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/TelematicConfiguration/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_telematic_configuration(
        self,
        provider_name: str,
        provider_configuration: ProviderConfigurationModel | None = None,
        auto_creation_settings: list[AutomaticVehicleConfigurationCreationSettings] | None = None,
    ) -> TelematicConfigurationResponse:
        _body: dict[str, object] = {
            "providerName": provider_name,
        }
        if provider_configuration is not None:
            _body["providerConfiguration"] = provider_configuration
        if auto_creation_settings is not None:
            _body["autoCreationSettings"] = auto_creation_settings
        response = await self._http.post(
            f"{_PREFIX}/TelematicConfiguration",
            json=_body,
        )
        response.raise_for_status()
        return TelematicConfigurationResponse.model_validate(response.json())

    async def update_telematic_configuration(
        self,
        provider_configuration: PatchProviderConfiguration | None = None,
        auto_creation_settings: list[AutomaticVehicleConfigurationCreationSettings] | None = None,
        id: UUID | None = None,
    ) -> TelematicConfigurationResponse:
        _body: dict[str, object] = {
        }
        if provider_configuration is not None:
            _body["providerConfiguration"] = provider_configuration
        if auto_creation_settings is not None:
            _body["autoCreationSettings"] = auto_creation_settings
        response = await self._http.patch(
            f"{_PREFIX}/TelematicConfiguration",
            json=_body,
        )
        response.raise_for_status()
        return TelematicConfigurationResponse.model_validate(response.json())

    async def get_for_provider(
        self,
        name: str,
    ) -> TelematicConfigurationResponse:
        response = await self._http.get(
            f"{_PREFIX}/TelematicConfiguration/get-for-provider/{name}",
        )
        response.raise_for_status()
        return TelematicConfigurationResponse.model_validate(response.json())

    async def cleanup_jobs(
        self,
        key: str | None = None,
    ) -> TelematicConfigurationResponse:
        _params: dict[str, object] = {}
        if key is not None:
            _params["key"] = key
        response = await self._http.post(
            f"{_PREFIX}/TelematicConfiguration/cleanup-jobs",
            params=_params,
        )
        response.raise_for_status()
        return TelematicConfigurationResponse.model_validate(response.json())

    async def get_vehicle_configuration_by_id(
        self,
        id: UUID,
    ) -> VehicleConfigurationModel:
        response = await self._http.get(
            f"{_PREFIX}/VehicleConfiguration/{id}",
        )
        response.raise_for_status()
        return VehicleConfigurationModel.model_validate(response.json())

    async def update_vehicle_configuration_by_id(
        self,
        id: UUID,
        vehicle_id: UUID | None = None,
        match_code: str | None = None,
        provider_name: str | None = None,
        external_vehicle_identifier: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        active_services: list[str] | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
    ) -> VehicleConfigurationModel:
        _body: dict[str, object] = {
        }
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if match_code is not None:
            _body["matchCode"] = match_code
        if provider_name is not None:
            _body["providerName"] = provider_name
        if external_vehicle_identifier is not None:
            _body["externalVehicleIdentifier"] = external_vehicle_identifier
        if valid_from is not None:
            _body["validFrom"] = valid_from
        if valid_to is not None:
            _body["validTo"] = valid_to
        if active_services is not None:
            _body["activeServices"] = active_services
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        response = await self._http.patch(
            f"{_PREFIX}/VehicleConfiguration/{id}",
            json=_body,
        )
        response.raise_for_status()
        return VehicleConfigurationModel.model_validate(response.json())

    async def delete_vehicle_configuration_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/VehicleConfiguration/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_vehicle_configuration(
        self,
        vehicle_id: UUID | None = None,
        match_code: str | None = None,
        provider_name: str | None = None,
        external_vehicle_identifier: str | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        active_services: list[str] | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
    ) -> VehicleConfigurationModel:
        _body: dict[str, object] = {
        }
        if vehicle_id is not None:
            _body["vehicleId"] = str(vehicle_id)
        if match_code is not None:
            _body["matchCode"] = match_code
        if provider_name is not None:
            _body["providerName"] = provider_name
        if external_vehicle_identifier is not None:
            _body["externalVehicleIdentifier"] = external_vehicle_identifier
        if valid_from is not None:
            _body["validFrom"] = valid_from
        if valid_to is not None:
            _body["validTo"] = valid_to
        if active_services is not None:
            _body["activeServices"] = active_services
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        response = await self._http.post(
            f"{_PREFIX}/VehicleConfiguration",
            json=_body,
        )
        response.raise_for_status()
        return VehicleConfigurationModel.model_validate(response.json())

    async def get_for_vehicle(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/VehicleConfiguration/get-for-vehicle/{id}",
        )
        response.raise_for_status()

    async def get_workflow_by_id(
        self,
        id: UUID,
    ) -> WorkflowResponse:
        response = await self._http.get(
            f"{_PREFIX}/Workflow/{id}",
        )
        response.raise_for_status()
        return WorkflowResponse.model_validate(response.json())

    async def update_workflow_by_id(
        self,
        id: UUID,
        name: str | None = None,
        value: str | None = None,
        description: str | None = None,
        steps: list[WorkflowStepAssignmentSet] | None = None,
    ) -> WorkflowResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if value is not None:
            _body["value"] = value
        if description is not None:
            _body["description"] = description
        if steps is not None:
            _body["steps"] = steps
        response = await self._http.patch(
            f"{_PREFIX}/Workflow/{id}",
            json=_body,
        )
        response.raise_for_status()
        return WorkflowResponse.model_validate(response.json())

    async def delete_workflow_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/Workflow/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_workflow(
        self,
        name: str | None = None,
        value: str | None = None,
        description: str | None = None,
        steps: list[WorkflowStepAssignmentSet] | None = None,
    ) -> WorkflowResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if value is not None:
            _body["value"] = value
        if description is not None:
            _body["description"] = description
        if steps is not None:
            _body["steps"] = steps
        response = await self._http.post(
            f"{_PREFIX}/Workflow",
            json=_body,
        )
        response.raise_for_status()
        return WorkflowResponse.model_validate(response.json())

    async def get_workflow_step_by_id(
        self,
        id: UUID,
    ) -> WorkflowStepResponse:
        response = await self._http.get(
            f"{_PREFIX}/WorkflowStep/{id}",
        )
        response.raise_for_status()
        return WorkflowStepResponse.model_validate(response.json())

    async def update_workflow_step_by_id(
        self,
        id: UUID,
        name: str | None = None,
        localizations: list[WorkflowStepLocalizationModel] | None = None,
        data_fields: list[WorkflowStepDataFieldSet] | None = None,
        step_order: int | None = None,
        roles: list[str] | None = None,
    ) -> WorkflowStepResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if localizations is not None:
            _body["localizations"] = localizations
        if data_fields is not None:
            _body["dataFields"] = data_fields
        if step_order is not None:
            _body["stepOrder"] = step_order
        if roles is not None:
            _body["roles"] = roles
        response = await self._http.patch(
            f"{_PREFIX}/WorkflowStep/{id}",
            json=_body,
        )
        response.raise_for_status()
        return WorkflowStepResponse.model_validate(response.json())

    async def delete_workflow_step_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/WorkflowStep/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_workflow_step(
        self,
        name: str | None = None,
        localizations: list[WorkflowStepLocalizationModel] | None = None,
        data_fields: list[WorkflowStepDataFieldSet] | None = None,
        step_order: int | None = None,
        roles: list[str] | None = None,
    ) -> WorkflowStepResponse:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if localizations is not None:
            _body["localizations"] = localizations
        if data_fields is not None:
            _body["dataFields"] = data_fields
        if step_order is not None:
            _body["stepOrder"] = step_order
        if roles is not None:
            _body["roles"] = roles
        response = await self._http.post(
            f"{_PREFIX}/WorkflowStep",
            json=_body,
        )
        response.raise_for_status()
        return WorkflowStepResponse.model_validate(response.json())
