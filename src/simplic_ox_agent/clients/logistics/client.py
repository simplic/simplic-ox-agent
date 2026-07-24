"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    AddBillingLinesToTransactionResponse,
    AddonFieldResponse,
    AppointmentModel,
    AutoPlanToursResponse,
    BillingLineStatusModel,
    CalculateRouteResponse,
    CarrierOrderReportResponse,
    ComposedResourceSettingsResponse,
    DefaultPlanningAssignmentResponse,
    DepartmentResponse,
    EmptyTourResponse,
    EndpointContract,
    EstimatedTimeOfArrivalResponse,
    GeofenceResourceTracking,
    GeofenceResponse,
    GetComposedResourceResponse,
    GroupedResourcesModel,
    IActionResult,
    IncotermResponse,
    LoadingAidBookingModel,
    LoadingAidTypeResponse,
    OrganizationSettingResult,
    OxQLQueryResult,
    PlanningRegionModel,
    ResourceModel,
    ScheduledPlanningAssignmentResponse,
    ServiceObject,
    ShiftResponse,
    ShipmentItemModel,
    ShipmentItemStatusModel,
    ShipmentModel,
    ShipmentPreAdviceModel,
    ShipmentStatusModel,
    ShipmentTagModel,
    ShipmentTemplateModel,
    ShippingUnitModel,
    ShippingUnitStatusModel,
    ShippingUnitTagModel,
    TourManipulateResponse,
    TourModel,
    TourReportingModel,
    TourStatusModel,
    TourTagModel,
    TourTemplateResponse,
    ValidateResponse,
)

_PREFIX = "logistics-api/v2"


class LogisticsClient:
    """Typed client for ``logistics-api/v2``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.logistics import LogisticsClient

        client = LogisticsClient(context.http)
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

    async def addon_field_get_by_id(
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

    async def prompt(
        self,
        prompt: str | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if prompt is not None:
            _body["prompt"] = prompt
        response = await self._http.post(
            f"{_PREFIX}/AI/prompt",
            json=_body,
        )
        response.raise_for_status()

    async def get_appointment_by_id(
        self,
        id: UUID,
    ) -> AppointmentModel:
        response = await self._http.get(
            f"{_PREFIX}/Appointment/{id}",
        )
        response.raise_for_status()
        return AppointmentModel.model_validate(response.json())

    async def update_appointment_by_id(
        self,
        id: UUID,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        resources: list[UUID] | None = None,
        functions: list[str] | None = None,
        title: str | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        hex_color: str | None = None,
    ) -> AppointmentModel:
        _body: dict[str, object] = {
        }
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if resources is not None:
            _body["resources"] = str(resources)
        if functions is not None:
            _body["functions"] = functions
        if title is not None:
            _body["title"] = title
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/Appointment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentModel.model_validate(response.json())

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
        title: str,
        start_date_time: str,
        end_date_time: str,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        resources: list[UUID] | None = None,
        functions: list[str] | None = None,
        hex_color: str | None = None,
    ) -> AppointmentModel:
        _body: dict[str, object] = {
            "title": title,
            "startDateTime": start_date_time,
            "endDateTime": end_date_time,
        }
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if resources is not None:
            _body["resources"] = str(resources)
        if functions is not None:
            _body["functions"] = functions
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/Appointment",
            json=_body,
        )
        response.raise_for_status()
        return AppointmentModel.model_validate(response.json())

    async def plan(
        self,
        shipments: list[AutoPlanShipmentRequest],
        resources: list[AutoPlanResourceRequest],
        optimization_mode: str,
    ) -> AutoPlanToursResponse:
        """Automatically plans tours by solving a vehicle routing problem.

Takes a set of shipments and resources, then uses route Optimization API
to find an optimal distribution of shipments across the available resources based on the
specified optimization mode and constraints (weight, loading meters, travel time)."""
        response = await self._http.post(
            f"{_PREFIX}/AutoPlan/plan",
            json={"shipments": shipments, "resources": resources, "optimizationMode": optimization_mode},
        )
        response.raise_for_status()
        return AutoPlanToursResponse.model_validate(response.json())

    async def create_tours(
        self,
        planned_tours: list[PlannedTourResult],
        persist: bool | None = None,
        auto_assign_resource_modes: list[str] | None = None,
        action_optimization_mode: str | None = None,
        tour_number: str | None = None,
    ) -> None:
        """Creates tours from a previously generated auto-plan result.

Takes the planned tours (possibly modified in the UI) and creates actual tours
by resolving the shipments and resources for each planned tour."""
        _body: dict[str, object] = {
            "plannedTours": planned_tours,
        }
        if persist is not None:
            _body["persist"] = persist
        if auto_assign_resource_modes is not None:
            _body["autoAssignResourceModes"] = auto_assign_resource_modes
        if action_optimization_mode is not None:
            _body["actionOptimizationMode"] = action_optimization_mode
        if tour_number is not None:
            _body["tourNumber"] = tour_number
        response = await self._http.post(
            f"{_PREFIX}/AutoPlan/create-tours",
            json=_body,
        )
        response.raise_for_status()

    async def add_to_transaction(
        self,
        billing_lines: list[AddToTransactionBillingLineReferenceRequest] | None = None,
        transaction_id: UUID | None = None,
        mode: AddBillingLinesToTransactionMode | None = None,
    ) -> AddBillingLinesToTransactionResponse:
        """Adds a set of billing lines to a transaction.

Each billing line is identified by its parent shipment id or tour id and its own id.
Exactly one of shipment id or tour id must be set per reference.
The billing lines are converted to their erp equivalent and
dispatched via the erp internal client.
If `transactionId` is omitted or null, a new draft transaction
will be created by the ERP microservice rather than adding the billing lines to an existing one."""
        _body: dict[str, object] = {
        }
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        if transaction_id is not None:
            _body["transactionId"] = str(transaction_id)
        if mode is not None:
            _body["mode"] = mode
        response = await self._http.post(
            f"{_PREFIX}/Billing/add-to-transaction",
            json=_body,
        )
        response.raise_for_status()
        return AddBillingLinesToTransactionResponse.model_validate(response.json())

    async def create_billing_line_status(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        type: str | None = None,
        hex_color: str | None = None,
    ) -> BillingLineStatusModel:
        """Creates a new billing line status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if type is not None:
            _body["type"] = type
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/BillingLineStatus",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineStatusModel.model_validate(response.json())

    async def get_billing_line_status_by_id(
        self,
        id: UUID,
    ) -> BillingLineStatusModel:
        """Retrives the billing line status with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/BillingLineStatus/{id}",
        )
        response.raise_for_status()
        return BillingLineStatusModel.model_validate(response.json())

    async def update_billing_line_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        type: str | None = None,
        hex_color: str | None = None,
    ) -> BillingLineStatusModel:
        """Updates/saves the given billing line status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if type is not None:
            _body["type"] = type
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/BillingLineStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineStatusModel.model_validate(response.json())

    async def billing_line_status_get_all(
        self,
    ) -> None:
        """Retrieves all billing line statuses."""
        response = await self._http.get(
            f"{_PREFIX}/BillingLineStatus/get-all",
        )
        response.raise_for_status()

    async def create_billing_line_status_deployment(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        type: str | None = None,
        hex_color: str | None = None,
    ) -> BillingLineStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if type is not None:
            _body["type"] = type
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/BillingLineStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineStatusModel.model_validate(response.json())

    async def update_billing_line_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        type: str | None = None,
        hex_color: str | None = None,
    ) -> BillingLineStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if type is not None:
            _body["type"] = type
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/BillingLineStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineStatusModel.model_validate(response.json())

    async def get_composed_resource_by_id(
        self,
        id: UUID,
    ) -> GetComposedResourceResponse:
        response = await self._http.get(
            f"{_PREFIX}/ComposedResource/{id}",
        )
        response.raise_for_status()
        return GetComposedResourceResponse.model_validate(response.json())

    async def attach_main_driver(
        self,
        composed_resource_id: UUID,
        driver_resource_id: UUID,
        move_current_to_co_driver_seat: bool | None = None,
    ) -> None:
        _body: dict[str, object] = {
            "composedResourceId": str(composed_resource_id),
            "driverResourceId": str(driver_resource_id),
        }
        if move_current_to_co_driver_seat is not None:
            _body["moveCurrentToCoDriverSeat"] = move_current_to_co_driver_seat
        response = await self._http.post(
            f"{_PREFIX}/ComposedResource/attach-main-driver",
            json=_body,
        )
        response.raise_for_status()

    async def attach_co_driver(
        self,
        composed_resource_id: UUID,
        driver_resource_id: UUID,
        move_current_to_main_driver_seat: bool | None = None,
    ) -> None:
        _body: dict[str, object] = {
            "composedResourceId": str(composed_resource_id),
            "driverResourceId": str(driver_resource_id),
        }
        if move_current_to_main_driver_seat is not None:
            _body["moveCurrentToMainDriverSeat"] = move_current_to_main_driver_seat
        response = await self._http.post(
            f"{_PREFIX}/ComposedResource/attach-co-driver",
            json=_body,
        )
        response.raise_for_status()

    async def attach_tractor_unit(
        self,
        composed_resource_id: UUID,
        tractor_unit_resource_id: UUID,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/ComposedResource/attach-tractor-unit",
            json={"composedResourceId": str(composed_resource_id), "tractorUnitResourceId": str(tractor_unit_resource_id)},
        )
        response.raise_for_status()

    async def attach_trailer(
        self,
        composed_resource_id: UUID,
        tractor_unit_resource_id: UUID,
        attach_as_additional_trailer: bool | None = None,
    ) -> None:
        _body: dict[str, object] = {
            "composedResourceId": str(composed_resource_id),
            "tractorUnitResourceId": str(tractor_unit_resource_id),
        }
        if attach_as_additional_trailer is not None:
            _body["attachAsAdditionalTrailer"] = attach_as_additional_trailer
        response = await self._http.post(
            f"{_PREFIX}/ComposedResource/attach-trailer",
            json=_body,
        )
        response.raise_for_status()

    async def attach_resource(
        self,
        first_resource_id: UUID,
        second_resource_id: UUID,
        settings: AttachResourceRequestSettings | None = None,
    ) -> GetComposedResourceResponse:
        _body: dict[str, object] = {
            "firstResourceId": str(first_resource_id),
            "secondResourceId": str(second_resource_id),
        }
        if settings is not None:
            _body["settings"] = settings
        response = await self._http.post(
            f"{_PREFIX}/ComposedResource/attach-resource",
            json=_body,
        )
        response.raise_for_status()
        return GetComposedResourceResponse.model_validate(response.json())

    async def set_message_recognized(
        self,
        composed_resource_id: UUID,
    ) -> GetComposedResourceResponse:
        response = await self._http.put(
            f"{_PREFIX}/ComposedResource/set-message-recognized/{composed_resource_id}",
        )
        response.raise_for_status()
        return GetComposedResourceResponse.model_validate(response.json())

    async def get_composed_resource_settings(
        self,
    ) -> ComposedResourceSettingsResponse:
        """Gets the current composed resource settings."""
        response = await self._http.get(
            f"{_PREFIX}/ComposedResourceSettings",
        )
        response.raise_for_status()
        return ComposedResourceSettingsResponse.model_validate(response.json())

    async def update_composed_resource_settings(
        self,
        composed_resources_enabled: bool | None = None,
    ) -> ComposedResourceSettingsResponse:
        """Patches the composed resource settings and initializes composed resources when getting enabled."""
        _body: dict[str, object] = {
        }
        if composed_resources_enabled is not None:
            _body["composedResourcesEnabled"] = composed_resources_enabled
        response = await self._http.patch(
            f"{_PREFIX}/ComposedResourceSettings",
            json=_body,
        )
        response.raise_for_status()
        return ComposedResourceSettingsResponse.model_validate(response.json())

    async def default_planning_get_by_shift(
        self,
        shift_id: UUID,
    ) -> DefaultPlanningAssignmentResponse:
        """Gets the plan with given id."""
        response = await self._http.get(
            f"{_PREFIX}/DefaultPlanning/get-by-shift/{shift_id}",
        )
        response.raise_for_status()
        return DefaultPlanningAssignmentResponse.model_validate(response.json())

    async def default_planning_get_by_resource(
        self,
        resource_id: UUID,
        shift_id: UUID | None = None,
    ) -> DefaultPlanningAssignmentResponse:
        """Gets plan for resource matching given id."""
        _params: dict[str, object] = {}
        if shift_id is not None:
            _params["shiftId"] = str(shift_id)
        response = await self._http.get(
            f"{_PREFIX}/DefaultPlanning/get-by-resource/{resource_id}",
            params=_params,
        )
        response.raise_for_status()
        return DefaultPlanningAssignmentResponse.model_validate(response.json())

    async def update_default_planning_by_shift_id(
        self,
        shift_id: UUID,
        assignments: list[ResourceAssignmentPatch] | None = None,
    ) -> DefaultPlanningAssignmentResponse:
        """Patches plan matching given id."""
        _body: dict[str, object] = {
        }
        if assignments is not None:
            _body["assignments"] = assignments
        response = await self._http.patch(
            f"{_PREFIX}/DefaultPlanning/{shift_id}",
            json=_body,
        )
        response.raise_for_status()
        return DefaultPlanningAssignmentResponse.model_validate(response.json())

    async def delete_default_planning_by_shift_id(
        self,
        shift_id: UUID,
    ) -> None:
        """Deletes plan matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/DefaultPlanning/{shift_id}",
        )
        response.raise_for_status()

    async def create_default_planning(
        self,
        shift_id: UUID,
        assignments: list[ResourceAssignmentRequest] | None = None,
    ) -> DefaultPlanningAssignmentResponse:
        """Posts a new plan."""
        _body: dict[str, object] = {
            "shiftId": str(shift_id),
        }
        if assignments is not None:
            _body["assignments"] = assignments
        response = await self._http.post(
            f"{_PREFIX}/DefaultPlanning",
            json=_body,
        )
        response.raise_for_status()
        return DefaultPlanningAssignmentResponse.model_validate(response.json())

    async def default_planning_get_validate(
        self,
    ) -> ValidateResponse:
        """Checks whether any resource has been assigned in multiple plans."""
        response = await self._http.get(
            f"{_PREFIX}/DefaultPlanning/validate",
        )
        response.raise_for_status()
        return ValidateResponse.model_validate(response.json())

    async def get_department_by_id(
        self,
        id: UUID,
    ) -> DepartmentResponse:
        """Gets department matching given id."""
        response = await self._http.get(
            f"{_PREFIX}/Department/{id}",
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def update_department_by_id(
        self,
        id: UUID,
        name: str | None = None,
        order_id: int | None = None,
        hex_color: str | None = None,
    ) -> DepartmentResponse:
        """Patches department matching given id."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if order_id is not None:
            _body["orderId"] = order_id
        if hex_color is not None:
            _body["hexColor"] = hex_color
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
        """Deletes department matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Department/{id}",
        )
        response.raise_for_status()

    async def department_get_by_order(
        self,
        order_id: int,
    ) -> None:
        """Gets departments with given order id."""
        response = await self._http.get(
            f"{_PREFIX}/Department/get-by-order/{order_id}",
        )
        response.raise_for_status()

    async def department_get_by_name(
        self,
        name: str,
    ) -> None:
        """Gets departments with given name."""
        response = await self._http.get(
            f"{_PREFIX}/Department/get-by-name/{name}",
        )
        response.raise_for_status()

    async def create_department(
        self,
        name: str,
        order_id: int,
        hex_color: str | None = None,
    ) -> DepartmentResponse:
        """Creates a new department."""
        _body: dict[str, object] = {
            "name": name,
            "orderId": order_id,
        }
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/Department",
            json=_body,
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def get_by_previous_tour_id(
        self,
        tour_id: UUID,
    ) -> EmptyTourResponse:
        """Retrieves all empty tours whose preceding tour matches the given id."""
        response = await self._http.get(
            f"{_PREFIX}/EmptyTour/get-by-previous-tour-id/{tour_id}",
        )
        response.raise_for_status()
        return EmptyTourResponse.model_validate(response.json())

    async def get_by_next_tour_id(
        self,
        tour_id: UUID,
    ) -> EmptyTourResponse:
        """Retrieves all empty tours whose following tour matches the given id."""
        response = await self._http.get(
            f"{_PREFIX}/EmptyTour/get-by-next-tour-id/{tour_id}",
        )
        response.raise_for_status()
        return EmptyTourResponse.model_validate(response.json())

    async def recreate(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> None:
        """Recreates the empty tours for all tours whose start date time is within the given time range."""
        _params: dict[str, object] = {}
        if from_ is not None:
            _params["from"] = from_
        if to is not None:
            _params["to"] = to
        response = await self._http.post(
            f"{_PREFIX}/EmptyTour/recreate",
            params=_params,
        )
        response.raise_for_status()

    async def get_estimated_time_of_arrival_by_id(
        self,
        id: UUID,
    ) -> EstimatedTimeOfArrivalResponse:
        """Retrives the eta with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/EstimatedTimeOfArrival/{id}",
        )
        response.raise_for_status()
        return EstimatedTimeOfArrivalResponse.model_validate(response.json())

    async def estimated_time_of_arrival_get_by_tour(
        self,
        id: str,
        tour_id: UUID | None = None,
    ) -> EstimatedTimeOfArrivalResponse:
        """Retrives the eta with the given tourId."""
        _params: dict[str, object] = {}
        if tour_id is not None:
            _params["tourId"] = str(tour_id)
        response = await self._http.get(
            f"{_PREFIX}/EstimatedTimeOfArrival/get-by-tour/{id}",
            params=_params,
        )
        response.raise_for_status()
        return EstimatedTimeOfArrivalResponse.model_validate(response.json())

    async def estimated_time_of_arrival_get_all(
        self,
    ) -> None:
        """Retrives all etas for the current organization."""
        response = await self._http.get(
            f"{_PREFIX}/EstimatedTimeOfArrival/get-all",
        )
        response.raise_for_status()

    async def get_geofence_by_id(
        self,
        id: UUID,
    ) -> GeofenceResponse:
        """Gets geofence matching given id."""
        response = await self._http.get(
            f"{_PREFIX}/Geofence/{id}",
        )
        response.raise_for_status()
        return GeofenceResponse.model_validate(response.json())

    async def update_geofence_by_id(
        self,
        id: UUID,
        name: str | None = None,
        address_id: UUID | None = None,
        color: str | None = None,
        enable_tracking: bool | None = None,
        on_enter_flow_name: str | None = None,
        on_leave_flow_name: str | None = None,
        location: list[GeoLocationModel] | None = None,
    ) -> GeofenceResponse:
        """Patches geofence matching given id."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if address_id is not None:
            _body["addressId"] = str(address_id)
        if color is not None:
            _body["color"] = color
        if enable_tracking is not None:
            _body["enableTracking"] = enable_tracking
        if on_enter_flow_name is not None:
            _body["onEnterFlowName"] = on_enter_flow_name
        if on_leave_flow_name is not None:
            _body["onLeaveFlowName"] = on_leave_flow_name
        if location is not None:
            _body["location"] = location
        response = await self._http.patch(
            f"{_PREFIX}/Geofence/{id}",
            json=_body,
        )
        response.raise_for_status()
        return GeofenceResponse.model_validate(response.json())

    async def delete_geofence_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes geofence matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Geofence/{id}",
        )
        response.raise_for_status()

    async def create_geofence(
        self,
        name: str | None = None,
        color: str | None = None,
        address_id: UUID | None = None,
        enable_tracking: bool | None = None,
        on_enter_flow_name: str | None = None,
        on_leave_flow_name: str | None = None,
        location: list[GeoLocationModel] | None = None,
    ) -> GeofenceResponse:
        """Creates a new geofence."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if color is not None:
            _body["color"] = color
        if address_id is not None:
            _body["addressId"] = str(address_id)
        if enable_tracking is not None:
            _body["enableTracking"] = enable_tracking
        if on_enter_flow_name is not None:
            _body["onEnterFlowName"] = on_enter_flow_name
        if on_leave_flow_name is not None:
            _body["onLeaveFlowName"] = on_leave_flow_name
        if location is not None:
            _body["location"] = location
        response = await self._http.post(
            f"{_PREFIX}/Geofence",
            json=_body,
        )
        response.raise_for_status()
        return GeofenceResponse.model_validate(response.json())

    async def geofence_get_by_location(
        self,
        longitude: float | None = None,
        latitude: float | None = None,
        radius_in_meters: float | None = None,
    ) -> None:
        """Retrieves geofences from a location."""
        _params: dict[str, object] = {}
        if longitude is not None:
            _params["longitude"] = longitude
        if latitude is not None:
            _params["latitude"] = latitude
        if radius_in_meters is not None:
            _params["radiusInMeters"] = radius_in_meters
        response = await self._http.get(
            f"{_PREFIX}/Geofence/get-by-location",
            params=_params,
        )
        response.raise_for_status()

    async def get_geofence_resource_tracking_by_id(
        self,
        id: UUID,
    ) -> GeofenceResourceTracking:
        """Gets a geofence resource tracking by id."""
        response = await self._http.get(
            f"{_PREFIX}/GeofenceResourceTracking/{id}",
        )
        response.raise_for_status()
        return GeofenceResourceTracking.model_validate(response.json())

    async def get_active(
        self,
        resource_id: UUID,
    ) -> None:
        """Gets all active geofence resource trackings for a resource."""
        response = await self._http.get(
            f"{_PREFIX}/GeofenceResourceTracking/active/{resource_id}",
        )
        response.raise_for_status()

    async def filter(
        self,
        id: UUID | None = None,
        organization_id: UUID | None = None,
        is_deleted: bool | None = None,
        query_all_organizations: bool | None = None,
        include_ids: list[UUID] | None = None,
        exclude_id: UUID | None = None,
        resource_id: UUID | None = None,
        geofence_id: UUID | None = None,
        is_active: bool | None = None,
    ) -> None:
        """Gets geofence resource trackings by filter."""
        _body: dict[str, object] = {
        }
        if id is not None:
            _body["id"] = str(id)
        if organization_id is not None:
            _body["organizationId"] = str(organization_id)
        if is_deleted is not None:
            _body["isDeleted"] = is_deleted
        if query_all_organizations is not None:
            _body["queryAllOrganizations"] = query_all_organizations
        if include_ids is not None:
            _body["includeIds"] = str(include_ids)
        if exclude_id is not None:
            _body["excludeId"] = str(exclude_id)
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if geofence_id is not None:
            _body["geofenceId"] = str(geofence_id)
        if is_active is not None:
            _body["isActive"] = is_active
        response = await self._http.post(
            f"{_PREFIX}/GeofenceResourceTracking/filter",
            json=_body,
        )
        response.raise_for_status()

    async def get_incoterm_by_id(
        self,
        id: UUID,
    ) -> IncotermResponse:
        """Gets incoterm matching given id."""
        response = await self._http.get(
            f"{_PREFIX}/Incoterm/{id}",
        )
        response.raise_for_status()
        return IncotermResponse.model_validate(response.json())

    async def update_incoterm_by_id(
        self,
        id: UUID,
        name: str | None = None,
        order_id: int | None = None,
        abbreviation: str | None = None,
        description: str | None = None,
    ) -> IncotermResponse:
        """Patches incoterm matching given id."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if order_id is not None:
            _body["orderId"] = order_id
        if abbreviation is not None:
            _body["abbreviation"] = abbreviation
        if description is not None:
            _body["description"] = description
        response = await self._http.patch(
            f"{_PREFIX}/Incoterm/{id}",
            json=_body,
        )
        response.raise_for_status()
        return IncotermResponse.model_validate(response.json())

    async def delete_incoterm_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes incoterm matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Incoterm/{id}",
        )
        response.raise_for_status()

    async def incoterm_get_by_order(
        self,
        order_id: int,
    ) -> None:
        """Gets incoterms with given order id."""
        response = await self._http.get(
            f"{_PREFIX}/Incoterm/get-by-order/{order_id}",
        )
        response.raise_for_status()

    async def incoterm_get_by_name(
        self,
        name: str,
    ) -> None:
        """Gets incoterms with given name."""
        response = await self._http.get(
            f"{_PREFIX}/Incoterm/get-by-name/{name}",
        )
        response.raise_for_status()

    async def get_by_abbreviation(
        self,
        abbreviation: str,
    ) -> None:
        """Gets incoterms with given abbreviation."""
        response = await self._http.get(
            f"{_PREFIX}/Incoterm/get-by-abbreviation/{abbreviation}",
        )
        response.raise_for_status()

    async def create_incoterm(
        self,
        name: str,
        order_id: int,
        abbreviation: str,
        description: str | None = None,
    ) -> IncotermResponse:
        """Creates a new incoterm."""
        _body: dict[str, object] = {
            "name": name,
            "orderId": order_id,
            "abbreviation": abbreviation,
        }
        if description is not None:
            _body["description"] = description
        response = await self._http.post(
            f"{_PREFIX}/Incoterm",
            json=_body,
        )
        response.raise_for_status()
        return IncotermResponse.model_validate(response.json())

    async def internal_department_get_by_id(
        self,
        id: UUID | None = None,
    ) -> DepartmentResponse:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalDepartment/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return DepartmentResponse.model_validate(response.json())

    async def internal_incoterm_get_by_id(
        self,
        id: UUID | None = None,
    ) -> IncotermResponse:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalIncoterm/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return IncotermResponse.model_validate(response.json())

    async def internal_loading_aid_type_get_by_id(
        self,
        id: UUID | None = None,
    ) -> LoadingAidTypeResponse:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalLoadingAidType/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

    async def create_loading_aid_type(
        self,
        number: int,
        display_name: str | None = None,
        weight: float | None = None,
        short_text: str | None = None,
        width: int | None = None,
        length: int | None = None,
        storage_position: float | None = None,
    ) -> LoadingAidTypeResponse:
        """Creates a new loading aid type."""
        _body: dict[str, object] = {
            "number": number,
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if weight is not None:
            _body["weight"] = weight
        if short_text is not None:
            _body["shortText"] = short_text
        if width is not None:
            _body["width"] = width
        if length is not None:
            _body["length"] = length
        if storage_position is not None:
            _body["storagePosition"] = storage_position
        response = await self._http.post(
            f"{_PREFIX}/LoadingAidType",
            json=_body,
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

    async def get_loading_aid_type_by_id(
        self,
        id: UUID,
    ) -> LoadingAidTypeResponse:
        """Retrives the loading aid type with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/LoadingAidType/{id}",
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

    async def update_loading_aid_type_by_id(
        self,
        id: UUID,
        number: int | None = None,
        display_name: str | None = None,
        weight: float | None = None,
        short_text: str | None = None,
        width: int | None = None,
        length: int | None = None,
        storage_position: float | None = None,
    ) -> LoadingAidTypeResponse:
        """Patches the loading aid type."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if display_name is not None:
            _body["displayName"] = display_name
        if weight is not None:
            _body["weight"] = weight
        if short_text is not None:
            _body["shortText"] = short_text
        if width is not None:
            _body["width"] = width
        if length is not None:
            _body["length"] = length
        if storage_position is not None:
            _body["storagePosition"] = storage_position
        response = await self._http.patch(
            f"{_PREFIX}/LoadingAidType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

    async def delete_loading_aid_type_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes loading aid type matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/LoadingAidType/{id}",
        )
        response.raise_for_status()

    async def loading_aid_type_get_all(
        self,
    ) -> None:
        """Retrieves all loading aid types."""
        response = await self._http.get(
            f"{_PREFIX}/LoadingAidType/get-all",
        )
        response.raise_for_status()

    async def create_loading_aid_type_deployment(
        self,
        number: int,
        display_name: str | None = None,
        weight: float | None = None,
        short_text: str | None = None,
        width: int | None = None,
        length: int | None = None,
        storage_position: float | None = None,
    ) -> LoadingAidTypeResponse:
        _body: dict[str, object] = {
            "number": number,
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if weight is not None:
            _body["weight"] = weight
        if short_text is not None:
            _body["shortText"] = short_text
        if width is not None:
            _body["width"] = width
        if length is not None:
            _body["length"] = length
        if storage_position is not None:
            _body["storagePosition"] = storage_position
        response = await self._http.post(
            f"{_PREFIX}/LoadingAidTypeDeployment",
            json=_body,
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

    async def update_loading_aid_type_deployment_by_id(
        self,
        id: UUID,
        number: int | None = None,
        display_name: str | None = None,
        weight: float | None = None,
        short_text: str | None = None,
        width: int | None = None,
        length: int | None = None,
        storage_position: float | None = None,
    ) -> LoadingAidTypeResponse:
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if display_name is not None:
            _body["displayName"] = display_name
        if weight is not None:
            _body["weight"] = weight
        if short_text is not None:
            _body["shortText"] = short_text
        if width is not None:
            _body["width"] = width
        if length is not None:
            _body["length"] = length
        if storage_position is not None:
            _body["storagePosition"] = storage_position
        response = await self._http.patch(
            f"{_PREFIX}/LoadingAidTypeDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return LoadingAidTypeResponse.model_validate(response.json())

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

    async def query(
        self,
        entity_type: str,
        pipeline: list[PipelineStage],
        variables: QueryVariables | None = None,
    ) -> OxQLQueryResult:
        _body: dict[str, object] = {
            "entityType": entity_type,
            "pipeline": pipeline,
        }
        if variables is not None:
            _body["variables"] = variables
        response = await self._http.post(
            f"{_PREFIX}/OxQL/query",
            json=_body,
        )
        response.raise_for_status()
        return OxQLQueryResult.model_validate(response.json())

    async def get_types(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/OxQL/types",
        )
        response.raise_for_status()

    async def get_health(
        self,
    ) -> None:
        response = await self._http.get(
            f"{_PREFIX}/OxQL/health",
        )
        response.raise_for_status()

    async def create_planning_region(
        self,
        name: str,
        hex_color: str | None = None,
        include: list[RegionModel] | None = None,
        exclude: list[RegionModel] | None = None,
        functions: list[str] | None = None,
    ) -> PlanningRegionModel:
        """Creates a new planning region."""
        _body: dict[str, object] = {
            "name": name,
        }
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if include is not None:
            _body["include"] = include
        if exclude is not None:
            _body["exclude"] = exclude
        if functions is not None:
            _body["functions"] = functions
        response = await self._http.post(
            f"{_PREFIX}/PlanningRegion",
            json=_body,
        )
        response.raise_for_status()
        return PlanningRegionModel.model_validate(response.json())

    async def get_planning_region_by_id(
        self,
        id: UUID,
    ) -> PlanningRegionModel:
        """Retrives the planning region with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/PlanningRegion/{id}",
        )
        response.raise_for_status()
        return PlanningRegionModel.model_validate(response.json())

    async def update_planning_region_by_id(
        self,
        id: UUID,
        name: str | None = None,
        hex_color: str | None = None,
        include: list[RegionModel] | None = None,
        exclude: list[RegionModel] | None = None,
        functions: list[str] | None = None,
    ) -> PlanningRegionModel:
        """Updates/saves the given planning region."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if include is not None:
            _body["include"] = include
        if exclude is not None:
            _body["exclude"] = exclude
        if functions is not None:
            _body["functions"] = functions
        response = await self._http.patch(
            f"{_PREFIX}/PlanningRegion/{id}",
            json=_body,
        )
        response.raise_for_status()
        return PlanningRegionModel.model_validate(response.json())

    async def delete_planning_region_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a planning region."""
        response = await self._http.delete(
            f"{_PREFIX}/PlanningRegion/{id}",
        )
        response.raise_for_status()

    async def planning_region_get_all(
        self,
    ) -> None:
        """Retrieves all planning region."""
        response = await self._http.get(
            f"{_PREFIX}/PlanningRegion/get-all",
        )
        response.raise_for_status()

    async def reporting_get_by_tour(
        self,
        id: UUID,
    ) -> TourReportingModel:
        """Retrieves the tour with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Reporting/get-by-tour/{id}",
        )
        response.raise_for_status()
        return TourReportingModel.model_validate(response.json())

    async def get_carrier_report(
        self,
        tour_id: UUID,
    ) -> CarrierOrderReportResponse:
        response = await self._http.get(
            f"{_PREFIX}/Reporting/{tour_id}/carrier-report",
        )
        response.raise_for_status()
        return CarrierOrderReportResponse.model_validate(response.json())

    async def get_resource_by_id(
        self,
        id: UUID,
    ) -> ResourceModel:
        """Retrives the resource with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Resource/{id}",
        )
        response.raise_for_status()
        return ResourceModel.model_validate(response.json())

    async def update_resource_by_id(
        self,
        id: UUID,
        type: str,
        match_code: str,
        display_name: str | None = None,
        loading_slots: list[LoadingSlotModel] | None = None,
        location: ResourceLocationModel | None = None,
        is_loadable: bool | None = None,
        planning_order_key: str | None = None,
        usable_until: str | None = None,
        notes: str | None = None,
    ) -> ResourceModel:
        _body: dict[str, object] = {
            "type": type,
            "matchCode": match_code,
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if loading_slots is not None:
            _body["loadingSlots"] = loading_slots
        if location is not None:
            _body["location"] = location
        if is_loadable is not None:
            _body["isLoadable"] = is_loadable
        if planning_order_key is not None:
            _body["planningOrderKey"] = planning_order_key
        if usable_until is not None:
            _body["usableUntil"] = usable_until
        if notes is not None:
            _body["notes"] = notes
        response = await self._http.put(
            f"{_PREFIX}/Resource/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ResourceModel.model_validate(response.json())

    async def resource_get_all(
        self,
        useable_until: str | None = None,
    ) -> None:
        """Retrieves all resources."""
        _params: dict[str, object] = {}
        if useable_until is not None:
            _params["useableUntil"] = useable_until
        response = await self._http.get(
            f"{_PREFIX}/Resource/get-all",
            params=_params,
        )
        response.raise_for_status()

    async def get_all_by_group(
        self,
        group: str | None = None,
        useable_until: str | None = None,
    ) -> None:
        """Retrieves all resources."""
        _params: dict[str, object] = {}
        if group is not None:
            _params["group"] = group
        if useable_until is not None:
            _params["useableUntil"] = useable_until
        response = await self._http.get(
            f"{_PREFIX}/Resource/get-all-by-group",
            params=_params,
        )
        response.raise_for_status()

    async def get_page_data(
        self,
        skip: int | None = None,
        page: int | None = None,
        page_size: int | None = None,
        filter_string: str | None = None,
    ) -> None:
        """Retrieves a data page of resources."""
        _params: dict[str, object] = {}
        if skip is not None:
            _params["skip"] = skip
        if page is not None:
            _params["page"] = page
        if page_size is not None:
            _params["pageSize"] = page_size
        if filter_string is not None:
            _params["filterString"] = filter_string
        response = await self._http.get(
            f"{_PREFIX}/Resource/get-page-data",
            params=_params,
        )
        response.raise_for_status()

    async def resource_get_by_location(
        self,
        longitude: float | None = None,
        latitude: float | None = None,
        max_distance_meter: float | None = None,
        min_distance_meter: float | None = None,
        group: str | None = None,
    ) -> None:
        """Retrieves resources from a specific group and location."""
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
            f"{_PREFIX}/Resource/get-by-location",
            params=_params,
        )
        response.raise_for_status()

    async def get_in_geofence(
        self,
        geofence_id: UUID,
    ) -> None:
        """Retrieves resources in a geofence."""
        response = await self._http.get(
            f"{_PREFIX}/Resource/get-in-geofence/{geofence_id}",
        )
        response.raise_for_status()

    async def create_resource(
        self,
        type: str,
        match_code: str,
        display_name: str | None = None,
        loading_slots: list[LoadingSlotModel] | None = None,
        location: ResourceLocationModel | None = None,
        is_loadable: bool | None = None,
        planning_order_key: str | None = None,
        usable_until: str | None = None,
        notes: str | None = None,
    ) -> ResourceModel:
        _body: dict[str, object] = {
            "type": type,
            "matchCode": match_code,
        }
        if display_name is not None:
            _body["displayName"] = display_name
        if loading_slots is not None:
            _body["loadingSlots"] = loading_slots
        if location is not None:
            _body["location"] = location
        if is_loadable is not None:
            _body["isLoadable"] = is_loadable
        if planning_order_key is not None:
            _body["planningOrderKey"] = planning_order_key
        if usable_until is not None:
            _body["usableUntil"] = usable_until
        if notes is not None:
            _body["notes"] = notes
        response = await self._http.post(
            f"{_PREFIX}/Resource",
            json=_body,
        )
        response.raise_for_status()
        return ResourceModel.model_validate(response.json())

    async def get_resource_group_by_id(
        self,
        id: UUID,
    ) -> GroupedResourcesModel:
        """Retrives the resource group with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ResourceGroup/{id}",
        )
        response.raise_for_status()
        return GroupedResourcesModel.model_validate(response.json())

    async def update_resource_group_by_id(
        self,
        id: UUID,
        name: str | None = None,
        resource_ids: list[UUID] | None = None,
    ) -> GroupedResourcesModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if resource_ids is not None:
            _body["resourceIds"] = str(resource_ids)
        response = await self._http.patch(
            f"{_PREFIX}/ResourceGroup/{id}",
            json=_body,
        )
        response.raise_for_status()
        return GroupedResourcesModel.model_validate(response.json())

    async def delete_resource_group_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/ResourceGroup/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def get_resource_group(
        self,
    ) -> None:
        """Retrives all resource groups"""
        response = await self._http.get(
            f"{_PREFIX}/ResourceGroup",
        )
        response.raise_for_status()

    async def create_resource_group(
        self,
        name: str,
        resource_ids: list[UUID],
    ) -> GroupedResourcesModel:
        response = await self._http.post(
            f"{_PREFIX}/ResourceGroup",
            json={"name": name, "resourceIds": str(resource_ids)},
        )
        response.raise_for_status()
        return GroupedResourcesModel.model_validate(response.json())

    async def resource_map_get_by_location(
        self,
        longitude: float | None = None,
        latitude: float | None = None,
        max_distance_meter: float | None = None,
        min_distance_meter: float | None = None,
        group: str | None = None,
    ) -> None:
        """Retrieves resources from a specific group and location."""
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
            f"{_PREFIX}/ResourceMap/get-by-location",
            params=_params,
        )
        response.raise_for_status()

    async def get_scheduled_planning_by_id(
        self,
        id: UUID,
    ) -> ScheduledPlanningAssignmentResponse:
        """Gets plan matching given id."""
        response = await self._http.get(
            f"{_PREFIX}/ScheduledPlanning/{id}",
        )
        response.raise_for_status()
        return ScheduledPlanningAssignmentResponse.model_validate(response.json())

    async def update_scheduled_planning_by_id(
        self,
        id: UUID,
        assignments: list[ResourceAssignmentPatch] | None = None,
        shift_id: UUID | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> ScheduledPlanningAssignmentResponse:
        """Patches plan matching given id."""
        _body: dict[str, object] = {
        }
        if assignments is not None:
            _body["assignments"] = assignments
        if shift_id is not None:
            _body["shiftId"] = str(shift_id)
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        response = await self._http.patch(
            f"{_PREFIX}/ScheduledPlanning/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ScheduledPlanningAssignmentResponse.model_validate(response.json())

    async def delete_scheduled_planning_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes plan matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ScheduledPlanning/{id}",
        )
        response.raise_for_status()

    async def get_by_date(
        self,
        date_time: str | None = None,
    ) -> None:
        """Gets all plans for given day."""
        _params: dict[str, object] = {}
        if date_time is not None:
            _params["dateTime"] = date_time
        response = await self._http.get(
            f"{_PREFIX}/ScheduledPlanning/get-by-date",
            params=_params,
        )
        response.raise_for_status()

    async def scheduled_planning_get_by_shift(
        self,
        shift_id: UUID,
        date_time: str | None = None,
    ) -> None:
        """Gets plans matching given shift id for given day."""
        _params: dict[str, object] = {}
        if date_time is not None:
            _params["dateTime"] = date_time
        response = await self._http.get(
            f"{_PREFIX}/ScheduledPlanning/get-by-shift/{shift_id}",
            params=_params,
        )
        response.raise_for_status()

    async def scheduled_planning_get_by_resource(
        self,
        resource_id: UUID,
        date_time: str | None = None,
        shift_id: UUID | None = None,
    ) -> ScheduledPlanningAssignmentResponse:
        """Gets shifts for resource on given day."""
        _params: dict[str, object] = {}
        if date_time is not None:
            _params["dateTime"] = date_time
        if shift_id is not None:
            _params["shiftId"] = str(shift_id)
        response = await self._http.get(
            f"{_PREFIX}/ScheduledPlanning/get-by-resource/{resource_id}",
            params=_params,
        )
        response.raise_for_status()
        return ScheduledPlanningAssignmentResponse.model_validate(response.json())

    async def create_scheduled_planning(
        self,
        shift_id: UUID,
        start_date: str,
        assignments: list[ResourceAssignmentRequest] | None = None,
    ) -> ScheduledPlanningAssignmentResponse:
        """Posts a new plan."""
        _body: dict[str, object] = {
            "shiftId": str(shift_id),
            "startDate": start_date,
        }
        if assignments is not None:
            _body["assignments"] = assignments
        response = await self._http.post(
            f"{_PREFIX}/ScheduledPlanning",
            json=_body,
        )
        response.raise_for_status()
        return ScheduledPlanningAssignmentResponse.model_validate(response.json())

    async def scheduled_planning_get_validate(
        self,
    ) -> ValidateResponse:
        """Checks whether any resource has been assigned in multiple plans."""
        response = await self._http.get(
            f"{_PREFIX}/ScheduledPlanning/validate",
        )
        response.raise_for_status()
        return ValidateResponse.model_validate(response.json())

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

    async def get_shift_by_id(
        self,
        id: UUID,
    ) -> ShiftResponse:
        """Gets shift matching given id."""
        response = await self._http.get(
            f"{_PREFIX}/Shift/{id}",
        )
        response.raise_for_status()
        return ShiftResponse.model_validate(response.json())

    async def update_shift_by_id(
        self,
        id: UUID,
        name: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
    ) -> ShiftResponse:
        """Patches shift matching given id."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if start_time is not None:
            _body["startTime"] = start_time
        if end_time is not None:
            _body["endTime"] = end_time
        response = await self._http.patch(
            f"{_PREFIX}/Shift/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShiftResponse.model_validate(response.json())

    async def delete_shift_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes shift matching given id."""
        response = await self._http.delete(
            f"{_PREFIX}/Shift/{id}",
        )
        response.raise_for_status()

    async def get_by_range(
        self,
        start: str | None = None,
        end: str | None = None,
    ) -> None:
        """Gets shifts in given range."""
        _params: dict[str, object] = {}
        if start is not None:
            _params["start"] = start
        if end is not None:
            _params["end"] = end
        response = await self._http.get(
            f"{_PREFIX}/Shift/get-by-range",
            params=_params,
        )
        response.raise_for_status()

    async def shift_get_by_name(
        self,
        name: str,
    ) -> None:
        """Gets shifts matching given name."""
        response = await self._http.get(
            f"{_PREFIX}/Shift/get-by-name/{name}",
        )
        response.raise_for_status()

    async def create_shift(
        self,
        name: str,
        start_time: str,
        end_time: str,
    ) -> ShiftResponse:
        """Creates a new shift."""
        response = await self._http.post(
            f"{_PREFIX}/Shift",
            json={"name": name, "startTime": start_time, "endTime": end_time},
        )
        response.raise_for_status()
        return ShiftResponse.model_validate(response.json())

    async def get_all_with_conditions(
        self,
        status: str | None = None,
        from_: str | None = None,
        to: str | None = None,
    ) -> None:
        """Retrives all shipments for the given conditions."""
        _params: dict[str, object] = {}
        if status is not None:
            _params["status"] = status
        if from_ is not None:
            _params["from"] = from_
        if to is not None:
            _params["to"] = to
        response = await self._http.get(
            f"{_PREFIX}/Shipment/get-all-with-conditions",
            params=_params,
        )
        response.raise_for_status()

    async def get_shipment_by_id(
        self,
        id: UUID,
    ) -> ShipmentModel:
        """Retrives the shipment with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Shipment/{id}",
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def update_shipment_by_id(
        self,
        id: UUID,
        load_address_id: UUID | None = None,
        delivery_address_id: UUID | None = None,
        recipient_address_id: UUID | None = None,
        sender_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        freight_payer_personal_account_id: UUID | None = None,
        freight_payer_address_id: UUID | None = None,
        customer_personal_account_id: UUID | None = None,
        customer_address_id: UUID | None = None,
        invoice_recipient_personal_account_id: UUID | None = None,
        invoice_recipient_address_id: UUID | None = None,
        supplier_personal_account_id: UUID | None = None,
        supplier_address_id: UUID | None = None,
        load_start: str | None = None,
        load_end: str | None = None,
        planned_load_start: str | None = None,
        planned_load_end: str | None = None,
        calculated_load_start: str | None = None,
        calculated_load_end: str | None = None,
        actual_load_start: str | None = None,
        actual_load_end: str | None = None,
        loading_time_type: LoadingDateTimeType | None = None,
        delivery_start: str | None = None,
        delivery_end: str | None = None,
        planned_delivery_start: str | None = None,
        planned_delivery_end: str | None = None,
        calculated_delivery_start: str | None = None,
        calculated_delivery_end: str | None = None,
        actual_delivery_start: str | None = None,
        actual_delivery_end: str | None = None,
        actual_start_date_time: str | None = None,
        actual_delivery_start_date_time: str | None = None,
        delivery_time_type: LoadingDateTimeType | None = None,
        order_date: str | None = None,
        shipment_number: str | None = None,
        reference_number: str | None = None,
        load_number: str | None = None,
        delivery_number: str | None = None,
        delivery_note_number: str | None = None,
        actual_weight: QuantityPatchRequest | None = None,
        is_template: bool | None = None,
        template_name: str | None = None,
        tags: list[UUID] | None = None,
        notes: str | None = None,
        external_notes: str | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
        construction_site_id: UUID | None = None,
        department_id: UUID | None = None,
        incoterm_id: UUID | None = None,
        addon: dict[str, object] | None = None,
        items: list[PatchShipmentItemRequest] | None = None,
        billing_lines: list[PatchBillingLineRequest] | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
    ) -> ShipmentModel:
        _body: dict[str, object] = {
        }
        if load_address_id is not None:
            _body["loadAddressId"] = str(load_address_id)
        if delivery_address_id is not None:
            _body["deliveryAddressId"] = str(delivery_address_id)
        if recipient_address_id is not None:
            _body["recipientAddressId"] = str(recipient_address_id)
        if sender_address_id is not None:
            _body["senderAddressId"] = str(sender_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if freight_payer_personal_account_id is not None:
            _body["freightPayerPersonalAccountId"] = str(freight_payer_personal_account_id)
        if freight_payer_address_id is not None:
            _body["freightPayerAddressId"] = str(freight_payer_address_id)
        if customer_personal_account_id is not None:
            _body["customerPersonalAccountId"] = str(customer_personal_account_id)
        if customer_address_id is not None:
            _body["customerAddressId"] = str(customer_address_id)
        if invoice_recipient_personal_account_id is not None:
            _body["invoiceRecipientPersonalAccountId"] = str(invoice_recipient_personal_account_id)
        if invoice_recipient_address_id is not None:
            _body["invoiceRecipientAddressId"] = str(invoice_recipient_address_id)
        if supplier_personal_account_id is not None:
            _body["supplierPersonalAccountId"] = str(supplier_personal_account_id)
        if supplier_address_id is not None:
            _body["supplierAddressId"] = str(supplier_address_id)
        if load_start is not None:
            _body["loadStart"] = load_start
        if load_end is not None:
            _body["loadEnd"] = load_end
        if planned_load_start is not None:
            _body["plannedLoadStart"] = planned_load_start
        if planned_load_end is not None:
            _body["plannedLoadEnd"] = planned_load_end
        if calculated_load_start is not None:
            _body["calculatedLoadStart"] = calculated_load_start
        if calculated_load_end is not None:
            _body["calculatedLoadEnd"] = calculated_load_end
        if actual_load_start is not None:
            _body["actualLoadStart"] = actual_load_start
        if actual_load_end is not None:
            _body["actualLoadEnd"] = actual_load_end
        if loading_time_type is not None:
            _body["loadingTimeType"] = loading_time_type
        if delivery_start is not None:
            _body["deliveryStart"] = delivery_start
        if delivery_end is not None:
            _body["deliveryEnd"] = delivery_end
        if planned_delivery_start is not None:
            _body["plannedDeliveryStart"] = planned_delivery_start
        if planned_delivery_end is not None:
            _body["plannedDeliveryEnd"] = planned_delivery_end
        if calculated_delivery_start is not None:
            _body["calculatedDeliveryStart"] = calculated_delivery_start
        if calculated_delivery_end is not None:
            _body["calculatedDeliveryEnd"] = calculated_delivery_end
        if actual_delivery_start is not None:
            _body["actualDeliveryStart"] = actual_delivery_start
        if actual_delivery_end is not None:
            _body["actualDeliveryEnd"] = actual_delivery_end
        if actual_start_date_time is not None:
            _body["actualStartDateTime"] = actual_start_date_time
        if actual_delivery_start_date_time is not None:
            _body["actualDeliveryStartDateTime"] = actual_delivery_start_date_time
        if delivery_time_type is not None:
            _body["deliveryTimeType"] = delivery_time_type
        if order_date is not None:
            _body["orderDate"] = order_date
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if load_number is not None:
            _body["loadNumber"] = load_number
        if delivery_number is not None:
            _body["deliveryNumber"] = delivery_number
        if delivery_note_number is not None:
            _body["deliveryNoteNumber"] = delivery_note_number
        if actual_weight is not None:
            _body["actualWeight"] = actual_weight
        if is_template is not None:
            _body["isTemplate"] = is_template
        if template_name is not None:
            _body["templateName"] = template_name
        if tags is not None:
            _body["tags"] = str(tags)
        if notes is not None:
            _body["notes"] = notes
        if external_notes is not None:
            _body["externalNotes"] = external_notes
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        if construction_site_id is not None:
            _body["constructionSiteId"] = str(construction_site_id)
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if incoterm_id is not None:
            _body["incotermId"] = str(incoterm_id)
        if addon is not None:
            _body["addon"] = addon
        if items is not None:
            _body["items"] = items
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        response = await self._http.patch(
            f"{_PREFIX}/Shipment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def delete_shipment_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/Shipment/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def get_updated_since(
        self,
        since: str | None = None,
    ) -> None:
        """Retrives the shipment with the given id."""
        _params: dict[str, object] = {}
        if since is not None:
            _params["since"] = since
        response = await self._http.get(
            f"{_PREFIX}/Shipment/get-updated-since",
            params=_params,
        )
        response.raise_for_status()

    async def shipment_create_shipment(
        self,
        load_address_id: UUID | None = None,
        delivery_address_id: UUID | None = None,
        recipient_address_id: UUID | None = None,
        sender_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        freight_payer_personal_account_id: UUID | None = None,
        freight_payer_address_id: UUID | None = None,
        customer_personal_account_id: UUID | None = None,
        customer_address_id: UUID | None = None,
        invoice_recipient_personal_account_id: UUID | None = None,
        invoice_recipient_address_id: UUID | None = None,
        supplier_personal_account_id: UUID | None = None,
        supplier_address_id: UUID | None = None,
        load_start: str | None = None,
        load_end: str | None = None,
        planned_load_start: str | None = None,
        planned_load_end: str | None = None,
        calculated_load_start: str | None = None,
        calculated_load_end: str | None = None,
        actual_load_start: str | None = None,
        actual_load_end: str | None = None,
        loading_time_type: LoadingDateTimeType | None = None,
        delivery_start: str | None = None,
        delivery_end: str | None = None,
        planned_delivery_start: str | None = None,
        planned_delivery_end: str | None = None,
        calculated_delivery_start: str | None = None,
        calculated_delivery_end: str | None = None,
        actual_delivery_start: str | None = None,
        actual_delivery_end: str | None = None,
        actual_start_date_time: str | None = None,
        actual_delivery_start_date_time: str | None = None,
        delivery_time_type: LoadingDateTimeType | None = None,
        order_date: str | None = None,
        shipment_number: str | None = None,
        reference_number: str | None = None,
        load_number: str | None = None,
        delivery_number: str | None = None,
        delivery_note_number: str | None = None,
        actual_weight: QuantityRequest | None = None,
        is_template: bool | None = None,
        template_name: str | None = None,
        tags: list[UUID] | None = None,
        notes: str | None = None,
        external_notes: str | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
        construction_site_id: UUID | None = None,
        department_id: UUID | None = None,
        incoterm_id: UUID | None = None,
        addon: dict[str, object] | None = None,
        items: list[CreateShipmentItemRequest] | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        billing_lines: list[CreateBillingLineRequest] | None = None,
    ) -> ShipmentModel:
        _body: dict[str, object] = {
        }
        if load_address_id is not None:
            _body["loadAddressId"] = str(load_address_id)
        if delivery_address_id is not None:
            _body["deliveryAddressId"] = str(delivery_address_id)
        if recipient_address_id is not None:
            _body["recipientAddressId"] = str(recipient_address_id)
        if sender_address_id is not None:
            _body["senderAddressId"] = str(sender_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if freight_payer_personal_account_id is not None:
            _body["freightPayerPersonalAccountId"] = str(freight_payer_personal_account_id)
        if freight_payer_address_id is not None:
            _body["freightPayerAddressId"] = str(freight_payer_address_id)
        if customer_personal_account_id is not None:
            _body["customerPersonalAccountId"] = str(customer_personal_account_id)
        if customer_address_id is not None:
            _body["customerAddressId"] = str(customer_address_id)
        if invoice_recipient_personal_account_id is not None:
            _body["invoiceRecipientPersonalAccountId"] = str(invoice_recipient_personal_account_id)
        if invoice_recipient_address_id is not None:
            _body["invoiceRecipientAddressId"] = str(invoice_recipient_address_id)
        if supplier_personal_account_id is not None:
            _body["supplierPersonalAccountId"] = str(supplier_personal_account_id)
        if supplier_address_id is not None:
            _body["supplierAddressId"] = str(supplier_address_id)
        if load_start is not None:
            _body["loadStart"] = load_start
        if load_end is not None:
            _body["loadEnd"] = load_end
        if planned_load_start is not None:
            _body["plannedLoadStart"] = planned_load_start
        if planned_load_end is not None:
            _body["plannedLoadEnd"] = planned_load_end
        if calculated_load_start is not None:
            _body["calculatedLoadStart"] = calculated_load_start
        if calculated_load_end is not None:
            _body["calculatedLoadEnd"] = calculated_load_end
        if actual_load_start is not None:
            _body["actualLoadStart"] = actual_load_start
        if actual_load_end is not None:
            _body["actualLoadEnd"] = actual_load_end
        if loading_time_type is not None:
            _body["loadingTimeType"] = loading_time_type
        if delivery_start is not None:
            _body["deliveryStart"] = delivery_start
        if delivery_end is not None:
            _body["deliveryEnd"] = delivery_end
        if planned_delivery_start is not None:
            _body["plannedDeliveryStart"] = planned_delivery_start
        if planned_delivery_end is not None:
            _body["plannedDeliveryEnd"] = planned_delivery_end
        if calculated_delivery_start is not None:
            _body["calculatedDeliveryStart"] = calculated_delivery_start
        if calculated_delivery_end is not None:
            _body["calculatedDeliveryEnd"] = calculated_delivery_end
        if actual_delivery_start is not None:
            _body["actualDeliveryStart"] = actual_delivery_start
        if actual_delivery_end is not None:
            _body["actualDeliveryEnd"] = actual_delivery_end
        if actual_start_date_time is not None:
            _body["actualStartDateTime"] = actual_start_date_time
        if actual_delivery_start_date_time is not None:
            _body["actualDeliveryStartDateTime"] = actual_delivery_start_date_time
        if delivery_time_type is not None:
            _body["deliveryTimeType"] = delivery_time_type
        if order_date is not None:
            _body["orderDate"] = order_date
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if load_number is not None:
            _body["loadNumber"] = load_number
        if delivery_number is not None:
            _body["deliveryNumber"] = delivery_number
        if delivery_note_number is not None:
            _body["deliveryNoteNumber"] = delivery_note_number
        if actual_weight is not None:
            _body["actualWeight"] = actual_weight
        if is_template is not None:
            _body["isTemplate"] = is_template
        if template_name is not None:
            _body["templateName"] = template_name
        if tags is not None:
            _body["tags"] = str(tags)
        if notes is not None:
            _body["notes"] = notes
        if external_notes is not None:
            _body["externalNotes"] = external_notes
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        if construction_site_id is not None:
            _body["constructionSiteId"] = str(construction_site_id)
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if incoterm_id is not None:
            _body["incotermId"] = str(incoterm_id)
        if addon is not None:
            _body["addon"] = addon
        if items is not None:
            _body["items"] = items
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.post(
            f"{_PREFIX}/Shipment",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def item_status(
        self,
        id: UUID,
        item_id: UUID,
        status_id: UUID,
    ) -> ShipmentItemModel:
        """Sets the status of a shipment item."""
        response = await self._http.patch(
            f"{_PREFIX}/Shipment/{id}/item/{item_id}/status/{status_id}",
        )
        response.raise_for_status()
        return ShipmentItemModel.model_validate(response.json())

    async def convert_to_loading_aid_booking(
        self,
        shipment_id: UUID,
    ) -> LoadingAidBookingModel:
        """Retrives the shipment with the given id."""
        response = await self._http.post(
            f"{_PREFIX}/Shipment/convert-to-loading-aid-booking",
            json={"shipmentId": str(shipment_id)},
        )
        response.raise_for_status()
        return LoadingAidBookingModel.model_validate(response.json())

    async def shipment_set_status(
        self,
        id: UUID,
        status_id: UUID,
    ) -> ShipmentModel:
        """Sets the status of a shipment."""
        response = await self._http.post(
            f"{_PREFIX}/Shipment/{id}/set-status",
            json={"statusId": str(status_id)},
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def shipment_execute_pricing(
        self,
        id: UUID,
    ) -> None:
        response = await self._http.post(
            f"{_PREFIX}/Shipment/{id}/execute-pricing",
        )
        response.raise_for_status()

    async def create_shipment_item_status(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShipmentItemStatusModel:
        """Creates a new shipment item status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShipmentItemStatus",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentItemStatusModel.model_validate(response.json())

    async def get_shipment_item_status_by_id(
        self,
        id: UUID,
    ) -> ShipmentItemStatusModel:
        """Retrieves the shipment item status with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentItemStatus/{id}",
        )
        response.raise_for_status()
        return ShipmentItemStatusModel.model_validate(response.json())

    async def update_shipment_item_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShipmentItemStatusModel:
        """Updates/saves the given shipment item status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentItemStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentItemStatusModel.model_validate(response.json())

    async def create_shipment_item_status_deployment(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShipmentItemStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShipmentItemStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentItemStatusModel.model_validate(response.json())

    async def update_shipment_item_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShipmentItemStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentItemStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentItemStatusModel.model_validate(response.json())

    async def create_shipment_pre_advice(
        self,
        shipment_id: UUID,
        type: ShipmentPreAdviceType,
        target: str | None = None,
        status: ShipmentPreAdviceStatus | None = None,
        comment: str | None = None,
        send_option: ShipmentPreAdviceSendOption | None = None,
        required: bool | None = None,
    ) -> ShipmentPreAdviceModel:
        """Creates a new shipment pre-advice."""
        _body: dict[str, object] = {
            "shipmentId": str(shipment_id),
            "type": type,
        }
        if target is not None:
            _body["target"] = target
        if status is not None:
            _body["status"] = status
        if comment is not None:
            _body["comment"] = comment
        if send_option is not None:
            _body["sendOption"] = send_option
        if required is not None:
            _body["required"] = required
        response = await self._http.post(
            f"{_PREFIX}/ShipmentPreAdvice",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentPreAdviceModel.model_validate(response.json())

    async def get_shipment_pre_advice_by_id(
        self,
        id: UUID,
    ) -> ShipmentPreAdviceModel:
        """Retrieves the shipment pre-advice with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentPreAdvice/{id}",
        )
        response.raise_for_status()
        return ShipmentPreAdviceModel.model_validate(response.json())

    async def update_shipment_pre_advice_by_id(
        self,
        id: UUID,
        type: ShipmentPreAdviceType | None = None,
        target: str | None = None,
        comment: str | None = None,
        send_option: ShipmentPreAdviceSendOption | None = None,
        required: bool | None = None,
    ) -> ShipmentPreAdviceModel:
        """Updates the given shipment pre-advice."""
        _body: dict[str, object] = {
        }
        if type is not None:
            _body["type"] = type
        if target is not None:
            _body["target"] = target
        if comment is not None:
            _body["comment"] = comment
        if send_option is not None:
            _body["sendOption"] = send_option
        if required is not None:
            _body["required"] = required
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentPreAdvice/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentPreAdviceModel.model_validate(response.json())

    async def delete_shipment_pre_advice_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes the shipment pre-advice with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShipmentPreAdvice/{id}",
        )
        response.raise_for_status()

    async def get_by_shipment(
        self,
        shipment_id: UUID,
    ) -> None:
        """Retrieves all shipment pre-advices for the given shipment."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentPreAdvice/get-by-shipment/{shipment_id}",
        )
        response.raise_for_status()

    async def shipment_pre_advice_set_status(
        self,
        id: UUID,
        status: ShipmentPreAdviceStatus,
    ) -> ShipmentPreAdviceModel:
        """Sets the status of a shipment pre-advice."""
        response = await self._http.post(
            f"{_PREFIX}/ShipmentPreAdvice/{id}/set-status",
            json={"status": status},
        )
        response.raise_for_status()
        return ShipmentPreAdviceModel.model_validate(response.json())

    async def create_shipment_status(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> ShipmentStatusModel:
        """Creates a new shipment status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.post(
            f"{_PREFIX}/ShipmentStatus",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentStatusModel.model_validate(response.json())

    async def get_shipment_status_by_id(
        self,
        id: UUID,
    ) -> ShipmentStatusModel:
        """Retrives the shipment status with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentStatus/{id}",
        )
        response.raise_for_status()
        return ShipmentStatusModel.model_validate(response.json())

    async def update_shipment_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> ShipmentStatusModel:
        """Updates/saves the given shipment status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentStatusModel.model_validate(response.json())

    async def shipment_status_get_all(
        self,
    ) -> None:
        """Retrieves all shipment status."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentStatus/get-all",
        )
        response.raise_for_status()

    async def create_shipment_status_deployment(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> ShipmentStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.post(
            f"{_PREFIX}/ShipmentStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentStatusModel.model_validate(response.json())

    async def update_shipment_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> ShipmentStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentStatusModel.model_validate(response.json())

    async def get_shipment_tag_by_id(
        self,
        id: UUID,
    ) -> ShipmentTagModel:
        """Retrives the shipment tag with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentTag/{id}",
        )
        response.raise_for_status()
        return ShipmentTagModel.model_validate(response.json())

    async def update_shipment_tag_by_id(
        self,
        id: UUID,
        name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
    ) -> ShipmentTagModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentTag/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentTagModel.model_validate(response.json())

    async def delete_shipment_tag_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/ShipmentTag/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_shipment_tag(
        self,
        name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
    ) -> ShipmentTagModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShipmentTag",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentTagModel.model_validate(response.json())

    async def get_shipment_template_by_id(
        self,
        id: UUID,
    ) -> ShipmentTemplateModel:
        """Gets a shipment template by id."""
        response = await self._http.get(
            f"{_PREFIX}/ShipmentTemplate/{id}",
        )
        response.raise_for_status()
        return ShipmentTemplateModel.model_validate(response.json())

    async def update_shipment_template_by_id(
        self,
        id: UUID,
        load_address_id: UUID | None = None,
        delivery_address_id: UUID | None = None,
        recipient_address_id: UUID | None = None,
        sender_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        freight_payer_personal_account_id: UUID | None = None,
        freight_payer_address_id: UUID | None = None,
        customer_personal_account_id: UUID | None = None,
        customer_address_id: UUID | None = None,
        invoice_recipient_personal_account_id: UUID | None = None,
        invoice_recipient_address_id: UUID | None = None,
        supplier_personal_account_id: UUID | None = None,
        supplier_address_id: UUID | None = None,
        order_date: str | None = None,
        shipment_number: str | None = None,
        reference_number: str | None = None,
        load_number: str | None = None,
        delivery_number: str | None = None,
        template_name: str | None = None,
        is_shipment_conversion_disabled: bool | None = None,
        documents: list[ShipmentDocumentModel] | None = None,
        tags: list[ShipmentTagModel] | None = None,
        notes: str | None = None,
        external_notes: str | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
        incoterm_id: UUID | None = None,
        is_deleted: bool | None = None,
        load_workflow: ShipmentTelematicWorkflowModel | None = None,
        delivery_workflow: ShipmentTelematicWorkflowModel | None = None,
        time_mode: TemplateTimeMode | None = None,
        load_start: TemplateTime | None = None,
        load_end: TemplateTime | None = None,
        delivery_start: TemplateTime | None = None,
        delivery_end: TemplateTime | None = None,
        construction_site_id: UUID | None = None,
        department_id: UUID | None = None,
        addon: dict[str, object] | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        loading_time_type: LoadingDateTimeType | None = None,
        delivery_time_type: LoadingDateTimeType | None = None,
        items: list[PatchShipmentItemRequest] | None = None,
        billing_lines: list[PatchBillingLineRequest] | None = None,
    ) -> ShipmentTemplateModel:
        """Patches an existing shipment template."""
        _body: dict[str, object] = {
        }
        if load_address_id is not None:
            _body["loadAddressId"] = str(load_address_id)
        if delivery_address_id is not None:
            _body["deliveryAddressId"] = str(delivery_address_id)
        if recipient_address_id is not None:
            _body["recipientAddressId"] = str(recipient_address_id)
        if sender_address_id is not None:
            _body["senderAddressId"] = str(sender_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if freight_payer_personal_account_id is not None:
            _body["freightPayerPersonalAccountId"] = str(freight_payer_personal_account_id)
        if freight_payer_address_id is not None:
            _body["freightPayerAddressId"] = str(freight_payer_address_id)
        if customer_personal_account_id is not None:
            _body["customerPersonalAccountId"] = str(customer_personal_account_id)
        if customer_address_id is not None:
            _body["customerAddressId"] = str(customer_address_id)
        if invoice_recipient_personal_account_id is not None:
            _body["invoiceRecipientPersonalAccountId"] = str(invoice_recipient_personal_account_id)
        if invoice_recipient_address_id is not None:
            _body["invoiceRecipientAddressId"] = str(invoice_recipient_address_id)
        if supplier_personal_account_id is not None:
            _body["supplierPersonalAccountId"] = str(supplier_personal_account_id)
        if supplier_address_id is not None:
            _body["supplierAddressId"] = str(supplier_address_id)
        if order_date is not None:
            _body["orderDate"] = order_date
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if load_number is not None:
            _body["loadNumber"] = load_number
        if delivery_number is not None:
            _body["deliveryNumber"] = delivery_number
        if template_name is not None:
            _body["templateName"] = template_name
        if is_shipment_conversion_disabled is not None:
            _body["isShipmentConversionDisabled"] = is_shipment_conversion_disabled
        if documents is not None:
            _body["documents"] = documents
        if tags is not None:
            _body["tags"] = tags
        if notes is not None:
            _body["notes"] = notes
        if external_notes is not None:
            _body["externalNotes"] = external_notes
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        if incoterm_id is not None:
            _body["incotermId"] = str(incoterm_id)
        if is_deleted is not None:
            _body["isDeleted"] = is_deleted
        if load_workflow is not None:
            _body["loadWorkflow"] = load_workflow
        if delivery_workflow is not None:
            _body["deliveryWorkflow"] = delivery_workflow
        if time_mode is not None:
            _body["timeMode"] = time_mode
        if load_start is not None:
            _body["loadStart"] = load_start
        if load_end is not None:
            _body["loadEnd"] = load_end
        if delivery_start is not None:
            _body["deliveryStart"] = delivery_start
        if delivery_end is not None:
            _body["deliveryEnd"] = delivery_end
        if construction_site_id is not None:
            _body["constructionSiteId"] = str(construction_site_id)
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if addon is not None:
            _body["addon"] = addon
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if loading_time_type is not None:
            _body["loadingTimeType"] = loading_time_type
        if delivery_time_type is not None:
            _body["deliveryTimeType"] = delivery_time_type
        if items is not None:
            _body["items"] = items
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.patch(
            f"{_PREFIX}/ShipmentTemplate/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentTemplateModel.model_validate(response.json())

    async def delete_shipment_template_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        """Deletes a shipment template by id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShipmentTemplate/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_shipment_template(
        self,
        load_address_id: UUID | None = None,
        delivery_address_id: UUID | None = None,
        recipient_address_id: UUID | None = None,
        sender_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        freight_payer_personal_account_id: UUID | None = None,
        freight_payer_address_id: UUID | None = None,
        customer_personal_account_id: UUID | None = None,
        customer_address_id: UUID | None = None,
        invoice_recipient_personal_account_id: UUID | None = None,
        invoice_recipient_address_id: UUID | None = None,
        supplier_personal_account_id: UUID | None = None,
        supplier_address_id: UUID | None = None,
        order_date: str | None = None,
        shipment_number: str | None = None,
        reference_number: str | None = None,
        load_number: str | None = None,
        delivery_number: str | None = None,
        template_name: str | None = None,
        is_shipment_conversion_disabled: bool | None = None,
        documents: list[ShipmentDocumentModel] | None = None,
        tags: list[ShipmentTagModel] | None = None,
        notes: str | None = None,
        external_notes: str | None = None,
        load_workflow_id: UUID | None = None,
        delivery_workflow_id: UUID | None = None,
        incoterm_id: UUID | None = None,
        is_deleted: bool | None = None,
        load_workflow: ShipmentTelematicWorkflowModel | None = None,
        delivery_workflow: ShipmentTelematicWorkflowModel | None = None,
        time_mode: TemplateTimeMode | None = None,
        load_start: TemplateTime | None = None,
        load_end: TemplateTime | None = None,
        delivery_start: TemplateTime | None = None,
        delivery_end: TemplateTime | None = None,
        construction_site_id: UUID | None = None,
        department_id: UUID | None = None,
        addon: dict[str, object] | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        loading_time_type: LoadingDateTimeType | None = None,
        delivery_time_type: LoadingDateTimeType | None = None,
        items: list[CreateShipmentItemRequest] | None = None,
        billing_lines: list[CreateBillingLineRequest] | None = None,
    ) -> ShipmentTemplateModel:
        """Creates a new shipment template."""
        _body: dict[str, object] = {
        }
        if load_address_id is not None:
            _body["loadAddressId"] = str(load_address_id)
        if delivery_address_id is not None:
            _body["deliveryAddressId"] = str(delivery_address_id)
        if recipient_address_id is not None:
            _body["recipientAddressId"] = str(recipient_address_id)
        if sender_address_id is not None:
            _body["senderAddressId"] = str(sender_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if freight_payer_personal_account_id is not None:
            _body["freightPayerPersonalAccountId"] = str(freight_payer_personal_account_id)
        if freight_payer_address_id is not None:
            _body["freightPayerAddressId"] = str(freight_payer_address_id)
        if customer_personal_account_id is not None:
            _body["customerPersonalAccountId"] = str(customer_personal_account_id)
        if customer_address_id is not None:
            _body["customerAddressId"] = str(customer_address_id)
        if invoice_recipient_personal_account_id is not None:
            _body["invoiceRecipientPersonalAccountId"] = str(invoice_recipient_personal_account_id)
        if invoice_recipient_address_id is not None:
            _body["invoiceRecipientAddressId"] = str(invoice_recipient_address_id)
        if supplier_personal_account_id is not None:
            _body["supplierPersonalAccountId"] = str(supplier_personal_account_id)
        if supplier_address_id is not None:
            _body["supplierAddressId"] = str(supplier_address_id)
        if order_date is not None:
            _body["orderDate"] = order_date
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if load_number is not None:
            _body["loadNumber"] = load_number
        if delivery_number is not None:
            _body["deliveryNumber"] = delivery_number
        if template_name is not None:
            _body["templateName"] = template_name
        if is_shipment_conversion_disabled is not None:
            _body["isShipmentConversionDisabled"] = is_shipment_conversion_disabled
        if documents is not None:
            _body["documents"] = documents
        if tags is not None:
            _body["tags"] = tags
        if notes is not None:
            _body["notes"] = notes
        if external_notes is not None:
            _body["externalNotes"] = external_notes
        if load_workflow_id is not None:
            _body["loadWorkflowId"] = str(load_workflow_id)
        if delivery_workflow_id is not None:
            _body["deliveryWorkflowId"] = str(delivery_workflow_id)
        if incoterm_id is not None:
            _body["incotermId"] = str(incoterm_id)
        if is_deleted is not None:
            _body["isDeleted"] = is_deleted
        if load_workflow is not None:
            _body["loadWorkflow"] = load_workflow
        if delivery_workflow is not None:
            _body["deliveryWorkflow"] = delivery_workflow
        if time_mode is not None:
            _body["timeMode"] = time_mode
        if load_start is not None:
            _body["loadStart"] = load_start
        if load_end is not None:
            _body["loadEnd"] = load_end
        if delivery_start is not None:
            _body["deliveryStart"] = delivery_start
        if delivery_end is not None:
            _body["deliveryEnd"] = delivery_end
        if construction_site_id is not None:
            _body["constructionSiteId"] = str(construction_site_id)
        if department_id is not None:
            _body["departmentId"] = str(department_id)
        if addon is not None:
            _body["addon"] = addon
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if loading_time_type is not None:
            _body["loadingTimeType"] = loading_time_type
        if delivery_time_type is not None:
            _body["deliveryTimeType"] = delivery_time_type
        if items is not None:
            _body["items"] = items
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.post(
            f"{_PREFIX}/ShipmentTemplate",
            json=_body,
        )
        response.raise_for_status()
        return ShipmentTemplateModel.model_validate(response.json())

    async def get_shipment_from_template(
        self,
        shipment_template_id: UUID,
        start_date: str | None = None,
    ) -> ShipmentModel:
        """Generates a shipment preview from a template and start date without persisting it."""
        _params: dict[str, object] = {}
        if start_date is not None:
            _params["startDate"] = start_date
        response = await self._http.get(
            f"{_PREFIX}/ShipmentTemplate/shipment-from-template/{shipment_template_id}",
            params=_params,
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def create_shipment_from_template(
        self,
        shipment_template_id: UUID,
        data: list[ShipmentFromTemplateData],
    ) -> None:
        """Creates and persists shipments from a shipment template request."""
        response = await self._http.post(
            f"{_PREFIX}/ShipmentTemplate/create-shipment-from-template",
            json={"shipmentTemplateId": str(shipment_template_id), "data": data},
        )
        response.raise_for_status()

    async def create_from_shipment(
        self,
        shipment_id: UUID,
    ) -> ShipmentTemplateModel:
        """Creates a shipment template from a single template-flagged shipment and deletes the source shipment."""
        response = await self._http.post(
            f"{_PREFIX}/ShipmentTemplate/create-from-shipment/{shipment_id}",
        )
        response.raise_for_status()
        return ShipmentTemplateModel.model_validate(response.json())

    async def create_from_all_shipments(
        self,
    ) -> None:
        """Creates shipment templates from all template-flagged shipments and deletes the source shipments."""
        response = await self._http.post(
            f"{_PREFIX}/ShipmentTemplate/create-from-all-shipments",
        )
        response.raise_for_status()

    async def create_shipping_unit(
        self,
        number: str | None = None,
        sscc: str | None = None,
        type: str | None = None,
        loading_aid_type_id: UUID | None = None,
        loading_aid_quantity: int | None = None,
        actual_loading_aid_type_id: UUID | None = None,
        actual_loading_aid_quantity: int | None = None,
        status_id: UUID | None = None,
        weight: QuantityRequest | None = None,
        width: float | None = None,
        height: float | None = None,
        length: float | None = None,
        actual_weight: QuantityRequest | None = None,
        actual_width: float | None = None,
        actual_height: float | None = None,
        actual_length: float | None = None,
        shipment_number: str | None = None,
        primary_shipment_id: UUID | None = None,
        tags: list[UUID] | None = None,
        addon: dict[str, object] | None = None,
    ) -> ShippingUnitModel:
        """Creates a new shippingUnit."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if sscc is not None:
            _body["sscc"] = sscc
        if type is not None:
            _body["type"] = type
        if loading_aid_type_id is not None:
            _body["loadingAidTypeId"] = str(loading_aid_type_id)
        if loading_aid_quantity is not None:
            _body["loadingAidQuantity"] = loading_aid_quantity
        if actual_loading_aid_type_id is not None:
            _body["actualLoadingAidTypeId"] = str(actual_loading_aid_type_id)
        if actual_loading_aid_quantity is not None:
            _body["actualLoadingAidQuantity"] = actual_loading_aid_quantity
        if status_id is not None:
            _body["statusId"] = str(status_id)
        if weight is not None:
            _body["weight"] = weight
        if width is not None:
            _body["width"] = width
        if height is not None:
            _body["height"] = height
        if length is not None:
            _body["length"] = length
        if actual_weight is not None:
            _body["actualWeight"] = actual_weight
        if actual_width is not None:
            _body["actualWidth"] = actual_width
        if actual_height is not None:
            _body["actualHeight"] = actual_height
        if actual_length is not None:
            _body["actualLength"] = actual_length
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if primary_shipment_id is not None:
            _body["primaryShipmentId"] = str(primary_shipment_id)
        if tags is not None:
            _body["tags"] = str(tags)
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnit",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitModel.model_validate(response.json())

    async def get_shipping_unit_by_id(
        self,
        id: UUID,
    ) -> ShippingUnitModel:
        """Retrieves the shippingUnit with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShippingUnit/{id}",
        )
        response.raise_for_status()
        return ShippingUnitModel.model_validate(response.json())

    async def update_shipping_unit_by_id(
        self,
        id: UUID,
        number: str | None = None,
        sscc: str | None = None,
        type: str | None = None,
        loading_aid_type_id: UUID | None = None,
        loading_aid_quantity: int | None = None,
        actual_loading_aid_type_id: UUID | None = None,
        actual_loading_aid_quantity: int | None = None,
        weight: QuantityPatchRequest | None = None,
        width: float | None = None,
        height: float | None = None,
        length: float | None = None,
        actual_weight: QuantityPatchRequest | None = None,
        actual_width: float | None = None,
        actual_height: float | None = None,
        actual_length: float | None = None,
        status_id: UUID | None = None,
        shipment_number: str | None = None,
        primary_shipment_id: UUID | None = None,
        tags: list[UUID] | None = None,
        addon: dict[str, object] | None = None,
    ) -> ShippingUnitModel:
        """Updates/saves the given shippingUnit."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if sscc is not None:
            _body["sscc"] = sscc
        if type is not None:
            _body["type"] = type
        if loading_aid_type_id is not None:
            _body["loadingAidTypeId"] = str(loading_aid_type_id)
        if loading_aid_quantity is not None:
            _body["loadingAidQuantity"] = loading_aid_quantity
        if actual_loading_aid_type_id is not None:
            _body["actualLoadingAidTypeId"] = str(actual_loading_aid_type_id)
        if actual_loading_aid_quantity is not None:
            _body["actualLoadingAidQuantity"] = actual_loading_aid_quantity
        if weight is not None:
            _body["weight"] = weight
        if width is not None:
            _body["width"] = width
        if height is not None:
            _body["height"] = height
        if length is not None:
            _body["length"] = length
        if actual_weight is not None:
            _body["actualWeight"] = actual_weight
        if actual_width is not None:
            _body["actualWidth"] = actual_width
        if actual_height is not None:
            _body["actualHeight"] = actual_height
        if actual_length is not None:
            _body["actualLength"] = actual_length
        if status_id is not None:
            _body["statusId"] = str(status_id)
        if shipment_number is not None:
            _body["shipmentNumber"] = shipment_number
        if primary_shipment_id is not None:
            _body["primaryShipmentId"] = str(primary_shipment_id)
        if tags is not None:
            _body["tags"] = str(tags)
        if addon is not None:
            _body["addon"] = addon
        response = await self._http.patch(
            f"{_PREFIX}/ShippingUnit/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitModel.model_validate(response.json())

    async def delete_shipping_unit_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes the shippingUnit with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShippingUnit/{id}",
        )
        response.raise_for_status()

    async def shipping_unit_tag(
        self,
        id: UUID,
        tag_id: UUID | None = None,
    ) -> ShippingUnitModel:
        """Adds a tag to the shipping unit with the given id."""
        _body: dict[str, object] = {
        }
        if tag_id is not None:
            _body["tagId"] = str(tag_id)
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnit/{id}/tag",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitModel.model_validate(response.json())

    async def shipping_unit_tag_1(
        self,
        id: UUID,
        tag_id: UUID,
    ) -> ShippingUnitModel:
        """Removes a tag from the shipping unit with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShippingUnit/{id}/tag/{tag_id}",
        )
        response.raise_for_status()
        return ShippingUnitModel.model_validate(response.json())

    async def shipping_unit_create_shipment(
        self,
        id: UUID,
    ) -> ShipmentModel:
        """Creates a new shipment for the given shipping unit, or attaches the shipping unit to an existing dispatchable shipment."""
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnit/create-shipment/{id}",
        )
        response.raise_for_status()
        return ShipmentModel.model_validate(response.json())

    async def create_shipping_unit_status(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitStatusModel:
        """Creates a new shippingUnit status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnitStatus",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitStatusModel.model_validate(response.json())

    async def get_shipping_unit_status_by_id(
        self,
        id: UUID,
    ) -> ShippingUnitStatusModel:
        """Retrieves the shippingUnit status with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShippingUnitStatus/{id}",
        )
        response.raise_for_status()
        return ShippingUnitStatusModel.model_validate(response.json())

    async def update_shipping_unit_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitStatusModel:
        """Updates/saves the given shippingUnit status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShippingUnitStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitStatusModel.model_validate(response.json())

    async def delete_shipping_unit_status_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        """Deletes the shippingUnit status with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShippingUnitStatus/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_shipping_unit_status_deployment(
        self,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnitStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitStatusModel.model_validate(response.json())

    async def update_shipping_unit_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        display_name: str | None = None,
        display_key: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if display_name is not None:
            _body["displayName"] = display_name
        if display_key is not None:
            _body["displayKey"] = display_key
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShippingUnitStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitStatusModel.model_validate(response.json())

    async def get_shipping_unit_tag_by_id(
        self,
        id: UUID,
    ) -> ShippingUnitTagModel:
        """Retrieves the shipping unit tag with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/ShippingUnitTag/{id}",
        )
        response.raise_for_status()
        return ShippingUnitTagModel.model_validate(response.json())

    async def update_shipping_unit_tag_by_id(
        self,
        id: UUID,
        name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitTagModel:
        """Updates the shipping unit tag with the given id."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.patch(
            f"{_PREFIX}/ShippingUnitTag/{id}",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitTagModel.model_validate(response.json())

    async def delete_shipping_unit_tag_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes the shipping unit tag with the given id."""
        response = await self._http.delete(
            f"{_PREFIX}/ShippingUnitTag/{id}",
        )
        response.raise_for_status()

    async def create_shipping_unit_tag(
        self,
        name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
    ) -> ShippingUnitTagModel:
        """Creates a new shipping unit tag."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        response = await self._http.post(
            f"{_PREFIX}/ShippingUnitTag",
            json=_body,
        )
        response.raise_for_status()
        return ShippingUnitTagModel.model_validate(response.json())

    async def get_tour_by_id(
        self,
        id: UUID,
    ) -> TourModel:
        """Retrieves the tour with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/Tour/{id}",
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def update_tour_by_id(
        self,
        id: UUID,
        number: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        actual_start_date_time: str | None = None,
        actual_end_date_time: str | None = None,
        calculated_start_date_time: str | None = None,
        calculated_end_date_time: str | None = None,
        financial_partner_personal_account_id: UUID | None = None,
        financial_partner_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[PatchTourActionRequest] | None = None,
        billing_lines: list[PatchBillingLineRequest] | None = None,
        auto_adjust_actions_mode: str | None = None,
    ) -> TourModel:
        """Patches a tour object."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if actual_start_date_time is not None:
            _body["actualStartDateTime"] = actual_start_date_time
        if actual_end_date_time is not None:
            _body["actualEndDateTime"] = actual_end_date_time
        if calculated_start_date_time is not None:
            _body["calculatedStartDateTime"] = calculated_start_date_time
        if calculated_end_date_time is not None:
            _body["calculatedEndDateTime"] = calculated_end_date_time
        if financial_partner_personal_account_id is not None:
            _body["financialPartnerPersonalAccountId"] = str(financial_partner_personal_account_id)
        if financial_partner_address_id is not None:
            _body["financialPartnerAddressId"] = str(financial_partner_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        if auto_adjust_actions_mode is not None:
            _body["autoAdjustActionsMode"] = auto_adjust_actions_mode
        response = await self._http.patch(
            f"{_PREFIX}/Tour/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def delete_tour_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        """Deletes the given tour."""
        response = await self._http.delete(
            f"{_PREFIX}/Tour/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def get_all_by_dates(
        self,
        start: str | None = None,
        end: str | None = None,
    ) -> None:
        """Retrieves all tours between two dates."""
        _params: dict[str, object] = {}
        if start is not None:
            _params["start"] = start
        if end is not None:
            _params["end"] = end
        response = await self._http.get(
            f"{_PREFIX}/Tour/get-all-by-dates",
            params=_params,
        )
        response.raise_for_status()

    async def create_tour(
        self,
        number: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        actual_start_date_time: str | None = None,
        actual_end_date_time: str | None = None,
        calculated_start_date_time: str | None = None,
        calculated_end_date_time: str | None = None,
        financial_partner_personal_account_id: UUID | None = None,
        financial_partner_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[CreateTourActionRequest] | None = None,
        billing_lines: list[CreateBillingLineRequest] | None = None,
    ) -> TourModel:
        """Creates a new tour object."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if actual_start_date_time is not None:
            _body["actualStartDateTime"] = actual_start_date_time
        if actual_end_date_time is not None:
            _body["actualEndDateTime"] = actual_end_date_time
        if calculated_start_date_time is not None:
            _body["calculatedStartDateTime"] = calculated_start_date_time
        if calculated_end_date_time is not None:
            _body["calculatedEndDateTime"] = calculated_end_date_time
        if financial_partner_personal_account_id is not None:
            _body["financialPartnerPersonalAccountId"] = str(financial_partner_personal_account_id)
        if financial_partner_address_id is not None:
            _body["financialPartnerAddressId"] = str(financial_partner_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.post(
            f"{_PREFIX}/Tour",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def manipulate(
        self,
        tour_id: UUID | None = None,
        new_start_date: str | None = None,
        new_end_date: str | None = None,
        new_resource_id: UUID | None = None,
    ) -> TourManipulateResponse:
        """Updates/saves the given tour."""
        _body: dict[str, object] = {
        }
        if tour_id is not None:
            _body["tourId"] = str(tour_id)
        if new_start_date is not None:
            _body["newStartDate"] = new_start_date
        if new_end_date is not None:
            _body["newEndDate"] = new_end_date
        if new_resource_id is not None:
            _body["newResourceId"] = str(new_resource_id)
        response = await self._http.post(
            f"{_PREFIX}/Tour/manipulate",
            json=_body,
        )
        response.raise_for_status()
        return TourManipulateResponse.model_validate(response.json())

    async def convert_shipment_to_tour(
        self,
        shipment_id: UUID,
        resource_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        auto_assign_resource_modes: list[str] | None = None,
        action_optimization_mode: str | None = None,
        persist: bool | None = None,
    ) -> TourModel:
        """Converts a single shipment into a tour.
Creates a new tour containing the specified shipment with automatically generated load and unload actions.
The tour will include all necessary actions to complete the shipment's transportation."""
        _body: dict[str, object] = {
            "shipmentId": str(shipment_id),
        }
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if auto_assign_resource_modes is not None:
            _body["autoAssignResourceModes"] = auto_assign_resource_modes
        if action_optimization_mode is not None:
            _body["actionOptimizationMode"] = action_optimization_mode
        if persist is not None:
            _body["persist"] = persist
        response = await self._http.post(
            f"{_PREFIX}/Tour/convert-shipment-to-tour",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def convert_shipments_to_tour(
        self,
        shipment_ids: list[UUID] | None = None,
        resource_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        auto_assign_resource_modes: list[str] | None = None,
        action_optimization_mode: str | None = None,
        persist: bool | None = None,
    ) -> TourModel:
        """Creates a single combined tour from multiple shipments.
All specified shipments will be included in one tour, with their load and unload actions
automatically sequenced and optimized according to the specified optimization mode.
This is useful for consolidating multiple shipments into an efficient single tour route."""
        _body: dict[str, object] = {
        }
        if shipment_ids is not None:
            _body["shipmentIds"] = str(shipment_ids)
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if auto_assign_resource_modes is not None:
            _body["autoAssignResourceModes"] = auto_assign_resource_modes
        if action_optimization_mode is not None:
            _body["actionOptimizationMode"] = action_optimization_mode
        if persist is not None:
            _body["persist"] = persist
        response = await self._http.post(
            f"{_PREFIX}/Tour/convert-shipments-to-tour",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def convert_shipments_to_tours(
        self,
        shipment_ids: list[UUID] | None = None,
        resource_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        auto_assign_resource_modes: list[str] | None = None,
        action_optimization_mode: str | None = None,
        tour_combination_mode: str | None = None,
        delay_between_tours_minutes: int | None = None,
        persist: bool | None = None,
    ) -> None:
        """Creates multiple separate tours from a list of shipments.
Each shipment will be converted into its own individual tour. Tours are automatically
scheduled in sequence, with each subsequent tour's start time calculated based on the previous
tour's end location, travel time to the next shipment's location, and the configured delay.
This is useful for creating a series of single-shipment tours for the same resource."""
        _body: dict[str, object] = {
        }
        if shipment_ids is not None:
            _body["shipmentIds"] = str(shipment_ids)
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if auto_assign_resource_modes is not None:
            _body["autoAssignResourceModes"] = auto_assign_resource_modes
        if action_optimization_mode is not None:
            _body["actionOptimizationMode"] = action_optimization_mode
        if tour_combination_mode is not None:
            _body["tourCombinationMode"] = tour_combination_mode
        if delay_between_tours_minutes is not None:
            _body["delayBetweenToursMinutes"] = delay_between_tours_minutes
        if persist is not None:
            _body["persist"] = persist
        response = await self._http.post(
            f"{_PREFIX}/Tour/convert-shipments-to-tours",
            json=_body,
        )
        response.raise_for_status()

    async def add_tag_to_tour(
        self,
        tour_id: UUID | None = None,
        tag_id: UUID | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if tour_id is not None:
            _body["tourId"] = str(tour_id)
        if tag_id is not None:
            _body["tagId"] = str(tag_id)
        response = await self._http.put(
            f"{_PREFIX}/Tour/add-tag-to-tour",
            json=_body,
        )
        response.raise_for_status()

    async def remove_tag_from_tour(
        self,
        tour_id: UUID | None = None,
        tag_id: UUID | None = None,
    ) -> None:
        _body: dict[str, object] = {
        }
        if tour_id is not None:
            _body["tourId"] = str(tour_id)
        if tag_id is not None:
            _body["tagId"] = str(tag_id)
        response = await self._http.put(
            f"{_PREFIX}/Tour/remove-tag-from-tour",
            json=_body,
        )
        response.raise_for_status()

    async def set_tour_actual_times(
        self,
        tour_id: UUID | None = None,
        actual_start: str | None = None,
        actual_end: str | None = None,
        new_status_id: UUID | None = None,
    ) -> None:
        """Sets the actual times of a tour. Also gives the option to change the tour status, e.g to started."""
        _body: dict[str, object] = {
        }
        if tour_id is not None:
            _body["tourId"] = str(tour_id)
        if actual_start is not None:
            _body["actualStart"] = actual_start
        if actual_end is not None:
            _body["actualEnd"] = actual_end
        if new_status_id is not None:
            _body["newStatusId"] = str(new_status_id)
        response = await self._http.put(
            f"{_PREFIX}/Tour/set-tour-actual-times",
            json=_body,
        )
        response.raise_for_status()

    async def get_by_global_tour_id(
        self,
        id: UUID | None = None,
    ) -> None:
        """Retrieves all tours with the given global tour id."""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/Tour/get-by-global-tour-id",
            params=_params,
        )
        response.raise_for_status()

    async def get_by_shipment_id(
        self,
        id: UUID | None = None,
    ) -> None:
        """Retrieves all tours that contains actions with the given shipment id."""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/Tour/get-by-shipment-id",
            params=_params,
        )
        response.raise_for_status()

    async def get_aggregated_loading_slots(
        self,
        resource_id: UUID | None = None,
        loading_slot_names: str | None = None,
        count: int | None = None,
    ) -> None:
        """Get all used loading slots for a specific resource"""
        _params: dict[str, object] = {}
        if resource_id is not None:
            _params["resourceId"] = str(resource_id)
        if loading_slot_names is not None:
            _params["loadingSlotNames"] = loading_slot_names
        if count is not None:
            _params["count"] = count
        response = await self._http.get(
            f"{_PREFIX}/Tour/get-aggregated-loading-slots",
            params=_params,
        )
        response.raise_for_status()

    async def send_to_telematic(
        self,
        tour_id: UUID | None = None,
    ) -> None:
        _params: dict[str, object] = {}
        if tour_id is not None:
            _params["tourId"] = str(tour_id)
        response = await self._http.put(
            f"{_PREFIX}/Tour/send-to-telematic",
            params=_params,
        )
        response.raise_for_status()

    async def tour_set_status(
        self,
        tour_id: UUID,
        status_id: UUID,
    ) -> None:
        response = await self._http.put(
            f"{_PREFIX}/Tour/set-status",
            json={"tourId": str(tour_id), "statusId": str(status_id)},
        )
        response.raise_for_status()

    async def tour_calculate_preview(
        self,
        number: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: str | None = None,
        end_date_time: str | None = None,
        actual_start_date_time: str | None = None,
        actual_end_date_time: str | None = None,
        calculated_start_date_time: str | None = None,
        calculated_end_date_time: str | None = None,
        financial_partner_personal_account_id: UUID | None = None,
        financial_partner_address_id: UUID | None = None,
        carrier_personal_account_id: UUID | None = None,
        carrier_address_id: UUID | None = None,
        tariff: TariffModel | None = None,
        carrier_tariff: TariffModel | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[CreateTourActionRequest] | None = None,
        billing_lines: list[CreateBillingLineRequest] | None = None,
    ) -> TourModel:
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if actual_start_date_time is not None:
            _body["actualStartDateTime"] = actual_start_date_time
        if actual_end_date_time is not None:
            _body["actualEndDateTime"] = actual_end_date_time
        if calculated_start_date_time is not None:
            _body["calculatedStartDateTime"] = calculated_start_date_time
        if calculated_end_date_time is not None:
            _body["calculatedEndDateTime"] = calculated_end_date_time
        if financial_partner_personal_account_id is not None:
            _body["financialPartnerPersonalAccountId"] = str(financial_partner_personal_account_id)
        if financial_partner_address_id is not None:
            _body["financialPartnerAddressId"] = str(financial_partner_address_id)
        if carrier_personal_account_id is not None:
            _body["carrierPersonalAccountId"] = str(carrier_personal_account_id)
        if carrier_address_id is not None:
            _body["carrierAddressId"] = str(carrier_address_id)
        if tariff is not None:
            _body["tariff"] = tariff
        if carrier_tariff is not None:
            _body["carrierTariff"] = carrier_tariff
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.post(
            f"{_PREFIX}/Tour/calculate-preview",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def get_main_tour(
        self,
        global_tour_id: UUID,
    ) -> TourModel:
        """Retrieves the main tour by the global tour id."""
        response = await self._http.get(
            f"{_PREFIX}/Tour/{global_tour_id}/main-tour",
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def optimize(
        self,
        parameters: list[str] | None = None,
        tour: CreateTourRequest | None = None,
    ) -> CalculateRouteResponse:
        _body: dict[str, object] = {
        }
        if parameters is not None:
            _body["parameters"] = parameters
        if tour is not None:
            _body["tour"] = tour
        response = await self._http.post(
            f"{_PREFIX}/Tour/optimize",
            json=_body,
        )
        response.raise_for_status()
        return CalculateRouteResponse.model_validate(response.json())

    async def tour_execute_pricing(
        self,
        id: UUID,
    ) -> None:
        """Remove old tariff billing lines (inidicated with a reference of type BillingLineReference.Types.Tariff),
execute the carrier and customer tariffs (if present) and create new billing lines."""
        response = await self._http.post(
            f"{_PREFIX}/Tour/{id}/execute-pricing",
        )
        response.raise_for_status()

    async def calculate_routes(
        self,
        metrics: list[str] | None = None,
        tour: CalculateTourModel | None = None,
    ) -> CalculateRouteResponse:
        _body: dict[str, object] = {
        }
        if metrics is not None:
            _body["metrics"] = metrics
        if tour is not None:
            _body["tour"] = tour
        response = await self._http.post(
            f"{_PREFIX}/TourCalculation/calculate-routes",
            json=_body,
        )
        response.raise_for_status()
        return CalculateRouteResponse.model_validate(response.json())

    async def create_tour_status(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> TourStatusModel:
        """Creates a new tour status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.post(
            f"{_PREFIX}/TourStatus",
            json=_body,
        )
        response.raise_for_status()
        return TourStatusModel.model_validate(response.json())

    async def get_tour_status_by_id(
        self,
        id: UUID,
    ) -> TourStatusModel:
        """Retrives the tour status with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/TourStatus/{id}",
        )
        response.raise_for_status()
        return TourStatusModel.model_validate(response.json())

    async def update_tour_status_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> TourStatusModel:
        """Updates/saves the given tour status."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.patch(
            f"{_PREFIX}/TourStatus/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TourStatusModel.model_validate(response.json())

    async def tour_status_get_all(
        self,
    ) -> None:
        """Retrieves all tour status."""
        response = await self._http.get(
            f"{_PREFIX}/TourStatus/get-all",
        )
        response.raise_for_status()

    async def create_tour_status_deployment(
        self,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> TourStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.post(
            f"{_PREFIX}/TourStatusDeployment",
            json=_body,
        )
        response.raise_for_status()
        return TourStatusModel.model_validate(response.json())

    async def update_tour_status_deployment_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: str | None = None,
        roles: list[str] | None = None,
        hex_color: str | None = None,
        order_nr: int | None = None,
        resolver: str | None = None,
    ) -> TourStatusModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if roles is not None:
            _body["roles"] = roles
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if order_nr is not None:
            _body["orderNr"] = order_nr
        if resolver is not None:
            _body["resolver"] = resolver
        response = await self._http.patch(
            f"{_PREFIX}/TourStatusDeployment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TourStatusModel.model_validate(response.json())

    async def get_tour_tag_by_id(
        self,
        id: UUID,
    ) -> TourTagModel:
        """Retrives the tour tag with the given id."""
        response = await self._http.get(
            f"{_PREFIX}/TourTag/{id}",
        )
        response.raise_for_status()
        return TourTagModel.model_validate(response.json())

    async def update_tour_tag_by_id(
        self,
        id: UUID,
        name: str | None = None,
        internal_name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
        functions: list[str] | None = None,
    ) -> TourTagModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if internal_name is not None:
            _body["internalName"] = internal_name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if functions is not None:
            _body["functions"] = functions
        response = await self._http.patch(
            f"{_PREFIX}/TourTag/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TourTagModel.model_validate(response.json())

    async def delete_tour_tag_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/TourTag/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def get_tour_tag(
        self,
    ) -> None:
        """Retrives all tour tags."""
        response = await self._http.get(
            f"{_PREFIX}/TourTag",
        )
        response.raise_for_status()

    async def create_tour_tag(
        self,
        name: str | None = None,
        internal_name: str | None = None,
        group_name: str | None = None,
        hex_color: str | None = None,
        functions: list[str] | None = None,
    ) -> TourTagModel:
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if internal_name is not None:
            _body["internalName"] = internal_name
        if group_name is not None:
            _body["groupName"] = group_name
        if hex_color is not None:
            _body["hexColor"] = hex_color
        if functions is not None:
            _body["functions"] = functions
        response = await self._http.post(
            f"{_PREFIX}/TourTag",
            json=_body,
        )
        response.raise_for_status()
        return TourTagModel.model_validate(response.json())

    async def get_tour_template_by_id(
        self,
        id: UUID,
    ) -> TourTemplateResponse:
        response = await self._http.get(
            f"{_PREFIX}/TourTemplate/{id}",
        )
        response.raise_for_status()
        return TourTemplateResponse.model_validate(response.json())

    async def update_tour_template_by_id(
        self,
        id: UUID,
        number: str | None = None,
        template_name: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: TemplateTimeModel | None = None,
        end_date_time: TemplateTimeModel | None = None,
        time_mode: TemplateTimeMode | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[PatchTourTemplateActionRequest] | None = None,
    ) -> TourTemplateResponse:
        """Patches a tour object."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if template_name is not None:
            _body["templateName"] = template_name
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if time_mode is not None:
            _body["timeMode"] = time_mode
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        response = await self._http.patch(
            f"{_PREFIX}/TourTemplate/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TourTemplateResponse.model_validate(response.json())

    async def delete_tour_template_by_id(
        self,
        id: UUID,
    ) -> IActionResult:
        response = await self._http.delete(
            f"{_PREFIX}/TourTemplate/{id}",
        )
        response.raise_for_status()
        return IActionResult.model_validate(response.json())

    async def create_tour_template(
        self,
        number: str | None = None,
        template_name: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: TemplateTimeModel | None = None,
        end_date_time: TemplateTimeModel | None = None,
        time_mode: TemplateTimeMode | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[CreateTourTemplateActionRequest] | None = None,
    ) -> TourTemplateResponse:
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if template_name is not None:
            _body["templateName"] = template_name
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if time_mode is not None:
            _body["timeMode"] = time_mode
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        response = await self._http.post(
            f"{_PREFIX}/TourTemplate",
            json=_body,
        )
        response.raise_for_status()
        return TourTemplateResponse.model_validate(response.json())

    async def tour_template_calculate_preview(
        self,
        number: str | None = None,
        template_name: str | None = None,
        reference: str | None = None,
        resource_id: UUID | None = None,
        start_address_id: UUID | None = None,
        end_address_id: UUID | None = None,
        start_date_time: TemplateTimeModel | None = None,
        end_date_time: TemplateTimeModel | None = None,
        time_mode: TemplateTimeMode | None = None,
        notes: str | None = None,
        tags: list[UUID] | None = None,
        actions: list[CreateTourTemplateActionRequest] | None = None,
    ) -> TourModel:
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if template_name is not None:
            _body["templateName"] = template_name
        if reference is not None:
            _body["reference"] = reference
        if resource_id is not None:
            _body["resourceId"] = str(resource_id)
        if start_address_id is not None:
            _body["startAddressId"] = str(start_address_id)
        if end_address_id is not None:
            _body["endAddressId"] = str(end_address_id)
        if start_date_time is not None:
            _body["startDateTime"] = start_date_time
        if end_date_time is not None:
            _body["endDateTime"] = end_date_time
        if time_mode is not None:
            _body["timeMode"] = time_mode
        if notes is not None:
            _body["notes"] = notes
        if tags is not None:
            _body["tags"] = str(tags)
        if actions is not None:
            _body["actions"] = actions
        response = await self._http.post(
            f"{_PREFIX}/TourTemplate/calculate-preview",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def tour_from_template(
        self,
        tour_template_id: UUID,
        start_date: str | None = None,
    ) -> TourModel:
        _body: dict[str, object] = {
            "tourTemplateId": str(tour_template_id),
        }
        if start_date is not None:
            _body["startDate"] = start_date
        response = await self._http.post(
            f"{_PREFIX}/TourTemplate/tour-from-template",
            json=_body,
        )
        response.raise_for_status()
        return TourModel.model_validate(response.json())

    async def create_tour_from_template(
        self,
        tour_template_id: UUID,
        data: list[TourFromTemplateData],
    ) -> None:
        """Creates and persists tours from a tour template request."""
        response = await self._http.post(
            f"{_PREFIX}/TourTemplate/create-tour-from-template",
            json={"tourTemplateId": str(tour_template_id), "data": data},
        )
        response.raise_for_status()
