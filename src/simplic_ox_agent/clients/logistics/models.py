"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

class AddBillingLinesToTransactionMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class AddBillingLinesToTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_lines: list[AddToTransactionBillingLineReferenceRequest] | None = Field(None, alias="billingLines")
    transaction_id: UUID | None = Field(None, alias="transactionId")
    mode: AddBillingLinesToTransactionMode | None = None

class AddBillingLinesToTransactionResponse(BaseModel):
    success: bool | None = None
    errors: list[LocalizableErrorResponse] | None = None

class AddTagToShippingUnitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tag_id: UUID | None = Field(None, alias="tagId")

class AddTagToTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    tag_id: UUID | None = Field(None, alias="tagId")

class AddToTransactionBillingLineReferenceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID | None = Field(None, alias="shipmentId")
    tour_id: UUID | None = Field(None, alias="tourId")
    billing_line_id: UUID | None = Field(None, alias="billingLineId")

class AddonFieldResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class Address(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_id: UUID | None = Field(None, alias="contactId")
    company_name: str | None = Field(None, alias="companyName")
    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    additional01: str | None = None
    additional02: str | None = None
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    match_code: str | None = Field(None, alias="matchCode")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    organization_id: UUID | None = Field(None, alias="organizationId")

class AddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_id: UUID | None = Field(None, alias="contactId")
    company_name: str | None = Field(None, alias="companyName")
    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    additional01: str | None = None
    additional02: str | None = None
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    match_code: str | None = Field(None, alias="matchCode")

class AggregationExpression(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    function: str | None = None
    argument: QueryExpression | None = None
    is_count: bool | None = Field(None, alias="isCount")

class AppointmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    resources: list[ResourceModel] | None = None
    functions: list[str] | None = None
    title: str | None = None
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    hex_color: str | None = Field(None, alias="hexColor")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    organization_id: UUID | None = Field(None, alias="organizationId")

class AttachCoDriverRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resource_id: UUID = Field(alias="composedResourceId")
    driver_resource_id: UUID = Field(alias="driverResourceId")
    move_current_to_main_driver_seat: bool | None = Field(None, alias="moveCurrentToMainDriverSeat")

class AttachMainDriverRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resource_id: UUID = Field(alias="composedResourceId")
    driver_resource_id: UUID = Field(alias="driverResourceId")
    move_current_to_co_driver_seat: bool | None = Field(None, alias="moveCurrentToCoDriverSeat")

class AttachResourceRequestSettings(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    attach_driver_as_co_driver: bool | None = Field(None, alias="attachDriverAsCoDriver")
    move_current_driver_to_co_driver: bool | None = Field(None, alias="moveCurrentDriverToCoDriver")
    move_co_driver_to_main_driver: bool | None = Field(None, alias="moveCoDriverToMainDriver")
    add_trailer_as_additional_trailer: bool | None = Field(None, alias="addTrailerAsAdditionalTrailer")

class AttachResourcesRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_resource_id: UUID = Field(alias="firstResourceId")
    second_resource_id: UUID = Field(alias="secondResourceId")
    settings: AttachResourceRequestSettings | None = None

class AttachTractorUnitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resource_id: UUID = Field(alias="composedResourceId")
    tractor_unit_resource_id: UUID = Field(alias="tractorUnitResourceId")

class AttachTrailerRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resource_id: UUID = Field(alias="composedResourceId")
    tractor_unit_resource_id: UUID = Field(alias="tractorUnitResourceId")
    attach_as_additional_trailer: bool | None = Field(None, alias="attachAsAdditionalTrailer")

class AttachedEntityModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    entitiy: TourEntityModel | None = None
    attaching_action: TourActionModel | None = Field(None, alias="attachingAction")
    detaching_action: TourActionModel | None = Field(None, alias="detachingAction")

class AttachedResourceModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    resource: ResourceModel | None = None
    attach_action: TourActionModel | None = Field(None, alias="attachAction")
    detach_action: TourActionModel | None = Field(None, alias="detachAction")

class AutoPlanResourceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    resource_id: UUID = Field(alias="resourceId")
    max_weight: float | None = Field(None, alias="maxWeight")
    max_loading_meters: float | None = Field(None, alias="maxLoadingMeters")
    max_traveling_time: str | None = Field(None, alias="maxTravelingTime")
    earliest_start: datetime | None = Field(None, alias="earliestStart")
    latest_end: datetime | None = Field(None, alias="latestEnd")
    start_latitude: float | None = Field(None, alias="startLatitude")
    start_longitude: float | None = Field(None, alias="startLongitude")
    end_latitude: float | None = Field(None, alias="endLatitude")
    end_longitude: float | None = Field(None, alias="endLongitude")

class AutoPlanShipmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID = Field(alias="shipmentId")
    load_duration: str | None = Field(None, alias="loadDuration")
    unload_duration: str | None = Field(None, alias="unloadDuration")

class AutoPlanToursRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipments: list[AutoPlanShipmentRequest]
    resources: list[AutoPlanResourceRequest]
    optimization_mode: str = Field(alias="optimizationMode")

class AutoPlanToursResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    planned_tours: list[PlannedTourResult] | None = Field(None, alias="plannedTours")
    unassigned_shipment_ids: list[UUID] | None = Field(None, alias="unassignedShipmentIds")

class BillableContactModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address: AddressModel | None = None
    account_number: str | None = Field(None, alias="accountNumber")
    personal_account_id: UUID | None = Field(None, alias="personalAccountId")

class BillingLineAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    name: str | None = None
    street: str | None = None
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None

class BillingLineContactModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    account_number: str | None = Field(None, alias="accountNumber")
    company_name: str | None = Field(None, alias="companyName")
    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    address: BillingLineAddressModel | None = None

class BillingLineContactRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    personal_account_id: UUID | None = Field(None, alias="personalAccountId")

class BillingLineCostCenterAssignmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cost_center: BillingLineCostCenterModel | None = Field(None, alias="costCenter")
    percentage: float | None = None

class BillingLineCostCenterAssignmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cost_center_id: UUID | None = Field(None, alias="costCenterId")
    percentage: float | None = None
    _remove: bool | None = None

class BillingLineCostCenterModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: int | None = None
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")

class BillingLineGeneralLedgerAccountGroupModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    number: str | None = None

class BillingLineModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    financial_partner: BillingLineContactModel | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    type: BillingLineType | None = None
    status: BillingLineStatusModel | None = None
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    cost_centers: list[BillingLineCostCenterAssignmentModel] | None = Field(None, alias="costCenters")
    cost_objects: list[BillingLineCostCenterAssignmentModel] | None = Field(None, alias="costObjects")
    tax_rate: BillingLineTaxRateModel | None = Field(None, alias="taxRate")
    general_ledger_account_group: BillingLineGeneralLedgerAccountGroupModel | None = Field(None, alias="generalLedgerAccountGroup")
    quantity: QuantityModel | None = None
    reference: str | None = None
    references: list[BillingLineReferenceModel] | None = None
    text: str | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    addon: dict[str, object] | None = None
    assigned_transaction_id: UUID | None = Field(None, alias="assignedTransactionId")

class BillingLineReferenceModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    data_type: str | None = Field(None, alias="dataType")
    reference_id: str | None = Field(None, alias="referenceId")

class BillingLineReferenceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    data_type: str | None = Field(None, alias="dataType")
    reference_id: str | None = Field(None, alias="referenceId")
    _remove: bool | None = None

class BillingLineStatusModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    type: str | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class BillingLineTaxRateModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    number: int | None = None

class BillingLineType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class BsonBinaryData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    bytes: str | None = None
    sub_type: BsonBinarySubType | None = Field(None, alias="subType")

class BsonBinarySubType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_128 = 128

class BsonDateTime(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    milliseconds_since_epoch: int | None = Field(None, alias="millisecondsSinceEpoch")

class BsonElement(BaseModel):
    name: str | None = None
    value: BsonValue | None = None

class BsonJavaScript(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    code: str | None = None

class BsonJavaScriptWithScope(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    code: str | None = None
    bson_type: BsonType | None = Field(None, alias="bsonType")
    scope: list[BsonElement] | None = None

class BsonMaxKey(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")

class BsonMinKey(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")

class BsonNull(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")

class BsonRegularExpression(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    pattern: str | None = None
    options: str | None = None

class BsonSymbol(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    name: str | None = None

class BsonTimestamp(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    value: int | None = None
    increment: int | None = None
    timestamp: int | None = None

class BsonType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_127 = 127
    VALUE_255 = 255

class BsonUndefined(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")

class BsonValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_boolean: bool | None = Field(None, alias="asBoolean")
    as_bson_array: list[BsonValue] | None = Field(None, alias="asBsonArray")
    as_bson_binary_data: BsonBinaryData | None = Field(None, alias="asBsonBinaryData")
    as_bson_date_time: BsonDateTime | None = Field(None, alias="asBsonDateTime")
    as_bson_document: list[BsonElement] | None = Field(None, alias="asBsonDocument")
    as_bson_java_script: BsonJavaScript | None = Field(None, alias="asBsonJavaScript")
    as_bson_java_script_with_scope: BsonJavaScriptWithScope | None = Field(None, alias="asBsonJavaScriptWithScope")
    as_bson_max_key: BsonMaxKey | None = Field(None, alias="asBsonMaxKey")
    as_bson_min_key: BsonMinKey | None = Field(None, alias="asBsonMinKey")
    as_bson_null: BsonNull | None = Field(None, alias="asBsonNull")
    as_bson_regular_expression: BsonRegularExpression | None = Field(None, alias="asBsonRegularExpression")
    as_bson_symbol: BsonSymbol | None = Field(None, alias="asBsonSymbol")
    as_bson_timestamp: BsonTimestamp | None = Field(None, alias="asBsonTimestamp")
    as_bson_undefined: BsonUndefined | None = Field(None, alias="asBsonUndefined")
    as_bson_value: BsonValue | None = Field(None, alias="asBsonValue")
    as_byte_array: str | None = Field(None, alias="asByteArray")
    as_decimal: float | None = Field(None, alias="asDecimal")
    as_decimal128: Decimal128 | None = Field(None, alias="asDecimal128")
    as_double: float | None = Field(None, alias="asDouble")
    as_guid: UUID | None = Field(None, alias="asGuid")
    as_int32: int | None = Field(None, alias="asInt32")
    as_int64: int | None = Field(None, alias="asInt64")
    as_local_time: datetime | None = Field(None, alias="asLocalTime")
    as_nullable_boolean: bool | None = Field(None, alias="asNullableBoolean")
    as_nullable_decimal: float | None = Field(None, alias="asNullableDecimal")
    as_nullable_decimal128: Decimal128 | None = Field(None, alias="asNullableDecimal128")
    as_nullable_double: float | None = Field(None, alias="asNullableDouble")
    as_nullable_guid: UUID | None = Field(None, alias="asNullableGuid")
    as_nullable_int32: int | None = Field(None, alias="asNullableInt32")
    as_nullable_int64: int | None = Field(None, alias="asNullableInt64")
    as_nullable_local_time: datetime | None = Field(None, alias="asNullableLocalTime")
    as_nullable_object_id: ObjectId | None = Field(None, alias="asNullableObjectId")
    as_nullable_universal_time: datetime | None = Field(None, alias="asNullableUniversalTime")
    as_object_id: ObjectId | None = Field(None, alias="asObjectId")
    as_regex: Regex | None = Field(None, alias="asRegex")
    as_string: str | None = Field(None, alias="asString")
    as_universal_time: datetime | None = Field(None, alias="asUniversalTime")
    bson_type: BsonType | None = Field(None, alias="bsonType")
    is_boolean: bool | None = Field(None, alias="isBoolean")
    is_bson_array: bool | None = Field(None, alias="isBsonArray")
    is_bson_binary_data: bool | None = Field(None, alias="isBsonBinaryData")
    is_bson_date_time: bool | None = Field(None, alias="isBsonDateTime")
    is_bson_document: bool | None = Field(None, alias="isBsonDocument")
    is_bson_java_script: bool | None = Field(None, alias="isBsonJavaScript")
    is_bson_java_script_with_scope: bool | None = Field(None, alias="isBsonJavaScriptWithScope")
    is_bson_max_key: bool | None = Field(None, alias="isBsonMaxKey")
    is_bson_min_key: bool | None = Field(None, alias="isBsonMinKey")
    is_bson_null: bool | None = Field(None, alias="isBsonNull")
    is_bson_regular_expression: bool | None = Field(None, alias="isBsonRegularExpression")
    is_bson_symbol: bool | None = Field(None, alias="isBsonSymbol")
    is_bson_timestamp: bool | None = Field(None, alias="isBsonTimestamp")
    is_bson_undefined: bool | None = Field(None, alias="isBsonUndefined")
    is_decimal128: bool | None = Field(None, alias="isDecimal128")
    is_double: bool | None = Field(None, alias="isDouble")
    is_guid: bool | None = Field(None, alias="isGuid")
    is_int32: bool | None = Field(None, alias="isInt32")
    is_int64: bool | None = Field(None, alias="isInt64")
    is_numeric: bool | None = Field(None, alias="isNumeric")
    is_object_id: bool | None = Field(None, alias="isObjectId")
    is_string: bool | None = Field(None, alias="isString")
    is_valid_date_time: bool | None = Field(None, alias="isValidDateTime")

class CalculateAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_id: UUID | None = Field(None, alias="contactId")
    company_name: str | None = Field(None, alias="companyName")
    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    additional01: str | None = None
    additional02: str | None = None
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None

class CalculateRouteRequest(BaseModel):
    metrics: list[str] | None = None
    tour: CalculateTourModel | None = None

class CalculateRouteResponse(BaseModel):
    transits: list[TransitModel] | None = None

class CalculateTourActionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address: AddressModel | None = None
    id: UUID | None = None
    order_id: int | None = Field(None, alias="orderId")
    date_time: datetime | None = Field(None, alias="dateTime")

class CalculateTourModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    start_address: CalculateAddressModel | None = Field(None, alias="startAddress")
    end_address: CalculateAddressModel | None = Field(None, alias="endAddress")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    actions: list[CalculateTourActionModel] | None = None

class CarrierOrderReportResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    carrier: AddressModel | None = None
    load_address_opening_hours: list[OpeningHoursModel] | None = Field(None, alias="loadAddressOpeningHours")
    delivery_address_opening_hours: list[OpeningHoursModel] | None = Field(None, alias="deliveryAddressOpeningHours")
    tour_start_date_time: datetime | None = Field(None, alias="tourStartDateTime")
    tour_end_date_time: datetime | None = Field(None, alias="tourEndDateTime")
    shipment: ShipmentModel | None = None
    shipment_item: ShipmentItemModel | None = Field(None, alias="shipmentItem")
    total_carrier_price: float | None = Field(None, alias="totalCarrierPrice")
    single_carrier_price: float | None = Field(None, alias="singleCarrierPrice")
    tour: TourModel | None = None
    composed_reference: str | None = Field(None, alias="composedReference")
    profile: UserProfileModel | None = None
    carrier_billing_lines: list[BillingLineModel] | None = Field(None, alias="carrierBillingLines")
    tractor_unit: ResourceModel | None = Field(None, alias="tractorUnit")

class CleaningModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cleaning_station: AddressModel | None = Field(None, alias="cleaningStation")
    customer: BillableContactModel | None = None
    date_time: datetime | None = Field(None, alias="dateTime")
    number: str | None = None

class ComposedResourceSettingsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resources_enabled: bool | None = Field(None, alias="composedResourcesEnabled")

class ConstructionSiteModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    name: str | None = None
    reference_number: str | None = Field(None, alias="referenceNumber")
    start_date: datetime | None = Field(None, alias="startDate")
    end_date: datetime | None = Field(None, alias="endDate")
    address: Address | None = None
    contact_person: Address | None = Field(None, alias="contactPerson")
    construction_site_type: ConstructionSiteTypeModel | None = Field(None, alias="constructionSiteType")
    additional_information: str | None = Field(None, alias="additionalInformation")
    construction_time: str | None = Field(None, alias="constructionTime")

class ConstructionSiteTypeModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    number: str | None = None

class CreateAddonFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class CreateAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str
    start_date_time: datetime = Field(alias="startDateTime")
    end_date_time: datetime = Field(alias="endDateTime")
    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    resources: list[UUID] | None = None
    functions: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class CreateBillingLineRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    financial_partner: BillingLineContactRequest | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    type: BillingLineType | None = None
    status_id: UUID | None = Field(None, alias="statusId")
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    cost_centers: list[BillingLineCostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[BillingLineCostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    general_ledger_account_group_id: UUID | None = Field(None, alias="generalLedgerAccountGroupId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    text: str | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    addon: dict[str, object] | None = None
    quantity: QuantityRequest | None = None

class CreateBillingLineStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    type: str | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class CreateGeofenceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    color: str | None = None
    address_id: UUID | None = Field(None, alias="addressId")
    enable_tracking: bool | None = Field(None, alias="enableTracking")
    on_enter_flow_name: str | None = Field(None, alias="onEnterFlowName")
    on_leave_flow_name: str | None = Field(None, alias="onLeaveFlowName")
    location: list[GeoLocationModel] | None = None

class CreateLoadingAidTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int
    display_name: str | None = Field(None, alias="displayName")
    weight: float | None = None
    short_text: str | None = Field(None, alias="shortText")
    width: int | None = None
    length: int | None = None
    storage_position: float | None = Field(None, alias="storagePosition")

class CreatePlanningRegionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    hex_color: str | None = Field(None, alias="hexColor")
    include: list[RegionModel] | None = None
    exclude: list[RegionModel] | None = None
    functions: list[str] | None = None

class CreateResourceGroupRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    resource_ids: list[UUID] = Field(alias="resourceIds")

class CreateResourceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    match_code: str = Field(alias="matchCode")
    display_name: str | None = Field(None, alias="displayName")
    loading_slots: list[LoadingSlotModel] | None = Field(None, alias="loadingSlots")
    location: ResourceLocationModel | None = None
    is_loadable: bool | None = Field(None, alias="isLoadable")
    planning_order_key: str | None = Field(None, alias="planningOrderKey")
    usable_until: datetime | None = Field(None, alias="usableUntil")
    notes: str | None = None

class CreateShipmentItemRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str | None = None
    loading_meters: float | None = Field(None, alias="loadingMeters")
    reference: str | None = None
    quantity: QuantityRequest | None = None
    weight: QuantityRequest | None = None
    article_id: UUID | None = Field(None, alias="articleId")
    weight_notes: list[CreateWeightNoteRequest] | None = Field(None, alias="weightNotes")
    loading_aid_id: UUID | None = Field(None, alias="loadingAidId")
    shipping_unit_id: UUID | None = Field(None, alias="shippingUnitId")
    order_number: int | None = Field(None, alias="orderNumber")
    addon: dict[str, object] | None = None

class CreateShipmentItemStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class CreateShipmentPreAdviceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID = Field(alias="shipmentId")
    type: ShipmentPreAdviceType
    target: str | None = None
    status: ShipmentPreAdviceStatus | None = None
    comment: str | None = None
    send_option: ShipmentPreAdviceSendOption | None = Field(None, alias="sendOption")
    required: bool | None = None

class CreateShipmentPromptRequest(BaseModel):
    prompt: str | None = None

class CreateShipmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    load_address_id: UUID | None = Field(None, alias="loadAddressId")
    delivery_address_id: UUID | None = Field(None, alias="deliveryAddressId")
    recipient_address_id: UUID | None = Field(None, alias="recipientAddressId")
    sender_address_id: UUID | None = Field(None, alias="senderAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    freight_payer_personal_account_id: UUID | None = Field(None, alias="freightPayerPersonalAccountId")
    freight_payer_address_id: UUID | None = Field(None, alias="freightPayerAddressId")
    customer_personal_account_id: UUID | None = Field(None, alias="customerPersonalAccountId")
    customer_address_id: UUID | None = Field(None, alias="customerAddressId")
    invoice_recipient_personal_account_id: UUID | None = Field(None, alias="invoiceRecipientPersonalAccountId")
    invoice_recipient_address_id: UUID | None = Field(None, alias="invoiceRecipientAddressId")
    supplier_personal_account_id: UUID | None = Field(None, alias="supplierPersonalAccountId")
    supplier_address_id: UUID | None = Field(None, alias="supplierAddressId")
    load_start: datetime | None = Field(None, alias="loadStart")
    load_end: datetime | None = Field(None, alias="loadEnd")
    planned_load_start: datetime | None = Field(None, alias="plannedLoadStart")
    planned_load_end: datetime | None = Field(None, alias="plannedLoadEnd")
    calculated_load_start: datetime | None = Field(None, alias="calculatedLoadStart")
    calculated_load_end: datetime | None = Field(None, alias="calculatedLoadEnd")
    actual_load_start: datetime | None = Field(None, alias="actualLoadStart")
    actual_load_end: datetime | None = Field(None, alias="actualLoadEnd")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_start: datetime | None = Field(None, alias="deliveryStart")
    delivery_end: datetime | None = Field(None, alias="deliveryEnd")
    planned_delivery_start: datetime | None = Field(None, alias="plannedDeliveryStart")
    planned_delivery_end: datetime | None = Field(None, alias="plannedDeliveryEnd")
    calculated_delivery_start: datetime | None = Field(None, alias="calculatedDeliveryStart")
    calculated_delivery_end: datetime | None = Field(None, alias="calculatedDeliveryEnd")
    actual_delivery_start: datetime | None = Field(None, alias="actualDeliveryStart")
    actual_delivery_end: datetime | None = Field(None, alias="actualDeliveryEnd")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_delivery_start_date_time: datetime | None = Field(None, alias="actualDeliveryStartDateTime")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    delivery_note_number: str | None = Field(None, alias="deliveryNoteNumber")
    actual_weight: QuantityRequest | None = Field(None, alias="actualWeight")
    is_template: bool | None = Field(None, alias="isTemplate")
    template_name: str | None = Field(None, alias="templateName")
    tags: list[UUID] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")
    construction_site_id: UUID | None = Field(None, alias="constructionSiteId")
    department_id: UUID | None = Field(None, alias="departmentId")
    incoterm_id: UUID | None = Field(None, alias="incotermId")
    addon: dict[str, object] | None = None
    items: list[CreateShipmentItemRequest] | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    billing_lines: list[CreateBillingLineRequest] | None = Field(None, alias="billingLines")

class CreateShipmentStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None

class CreateShipmentTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")

class CreateShipmentTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    load_address_id: UUID | None = Field(None, alias="loadAddressId")
    delivery_address_id: UUID | None = Field(None, alias="deliveryAddressId")
    recipient_address_id: UUID | None = Field(None, alias="recipientAddressId")
    sender_address_id: UUID | None = Field(None, alias="senderAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    freight_payer_personal_account_id: UUID | None = Field(None, alias="freightPayerPersonalAccountId")
    freight_payer_address_id: UUID | None = Field(None, alias="freightPayerAddressId")
    customer_personal_account_id: UUID | None = Field(None, alias="customerPersonalAccountId")
    customer_address_id: UUID | None = Field(None, alias="customerAddressId")
    invoice_recipient_personal_account_id: UUID | None = Field(None, alias="invoiceRecipientPersonalAccountId")
    invoice_recipient_address_id: UUID | None = Field(None, alias="invoiceRecipientAddressId")
    supplier_personal_account_id: UUID | None = Field(None, alias="supplierPersonalAccountId")
    supplier_address_id: UUID | None = Field(None, alias="supplierAddressId")
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    template_name: str | None = Field(None, alias="templateName")
    is_shipment_conversion_disabled: bool | None = Field(None, alias="isShipmentConversionDisabled")
    documents: list[ShipmentDocumentModel] | None = None
    tags: list[ShipmentTagModel] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")
    incoterm_id: UUID | None = Field(None, alias="incotermId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    load_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="loadWorkflow")
    delivery_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="deliveryWorkflow")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    load_start: TemplateTime | None = Field(None, alias="loadStart")
    load_end: TemplateTime | None = Field(None, alias="loadEnd")
    delivery_start: TemplateTime | None = Field(None, alias="deliveryStart")
    delivery_end: TemplateTime | None = Field(None, alias="deliveryEnd")
    construction_site_id: UUID | None = Field(None, alias="constructionSiteId")
    department_id: UUID | None = Field(None, alias="departmentId")
    addon: dict[str, object] | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    items: list[CreateShipmentItemRequest] | None = None
    billing_lines: list[CreateBillingLineRequest] | None = Field(None, alias="billingLines")

class CreateShippingUnitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    sscc: str | None = None
    type: str | None = None
    loading_aid_type_id: UUID | None = Field(None, alias="loadingAidTypeId")
    loading_aid_quantity: int | None = Field(None, alias="loadingAidQuantity")
    actual_loading_aid_type_id: UUID | None = Field(None, alias="actualLoadingAidTypeId")
    actual_loading_aid_quantity: int | None = Field(None, alias="actualLoadingAidQuantity")
    status_id: UUID | None = Field(None, alias="statusId")
    weight: QuantityRequest | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    actual_weight: QuantityRequest | None = Field(None, alias="actualWeight")
    actual_width: float | None = Field(None, alias="actualWidth")
    actual_height: float | None = Field(None, alias="actualHeight")
    actual_length: float | None = Field(None, alias="actualLength")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    primary_shipment_id: UUID | None = Field(None, alias="primaryShipmentId")
    tags: list[UUID] | None = None
    addon: dict[str, object] | None = None

class CreateShippingUnitStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class CreateShippingUnitTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")

class CreateTourActionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    order_id: int | None = Field(None, alias="orderId")
    date_time: datetime | None = Field(None, alias="dateTime")
    actual_date_time: datetime | None = Field(None, alias="actualDateTime")
    calculated_date_time: datetime | None = Field(None, alias="calculatedDateTime")
    mirrored_tour_number: str | None = Field(None, alias="mirroredTourNumber")
    type: str | None = None
    notes: str | None = None
    entity_id: UUID | None = Field(None, alias="entityId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    address_id: UUID | None = Field(None, alias="addressId")
    mirrored_tour_tags: list[UUID] | None = Field(None, alias="mirroredTourTags")
    cleaning_slots: list[LoadingSlotModel] | None = Field(None, alias="cleaningSlots")
    used_loading_slots: list[LoadingSlotModel] | None = Field(None, alias="usedLoadingSlots")

class CreateTourFromTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_template_id: UUID = Field(alias="tourTemplateId")
    data: list[TourFromTemplateData]

class CreateTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    reference: str | None = None
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_end_date_time: datetime | None = Field(None, alias="actualEndDateTime")
    calculated_start_date_time: datetime | None = Field(None, alias="calculatedStartDateTime")
    calculated_end_date_time: datetime | None = Field(None, alias="calculatedEndDateTime")
    financial_partner_personal_account_id: UUID | None = Field(None, alias="financialPartnerPersonalAccountId")
    financial_partner_address_id: UUID | None = Field(None, alias="financialPartnerAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    notes: str | None = None
    tags: list[UUID] | None = None
    actions: list[CreateTourActionRequest] | None = None
    billing_lines: list[CreateBillingLineRequest] | None = Field(None, alias="billingLines")

class CreateTourStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None

class CreateTourTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    internal_name: str | None = Field(None, alias="internalName")
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")
    functions: list[str] | None = None

class CreateTourTemplateActionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    order_id: int | None = Field(None, alias="orderId")
    date_time: TemplateTimeModel | None = Field(None, alias="dateTime")
    type: str | None = None
    notes: str | None = None
    entity_id: UUID | None = Field(None, alias="entityId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    address_id: UUID | None = Field(None, alias="addressId")
    used_loading_slots: list[LoadingSlotModel] | None = Field(None, alias="usedLoadingSlots")

class CreateTourTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    template_name: str | None = Field(None, alias="templateName")
    reference: str | None = None
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    start_date_time: TemplateTimeModel | None = Field(None, alias="startDateTime")
    end_date_time: TemplateTimeModel | None = Field(None, alias="endDateTime")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    notes: str | None = None
    tags: list[UUID] | None = None
    actions: list[CreateTourTemplateActionRequest] | None = None

class CreateToursFromAutoPlanRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    planned_tours: list[PlannedTourResult] = Field(alias="plannedTours")
    persist: bool | None = None
    auto_assign_resource_modes: list[str] | None = Field(None, alias="autoAssignResourceModes")
    action_optimization_mode: str | None = Field(None, alias="actionOptimizationMode")
    tour_number: str | None = Field(None, alias="tourNumber")

class CreateWeightNoteRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: str | None = None
    document_id: UUID | None = Field(None, alias="documentId")
    quantity: QuantityRequest | None = None
    type: WeightNoteType | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    first_weight: QuantityRequest | None = Field(None, alias="firstWeight")
    second_weight: QuantityRequest | None = Field(None, alias="secondWeight")
    first_date_time: datetime | None = Field(None, alias="firstDateTime")
    second_date_time: datetime | None = Field(None, alias="secondDateTime")
    reference: str | None = None

class DateTruncExpression(BaseModel):
    path: str | None
    unit: str | None

class DayOfWeek(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6

class Decimal128(BaseModel):
    pass

class DefaultPlanningAssignmentResponse(BaseModel):
    id: UUID | None = None
    assignments: list[ResourceAssignmentResponse] | None = None

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    order_id: int | None = Field(None, alias="orderId")
    hex_color: str | None = Field(None, alias="hexColor")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class ETAState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class EmptyTourResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    resource: ResourceModel | None = None
    distance: float | None = None
    toll_mileage: float | None = Field(None, alias="tollMileage")
    toll_costs: float | None = Field(None, alias="tollCosts")
    driving_time: str | None = Field(None, alias="drivingTime")
    previous_tour_id: UUID | None = Field(None, alias="previousTourId")
    next_tour_id: UUID | None = Field(None, alias="nextTourId")
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")

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

class EstimatedTimeOfArrivalResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_action_id: UUID | None = Field(None, alias="startActionId")
    global_start_action_id: UUID | None = Field(None, alias="globalStartActionId")
    end_action_id: UUID | None = Field(None, alias="endActionId")
    global_end_action_id: UUID | None = Field(None, alias="globalEndActionId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    start_longitude: float | None = Field(None, alias="startLongitude")
    start_latitude: float | None = Field(None, alias="startLatitude")
    current_longitude: float | None = Field(None, alias="currentLongitude")
    current_latitude: float | None = Field(None, alias="currentLatitude")
    end_longitude: float | None = Field(None, alias="endLongitude")
    end_latitude: float | None = Field(None, alias="endLatitude")
    remaining_minutes: int | None = Field(None, alias="remainingMinutes")
    remaining_distance_meters: int | None = Field(None, alias="remainingDistanceMeters")
    remaining_time_percent: int | None = Field(None, alias="remainingTimePercent")
    remaining_distance_percent: int | None = Field(None, alias="remainingDistancePercent")
    calculated_end_date_time: datetime | None = Field(None, alias="calculatedEndDateTime")
    planned_end_date_time: datetime | None = Field(None, alias="plannedEndDateTime")
    tolerance_minutes: int | None = Field(None, alias="toleranceMinutes")
    last_calculation: datetime | None = Field(None, alias="lastCalculation")
    state: ETAState | None = None

class FilterCondition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    path: str | None = None
    op: str | None = None
    value: dict[str, object] | None = None
    options: FilterConditionOptions | None = None
    and_: list[FilterCondition] | None = Field(None, alias="and")
    or_: list[FilterCondition] | None = Field(None, alias="or")
    not_: FilterCondition | None = Field(None, alias="not")

class FilterConditionOptions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ignore_case: bool | None = Field(None, alias="ignoreCase")

class GeoJson2DGeographicCoordinates(BaseModel):
    values: list[float] | None = None
    longitude: float | None = None
    latitude: float | None = None

class GeoJson2DGeographicCoordinatesGeoJsonBoundingBox(BaseModel):
    max: GeoJson2DGeographicCoordinates | None = None
    min: GeoJson2DGeographicCoordinates | None = None

class GeoJson2DGeographicCoordinatesGeoJsonLinearRingCoordinates(BaseModel):
    positions: list[GeoJson2DGeographicCoordinates] | None = None

class GeoJson2DGeographicCoordinatesGeoJsonPoint(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bounding_box: GeoJson2DGeographicCoordinatesGeoJsonBoundingBox | None = Field(None, alias="boundingBox")
    coordinate_reference_system: GeoJsonCoordinateReferenceSystem | None = Field(None, alias="coordinateReferenceSystem")
    extra_members: list[BsonElement] | None = Field(None, alias="extraMembers")
    coordinates: GeoJson2DGeographicCoordinates | None = None
    type: GeoJsonObjectType | None = None

class GeoJson2DGeographicCoordinatesGeoJsonPolygon(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bounding_box: GeoJson2DGeographicCoordinatesGeoJsonBoundingBox | None = Field(None, alias="boundingBox")
    coordinate_reference_system: GeoJsonCoordinateReferenceSystem | None = Field(None, alias="coordinateReferenceSystem")
    extra_members: list[BsonElement] | None = Field(None, alias="extraMembers")
    coordinates: GeoJson2DGeographicCoordinatesGeoJsonPolygonCoordinates | None = None
    type: GeoJsonObjectType | None = None

class GeoJson2DGeographicCoordinatesGeoJsonPolygonCoordinates(BaseModel):
    exterior: GeoJson2DGeographicCoordinatesGeoJsonLinearRingCoordinates | None = None
    holes: list[GeoJson2DGeographicCoordinatesGeoJsonLinearRingCoordinates] | None = None

class GeoJsonCoordinateReferenceSystem(BaseModel):
    type: str | None = None

class GeoJsonObjectType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8

class GeoLocationModel(BaseModel):
    longitude: float | None = None
    latitude: float | None = None

class Geofence(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    name: str | None = None
    color: str | None = None
    address: Address | None = None
    enable_tracking: bool | None = Field(None, alias="enableTracking")
    on_enter_flow_name: str | None = Field(None, alias="onEnterFlowName")
    on_leave_flow_name: str | None = Field(None, alias="onLeaveFlowName")
    location: GeoJson2DGeographicCoordinatesGeoJsonPolygon | None = None

class GeofenceResourceTracking(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    resource: Resource | None = None
    enter_date: datetime | None = Field(None, alias="enterDate")
    leave_date: datetime | None = Field(None, alias="leaveDate")
    geofence: Geofence | None = None

class GeofenceResourceTrackingFilter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    query_all_organizations: bool | None = Field(None, alias="queryAllOrganizations")
    include_ids: list[UUID] | None = Field(None, alias="includeIds")
    exclude_id: UUID | None = Field(None, alias="excludeId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    geofence_id: UUID | None = Field(None, alias="geofenceId")
    is_active: bool | None = Field(None, alias="isActive")

class GeofenceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    color: str | None = None
    address: AddressModel | None = None
    enable_tracking: bool | None = Field(None, alias="enableTracking")
    on_enter_flow_name: str | None = Field(None, alias="onEnterFlowName")
    on_leave_flow_name: str | None = Field(None, alias="onLeaveFlowName")
    location: list[GeoLocationModel] | None = None

class GetComposedAddressResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None

class GetComposedDriverResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    match_code: str | None = Field(None, alias="matchCode")
    dtco: GetComposedDtcoResponse | None = None

class GetComposedDtcoResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    activity: str | None = None
    remaining_daily_work_time: str | None = Field(None, alias="remainingDailyWorkTime")
    remaining_daily_driving_time: str | None = Field(None, alias="remainingDailyDrivingTime")
    remaining_weekly_work_time: str | None = Field(None, alias="remainingWeeklyWorkTime")
    remaining_weekly_driving_time: str | None = Field(None, alias="remainingWeeklyDrivingTime")
    remaining_double_weekly_driving_time: str | None = Field(None, alias="remainingDoubleWeeklyDrivingTime")

class GetComposedLoadingSlotStateResponse(BaseModel):
    id: UUID | None = None
    name: str | None = None
    state: str | None = None

class GetComposedLocationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    latitude: float | None = None
    longitude: float | None = None
    address: GetComposedAddressResponse | None = None
    geofence_id: UUID | None = Field(None, alias="geofenceId")
    geofence_name: str | None = Field(None, alias="geofenceName")

class GetComposedMessageResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date_time: datetime | None = Field(None, alias="dateTime")
    message: str | None = None
    unrecognized: bool | None = None
    notification_id: UUID | None = Field(None, alias="notificationId")

class GetComposedResourceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    tractor_unit: GetComposedTractorUnitResponse | None = Field(None, alias="tractorUnit")
    trailer: list[GetComposedTrailerResponse] | None = None
    main_driver: GetComposedDriverResponse | None = Field(None, alias="mainDriver")
    co_driver: GetComposedDriverResponse | None = Field(None, alias="coDriver")
    location: GetComposedLocationResponse | None = None
    latest_message: GetComposedMessageResponse | None = Field(None, alias="latestMessage")

class GetComposedTractorUnitDetailsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fuel_level_percent: float | None = Field(None, alias="fuelLevelPercent")

class GetComposedTractorUnitResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    match_code: str | None = Field(None, alias="matchCode")
    details: GetComposedTractorUnitDetailsResponse | None = None

class GetComposedTrailerResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    match_code: str | None = Field(None, alias="matchCode")
    loading_slot_states: list[GetComposedLoadingSlotStateResponse] | None = Field(None, alias="loadingSlotStates")

class GroupByField(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_: str | None = Field(alias="as")
    path: str | None = None
    date_trunc: DateTruncExpression | None = Field(None, alias="dateTrunc")

class GroupStage(BaseModel):
    by: list[GroupByField] | None
    fields: dict[str, AggregationExpression] | None

class GroupedResourcesModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    resources: list[ResourceModel] | None = None
    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")

class GrpcDefinitions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    package: str | None = None
    service: str | None = None
    proto_file: str | None = Field(None, alias="protoFile")

class IActionResult(BaseModel):
    pass

class IncotermResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    order_id: int | None = Field(None, alias="orderId")
    abbreviation: str | None = None
    description: str | None = None

class LoadingAidBookingBarcodeModel(BaseModel):
    name: str | None = None
    value: str | None = None

class LoadingAidBookingModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    customer: AddressModel | None = None
    location: AddressModel | None = None
    driver: AddressModel | None = None
    vehicle: LoadingAidBookingVehicleModel | None = None
    carrier: AddressModel | None = None
    external_vehicle: str | None = Field(None, alias="externalVehicle")
    external_carrier: str | None = Field(None, alias="externalCarrier")
    external_driver: str | None = Field(None, alias="externalDriver")
    date: datetime | None = None
    eco_number: str | None = Field(None, alias="ecoNumber")
    delivery_note: str | None = Field(None, alias="deliveryNote")
    loading_aids: list[LoadingAidModel] | None = Field(None, alias="loadingAids")
    seals_arrival: list[str] | None = Field(None, alias="sealsArrival")
    seals_departure: list[str] | None = Field(None, alias="sealsDeparture")

class LoadingAidBookingVehicleModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    match_code: str | None = Field(None, alias="matchCode")
    display_name: str | None = Field(None, alias="displayName")

class LoadingAidModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    amount: int | None = None
    type: LoadingAidTypeModel | None = None
    movement_type: MovementType | None = Field(None, alias="movementType")
    barcodes: list[LoadingAidBookingBarcodeModel] | None = None

class LoadingAidTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    number: int | None = None

class LoadingAidTypeResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: int | None = None
    display_name: str | None = Field(None, alias="displayName")
    weight: float | None = None
    short_text: str | None = Field(None, alias="shortText")
    width: int | None = None
    length: int | None = None
    storage_position: float | None = Field(None, alias="storagePosition")

class LoadingDateTimeType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class LoadingSlotModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    resource_id: UUID = Field(alias="resourceId")
    id: UUID | None = None
    description: str | None = None

class LocalizableErrorResponse(BaseModel):
    key: str | None = None
    code: str | None = None
    params: dict[str, object] | None = None

class LookupStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_: str | None = Field(alias="from")
    local_path: str | None = Field(alias="localPath")
    foreign_path: str | None = Field(alias="foreignPath")
    as_: str | None = Field(alias="as")

class ManipulateTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    new_start_date: datetime | None = Field(None, alias="newStartDate")
    new_end_date: datetime | None = Field(None, alias="newEndDate")
    new_resource_id: UUID | None = Field(None, alias="newResourceId")

class MatchStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    and_: list[FilterCondition] | None = Field(None, alias="and")
    or_: list[FilterCondition] | None = Field(None, alias="or")
    not_: FilterCondition | None = Field(None, alias="not")
    condition: FilterCondition | None = None

class MovementType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

class ObjectId(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    timestamp: int | None = None
    creation_time: datetime | None = Field(None, alias="creationTime")

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
    group_key: str | None = Field(None, alias="groupKey")
    group_display_key: str | None = Field(None, alias="groupDisplayKey")
    group_display_name: str | None = Field(None, alias="groupDisplayName")

class OxQLQueryResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    items: list[object] | None
    page_info: PageInfo = Field(alias="pageInfo")

class PageInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    has_next_page: bool = Field(alias="hasNextPage")
    next_cursor: str | None = Field(None, alias="nextCursor")
    total_count: int | None = Field(None, alias="totalCount")

class PageStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    limit: int | None = None
    cursor: str | None = None
    include_total_count: bool | None = Field(None, alias="includeTotalCount")

class PatchAppointmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    resources: list[UUID] | None = None
    functions: list[str] | None = None
    title: str | None = None
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    hex_color: str | None = Field(None, alias="hexColor")

class PatchBillingLineRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    financial_partner: BillingLineContactRequest | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    type: BillingLineType | None = None
    status_id: UUID | None = Field(None, alias="statusId")
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    cost_centers: list[BillingLineCostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[BillingLineCostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    general_ledger_account_group_id: UUID | None = Field(None, alias="generalLedgerAccountGroupId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    text: str | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    addon: dict[str, object] | None = None
    id: UUID | None = None
    quantity: QuantityPatchRequest | None = None
    _remove: bool | None = None

class PatchComposedResourceSettingsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    composed_resources_enabled: bool | None = Field(None, alias="composedResourcesEnabled")

class PatchDefaultPlanningRequest(BaseModel):
    assignments: list[ResourceAssignmentPatch] | None = None

class PatchDepartmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    order_id: int | None = Field(None, alias="orderId")
    hex_color: str | None = Field(None, alias="hexColor")

class PatchGeofenceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    address_id: UUID | None = Field(None, alias="addressId")
    color: str | None = None
    enable_tracking: bool | None = Field(None, alias="enableTracking")
    on_enter_flow_name: str | None = Field(None, alias="onEnterFlowName")
    on_leave_flow_name: str | None = Field(None, alias="onLeaveFlowName")
    location: list[GeoLocationModel] | None = None

class PatchIncotermRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    order_id: int | None = Field(None, alias="orderId")
    abbreviation: str | None = None
    description: str | None = None

class PatchLoadingAidTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int | None = None
    display_name: str | None = Field(None, alias="displayName")
    weight: float | None = None
    short_text: str | None = Field(None, alias="shortText")
    width: int | None = None
    length: int | None = None
    storage_position: float | None = Field(None, alias="storagePosition")

class PatchLoadingSlotRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    resource_id: UUID = Field(alias="resourceId")
    id: UUID | None = None
    description: str | None = None

class PatchPlanningRegionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    include: list[RegionModel] | None = None
    exclude: list[RegionModel] | None = None
    functions: list[str] | None = None

class PatchScheduledPlanningRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    assignments: list[ResourceAssignmentPatch] | None = None
    shift_id: UUID | None = Field(None, alias="shiftId")
    start_date: datetime | None = Field(None, alias="startDate")
    end_date: datetime | None = Field(None, alias="endDate")

class PatchShiftRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    start_time: str | None = Field(None, alias="startTime")
    end_time: str | None = Field(None, alias="endTime")

class PatchShipmentItemRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    text: str | None = None
    loading_meters: float | None = Field(None, alias="loadingMeters")
    reference: str | None = None
    quantity: QuantityPatchRequest | None = None
    weight: QuantityPatchRequest | None = None
    article_id: UUID | None = Field(None, alias="articleId")
    weight_notes: list[WeightNoteModel] | None = Field(None, alias="weightNotes")
    loading_aid_id: UUID | None = Field(None, alias="loadingAidId")
    order_number: int | None = Field(None, alias="orderNumber")
    shipping_unit_id: UUID | None = Field(None, alias="shippingUnitId")
    addon: dict[str, object] | None = None
    _remove: bool | None = None

class PatchShipmentPreAdviceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: ShipmentPreAdviceType | None = None
    target: str | None = None
    comment: str | None = None
    send_option: ShipmentPreAdviceSendOption | None = Field(None, alias="sendOption")
    required: bool | None = None

class PatchShipmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    load_address_id: UUID | None = Field(None, alias="loadAddressId")
    delivery_address_id: UUID | None = Field(None, alias="deliveryAddressId")
    recipient_address_id: UUID | None = Field(None, alias="recipientAddressId")
    sender_address_id: UUID | None = Field(None, alias="senderAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    freight_payer_personal_account_id: UUID | None = Field(None, alias="freightPayerPersonalAccountId")
    freight_payer_address_id: UUID | None = Field(None, alias="freightPayerAddressId")
    customer_personal_account_id: UUID | None = Field(None, alias="customerPersonalAccountId")
    customer_address_id: UUID | None = Field(None, alias="customerAddressId")
    invoice_recipient_personal_account_id: UUID | None = Field(None, alias="invoiceRecipientPersonalAccountId")
    invoice_recipient_address_id: UUID | None = Field(None, alias="invoiceRecipientAddressId")
    supplier_personal_account_id: UUID | None = Field(None, alias="supplierPersonalAccountId")
    supplier_address_id: UUID | None = Field(None, alias="supplierAddressId")
    load_start: datetime | None = Field(None, alias="loadStart")
    load_end: datetime | None = Field(None, alias="loadEnd")
    planned_load_start: datetime | None = Field(None, alias="plannedLoadStart")
    planned_load_end: datetime | None = Field(None, alias="plannedLoadEnd")
    calculated_load_start: datetime | None = Field(None, alias="calculatedLoadStart")
    calculated_load_end: datetime | None = Field(None, alias="calculatedLoadEnd")
    actual_load_start: datetime | None = Field(None, alias="actualLoadStart")
    actual_load_end: datetime | None = Field(None, alias="actualLoadEnd")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_start: datetime | None = Field(None, alias="deliveryStart")
    delivery_end: datetime | None = Field(None, alias="deliveryEnd")
    planned_delivery_start: datetime | None = Field(None, alias="plannedDeliveryStart")
    planned_delivery_end: datetime | None = Field(None, alias="plannedDeliveryEnd")
    calculated_delivery_start: datetime | None = Field(None, alias="calculatedDeliveryStart")
    calculated_delivery_end: datetime | None = Field(None, alias="calculatedDeliveryEnd")
    actual_delivery_start: datetime | None = Field(None, alias="actualDeliveryStart")
    actual_delivery_end: datetime | None = Field(None, alias="actualDeliveryEnd")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_delivery_start_date_time: datetime | None = Field(None, alias="actualDeliveryStartDateTime")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    delivery_note_number: str | None = Field(None, alias="deliveryNoteNumber")
    actual_weight: QuantityPatchRequest | None = Field(None, alias="actualWeight")
    is_template: bool | None = Field(None, alias="isTemplate")
    template_name: str | None = Field(None, alias="templateName")
    tags: list[UUID] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")
    construction_site_id: UUID | None = Field(None, alias="constructionSiteId")
    department_id: UUID | None = Field(None, alias="departmentId")
    incoterm_id: UUID | None = Field(None, alias="incotermId")
    addon: dict[str, object] | None = None
    items: list[PatchShipmentItemRequest] | None = None
    billing_lines: list[PatchBillingLineRequest] | None = Field(None, alias="billingLines")
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")

class PatchShipmentTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")

class PatchShipmentTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    load_address_id: UUID | None = Field(None, alias="loadAddressId")
    delivery_address_id: UUID | None = Field(None, alias="deliveryAddressId")
    recipient_address_id: UUID | None = Field(None, alias="recipientAddressId")
    sender_address_id: UUID | None = Field(None, alias="senderAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    freight_payer_personal_account_id: UUID | None = Field(None, alias="freightPayerPersonalAccountId")
    freight_payer_address_id: UUID | None = Field(None, alias="freightPayerAddressId")
    customer_personal_account_id: UUID | None = Field(None, alias="customerPersonalAccountId")
    customer_address_id: UUID | None = Field(None, alias="customerAddressId")
    invoice_recipient_personal_account_id: UUID | None = Field(None, alias="invoiceRecipientPersonalAccountId")
    invoice_recipient_address_id: UUID | None = Field(None, alias="invoiceRecipientAddressId")
    supplier_personal_account_id: UUID | None = Field(None, alias="supplierPersonalAccountId")
    supplier_address_id: UUID | None = Field(None, alias="supplierAddressId")
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    template_name: str | None = Field(None, alias="templateName")
    is_shipment_conversion_disabled: bool | None = Field(None, alias="isShipmentConversionDisabled")
    documents: list[ShipmentDocumentModel] | None = None
    tags: list[ShipmentTagModel] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    load_workflow_id: UUID | None = Field(None, alias="loadWorkflowId")
    delivery_workflow_id: UUID | None = Field(None, alias="deliveryWorkflowId")
    incoterm_id: UUID | None = Field(None, alias="incotermId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    load_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="loadWorkflow")
    delivery_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="deliveryWorkflow")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    load_start: TemplateTime | None = Field(None, alias="loadStart")
    load_end: TemplateTime | None = Field(None, alias="loadEnd")
    delivery_start: TemplateTime | None = Field(None, alias="deliveryStart")
    delivery_end: TemplateTime | None = Field(None, alias="deliveryEnd")
    construction_site_id: UUID | None = Field(None, alias="constructionSiteId")
    department_id: UUID | None = Field(None, alias="departmentId")
    addon: dict[str, object] | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    items: list[PatchShipmentItemRequest] | None = None
    billing_lines: list[PatchBillingLineRequest] | None = Field(None, alias="billingLines")

class PatchShippingUnitRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    sscc: str | None = None
    type: str | None = None
    loading_aid_type_id: UUID | None = Field(None, alias="loadingAidTypeId")
    loading_aid_quantity: int | None = Field(None, alias="loadingAidQuantity")
    actual_loading_aid_type_id: UUID | None = Field(None, alias="actualLoadingAidTypeId")
    actual_loading_aid_quantity: int | None = Field(None, alias="actualLoadingAidQuantity")
    weight: QuantityPatchRequest | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    actual_weight: QuantityPatchRequest | None = Field(None, alias="actualWeight")
    actual_width: float | None = Field(None, alias="actualWidth")
    actual_height: float | None = Field(None, alias="actualHeight")
    actual_length: float | None = Field(None, alias="actualLength")
    status_id: UUID | None = Field(None, alias="statusId")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    primary_shipment_id: UUID | None = Field(None, alias="primaryShipmentId")
    tags: list[UUID] | None = None
    addon: dict[str, object] | None = None

class PatchShippingUnitTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")

class PatchTourActionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    order_id: int | None = Field(None, alias="orderId")
    date_time: datetime | None = Field(None, alias="dateTime")
    actual_date_time: datetime | None = Field(None, alias="actualDateTime")
    calculated_date_time: datetime | None = Field(None, alias="calculatedDateTime")
    mirrored_tour_number: str | None = Field(None, alias="mirroredTourNumber")
    type: str | None = None
    notes: str | None = None
    entity_id: UUID | None = Field(None, alias="entityId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    address_id: UUID | None = Field(None, alias="addressId")
    mirrored_tour_tags: list[UUID] | None = Field(None, alias="mirroredTourTags")
    _remove: bool | None = None
    cleaning_slots: list[PatchLoadingSlotRequest] | None = Field(None, alias="cleaningSlots")
    used_loading_slots: list[PatchLoadingSlotRequest] | None = Field(None, alias="usedLoadingSlots")

class PatchTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    reference: str | None = None
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_end_date_time: datetime | None = Field(None, alias="actualEndDateTime")
    calculated_start_date_time: datetime | None = Field(None, alias="calculatedStartDateTime")
    calculated_end_date_time: datetime | None = Field(None, alias="calculatedEndDateTime")
    financial_partner_personal_account_id: UUID | None = Field(None, alias="financialPartnerPersonalAccountId")
    financial_partner_address_id: UUID | None = Field(None, alias="financialPartnerAddressId")
    carrier_personal_account_id: UUID | None = Field(None, alias="carrierPersonalAccountId")
    carrier_address_id: UUID | None = Field(None, alias="carrierAddressId")
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    notes: str | None = None
    tags: list[UUID] | None = None
    actions: list[PatchTourActionRequest] | None = None
    billing_lines: list[PatchBillingLineRequest] | None = Field(None, alias="billingLines")
    auto_adjust_actions_mode: str | None = Field(None, alias="autoAdjustActionsMode")

class PatchTourStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None

class PatchTourTagRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    internal_name: str | None = Field(None, alias="internalName")
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")
    functions: list[str] | None = None

class PatchTourTemplateActionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    order_id: int | None = Field(None, alias="orderId")
    date_time: TemplateTimeModel | None = Field(None, alias="dateTime")
    type: str | None = None
    notes: str | None = None
    entity_id: UUID | None = Field(None, alias="entityId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    address_id: UUID | None = Field(None, alias="addressId")
    used_loading_slots: list[PatchLoadingSlotRequest] | None = Field(None, alias="usedLoadingSlots")
    _remove: bool | None = None

class PatchTourTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    template_name: str | None = Field(None, alias="templateName")
    reference: str | None = None
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_address_id: UUID | None = Field(None, alias="startAddressId")
    end_address_id: UUID | None = Field(None, alias="endAddressId")
    start_date_time: TemplateTimeModel | None = Field(None, alias="startDateTime")
    end_date_time: TemplateTimeModel | None = Field(None, alias="endDateTime")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    notes: str | None = None
    tags: list[UUID] | None = None
    actions: list[PatchTourTemplateActionRequest] | None = None

class PipelineStage(BaseModel):
    match: MatchStage | None = None
    lookup: LookupStage | None = None
    resolve: ResolveStage | None = None
    unwind: UnwindStage | None = None
    group: GroupStage | None = None
    project: ProjectStage | None = None
    sort: list[SortField] | None = None
    page: PageStage | None = None

class PlannedStop(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID | None = Field(None, alias="shipmentId")
    stop_type: str | None = Field(None, alias="stopType")
    estimated_arrival: datetime | None = Field(None, alias="estimatedArrival")
    latitude: float | None = None
    longitude: float | None = None

class PlannedTourResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    resource_id: UUID | None = Field(None, alias="resourceId")
    stops: list[PlannedStop] | None = None
    estimated_travel_time: str | None = Field(None, alias="estimatedTravelTime")
    estimated_distance_meters: float | None = Field(None, alias="estimatedDistanceMeters")
    total_weight: float | None = Field(None, alias="totalWeight")
    total_loading_meters: float | None = Field(None, alias="totalLoadingMeters")

class PlanningRegionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    include: list[RegionModel] | None = None
    exclude: list[RegionModel] | None = None
    functions: list[str] | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class PlanningResourceResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    type: str | None = None
    order_id: int | None = Field(None, alias="orderId")

class PostDefaultPlanningRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shift_id: UUID = Field(alias="shiftId")
    assignments: list[ResourceAssignmentRequest] | None = None

class PostDepartmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    order_id: int = Field(alias="orderId")
    hex_color: str | None = Field(None, alias="hexColor")

class PostIncotermRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    order_id: int = Field(alias="orderId")
    abbreviation: str
    description: str | None = None

class PostScheduledPlanningRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shift_id: UUID = Field(alias="shiftId")
    start_date: datetime = Field(alias="startDate")
    assignments: list[ResourceAssignmentRequest] | None = None

class PostShiftRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    start_time: str = Field(alias="startTime")
    end_time: str = Field(alias="endTime")

class ProjectStage(BaseModel):
    fields: dict[str, int] | None

class QuantityModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    quantity_unit: QuantityUnitModel | None = Field(None, alias="quantityUnit")

class QuantityPatchRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    quantity_unit_id: UUID | None = Field(None, alias="quantityUnitId")

class QuantityRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    quantity_unit_id: UUID | None = Field(None, alias="quantityUnitId")

class QuantityUnitModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guid: UUID | None = None
    name: str | None = None
    short_name: str | None = Field(None, alias="shortName")
    digits: int | None = None

class QueryExpression(BaseModel):
    path: str | None = None
    literal: dict[str, object] | None = None
    var: str | None = None
    operator: str | None = None
    operands: list[QueryExpression] | None = None

class QueryRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    entity_type: str | None = Field(alias="entityType")
    pipeline: list[PipelineStage] | None
    variables: QueryVariables | None = None

class QueryVariables(BaseModel):
    pass

class Regex(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    options: RegexOptions | None = None
    right_to_left: bool | None = Field(None, alias="rightToLeft")
    match_timeout: str | None = Field(None, alias="matchTimeout")

class RegexOptions(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_256 = 256
    VALUE_512 = 512
    VALUE_1024 = 1024

class RegionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    country_iso: str = Field(alias="countryIso")
    zip_code: str = Field(alias="zipCode")

class RemoveTagFromTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    tag_id: UUID | None = Field(None, alias="tagId")

class ReportingShipmentItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str | None = None
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    quantity: QuantityModel | None = None
    weight: QuantityModel | None = None

class RequiredEndpointContractDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    allow_multiple: bool | None = Field(None, alias="allowMultiple")

class ResolveStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    source: str | None
    local_path: str | None = Field(alias="localPath")
    as_: str | None = Field(alias="as")

class Resource(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    type: str | None = None
    match_code: str | None = Field(None, alias="matchCode")
    display_name: str | None = Field(None, alias="displayName")
    attached_resource: list[Resource] | None = Field(None, alias="attachedResource")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_name: str | None = Field(None, alias="updateUserName")
    location: ResourceLocation | None = None
    usable_until: datetime | None = Field(None, alias="usableUntil")
    planning_order_key: str | None = Field(None, alias="planningOrderKey")
    notes: str | None = None

class ResourceAssignmentPatch(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    department_id: UUID | None = Field(None, alias="departmentId")
    resources: list[UUID] | None = None

class ResourceAssignmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    department_id: UUID = Field(alias="departmentId")
    resource_ids: list[UUID] | None = Field(None, alias="resourceIds")

class ResourceAssignmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    department_id: UUID | None = Field(None, alias="departmentId")
    resources: list[PlanningResourceResponse] | None = None

class ResourceLocation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    latitude: float | None = None
    longitude: float | None = None
    location_set_at: datetime | None = Field(None, alias="locationSetAt")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None
    location: GeoJson2DGeographicCoordinatesGeoJsonPoint | None = None

class ResourceLocationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    latitude: float | None = None
    longitude: float | None = None
    location_set_at: datetime | None = Field(None, alias="locationSetAt")
    street: str | None = None
    house_number: str | None = Field(None, alias="houseNumber")
    zipcode: str | None = None
    district: str | None = None
    federal_state: str | None = Field(None, alias="federalState")
    country: str | None = None
    country_iso: str | None = Field(None, alias="countryIso")
    city: str | None = None

class ResourceModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    match_code: str = Field(alias="matchCode")
    display_name: str | None = Field(None, alias="displayName")
    loading_slots: list[LoadingSlotModel] | None = Field(None, alias="loadingSlots")
    location: ResourceLocationModel | None = None
    is_loadable: bool | None = Field(None, alias="isLoadable")
    planning_order_key: str | None = Field(None, alias="planningOrderKey")
    usable_until: datetime | None = Field(None, alias="usableUntil")
    notes: str | None = None
    id: UUID | None = None
    attached_resource: list[ResourceModel] | None = Field(None, alias="attachedResource")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")
    organization_id: UUID | None = Field(None, alias="organizationId")

class ScheduledPlanningAssignmentResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    assignments: list[ResourceAssignmentResponse] | None = None
    shift_id: UUID | None = Field(None, alias="shiftId")
    start_date: datetime | None = Field(None, alias="startDate")
    end_date: datetime | None = Field(None, alias="endDate")

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

class SetShipmentPreAdviceStatusRequest(BaseModel):
    status: ShipmentPreAdviceStatus

class SetShipmentStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    status_id: UUID = Field(alias="statusId")

class SetTourActualTimesRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    actual_start: datetime | None = Field(None, alias="actualStart")
    actual_end: datetime | None = Field(None, alias="actualEnd")
    new_status_id: UUID | None = Field(None, alias="newStatusId")

class SetTourStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID = Field(alias="tourId")
    status_id: UUID = Field(alias="statusId")

class SettingOption(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: dict[str, object] | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")

class ShiftResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    start_time: str | None = Field(None, alias="startTime")
    end_time: str | None = Field(None, alias="endTime")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class ShipmentArticleModel(BaseModel):
    id: UUID | None = None
    number: str | None = None
    name: str | None = None

class ShipmentDocumentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    document_id: UUID | None = Field(None, alias="documentId")
    shipment_id: UUID | None = Field(None, alias="shipmentId")
    shipment_item_id: UUID | None = Field(None, alias="shipmentItemId")
    weight_note_id: UUID | None = Field(None, alias="weightNoteId")
    invoice_order_nr: int | None = Field(None, alias="invoiceOrderNr")
    is_invoice_attachment: bool | None = Field(None, alias="isInvoiceAttachment")

class ShipmentFromTemplateData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    start_date: datetime = Field(alias="startDate")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    amount: int | None = None

class ShipmentFromTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_template_id: UUID = Field(alias="shipmentTemplateId")
    data: list[ShipmentFromTemplateData]

class ShipmentItemModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str | None = None
    loading_meters: float | None = Field(None, alias="loadingMeters")
    reference: str | None = None
    quantity: QuantityModel | None = None
    weight: QuantityModel | None = None
    order_number: int | None = Field(None, alias="orderNumber")
    addon: dict[str, object] | None = None
    id: UUID | None = None
    status: ShipmentItemStatusModel | None = None
    article: ShipmentArticleModel | None = None
    weight_notes: list[WeightNoteModel] | None = Field(None, alias="weightNotes")
    loading_aid_type: ShipmentLoadingAidTypeModel | None = Field(None, alias="loadingAidType")
    shipping_unit: ShippingUnitSubsetModel | None = Field(None, alias="shippingUnit")

class ShipmentItemStatusModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class ShipmentLoadingAidTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: int | None = None
    display_name: str | None = Field(None, alias="displayName")
    weight: float | None = None
    short_text: str | None = Field(None, alias="shortText")
    width: int | None = None
    length: int | None = None
    storage_position: float | None = Field(None, alias="storagePosition")

class ShipmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    load_address: AddressModel | None = Field(None, alias="loadAddress")
    delivery_address: AddressModel | None = Field(None, alias="deliveryAddress")
    carrier: BillableContactModel | None = None
    freight_payer: BillableContactModel | None = Field(None, alias="freightPayer")
    customer: BillableContactModel | None = None
    recipient_address: AddressModel | None = Field(None, alias="recipientAddress")
    invoice_recipient: BillableContactModel | None = Field(None, alias="invoiceRecipient")
    sender_address: AddressModel | None = Field(None, alias="senderAddress")
    supplier: BillableContactModel | None = None
    load_start: datetime | None = Field(None, alias="loadStart")
    load_end: datetime | None = Field(None, alias="loadEnd")
    planned_load_start: datetime | None = Field(None, alias="plannedLoadStart")
    planned_load_end: datetime | None = Field(None, alias="plannedLoadEnd")
    calculated_load_start: datetime | None = Field(None, alias="calculatedLoadStart")
    calculated_load_end: datetime | None = Field(None, alias="calculatedLoadEnd")
    actual_load_start: datetime | None = Field(None, alias="actualLoadStart")
    actual_load_end: datetime | None = Field(None, alias="actualLoadEnd")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_start: datetime | None = Field(None, alias="deliveryStart")
    delivery_end: datetime | None = Field(None, alias="deliveryEnd")
    planned_delivery_start: datetime | None = Field(None, alias="plannedDeliveryStart")
    planned_delivery_end: datetime | None = Field(None, alias="plannedDeliveryEnd")
    calculated_delivery_start: datetime | None = Field(None, alias="calculatedDeliveryStart")
    calculated_delivery_end: datetime | None = Field(None, alias="calculatedDeliveryEnd")
    actual_delivery_start: datetime | None = Field(None, alias="actualDeliveryStart")
    actual_delivery_end: datetime | None = Field(None, alias="actualDeliveryEnd")
    effective_load_start: datetime | None = Field(None, alias="effectiveLoadStart")
    effective_load_end: datetime | None = Field(None, alias="effectiveLoadEnd")
    effective_delivery_start: datetime | None = Field(None, alias="effectiveDeliveryStart")
    effective_delivery_end: datetime | None = Field(None, alias="effectiveDeliveryEnd")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_delivery_start_date_time: datetime | None = Field(None, alias="actualDeliveryStartDateTime")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    delivery_note_number: str | None = Field(None, alias="deliveryNoteNumber")
    actual_weight: QuantityModel | None = Field(None, alias="actualWeight")
    is_template: bool | None = Field(None, alias="isTemplate")
    template_name: str | None = Field(None, alias="templateName")
    status: ShipmentStatusModel | None = None
    items: list[ShipmentItemModel] | None = None
    tags: list[ShipmentTagModel] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    load_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="loadWorkflow")
    delivery_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="deliveryWorkflow")
    tours: list[ShipmentTourModel] | None = None
    construction_site: ConstructionSiteModel | None = Field(None, alias="constructionSite")
    department: DepartmentResponse | None = None
    incoterm: IncotermResponse | None = None
    addon: dict[str, object] | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    billing_lines: list[BillingLineModel] | None = Field(None, alias="billingLines")

class ShipmentPreAdviceModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    shipment_id: UUID | None = Field(None, alias="shipmentId")
    type: ShipmentPreAdviceType | None = None
    target: str | None = None
    status: ShipmentPreAdviceStatus | None = None
    comment: str | None = None
    send_option: ShipmentPreAdviceSendOption | None = Field(None, alias="sendOption")
    required: bool | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")

class ShipmentPreAdviceSendOption(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ShipmentPreAdviceStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ShipmentPreAdviceType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

class ShipmentStatusModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None
    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class ShipmentSubsetModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    load_start: datetime | None = Field(None, alias="loadStart")
    load_end: datetime | None = Field(None, alias="loadEnd")
    delivery_start: datetime | None = Field(None, alias="deliveryStart")
    delivery_end: datetime | None = Field(None, alias="deliveryEnd")
    load_address: AddressModel | None = Field(None, alias="loadAddress")
    delivery_address: AddressModel | None = Field(None, alias="deliveryAddress")
    sender_address: AddressModel | None = Field(None, alias="senderAddress")
    recipient_address: AddressModel | None = Field(None, alias="recipientAddress")

class ShipmentTagModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class ShipmentTelematicWorkflowModel(BaseModel):
    id: UUID | None = None
    name: str | None = None

class ShipmentTemplateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    create_user_id: UUID | None = Field(None, alias="createUserId")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    load_address: AddressModel | None = Field(None, alias="loadAddress")
    delivery_address: AddressModel | None = Field(None, alias="deliveryAddress")
    carrier: BillableContactModel | None = None
    freight_payer: BillableContactModel | None = Field(None, alias="freightPayer")
    customer: BillableContactModel | None = None
    recipient_address: AddressModel | None = Field(None, alias="recipientAddress")
    invoice_recipient: BillableContactModel | None = Field(None, alias="invoiceRecipient")
    sender_address: AddressModel | None = Field(None, alias="senderAddress")
    supplier: BillableContactModel | None = None
    order_date: datetime | None = Field(None, alias="orderDate")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    reference_number: str | None = Field(None, alias="referenceNumber")
    load_number: str | None = Field(None, alias="loadNumber")
    delivery_number: str | None = Field(None, alias="deliveryNumber")
    template_name: str | None = Field(None, alias="templateName")
    is_shipment_conversion_disabled: bool | None = Field(None, alias="isShipmentConversionDisabled")
    items: list[ShipmentItemModel] | None = None
    documents: list[ShipmentDocumentModel] | None = None
    tags: list[ShipmentTagModel] | None = None
    notes: str | None = None
    external_notes: str | None = Field(None, alias="externalNotes")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    load_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="loadWorkflow")
    delivery_workflow: ShipmentTelematicWorkflowModel | None = Field(None, alias="deliveryWorkflow")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    loading_time_type: LoadingDateTimeType | None = Field(None, alias="loadingTimeType")
    delivery_time_type: LoadingDateTimeType | None = Field(None, alias="deliveryTimeType")
    load_start: TemplateTime | None = Field(None, alias="loadStart")
    load_end: TemplateTime | None = Field(None, alias="loadEnd")
    delivery_start: TemplateTime | None = Field(None, alias="deliveryStart")
    delivery_end: TemplateTime | None = Field(None, alias="deliveryEnd")
    construction_site: ConstructionSiteModel | None = Field(None, alias="constructionSite")
    department: DepartmentResponse | None = None
    addon: dict[str, object] | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    billing_lines: list[BillingLineModel] | None = Field(None, alias="billingLines")

class ShipmentToLoadingAidBookingRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID = Field(alias="shipmentId")

class ShipmentToTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_id: UUID = Field(alias="shipmentId")
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    auto_assign_resource_modes: list[str] | None = Field(None, alias="autoAssignResourceModes")
    action_optimization_mode: str | None = Field(None, alias="actionOptimizationMode")
    persist: bool | None = None

class ShipmentTourModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_id: UUID | None = Field(None, alias="tourId")
    resource: ResourceModel | None = None
    number: str | None = None
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")

class ShipmentsToTourRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_ids: list[UUID] | None = Field(None, alias="shipmentIds")
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    auto_assign_resource_modes: list[str] | None = Field(None, alias="autoAssignResourceModes")
    action_optimization_mode: str | None = Field(None, alias="actionOptimizationMode")
    persist: bool | None = None

class ShipmentsToToursRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    shipment_ids: list[UUID] | None = Field(None, alias="shipmentIds")
    resource_id: UUID | None = Field(None, alias="resourceId")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    auto_assign_resource_modes: list[str] | None = Field(None, alias="autoAssignResourceModes")
    action_optimization_mode: str | None = Field(None, alias="actionOptimizationMode")
    tour_combination_mode: str | None = Field(None, alias="tourCombinationMode")
    delay_between_tours_minutes: int | None = Field(None, alias="delayBetweenToursMinutes")
    persist: bool | None = None

class ShippingUnitModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    sscc: str | None = None
    status: ShippingUnitStatusModel | None = None
    type: str | None = None
    loading_aid_type: ShipmentLoadingAidTypeModel | None = Field(None, alias="loadingAidType")
    loading_aid_quantity: int | None = Field(None, alias="loadingAidQuantity")
    actual_loading_aid_type: ShipmentLoadingAidTypeModel | None = Field(None, alias="actualLoadingAidType")
    actual_loading_aid_quantity: int | None = Field(None, alias="actualLoadingAidQuantity")
    weight: QuantityModel | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    actual_weight: QuantityModel | None = Field(None, alias="actualWeight")
    actual_width: float | None = Field(None, alias="actualWidth")
    actual_height: float | None = Field(None, alias="actualHeight")
    actual_length: float | None = Field(None, alias="actualLength")
    shipment_number: str | None = Field(None, alias="shipmentNumber")
    primary_shipment: ShipmentSubsetModel | None = Field(None, alias="primaryShipment")
    tags: list[ShippingUnitTagModel] | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    addon: dict[str, object] | None = None

class ShippingUnitStatusModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class ShippingUnitSubsetModel(BaseModel):
    id: UUID | None = None
    number: str | None = None
    sscc: str | None = None
    type: str | None = None

class ShippingUnitTagModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class SortField(BaseModel):
    path: str | None
    direction: str | None

class TariffModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    name: str | None = None
    parameters: list[TariffParameterModel] | None = None

class TariffParameterModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    type: str | None = None
    value: dict[str, object] | None = None

class TemplateTime(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    absolute_time: datetime | None = Field(None, alias="absoluteTime")
    relative_time: str | None = Field(None, alias="relativeTime")

class TemplateTimeMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class TemplateTimeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    absolute_time: datetime | None = Field(None, alias="absoluteTime")
    relative_time: str | None = Field(None, alias="relativeTime")

class TourActionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    order_id: int | None = Field(None, alias="orderId")
    date_time: datetime | None = Field(None, alias="dateTime")
    actual_date_time: datetime | None = Field(None, alias="actualDateTime")
    calculated_date_time: datetime | None = Field(None, alias="calculatedDateTime")
    mirrored_tour_number: str | None = Field(None, alias="mirroredTourNumber")
    type: str | None = None
    notes: str | None = None
    global_action_id: UUID | None = Field(None, alias="globalActionId")
    entity: TourEntityModel | None = None
    resource: ResourceModel | None = None
    address: AddressModel | None = None
    cleaning_slots: list[LoadingSlotModel] | None = Field(None, alias="cleaningSlots")
    used_loading_slots: list[LoadingSlotModel] | None = Field(None, alias="usedLoadingSlots")
    mirrored_tour_tags: list[TourTagModel] | None = Field(None, alias="mirroredTourTags")
    mirrored_tour_status: TourStatusModel | None = Field(None, alias="mirroredTourStatus")
    out_of_tour: bool | None = Field(None, alias="outOfTour")

class TourEntityModel(BaseModel):
    shipment: ShipmentModel | None = None
    cleaning: CleaningModel | None = None

class TourFromTemplateData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    start_date: datetime = Field(alias="startDate")

class TourFromTemplateRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tour_template_id: UUID = Field(alias="tourTemplateId")
    start_date: datetime | None = Field(None, alias="startDate")

class TourManipulateResponse(BaseModel):
    success: bool | None = None

class TourMetricsResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    total_distance: float | None = Field(None, alias="totalDistance")
    total_toll_distance: float | None = Field(None, alias="totalTollDistance")
    toll_cost: float | None = Field(None, alias="tollCost")
    driving_time: str | None = Field(None, alias="drivingTime")
    total_time: str | None = Field(None, alias="totalTime")
    empty_distance: float | None = Field(None, alias="emptyDistance")
    cost: float | None = None
    revenue: float | None = None

class TourModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    global_tour_id: UUID | None = Field(None, alias="globalTourId")
    number: str | None = None
    reference: str | None = None
    resource: ResourceModel | None = None
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    actual_start_date_time: datetime | None = Field(None, alias="actualStartDateTime")
    actual_end_date_time: datetime | None = Field(None, alias="actualEndDateTime")
    calculated_start_date_time: datetime | None = Field(None, alias="calculatedStartDateTime")
    calculated_end_date_time: datetime | None = Field(None, alias="calculatedEndDateTime")
    actions: list[TourActionModel] | None = None
    attached_resources: list[AttachedResourceModel] | None = Field(None, alias="attachedResources")
    attached_entities: list[AttachedEntityModel] | None = Field(None, alias="attachedEntities")
    tags: list[TourTagModel] | None = None
    transits: list[TransitModel] | None = None
    billing_lines: list[BillingLineModel] | None = Field(None, alias="billingLines")
    status: TourStatusModel | None = None
    metrics: TourMetricsResponse | None = None
    is_mirrored_tour: bool | None = Field(None, alias="isMirroredTour")
    financial_partner: BillableContactModel | None = Field(None, alias="financialPartner")
    carrier: BillableContactModel | None = None
    tariff: TariffModel | None = None
    carrier_tariff: TariffModel | None = Field(None, alias="carrierTariff")
    notes: str | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")

class TourOptimizationRequest(BaseModel):
    parameters: list[str] | None = None
    tour: CreateTourRequest | None = None

class TourReportingModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    global_tour_id: UUID | None = Field(None, alias="globalTourId")
    number: str | None = None
    reference: str | None = None
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    tractor_unit1: ResourceModel | None = Field(None, alias="tractorUnit1")
    tractor_unit2: ResourceModel | None = Field(None, alias="tractorUnit2")
    tractor_unit3: ResourceModel | None = Field(None, alias="tractorUnit3")
    trailer1: ResourceModel | None = None
    trailer2: ResourceModel | None = None
    driver1: ResourceModel | None = None
    driver2: ResourceModel | None = None
    carrier1: ResourceModel | None = None
    carrier2: ResourceModel | None = None
    container1: ResourceModel | None = None
    container2: ResourceModel | None = None
    shipments: list[ShipmentModel] | None = None
    first_shipment: ShipmentModel | None = Field(None, alias="firstShipment")
    last_shipment: ShipmentModel | None = Field(None, alias="lastShipment")
    shipment_items: list[ReportingShipmentItem] | None = Field(None, alias="shipmentItems")

class TourStatusModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class TourTagModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    internal_name: str | None = Field(None, alias="internalName")
    group_name: str | None = Field(None, alias="groupName")
    hex_color: str | None = Field(None, alias="hexColor")
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    functions: list[str] | None = None

class TourTemplateActionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    date_time: TemplateTimeModel | None = Field(None, alias="dateTime")
    entity: TourTemplateEntityModel | None = None
    resource: ResourceModel | None = None
    address: AddressModel | None = None
    used_loading_slots: list[LoadingSlotModel] | None = Field(None, alias="usedLoadingSlots")
    order_id: int | None = Field(None, alias="orderId")
    type: str | None = None
    notes: str | None = None

class TourTemplateEntityModel(BaseModel):
    shipment: ShipmentTemplateModel | None = None

class TourTemplateResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    template_name: str | None = Field(None, alias="templateName")
    reference: str | None = None
    resource: ResourceModel | None = None
    start_address: AddressModel | None = Field(None, alias="startAddress")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    start_date_time: TemplateTimeModel | None = Field(None, alias="startDateTime")
    end_date_time: TemplateTimeModel | None = Field(None, alias="endDateTime")
    time_mode: TemplateTimeMode | None = Field(None, alias="timeMode")
    actions: list[TourTemplateActionModel] | None = None
    attached_resources: list[AttachedResourceModel] | None = Field(None, alias="attachedResources")
    attached_entities: list[AttachedEntityModel] | None = Field(None, alias="attachedEntities")
    tags: list[TourTagModel] | None = None
    transits: list[TransitModel] | None = None
    metrics: TourMetricsResponse | None = None
    notes: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TransitModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    start_address: AddressModel | None = Field(None, alias="startAddress")
    start_date_time: datetime | None = Field(None, alias="startDateTime")
    end_address: AddressModel | None = Field(None, alias="endAddress")
    end_date_time: datetime | None = Field(None, alias="endDateTime")
    start_action_id: UUID | None = Field(None, alias="startActionId")
    global_start_action_id: UUID | None = Field(None, alias="globalStartActionId")
    end_action_id: UUID | None = Field(None, alias="endActionId")
    global_end_action_id: UUID | None = Field(None, alias="globalEndActionId")
    distance: int | None = None
    toll_distance: int | None = Field(None, alias="tollDistance")
    toll_costs: float | None = Field(None, alias="tollCosts")
    driving_time: str | None = Field(None, alias="drivingTime")

class UnwindStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    path: str | None
    as_: str | None = Field(None, alias="as")
    preserve_null: bool | None = Field(None, alias="preserveNull")
    include_index: str | None = Field(None, alias="includeIndex")

class UpdateAddonFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class UpdateBillingLineStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    type: str | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class UpdateResourceGroupRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    resource_ids: list[UUID] = Field(alias="resourceIds")

class UpdateResourceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    match_code: str = Field(alias="matchCode")
    display_name: str | None = Field(None, alias="displayName")
    loading_slots: list[LoadingSlotModel] | None = Field(None, alias="loadingSlots")
    location: ResourceLocationModel | None = None
    is_loadable: bool | None = Field(None, alias="isLoadable")
    planning_order_key: str | None = Field(None, alias="planningOrderKey")
    usable_until: datetime | None = Field(None, alias="usableUntil")
    notes: str | None = None

class UpdateSettingRequest(BaseModel):
    value: dict[str, object] | None = None

class UpdateShipmentItemStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class UpdateShipmentStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")
    order_nr: int | None = Field(None, alias="orderNr")
    resolver: str | None = None

class UpdateShippingUnitStatusRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    display_name: str | None = Field(None, alias="displayName")
    display_key: str | None = Field(None, alias="displayKey")
    number: str | None = None
    roles: list[str] | None = None
    hex_color: str | None = Field(None, alias="hexColor")

class UserProfileModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    e_mail: str | None = Field(None, alias="eMail")
    name: str | None = None
    phone_number: str | None = Field(None, alias="phoneNumber")

class ValidateResponse(BaseModel):
    message: str | None = None
    redundancies: int | None = None

class WeightNoteModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: str | None = None
    document_id: UUID | None = Field(None, alias="documentId")
    quantity: QuantityModel | None = None
    type: WeightNoteType | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    first_weight: QuantityModel | None = Field(None, alias="firstWeight")
    second_weight: QuantityModel | None = Field(None, alias="secondWeight")
    first_date_time: datetime | None = Field(None, alias="firstDateTime")
    second_date_time: datetime | None = Field(None, alias="secondDateTime")
    reference: str | None = None

class WeightNoteType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
