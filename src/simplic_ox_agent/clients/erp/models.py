"""Pydantic models generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from datetime import datetime

from enum import IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field

class AddBillingLinesToDraftTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    draft_transaction_id: UUID | None = Field(None, alias="draftTransactionId")
    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")

class AddBillingLinesToDraftTransactionResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    draft_transaction_result: TransactionResultModel | None = Field(None, alias="draftTransactionResult")
    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")

class AddBillingLinesToTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    transaction_id: UUID | None = Field(None, alias="transactionId")
    billing_lines: list[CreateBillingLineRequest] | None = Field(None, alias="billingLines")

class AdditionalReferencedDocumentContentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    blob: str | None = None
    file_name: str | None = Field(None, alias="fileName")

class AdditionalReferencedDocumentReferenceTypeCode(IntEnum):
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
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33

class AdditionalReferencedDocumentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str | None = None
    type: AdditionalReferencedDocumentTypeCode | None = None
    content: AdditionalReferencedDocumentContentRequest | None = None
    reference_type: AdditionalReferencedDocumentReferenceTypeCode | None = Field(None, alias="referenceType")
    name: str | None = None
    url: str | None = None
    issue_time: datetime | None = Field(None, alias="issueTime")

class AdditionalReferencedDocumentTypeCode(IntEnum):
    VALUE_50 = 50
    VALUE_130 = 130
    VALUE_916 = 916
    VALUE_65536 = 65536

class AddonFieldResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class AggregationExpression(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    function: str | None = None
    argument: QueryExpression | None = None
    is_count: bool | None = Field(None, alias="isCount")

class AmbiguousBillingLineAssignmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")
    eligible_transactions: list[TransactionModel] | None = Field(None, alias="eligibleTransactions")

class AssignmentMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class AssignmentModeModel(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class Bank(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bank_id: str | None = Field(None, alias="bankId")
    name: str | None = None

class BankAccount(BaseModel):
    name: str | None = None
    iban: str | None = None
    bic: str | None = None
    bank: Bank | None = None

class BankAccountRequest(BaseModel):
    name: str | None = None
    iban: str | None = None
    bic: str | None = None
    bank: BankRequest | None = None

class BankRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    bank_id: str | None = Field(None, alias="bankId")
    name: str | None = None

class BehaviorDefinitionModel(BaseModel):
    id: UUID | None = None
    target: str | None = None
    expression: str | None = None

class BehaviorDefinitionRequest(BaseModel):
    id: UUID | None = None
    target: str | None = None
    expression: str | None = None

class BillingLineModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    financial_partner: TransactionContactModel | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    text: str | None = None
    source_text: str | None = Field(None, alias="sourceText")
    quantity: BillingLineQuantityModel | None = None
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    cost_centers: list[CostCenterAssignmentModel] | None = Field(None, alias="costCenters")
    cost_objects: list[CostCenterAssignmentModel] | None = Field(None, alias="costObjects")
    tax_rate: TaxRateModel | None = Field(None, alias="taxRate")
    general_ledger_account_group: TransactionGeneralLedgerAccountGroupModel | None = Field(None, alias="generalLedgerAccountGroup")
    reference: str | None = None
    references: list[BillingLineReferenceModel] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    state: BillingLineState | None = None
    addon: dict[str, object] | None = None
    assigned_transaction_id: UUID | None = Field(None, alias="assignedTransactionId")
    source_billing_line_reference: SourceBillingLineReferenceModel | None = Field(None, alias="sourceBillingLineReference")

class BillingLineQuantityModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    quantity_unit: QuantityUnitModel | None = Field(None, alias="quantityUnit")
    price_unit: QuantityUnitModel | None = Field(None, alias="priceUnit")

class BillingLineQuantityRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    quantity_unit_id: UUID | None = Field(None, alias="quantityUnitId")
    price_unit_id: UUID | None = Field(None, alias="priceUnitId")

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

class BillingLineResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_line: BillingLineModel | None = Field(None, alias="billingLine")
    errors: list[LocalizableErrorModel] | None = None

class BillingLineState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class BillingPeriodRequest(BaseModel):
    start: datetime | None = None
    end: datetime | None = None

class ConvertDraftTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    target_type_id: UUID = Field(alias="targetTypeId")
    target_subtype_id: UUID | None = Field(None, alias="targetSubtypeId")

class ConvertResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    transaction: TransactionModel | None = None
    errors: list[LocalizableErrorModel] | None = None
    convert_states: dict[str, TransactionConvertState] | None = Field(None, alias="convertStates")

class ConvertTransactionsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    transaction_subsets: dict[str, dict[str, float]] = Field(alias="transactionSubsets")
    target_type_id: UUID = Field(alias="targetTypeId")
    commit: bool
    target_subtype_id: UUID | None = Field(None, alias="targetSubtypeId")
    check_compatible_properties: list[str] | None = Field(None, alias="checkCompatibleProperties")

class CostCenterAssignmentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cost_center: TransactionItemCostCenterModel | None = Field(None, alias="costCenter")
    percentage: float | None = None

class CostCenterAssignmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    cost_center_id: UUID | None = Field(None, alias="costCenterId")
    percentage: float | None = None
    _remove: bool | None = None

class CountryCode(IntEnum):
    VALUE_0 = 0
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_16 = 16
    VALUE_20 = 20
    VALUE_24 = 24
    VALUE_28 = 28
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_36 = 36
    VALUE_40 = 40
    VALUE_44 = 44
    VALUE_48 = 48
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_56 = 56
    VALUE_60 = 60
    VALUE_64 = 64
    VALUE_68 = 68
    VALUE_70 = 70
    VALUE_72 = 72
    VALUE_74 = 74
    VALUE_76 = 76
    VALUE_84 = 84
    VALUE_86 = 86
    VALUE_90 = 90
    VALUE_92 = 92
    VALUE_96 = 96
    VALUE_100 = 100
    VALUE_104 = 104
    VALUE_108 = 108
    VALUE_112 = 112
    VALUE_116 = 116
    VALUE_120 = 120
    VALUE_124 = 124
    VALUE_132 = 132
    VALUE_136 = 136
    VALUE_140 = 140
    VALUE_144 = 144
    VALUE_148 = 148
    VALUE_152 = 152
    VALUE_156 = 156
    VALUE_158 = 158
    VALUE_162 = 162
    VALUE_166 = 166
    VALUE_170 = 170
    VALUE_174 = 174
    VALUE_175 = 175
    VALUE_178 = 178
    VALUE_180 = 180
    VALUE_184 = 184
    VALUE_188 = 188
    VALUE_191 = 191
    VALUE_192 = 192
    VALUE_196 = 196
    VALUE_203 = 203
    VALUE_204 = 204
    VALUE_208 = 208
    VALUE_212 = 212
    VALUE_214 = 214
    VALUE_218 = 218
    VALUE_222 = 222
    VALUE_226 = 226
    VALUE_231 = 231
    VALUE_232 = 232
    VALUE_233 = 233
    VALUE_234 = 234
    VALUE_238 = 238
    VALUE_239 = 239
    VALUE_242 = 242
    VALUE_246 = 246
    VALUE_248 = 248
    VALUE_250 = 250
    VALUE_254 = 254
    VALUE_258 = 258
    VALUE_260 = 260
    VALUE_262 = 262
    VALUE_266 = 266
    VALUE_268 = 268
    VALUE_270 = 270
    VALUE_275 = 275
    VALUE_276 = 276
    VALUE_288 = 288
    VALUE_292 = 292
    VALUE_296 = 296
    VALUE_300 = 300
    VALUE_304 = 304
    VALUE_308 = 308
    VALUE_312 = 312
    VALUE_316 = 316
    VALUE_320 = 320
    VALUE_324 = 324
    VALUE_328 = 328
    VALUE_332 = 332
    VALUE_334 = 334
    VALUE_336 = 336
    VALUE_340 = 340
    VALUE_344 = 344
    VALUE_348 = 348
    VALUE_352 = 352
    VALUE_356 = 356
    VALUE_360 = 360
    VALUE_364 = 364
    VALUE_368 = 368
    VALUE_372 = 372
    VALUE_376 = 376
    VALUE_380 = 380
    VALUE_384 = 384
    VALUE_388 = 388
    VALUE_392 = 392
    VALUE_398 = 398
    VALUE_400 = 400
    VALUE_404 = 404
    VALUE_408 = 408
    VALUE_410 = 410
    VALUE_414 = 414
    VALUE_417 = 417
    VALUE_418 = 418
    VALUE_422 = 422
    VALUE_426 = 426
    VALUE_428 = 428
    VALUE_430 = 430
    VALUE_434 = 434
    VALUE_438 = 438
    VALUE_440 = 440
    VALUE_442 = 442
    VALUE_446 = 446
    VALUE_450 = 450
    VALUE_454 = 454
    VALUE_458 = 458
    VALUE_462 = 462
    VALUE_466 = 466
    VALUE_470 = 470
    VALUE_474 = 474
    VALUE_478 = 478
    VALUE_480 = 480
    VALUE_484 = 484
    VALUE_492 = 492
    VALUE_496 = 496
    VALUE_498 = 498
    VALUE_499 = 499
    VALUE_500 = 500
    VALUE_504 = 504
    VALUE_508 = 508
    VALUE_512 = 512
    VALUE_516 = 516
    VALUE_520 = 520
    VALUE_524 = 524
    VALUE_528 = 528
    VALUE_531 = 531
    VALUE_533 = 533
    VALUE_534 = 534
    VALUE_535 = 535
    VALUE_540 = 540
    VALUE_548 = 548
    VALUE_554 = 554
    VALUE_558 = 558
    VALUE_562 = 562
    VALUE_566 = 566
    VALUE_570 = 570
    VALUE_574 = 574
    VALUE_578 = 578
    VALUE_580 = 580
    VALUE_581 = 581
    VALUE_583 = 583
    VALUE_584 = 584
    VALUE_585 = 585
    VALUE_586 = 586
    VALUE_591 = 591
    VALUE_598 = 598
    VALUE_600 = 600
    VALUE_604 = 604
    VALUE_608 = 608
    VALUE_612 = 612
    VALUE_616 = 616
    VALUE_620 = 620
    VALUE_624 = 624
    VALUE_626 = 626
    VALUE_630 = 630
    VALUE_634 = 634
    VALUE_638 = 638
    VALUE_642 = 642
    VALUE_643 = 643
    VALUE_646 = 646
    VALUE_652 = 652
    VALUE_654 = 654
    VALUE_659 = 659
    VALUE_660 = 660
    VALUE_662 = 662
    VALUE_663 = 663
    VALUE_666 = 666
    VALUE_670 = 670
    VALUE_674 = 674
    VALUE_678 = 678
    VALUE_682 = 682
    VALUE_686 = 686
    VALUE_688 = 688
    VALUE_690 = 690
    VALUE_694 = 694
    VALUE_702 = 702
    VALUE_703 = 703
    VALUE_704 = 704
    VALUE_705 = 705
    VALUE_706 = 706
    VALUE_710 = 710
    VALUE_716 = 716
    VALUE_724 = 724
    VALUE_728 = 728
    VALUE_729 = 729
    VALUE_732 = 732
    VALUE_740 = 740
    VALUE_744 = 744
    VALUE_748 = 748
    VALUE_752 = 752
    VALUE_756 = 756
    VALUE_760 = 760
    VALUE_762 = 762
    VALUE_764 = 764
    VALUE_768 = 768
    VALUE_772 = 772
    VALUE_776 = 776
    VALUE_780 = 780
    VALUE_784 = 784
    VALUE_788 = 788
    VALUE_792 = 792
    VALUE_795 = 795
    VALUE_796 = 796
    VALUE_798 = 798
    VALUE_800 = 800
    VALUE_804 = 804
    VALUE_807 = 807
    VALUE_818 = 818
    VALUE_826 = 826
    VALUE_831 = 831
    VALUE_832 = 832
    VALUE_833 = 833
    VALUE_834 = 834
    VALUE_840 = 840
    VALUE_850 = 850
    VALUE_854 = 854
    VALUE_858 = 858
    VALUE_860 = 860
    VALUE_862 = 862
    VALUE_876 = 876
    VALUE_882 = 882
    VALUE_887 = 887
    VALUE_894 = 894
    VALUE_999 = 999

class CreateAddonFieldRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    object_name: str | None = Field(None, alias="objectName")
    property_name: str | None = Field(None, alias="propertyName")
    property_type: str | None = Field(None, alias="propertyType")
    description: str | None = None

class CreateBillingLineRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    financial_partner: TransactionContactRequest | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    text: str | None = None
    source_text: str | None = Field(None, alias="sourceText")
    quantity: BillingLineQuantityRequest | None = None
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    general_ledger_account_group_id: UUID | None = Field(None, alias="generalLedgerAccountGroupId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    addon: dict[str, object] | None = None
    source_billing_line_reference: SourceBillingLineReferenceRequest | None = Field(None, alias="sourceBillingLineReference")

class CreateDraftTransactionsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")
    target: SplitTarget | None = None
    split_configuration_id: UUID | None = Field(None, alias="splitConfigurationId")

class CreateElectronicInvoiceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    pdf: str | None = None
    profile: Profile | None = None
    version: ZUGFeRDVersion | None = None
    rounding_mode: RoundingMode | None = Field(None, alias="roundingMode")
    electronic_invoice_type: ElectronicInvoiceType | None = Field(None, alias="electronicInvoiceType")
    add_peppol_address: bool | None = Field(None, alias="addPeppolAddress")
    leitweg_id_required: bool | None = Field(None, alias="leitwegIdRequired")
    invoice_data: InvoiceDataRequest | None = Field(None, alias="invoiceData")

class CreatePersonalAccountRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    address_contact_ids: list[UUID] | None = Field(None, alias="addressContactIds")
    sale_terms_of_payment_id: UUID | None = Field(None, alias="saleTermsOfPaymentId")
    purchase_terms_of_payment_id: UUID | None = Field(None, alias="purchaseTermsOfPaymentId")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    personal_account_group_id: UUID | None = Field(None, alias="personalAccountGroupId")
    number: str | None = None
    vat_id: str | None = Field(None, alias="vatId")
    type: str | None = None
    credit_limit: CreditLimitModel | None = Field(None, alias="creditLimit")

class CreateSplitConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    name: str | None = None
    split_definitions: list[SplitDefinition] | None = Field(None, alias="splitDefinitions")

class CreateTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str
    type_id: UUID = Field(alias="typeId")
    subtype_id: UUID = Field(alias="subtypeId")
    is_gross: bool = Field(alias="isGross")
    creator: TransactionContactRequest | None = None
    reference: str | None = None
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    terms_of_payment_id: UUID | None = Field(None, alias="termsOfPaymentId")
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    currency_id: UUID | None = Field(None, alias="currencyId")
    description: str | None = None
    financial_partner: TransactionContactRequest | None = Field(None, alias="financialPartner")
    delivery_address: TransactionContactRequest | None = Field(None, alias="deliveryAddress")
    invoice_recipient: TransactionContactRequest | None = Field(None, alias="invoiceRecipient")
    payer: TransactionContactRequest | None = None
    responsible: TransactionContactRequest | None = None
    representative: TransactionContactRequest | None = None
    items: list[TransactionItemRequest] | None = None
    alternative_payment_deadline: datetime | None = Field(None, alias="alternativePaymentDeadline")
    balance: float | None = None
    barcode: str | None = None
    bill_to_text: str | None = Field(None, alias="billToText")
    cash_discount_percent_value: float | None = Field(None, alias="cashDiscountPercentValue")
    cash_discount_total: float | None = Field(None, alias="cashDiscountTotal")
    financial_accounting_period_id: UUID | None = Field(None, alias="financialAccountingPeriodId")
    period_id: UUID | None = Field(None, alias="periodId")
    manual_vat: TransactionManualVatRequest | None = Field(None, alias="manualVAT")
    notes: str | None = None
    due_date: datetime | None = Field(None, alias="dueDate")
    reference_number: str | None = Field(None, alias="referenceNumber")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    operation_item_combination_mode: OperationItemCombinationModeModel | None = Field(None, alias="operationItemCombinationMode")
    financial_export_disabled: bool | None = Field(None, alias="financialExportDisabled")
    default_cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostCenters")
    default_cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostObjects")
    metadata_processing_data: MetadataProcessingDataRequest | None = Field(None, alias="metadataProcessingData")

class CreditLimitModel(BaseModel):
    insurance: float | None = None
    creditworthiness: str | None = None
    limit: str | None = None

class CurrencyCode(IntEnum):
    VALUE_0 = 0
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_12 = 12
    VALUE_20 = 20
    VALUE_24 = 24
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_36 = 36
    VALUE_40 = 40
    VALUE_44 = 44
    VALUE_48 = 48
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_56 = 56
    VALUE_60 = 60
    VALUE_64 = 64
    VALUE_68 = 68
    VALUE_70 = 70
    VALUE_72 = 72
    VALUE_76 = 76
    VALUE_84 = 84
    VALUE_90 = 90
    VALUE_96 = 96
    VALUE_100 = 100
    VALUE_104 = 104
    VALUE_108 = 108
    VALUE_112 = 112
    VALUE_116 = 116
    VALUE_124 = 124
    VALUE_132 = 132
    VALUE_136 = 136
    VALUE_144 = 144
    VALUE_152 = 152
    VALUE_156 = 156
    VALUE_170 = 170
    VALUE_174 = 174
    VALUE_180 = 180
    VALUE_188 = 188
    VALUE_191 = 191
    VALUE_192 = 192
    VALUE_196 = 196
    VALUE_200 = 200
    VALUE_203 = 203
    VALUE_208 = 208
    VALUE_214 = 214
    VALUE_218 = 218
    VALUE_222 = 222
    VALUE_226 = 226
    VALUE_230 = 230
    VALUE_232 = 232
    VALUE_233 = 233
    VALUE_238 = 238
    VALUE_242 = 242
    VALUE_246 = 246
    VALUE_250 = 250
    VALUE_262 = 262
    VALUE_268 = 268
    VALUE_270 = 270
    VALUE_276 = 276
    VALUE_278 = 278
    VALUE_288 = 288
    VALUE_292 = 292
    VALUE_300 = 300
    VALUE_320 = 320
    VALUE_324 = 324
    VALUE_328 = 328
    VALUE_332 = 332
    VALUE_340 = 340
    VALUE_344 = 344
    VALUE_348 = 348
    VALUE_352 = 352
    VALUE_356 = 356
    VALUE_360 = 360
    VALUE_364 = 364
    VALUE_368 = 368
    VALUE_372 = 372
    VALUE_376 = 376
    VALUE_380 = 380
    VALUE_388 = 388
    VALUE_392 = 392
    VALUE_398 = 398
    VALUE_400 = 400
    VALUE_404 = 404
    VALUE_408 = 408
    VALUE_410 = 410
    VALUE_414 = 414
    VALUE_417 = 417
    VALUE_418 = 418
    VALUE_422 = 422
    VALUE_426 = 426
    VALUE_428 = 428
    VALUE_430 = 430
    VALUE_434 = 434
    VALUE_440 = 440
    VALUE_442 = 442
    VALUE_446 = 446
    VALUE_450 = 450
    VALUE_454 = 454
    VALUE_458 = 458
    VALUE_462 = 462
    VALUE_466 = 466
    VALUE_470 = 470
    VALUE_478 = 478
    VALUE_480 = 480
    VALUE_484 = 484
    VALUE_496 = 496
    VALUE_498 = 498
    VALUE_504 = 504
    VALUE_508 = 508
    VALUE_512 = 512
    VALUE_516 = 516
    VALUE_524 = 524
    VALUE_528 = 528
    VALUE_532 = 532
    VALUE_533 = 533
    VALUE_548 = 548
    VALUE_554 = 554
    VALUE_558 = 558
    VALUE_566 = 566
    VALUE_578 = 578
    VALUE_586 = 586
    VALUE_590 = 590
    VALUE_598 = 598
    VALUE_600 = 600
    VALUE_604 = 604
    VALUE_608 = 608
    VALUE_616 = 616
    VALUE_620 = 620
    VALUE_624 = 624
    VALUE_626 = 626
    VALUE_634 = 634
    VALUE_642 = 642
    VALUE_643 = 643
    VALUE_646 = 646
    VALUE_654 = 654
    VALUE_678 = 678
    VALUE_682 = 682
    VALUE_690 = 690
    VALUE_694 = 694
    VALUE_702 = 702
    VALUE_703 = 703
    VALUE_704 = 704
    VALUE_705 = 705
    VALUE_706 = 706
    VALUE_710 = 710
    VALUE_716 = 716
    VALUE_720 = 720
    VALUE_724 = 724
    VALUE_728 = 728
    VALUE_736 = 736
    VALUE_740 = 740
    VALUE_748 = 748
    VALUE_752 = 752
    VALUE_756 = 756
    VALUE_760 = 760
    VALUE_762 = 762
    VALUE_764 = 764
    VALUE_776 = 776
    VALUE_780 = 780
    VALUE_784 = 784
    VALUE_788 = 788
    VALUE_792 = 792
    VALUE_795 = 795
    VALUE_800 = 800
    VALUE_804 = 804
    VALUE_807 = 807
    VALUE_810 = 810
    VALUE_818 = 818
    VALUE_826 = 826
    VALUE_834 = 834
    VALUE_840 = 840
    VALUE_858 = 858
    VALUE_860 = 860
    VALUE_862 = 862
    VALUE_882 = 882
    VALUE_886 = 886
    VALUE_890 = 890
    VALUE_891 = 891
    VALUE_894 = 894
    VALUE_901 = 901
    VALUE_927 = 927
    VALUE_928 = 928
    VALUE_929 = 929
    VALUE_930 = 930
    VALUE_931 = 931
    VALUE_932 = 932
    VALUE_933 = 933
    VALUE_934 = 934
    VALUE_935 = 935
    VALUE_936 = 936
    VALUE_937 = 937
    VALUE_938 = 938
    VALUE_939 = 939
    VALUE_940 = 940
    VALUE_941 = 941
    VALUE_942 = 942
    VALUE_943 = 943
    VALUE_944 = 944
    VALUE_945 = 945
    VALUE_946 = 946
    VALUE_947 = 947
    VALUE_948 = 948
    VALUE_949 = 949
    VALUE_950 = 950
    VALUE_951 = 951
    VALUE_952 = 952
    VALUE_953 = 953
    VALUE_954 = 954
    VALUE_955 = 955
    VALUE_956 = 956
    VALUE_957 = 957
    VALUE_958 = 958
    VALUE_959 = 959
    VALUE_960 = 960
    VALUE_961 = 961
    VALUE_962 = 962
    VALUE_963 = 963
    VALUE_964 = 964
    VALUE_965 = 965
    VALUE_967 = 967
    VALUE_968 = 968
    VALUE_969 = 969
    VALUE_970 = 970
    VALUE_971 = 971
    VALUE_972 = 972
    VALUE_973 = 973
    VALUE_974 = 974
    VALUE_975 = 975
    VALUE_976 = 976
    VALUE_977 = 977
    VALUE_978 = 978
    VALUE_979 = 979
    VALUE_980 = 980
    VALUE_981 = 981
    VALUE_982 = 982
    VALUE_983 = 983
    VALUE_984 = 984
    VALUE_985 = 985
    VALUE_986 = 986
    VALUE_987 = 987
    VALUE_988 = 988
    VALUE_989 = 989
    VALUE_990 = 990
    VALUE_991 = 991
    VALUE_992 = 992
    VALUE_993 = 993
    VALUE_994 = 994
    VALUE_995 = 995
    VALUE_996 = 996
    VALUE_997 = 997
    VALUE_998 = 998
    VALUE_999 = 999

class CurrencyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: int | None = None
    name: str | None = None
    short_name: str | None = Field(None, alias="shortName")
    symbol: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class CurrencyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int
    name: str
    short_name: str = Field(alias="shortName")
    symbol: str

class DateTruncExpression(BaseModel):
    path: str | None
    unit: str | None

class DiscountSurchargeMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class DiscountSurchargeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    discount_surcharge_type: DiscountSurchargeType | None = Field(None, alias="discountSurchargeType")
    discount_surcharge_mode: DiscountSurchargeMode | None = Field(None, alias="discountSurchargeMode")
    description: str | None = None
    delta_value_absolute: float | None = Field(None, alias="deltaValueAbsolute")
    delta_value_relative: float | None = Field(None, alias="deltaValueRelative")

class DiscountSurchargeType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class DistributeBillingLinesToDraftTransactionsRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")
    pinned_transaction_ids: dict[str, UUID] | None = Field(None, alias="pinnedTransactionIds")
    split_configuration_id: UUID | None = Field(None, alias="splitConfigurationId")

class DistributeBillingLinesToDraftTransactionsResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    draft_transaction_results: list[AddBillingLinesToDraftTransactionResultModel] | None = Field(None, alias="draftTransactionResults")
    ambiguous_assignments: list[AmbiguousBillingLineAssignmentModel] | None = Field(None, alias="ambiguousAssignments")
    errors: list[LocalizableErrorModel] | None = None

class DraftTransactionsResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    draft_transaction_results: list[TransactionResultModel] | None = Field(None, alias="draftTransactionResults")

class DueDateMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class ElectronicAddressType(IntEnum):
    VALUE_88 = 88
    VALUE_204 = 204
    VALUE_9910 = 9910
    VALUE_9922 = 9922
    VALUE_9923 = 9923
    VALUE_9924 = 9924
    VALUE_9925 = 9925
    VALUE_9926 = 9926
    VALUE_9927 = 9927
    VALUE_9928 = 9928
    VALUE_9929 = 9929
    VALUE_9930 = 9930
    VALUE_9931 = 9931
    VALUE_9932 = 9932
    VALUE_9933 = 9933
    VALUE_9934 = 9934
    VALUE_9935 = 9935
    VALUE_9936 = 9936
    VALUE_9937 = 9937
    VALUE_9938 = 9938
    VALUE_9939 = 9939
    VALUE_9940 = 9940
    VALUE_9941 = 9941
    VALUE_9942 = 9942
    VALUE_9943 = 9943
    VALUE_9944 = 9944
    VALUE_9945 = 9945
    VALUE_9946 = 9946
    VALUE_9947 = 9947
    VALUE_9948 = 9948
    VALUE_9949 = 9949
    VALUE_9950 = 9950
    VALUE_9951 = 9951
    VALUE_9952 = 9952
    VALUE_9953 = 9953
    VALUE_9955 = 9955
    VALUE_9956 = 9956
    VALUE_9957 = 9957
    VALUE_9958 = 9958
    VALUE_9959 = 9959
    VALUE_9960 = 9960
    VALUE_9961 = 9961
    VALUE_9962 = 9962
    VALUE_9963 = 9963
    VALUE_9964 = 9964

class ElectronicInvoiceCreateResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    electronic_invoice: str | None = Field(None, alias="electronicInvoice")
    validation_result: InvoiceValidationResult | None = Field(None, alias="validationResult")

class ElectronicInvoiceImportResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    invoice_data: ImportedInvoiceData | None = Field(None, alias="invoiceData")
    validation_result: InvoiceValidationResult | None = Field(None, alias="validationResult")
    xml: str | None = None

class ElectronicInvoiceType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ElectronicInvoicingPaymentMethodRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: PaymentMethodType | None = None
    description: str | None = None
    sepa_creditor_identifier: str | None = Field(None, alias="sepaCreditorIdentifier")
    sepa_mandate_reference: str | None = Field(None, alias="sepaMandateReference")
    card_number: str | None = Field(None, alias="cardNumber")
    card_holder_name: str | None = Field(None, alias="cardHolderName")

class ElectronicInvoicingTermsOfPaymentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = None
    payment_due: datetime | None = Field(None, alias="paymentDue")

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

class ExportCostQuantityType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

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

class FiscalYearModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: int | None = None
    name: str | None = None
    from_: datetime | None = Field(None, alias="from")
    to: datetime | None = None
    periods: list[PeriodModel] | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class FiscalYearRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int
    name: str
    from_: datetime = Field(alias="from")
    to: datetime
    periods: list[PeriodRequest]

class FiscalYearResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fiscal_year: FiscalYearModel | None = Field(None, alias="fiscalYear")
    errors: list[LocalizableErrorModel] | None = None

class GroupByField(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    as_: str | None = Field(alias="as")
    path: str | None = None
    date_trunc: DateTruncExpression | None = Field(None, alias="dateTrunc")

class GroupStage(BaseModel):
    by: list[GroupByField] | None
    fields: dict[str, AggregationExpression] | None

class GrpcDefinitions(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    package: str | None = None
    service: str | None = None
    proto_file: str | None = Field(None, alias="protoFile")

class ImportElectronicInvoiceRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    file_to_import: str | None = Field(None, alias="fileToImport")

class ImportedBillingPeriod(BaseModel):
    start: datetime | None = None
    end: datetime | None = None

class ImportedDiscountSurcharge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    discount_surcharge_type: DiscountSurchargeType | None = Field(None, alias="discountSurchargeType")
    description: str | None = None
    basis_amount: float | None = Field(None, alias="basisAmount")
    discount_surcharge_amount: float | None = Field(None, alias="discountSurchargeAmount")

class ImportedInvoiceData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    invoice_date: datetime | None = Field(None, alias="invoiceDate")
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    billing_period: ImportedBillingPeriod | None = Field(None, alias="billingPeriod")
    currency: CurrencyCode | None = None
    totals: ImportedTotals | None = None
    business_process: str | None = Field(None, alias="businessProcess")
    reference_number: str | None = Field(None, alias="referenceNumber")
    buyer_reference: str | None = Field(None, alias="buyerReference")
    buyer: ImportedParty | None = None
    seller: ImportedParty | None = None
    debitor_bank_accounts: list[BankAccount] | None = Field(None, alias="debitorBankAccounts")
    creditor_bank_accounts: list[BankAccount] | None = Field(None, alias="creditorBankAccounts")
    notes: list[str] | None = None
    payment_method: PaymentMethod | None = Field(None, alias="paymentMethod")
    terms_of_payment: TermsOfPayment | None = Field(None, alias="termsOfPayment")
    taxes: list[ImportedTax] | None = None
    type: InvoiceType | None = None
    text_items: list[ImportedInvoiceItemText] | None = Field(None, alias="textItems")
    billable_items: list[ImportedInvoiceItemBillable] | None = Field(None, alias="billableItems")
    discounts_surcharges: list[ImportedInvoiceDiscountSurcharge] | None = Field(None, alias="discountsSurcharges")

class ImportedInvoiceDiscountSurcharge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    discount_surcharge_type: DiscountSurchargeType | None = Field(None, alias="discountSurchargeType")
    description: str | None = None
    basis_amount: float | None = Field(None, alias="basisAmount")
    discount_surcharge_amount: float | None = Field(None, alias="discountSurchargeAmount")
    tax_type: TaxType | None = Field(None, alias="taxType")
    tax_category: TaxCategory | None = Field(None, alias="taxCategory")
    tax_rate: float | None = Field(None, alias="taxRate")

class ImportedInvoiceItemBillable(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str | None = None
    text: str | None = None
    quantity_unit: QuantityCode | None = Field(None, alias="quantityUnit")
    article_name: str | None = Field(None, alias="articleName")
    quantity: float | None = None
    tax_type: TaxType | None = Field(None, alias="taxType")
    tax_category: TaxCategory | None = Field(None, alias="taxCategory")
    discounts_surcharges: list[ImportedDiscountSurcharge] | None = Field(None, alias="discountsSurcharges")
    tax_rate: float | None = Field(None, alias="taxRate")
    single_price_net_base: float | None = Field(None, alias="singlePriceNetBase")
    single_price_net: float | None = Field(None, alias="singlePriceNet")
    total_price_net: float | None = Field(None, alias="totalPriceNet")

class ImportedInvoiceItemText(BaseModel):
    id: str | None = None
    text: str | None = None

class ImportedParty(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_name: str | None = Field(None, alias="contactName")
    company_name: str | None = Field(None, alias="companyName")
    zipcode: str | None = None
    city: str | None = None
    street: str | None = None
    country: CountryCode | None = None
    email_address: str | None = Field(None, alias="emailAddress")
    phone_number: str | None = Field(None, alias="phoneNumber")
    fax_number: str | None = Field(None, alias="faxNumber")
    tax_registrations: list[TaxRegistration] | None = Field(None, alias="taxRegistrations")
    electronic_address_type: ElectronicAddressType | None = Field(None, alias="electronicAddressType")

class ImportedTax(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: TaxType | None = None
    category: TaxCategory | None = None
    rate: float | None = None
    basis_amount: float | None = Field(None, alias="basisAmount")
    tax_amount: float | None = Field(None, alias="taxAmount")

class ImportedTotals(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    total_price_net: float | None = Field(None, alias="totalPriceNet")
    total_price_net_without_invoice_discounts_surcharges: float | None = Field(None, alias="totalPriceNetWithoutInvoiceDiscountsSurcharges")
    total_price_gross: float | None = Field(None, alias="totalPriceGross")
    total_price_tax: float | None = Field(None, alias="totalPriceTax")
    total_price_discount: float | None = Field(None, alias="totalPriceDiscount")
    total_price_surcharge: float | None = Field(None, alias="totalPriceSurcharge")

class InputPriceType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class InvoiceDataRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    invoice_date: datetime | None = Field(None, alias="invoiceDate")
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    billing_period: BillingPeriodRequest | None = Field(None, alias="billingPeriod")
    currency: CurrencyCode | None = None
    business_process: str | None = Field(None, alias="businessProcess")
    reference_number: str | None = Field(None, alias="referenceNumber")
    buyer_reference: str | None = Field(None, alias="buyerReference")
    buyer: PartyRequest | None = None
    seller: PartyRequest | None = None
    debitor_bank_accounts: list[BankAccountRequest] | None = Field(None, alias="debitorBankAccounts")
    creditor_bank_accounts: list[BankAccountRequest] | None = Field(None, alias="creditorBankAccounts")
    notes: list[str] | None = None
    payment_method: ElectronicInvoicingPaymentMethodRequest | None = Field(None, alias="paymentMethod")
    terms_of_payment: ElectronicInvoicingTermsOfPaymentRequest | None = Field(None, alias="termsOfPayment")
    taxes: list[TaxRequest] | None = None
    type: InvoiceType | None = None
    items: list[InvoiceItemRequest] | None = None
    additional_referenced_documents: list[AdditionalReferencedDocumentRequest] | None = Field(None, alias="additionalReferencedDocuments")

class InvoiceItemRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str | None = None
    text: str | None = None
    quantity_unit: QuantityCode | None = Field(None, alias="quantityUnit")
    article_name: str | None = Field(None, alias="articleName")
    single_price_net_base: float | None = Field(None, alias="singlePriceNetBase")
    total_price_net_base: float | None = Field(None, alias="totalPriceNetBase")
    quantity: float | None = None
    tax_type: TaxType | None = Field(None, alias="taxType")
    tax_category: TaxCategory | None = Field(None, alias="taxCategory")
    discounts_surcharges: list[DiscountSurchargeRequest] | None = Field(None, alias="discountsSurcharges")

class InvoiceType(IntEnum):
    VALUE_0 = 0
    VALUE_84 = 84
    VALUE_261 = 261
    VALUE_326 = 326
    VALUE_380 = 380
    VALUE_381 = 381
    VALUE_383 = 383
    VALUE_384 = 384
    VALUE_386 = 386
    VALUE_389 = 389
    VALUE_457 = 457
    VALUE_751 = 751
    VALUE_875 = 875
    VALUE_876 = 876
    VALUE_877 = 877
    VALUE_1380 = 1380

class InvoiceValidationResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    validation_errors: list[str] | None = Field(None, alias="validationErrors")
    valid: bool | None = None

class LocalizableErrorModel(BaseModel):
    key: str | None = None
    code: str | None = None
    params: dict[str, object] | None = None

class LockBillingLineResultModel(BaseModel):
    locked: bool | None = None
    errors: list[LocalizableErrorModel] | None = None

class LookupStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_: str | None = Field(alias="from")
    local_path: str | None = Field(alias="localPath")
    foreign_path: str | None = Field(alias="foreignPath")
    as_: str | None = Field(alias="as")

class MatchStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    and_: list[FilterCondition] | None = Field(None, alias="and")
    or_: list[FilterCondition] | None = Field(None, alias="or")
    not_: FilterCondition | None = Field(None, alias="not")
    condition: FilterCondition | None = None

class MetadataProcessingDataModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    check_sum: float | None = Field(None, alias="checkSum")

class MetadataProcessingDataRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    check_sum: float | None = Field(None, alias="checkSum")

class OperationItemCombinationModeModel(IntEnum):
    VALUE_0 = 0

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

class PartyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_name: str | None = Field(None, alias="contactName")
    company_name: str | None = Field(None, alias="companyName")
    zipcode: str | None = None
    city: str | None = None
    street: str | None = None
    country: CountryCode | None = None
    email_address: str | None = Field(None, alias="emailAddress")
    phone_number: str | None = Field(None, alias="phoneNumber")
    fax_number: str | None = Field(None, alias="faxNumber")
    tax_registrations: list[TaxRegistrationRequest] | None = Field(None, alias="taxRegistrations")
    electronic_address_type: ElectronicAddressType | None = Field(None, alias="electronicAddressType")

class PaymentMethod(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: PaymentMethodType | None = None
    description: str | None = None
    sepa_creditor_identifier: str | None = Field(None, alias="sepaCreditorIdentifier")
    sepa_mandate_reference: str | None = Field(None, alias="sepaMandateReference")
    card_number: str | None = Field(None, alias="cardNumber")
    card_holder_name: str | None = Field(None, alias="cardHolderName")

class PaymentMethodModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: int | None = None
    name: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class PaymentMethodRequest(BaseModel):
    number: int
    name: str

class PaymentMethodType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_3 = 3
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_42 = 42
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_97 = 97

class PeriodModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: int | None = None
    name: str | None = None
    from_: datetime | None = Field(None, alias="from")
    to: datetime | None = None
    status: PeriodStatus | None = None

class PeriodRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: int | None = None
    name: str | None = None
    from_: datetime | None = Field(None, alias="from")
    to: datetime | None = None
    status: PeriodStatus | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")

class PeriodStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class PersonalAccountAddressModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contact_id: UUID | None = Field(None, alias="contactId")
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
    latitude: float | None = None
    longitude: float | None = None

class PersonalAccountGroupModel(BaseModel):
    id: UUID | None = None
    number: str | None = None
    name: str | None = None

class PersonalAccountGroupRequest(BaseModel):
    number: str | None = None
    name: str | None = None

class PersonalAccountGroupSubsetModel(BaseModel):
    id: UUID | None = None
    number: str | None = None
    name: str | None = None

class PersonalAccountModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    vat_id: str | None = Field(None, alias="vatId")
    type: str | None = None
    credit_limit: CreditLimitModel | None = Field(None, alias="creditLimit")
    sale_terms_of_payment: TermsOfPaymentModel | None = Field(None, alias="saleTermsOfPayment")
    purchase_terms_of_payment: TermsOfPaymentModel | None = Field(None, alias="purchaseTermsOfPayment")
    tax_group: TaxGroupModel | None = Field(None, alias="taxGroup")
    personal_account_group: PersonalAccountGroupSubsetModel | None = Field(None, alias="personalAccountGroup")
    addresses: list[PersonalAccountAddressModel] | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class PipelineStage(BaseModel):
    match: MatchStage | None = None
    lookup: LookupStage | None = None
    resolve: ResolveStage | None = None
    unwind: UnwindStage | None = None
    group: GroupStage | None = None
    project: ProjectStage | None = None
    sort: list[SortField] | None = None
    page: PageStage | None = None

class PreviewItemCostCenterAssignmentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    temporary_item_id: UUID | None = Field(None, alias="temporaryItemId")
    cost_center_id: UUID | None = Field(None, alias="costCenterId")
    percentage: float | None = None

class PreviewTransactionItemRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    temporary_id: UUID | None = Field(None, alias="temporaryId")
    id: UUID | None = None
    text: str | None = None
    type_id: UUID | None = Field(None, alias="typeId")
    sort_number: int | None = Field(None, alias="sortNumber")
    deserialization_type: str | None = Field(None, alias="deserializationType")
    value_operator: ValueOperator | None = Field(None, alias="valueOperator")
    assignment_mode: AssignmentMode | None = Field(None, alias="assignmentMode")
    behavior_definitions: list[BehaviorDefinitionRequest] | None = Field(None, alias="behaviorDefinitions")
    quantity: QuantityRequest | None = None
    input_price: float | None = Field(None, alias="inputPrice")
    input_price_type: InputPriceType | None = Field(None, alias="inputPriceType")
    tax_key_id: UUID | None = Field(None, alias="taxKeyId")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    cost_centers: list[PreviewItemCostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[PreviewItemCostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    article_id: UUID | None = Field(None, alias="articleId")
    general_ledger_account_id: UUID | None = Field(None, alias="generalLedgerAccountId")
    price_unit_id: UUID | None = Field(None, alias="priceUnitId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    delta_value: float | None = Field(None, alias="deltaValue")
    items: list[PreviewTransactionItemRequest] | None = None
    _remove: bool | None = None

class PreviewTransactionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    preview_transaction: TransactionModel | None = Field(None, alias="previewTransaction")
    validation_result: TransactionValidationResultModel | None = Field(None, alias="validationResult")

class PreviewTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    creator: TransactionContactRequest | None = None
    number: str | None = None
    reference: str | None = None
    type_id: UUID | None = Field(None, alias="typeId")
    subtype_id: UUID | None = Field(None, alias="subtypeId")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    terms_of_payment_id: UUID | None = Field(None, alias="termsOfPaymentId")
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    currency_id: UUID | None = Field(None, alias="currencyId")
    description: str | None = None
    financial_partner: TransactionContactRequest | None = Field(None, alias="financialPartner")
    delivery_address: TransactionContactRequest | None = Field(None, alias="deliveryAddress")
    invoice_recipient: TransactionContactRequest | None = Field(None, alias="invoiceRecipient")
    payer: TransactionContactRequest | None = None
    responsible: TransactionContactRequest | None = None
    representative: TransactionContactRequest | None = None
    items: list[PreviewTransactionItemRequest] | None = None
    alternative_payment_deadline: datetime | None = Field(None, alias="alternativePaymentDeadline")
    balance: float | None = None
    barcode: str | None = None
    bill_to_text: str | None = Field(None, alias="billToText")
    cash_discount_percent_value: float | None = Field(None, alias="cashDiscountPercentValue")
    cash_discount_total: float | None = Field(None, alias="cashDiscountTotal")
    financial_accounting_period_id: UUID | None = Field(None, alias="financialAccountingPeriodId")
    period_id: UUID | None = Field(None, alias="periodId")
    manual_vat: TransactionManualVatRequest | None = Field(None, alias="manualVAT")
    notes: str | None = None
    due_date: datetime | None = Field(None, alias="dueDate")
    reference_number: str | None = Field(None, alias="referenceNumber")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    operation_item_combination_mode: OperationItemCombinationModeModel | None = Field(None, alias="operationItemCombinationMode")
    is_gross: bool | None = Field(None, alias="isGross")
    financial_export_disabled: bool | None = Field(None, alias="financialExportDisabled")
    default_cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostCenters")
    default_cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostObjects")
    metadata_processing_data: MetadataProcessingDataRequest | None = Field(None, alias="metadataProcessingData")
    validate_price_input: bool | None = Field(None, alias="validatePriceInput")

class Profile(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64
    VALUE_128 = 128
    VALUE_65536 = 65536

class ProjectStage(BaseModel):
    fields: dict[str, int] | None

class QuantityCode(IntEnum):
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
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49

class QuantityModel(BaseModel):
    value: float | None = None
    unit: QuantityUnitModel | None = None

class QuantityRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    value: float | None = None
    unit_id: UUID | None = Field(None, alias="unitId")

class QuantityUnitModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    short_name: str | None = Field(None, alias="shortName")

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

class RemoveBillingLinesFromDraftTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    billing_line_ids: list[UUID] | None = Field(None, alias="billingLineIds")

class RequiredEndpointContractDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    allow_multiple: bool | None = Field(None, alias="allowMultiple")

class ResolveStage(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    source: str | None
    local_path: str | None = Field(alias="localPath")
    as_: str | None = Field(alias="as")

class RoundingMode(IntEnum):
    VALUE_0 = 0

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

class SortField(BaseModel):
    path: str | None
    direction: str | None

class SourceBillingLineReferenceModel(BaseModel):
    type: str | None = None
    id: UUID | None = None

class SourceBillingLineReferenceRequest(BaseModel):
    type: str | None = None
    id: UUID | None = None

class SplitConfigurationModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: str | None = None
    name: str | None = None
    split_definitions: list[SplitDefinition] | None = Field(None, alias="splitDefinitions")

class SplitDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = None
    type: SplitDefinitionType | None = None
    addon_property_path: str | None = Field(None, alias="addonPropertyPath")

class SplitDefinitionType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7

class SplitTarget(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class StringTransactionPriceObjectModelKeyValuePair(BaseModel):
    key: str | None = None
    value: TransactionPriceObjectModel | None = None

class TaxCategory(IntEnum):
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
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21

class TaxGroupCountryIsoRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    iso_code: str | None = Field(None, alias="isoCode")

class TaxGroupCountryModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    iso_code: str | None = Field(None, alias="isoCode")

class TaxGroupModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: int | None = None
    name: str | None = None
    countries: list[TaxGroupCountryModel] | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TaxGroupRequest(BaseModel):
    number: int
    name: str
    countries: list[TaxGroupCountryIsoRequest]

class TaxGroupSubsetModel(BaseModel):
    id: UUID | None = None
    number: int | None = None
    name: str | None = None

class TaxKeyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    tax_group: TaxGroupSubsetModel | None = Field(None, alias="taxGroup")
    tax_rate: TaxRateSubsetModel | None = Field(None, alias="taxRate")
    value: float | None = None
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    bu_number: int | None = Field(None, alias="buNumber")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TaxKeyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    value: float
    valid_from: datetime = Field(alias="validFrom")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    valid_to: datetime | None = Field(None, alias="validTo")
    bu_number: int | None = Field(None, alias="buNumber")

class TaxKeyTotalPriceValuesModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tax_key_value: float | None = Field(None, alias="taxKeyValue")
    total_price_net: float | None = Field(None, alias="totalPriceNet")
    total_price_gross: float | None = Field(None, alias="totalPriceGross")
    total_price_tax: float | None = Field(None, alias="totalPriceTax")

class TaxRateModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: int | None = None
    name: str | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TaxRateRequest(BaseModel):
    number: int
    name: str

class TaxRateSubsetModel(BaseModel):
    id: UUID | None = None
    number: int | None = None
    name: str | None = None

class TaxRegistration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tax_registration_mode: TaxRegistrationMode | None = Field(None, alias="taxRegistrationMode")
    tax_id: str | None = Field(None, alias="taxId")

class TaxRegistrationMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class TaxRegistrationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    tax_registration_mode: TaxRegistrationMode | None = Field(None, alias="taxRegistrationMode")
    tax_id: str | None = Field(None, alias="taxId")

class TaxRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: TaxType | None = None
    category: TaxCategory | None = None
    rate: float | None = None
    assigned_items: list[str] | None = Field(None, alias="assignedItems")

class TaxType(IntEnum):
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
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_39 = 39
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54

class TermsOfPayment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = None
    payment_due: datetime | None = Field(None, alias="paymentDue")

class TermsOfPaymentModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: int | None = None
    name: str | None = None
    cash_discount: float | None = Field(None, alias="cashDiscount")
    cash_discount_days: int | None = Field(None, alias="cashDiscountDays")
    payment_deadline_days: int | None = Field(None, alias="paymentDeadlineDays")
    states: list[str] | None = None
    formatted_text: str | None = Field(None, alias="formattedText")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TermsOfPaymentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int
    name: str
    payment_deadline_days: int = Field(alias="paymentDeadlineDays")
    cash_discount: float | None = Field(None, alias="cashDiscount")
    cash_discount_days: int | None = Field(None, alias="cashDiscountDays")
    states: list[str] | None = None
    formatted_text: str | None = Field(None, alias="formattedText")

class TransactionAddressModel(BaseModel):
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

class TransactionContactModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    account_number: str | None = Field(None, alias="accountNumber")
    company_name: str | None = Field(None, alias="companyName")
    first_name: str | None = Field(None, alias="firstName")
    last_name: str | None = Field(None, alias="lastName")
    address: TransactionAddressModel | None = None

class TransactionContactRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    personal_account_id: UUID | None = Field(None, alias="personalAccountId")

class TransactionConvertState(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3

class TransactionDocumentModel(BaseModel):
    id: UUID | None = None
    number: int | None = None
    name: str | None = None

class TransactionEditableResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    errors: list[LocalizableErrorModel] | None = None
    is_editable: bool | None = Field(None, alias="isEditable")

class TransactionGeneralLedgerAccountGroupModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    number: str | None = None

class TransactionGeneralLedgerAccountModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: str | None = None
    tax_rate: TransactionTaxRateModel | None = Field(None, alias="taxRate")

class TransactionItemCostCenterModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: int | None = None
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")

class TransactionItemModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    text: str | None = None
    type: TransactionItemTypeModel | None = None
    booked_from_transaction_id: UUID | None = Field(None, alias="bookedFromTransactionId")
    transaction_item_collection_id: UUID | None = Field(None, alias="transactionItemCollectionId")
    sort_number: int | None = Field(None, alias="sortNumber")
    deserialization_type: str | None = Field(None, alias="deserializationType")
    assigned_transaction_items: list[TransactionItemModel] | None = Field(None, alias="assignedTransactionItems")
    value_operator: ValueOperatorModel | None = Field(None, alias="valueOperator")
    assignment_mode: AssignmentModeModel | None = Field(None, alias="assignmentMode")
    amount: float | None = None
    behavior_definitions: list[BehaviorDefinitionModel] | None = Field(None, alias="behaviorDefinitions")
    original_operation_item: TransactionItemModel | None = Field(None, alias="originalOperationItem")
    quantity: QuantityModel | None = None
    input_price: float | None = Field(None, alias="inputPrice")
    input_price_type: InputPriceType | None = Field(None, alias="inputPriceType")
    tax_key: TaxKeyModel | None = Field(None, alias="taxKey")
    tax_rate: TransactionTaxRateModel | None = Field(None, alias="taxRate")
    cost_centers: list[CostCenterAssignmentModel] | None = Field(None, alias="costCenters")
    cost_objects: list[CostCenterAssignmentModel] | None = Field(None, alias="costObjects")
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    single_price_net: float | None = Field(None, alias="singlePriceNet")
    total_price_net: float | None = Field(None, alias="totalPriceNet")
    single_price_gross: float | None = Field(None, alias="singlePriceGross")
    total_price_gross: float | None = Field(None, alias="totalPriceGross")
    single_price_vat: float | None = Field(None, alias="singlePriceVat")
    total_price_vat: float | None = Field(None, alias="totalPriceVat")
    pricing: list[StringTransactionPriceObjectModelKeyValuePair] | None = None
    article_id: UUID | None = Field(None, alias="articleId")
    general_ledger_account: TransactionGeneralLedgerAccountModel | None = Field(None, alias="generalLedgerAccount")
    billing_line_id: UUID | None = Field(None, alias="billingLineId")
    price_unit: QuantityUnitModel | None = Field(None, alias="priceUnit")
    reference: str | None = None
    references: list[BillingLineReferenceModel] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    delta_value: float | None = Field(None, alias="deltaValue")
    items: list[TransactionItemModel] | None = None

class TransactionItemRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    text: str | None = None
    type_id: UUID | None = Field(None, alias="typeId")
    sort_number: int | None = Field(None, alias="sortNumber")
    deserialization_type: str | None = Field(None, alias="deserializationType")
    value_operator: ValueOperator | None = Field(None, alias="valueOperator")
    assignment_mode: AssignmentMode | None = Field(None, alias="assignmentMode")
    behavior_definitions: list[BehaviorDefinitionRequest] | None = Field(None, alias="behaviorDefinitions")
    quantity: QuantityRequest | None = None
    input_price: float | None = Field(None, alias="inputPrice")
    input_price_type: InputPriceType | None = Field(None, alias="inputPriceType")
    tax_key_id: UUID | None = Field(None, alias="taxKeyId")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    article_id: UUID | None = Field(None, alias="articleId")
    general_ledger_account_id: UUID | None = Field(None, alias="generalLedgerAccountId")
    price_unit_id: UUID | None = Field(None, alias="priceUnitId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    delta_value: float | None = Field(None, alias="deltaValue")
    items: list[TransactionItemRequest] | None = None
    _remove: bool | None = None

class TransactionItemTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    deserialization_type: str | None = Field(None, alias="deserializationType")
    name: str | None = None
    number: int | None = None
    code: str | None = None
    has_position_number: bool | None = Field(None, alias="hasPositionNumber")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    detail_html: str | None = Field(None, alias="detailHtml")
    data_template: str | None = Field(None, alias="dataTemplate")
    article_gla_resolver: str | None = Field(None, alias="articleGLAResolver")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TransactionItemTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    number: int
    has_position_number: bool = Field(alias="hasPositionNumber")
    is_selectable: bool = Field(alias="isSelectable")
    deserialization_type: str | None = Field(None, alias="deserializationType")
    detail_html: str | None = Field(None, alias="detailHtml")
    data_template: str | None = Field(None, alias="dataTemplate")
    article_gla_resolver: str | None = Field(None, alias="articleGLAResolver")
    code: str | None = None

class TransactionManualVatModel(BaseModel):
    value: float | None = None
    date: datetime | None = None
    user: TransactionUserModel | None = None

class TransactionManualVatRequest(BaseModel):
    value: float | None = None
    date: datetime | None = None

class TransactionModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    is_deleted: bool | None = Field(None, alias="isDeleted")
    number: str | None = None
    reference: str | None = None
    type: TransactionTransactionTypeModel | None = None
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    terms_of_payment: TermsOfPaymentModel | None = Field(None, alias="termsOfPayment")
    payment_method: PaymentMethodModel | None = Field(None, alias="paymentMethod")
    currency: CurrencyModel | None = None
    description: str | None = None
    financial_partner: TransactionContactModel | None = Field(None, alias="financialPartner")
    delivery_address: TransactionContactModel | None = Field(None, alias="deliveryAddress")
    invoice_recipient: TransactionContactModel | None = Field(None, alias="invoiceRecipient")
    payer: TransactionContactModel | None = None
    creator: TransactionContactModel | None = None
    responsible: TransactionContactModel | None = None
    representative: TransactionContactModel | None = None
    items: list[TransactionItemModel] | None = None
    convert_state: TransactionConvertState | None = Field(None, alias="convertState")
    alternative_payment_deadline: datetime | None = Field(None, alias="alternativePaymentDeadline")
    balance: float | None = None
    barcode: str | None = None
    bill_to_text: str | None = Field(None, alias="billToText")
    cash_discount_percent_value: float | None = Field(None, alias="cashDiscountPercentValue")
    cash_discount_total: float | None = Field(None, alias="cashDiscountTotal")
    document: TransactionDocumentModel | None = None
    attached_documents: list[TransactionDocumentModel] | None = Field(None, alias="attachedDocuments")
    financial_accounting_period: TransactionPeriodModel | None = Field(None, alias="financialAccountingPeriod")
    period: TransactionPeriodModel | None = None
    states: list[str] | None = None
    manual_vat: TransactionManualVatModel | None = Field(None, alias="manualVat")
    notes: str | None = None
    due_date: datetime | None = Field(None, alias="dueDate")
    reference_number: str | None = Field(None, alias="referenceNumber")
    tax_group: TaxGroupModel | None = Field(None, alias="taxGroup")
    total_price: float | None = Field(None, alias="totalPrice")
    total_price_gross: float | None = Field(None, alias="totalPriceGross")
    total_price_net: float | None = Field(None, alias="totalPriceNet")
    total_price_tax: float | None = Field(None, alias="totalPriceTax")
    transaction_year: int | None = Field(None, alias="transactionYear")
    update_user: TransactionUserModel | None = Field(None, alias="updateUser")
    signed_total_price_net: float | None = Field(None, alias="signedTotalPriceNet")
    signed_total_price_gross: float | None = Field(None, alias="signedTotalPriceGross")
    signed_total_price: float | None = Field(None, alias="signedTotalPrice")
    signed_total_price_tax: float | None = Field(None, alias="signedTotalPriceTax")
    tax_key_total_prices: list[TaxKeyTotalPriceValuesModel] | None = Field(None, alias="taxKeyTotalPrices")
    sign: int | None = None
    operation_item_combination_mode: OperationItemCombinationModeModel | None = Field(None, alias="operationItemCombinationMode")
    is_gross: bool | None = Field(None, alias="isGross")
    financial_export_disabled: bool | None = Field(None, alias="financialExportDisabled")
    validation_result: TransactionValidationResultModel | None = Field(None, alias="validationResult")
    editable_result: TransactionEditableResultModel | None = Field(None, alias="editableResult")
    default_cost_centers: list[CostCenterAssignmentModel] | None = Field(None, alias="defaultCostCenters")
    default_cost_objects: list[CostCenterAssignmentModel] | None = Field(None, alias="defaultCostObjects")
    metadata_processing_data: MetadataProcessingDataModel | None = Field(None, alias="metadataProcessingData")
    cash_discount_date: datetime | None = Field(None, alias="cashDiscountDate")
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TransactionNumberDateSourceType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class TransactionPeriodModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fiscal_year_id: UUID | None = Field(None, alias="fiscalYearId")
    period_id: UUID | None = Field(None, alias="periodId")
    period_number: int | None = Field(None, alias="periodNumber")
    from_: datetime | None = Field(None, alias="from")
    to: datetime | None = None

class TransactionPriceObjectModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = None
    single_price_net: float | None = Field(None, alias="singlePriceNet")
    total_price_net: float | None = Field(None, alias="totalPriceNet")
    single_price_gross: float | None = Field(None, alias="singlePriceGross")
    total_price_gross: float | None = Field(None, alias="totalPriceGross")
    single_price_vat: float | None = Field(None, alias="singlePriceVat")
    total_price_vat: float | None = Field(None, alias="totalPriceVat")

class TransactionResultModel(BaseModel):
    transaction: TransactionModel | None = None
    errors: list[LocalizableErrorModel] | None = None

class TransactionSequenceNumberRange(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSequenceNumberRangeModel(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSubtypeArchiveMode(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2

class TransactionSubtypeCancellationTransactionType(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type_id: UUID | None = Field(None, alias="typeId")
    subtype_id: UUID | None = Field(None, alias="subtypeId")
    type_name: str | None = Field(None, alias="typeName")
    subtype_name: str | None = Field(None, alias="subtypeName")

class TransactionSubtypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    code: str | None = None
    report: TransactionSubtypeReportModel | None = None
    sequence_number_range: TransactionSequenceNumberRangeModel | None = Field(None, alias="sequenceNumberRange")
    output_queue: TransactionSubtypeOutputQueueModel | None = Field(None, alias="outputQueue")
    cancellation_transaction_type: TransactionSubtypeCancellationTransactionType | None = Field(None, alias="cancellationTransactionType")
    number: int | None = None
    name: str | None = None
    document_title_template: str | None = Field(None, alias="documentTitleTemplate")
    archive_mode: TransactionSubtypeArchiveMode | None = Field(None, alias="archiveMode")
    barcode_template: str | None = Field(None, alias="barcodeTemplate")
    use_number_reservation: bool | None = Field(None, alias="useNumberReservation")
    custom_field2_template: str | None = Field(None, alias="customField2Template")
    custom_field1_template: str | None = Field(None, alias="customField1Template")
    booking_text_template: str | None = Field(None, alias="bookingTextTemplate")
    summarize_bookings: bool | None = Field(None, alias="summarizeBookings")
    accounting_export_group: str | None = Field(None, alias="accountingExportGroup")
    due_date_mode: DueDateMode | None = Field(None, alias="dueDateMode")
    transaction_number_date_source: TransactionNumberDateSourceType | None = Field(None, alias="transactionNumberDateSource")
    export_cost_quantity: ExportCostQuantityType | None = Field(None, alias="exportCostQuantity")
    is_deleted: bool | None = Field(None, alias="isDeleted")

class TransactionSubtypeOutputQueue(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSubtypeOutputQueueModel(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSubtypeReport(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSubtypeReportModel(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionSubtypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    code: str | None = None
    report: TransactionSubtypeReport | None = None
    sequence_number_range: TransactionSequenceNumberRange | None = Field(None, alias="sequenceNumberRange")
    output_queue: TransactionSubtypeOutputQueue | None = Field(None, alias="outputQueue")
    cancellation_transaction_type: TransactionSubtypeCancellationTransactionType | None = Field(None, alias="cancellationTransactionType")
    number: int | None = None
    name: str | None = None
    document_title_template: str | None = Field(None, alias="documentTitleTemplate")
    archive_mode: TransactionSubtypeArchiveMode | None = Field(None, alias="archiveMode")
    barcode_template: str | None = Field(None, alias="barcodeTemplate")
    use_number_reservation: bool | None = Field(None, alias="useNumberReservation")
    custom_field2_template: str | None = Field(None, alias="customField2Template")
    custom_field1_template: str | None = Field(None, alias="customField1Template")
    booking_text_template: str | None = Field(None, alias="bookingTextTemplate")
    summarize_bookings: bool | None = Field(None, alias="summarizeBookings")
    accounting_export_group: str | None = Field(None, alias="accountingExportGroup")
    due_date_mode: DueDateMode | None = Field(None, alias="dueDateMode")
    transaction_number_date_source: TransactionNumberDateSourceType | None = Field(None, alias="transactionNumberDateSource")
    export_cost_quantity: ExportCostQuantityType | None = Field(None, alias="exportCostQuantity")

class TransactionTaxRateModel(BaseModel):
    id: UUID | None = None
    name: str | None = None
    number: str | None = None

class TransactionTransactionSubtypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    code: str | None = None
    report: TransactionSubtypeReportModel | None = None
    sequence_number_range: TransactionSequenceNumberRangeModel | None = Field(None, alias="sequenceNumberRange")
    output_queue: TransactionSubtypeOutputQueueModel | None = Field(None, alias="outputQueue")
    number: int | None = None
    name: str | None = None

class TransactionTransactionTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    name: str | None = None
    number: int | None = None
    report_name: str | None = Field(None, alias="reportName")
    short_name: str | None = Field(None, alias="shortName")
    functions: list[str] | None = None
    subtype: TransactionTransactionSubtypeModel | None = None

class TransactionTypeModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    organization_id: UUID | None = Field(None, alias="organizationId")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    name: str | None = None
    number: int | None = None
    report_name: str | None = Field(None, alias="reportName")
    short_name: str | None = Field(None, alias="shortName")
    functions: list[str] | None = None
    code: str | None = None
    subtypes: list[TransactionSubtypeModel] | None = None
    create_date_time: datetime | None = Field(None, alias="createDateTime")
    create_user_id: UUID | None = Field(None, alias="createUserId")
    create_user_name: str | None = Field(None, alias="createUserName")
    update_date_time: datetime | None = Field(None, alias="updateDateTime")
    update_user_id: UUID | None = Field(None, alias="updateUserId")
    update_user_name: str | None = Field(None, alias="updateUserName")

class TransactionTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    number: int
    subtypes: list[TransactionSubtypeRequest]
    report_name: str | None = Field(None, alias="reportName")
    short_name: str | None = Field(None, alias="shortName")
    functions: list[str] | None = None
    code: str | None = None

class TransactionUserModel(BaseModel):
    id: UUID | None = None
    name: str | None = None

class TransactionValidationResultModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    input_field_validation_results: dict[str, bool] | None = Field(None, alias="inputFieldValidationResults")
    errors: list[LocalizableErrorModel] | None = None
    is_valid: bool | None = Field(None, alias="isValid")

class UnlockBillingLineResultModel(BaseModel):
    unlocked: bool | None = None
    errors: list[LocalizableErrorModel] | None = None

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

class UpdateBillingLineRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    financial_partner: TransactionContactRequest | None = Field(None, alias="financialPartner")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    text: str | None = None
    source_text: str | None = Field(None, alias="sourceText")
    quantity: BillingLineQuantityRequest | None = None
    single_price: float | None = Field(None, alias="singlePrice")
    total_price: float | None = Field(None, alias="totalPrice")
    is_gross: bool | None = Field(None, alias="isGross")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="costCenters")
    cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="costObjects")
    general_ledger_account_group_id: UUID | None = Field(None, alias="generalLedgerAccountGroupId")
    reference: str | None = None
    references: list[BillingLineReferenceRequest] | None = None
    is_manual_billing_line: bool | None = Field(None, alias="isManualBillingLine")
    addon: dict[str, object] | None = None
    source_billing_line_reference: SourceBillingLineReferenceRequest | None = Field(None, alias="sourceBillingLineReference")

class UpdateCurrencyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int | None = None
    name: str | None = None
    short_name: str | None = Field(None, alias="shortName")
    symbol: str | None = None

class UpdateFiscalYearRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int | None = None
    name: str | None = None
    from_: datetime | None = Field(None, alias="from")
    to: datetime | None = None
    periods: list[PeriodRequest] | None = None

class UpdatePaymentMethodRequest(BaseModel):
    number: int | None = None
    name: str | None = None

class UpdatePersonalAccountGroupRequest(BaseModel):
    number: str | None = None
    name: str | None = None

class UpdatePersonalAccountRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: UUID | None = None
    number: str | None = None
    vat_id: str | None = Field(None, alias="vatId")
    type: str | None = None
    credit_limit: CreditLimitModel | None = Field(None, alias="creditLimit")
    address_contact_ids: list[UUID] | None = Field(None, alias="addressContactIds")
    sale_terms_of_payment_id: UUID | None = Field(None, alias="saleTermsOfPaymentId")
    purchase_terms_of_payment_id: UUID | None = Field(None, alias="purchaseTermsOfPaymentId")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    personal_account_group_id: UUID | None = Field(None, alias="personalAccountGroupId")

class UpdateSettingRequest(BaseModel):
    value: dict[str, object] | None = None

class UpdateSplitConfigurationRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    name: str | None = None
    split_definitions: list[SplitDefinition] | None = Field(None, alias="splitDefinitions")

class UpdateTaxGroupRequest(BaseModel):
    number: int | None = None
    name: str | None = None
    countries: list[TaxGroupCountryIsoRequest] | None = None

class UpdateTaxKeyRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    tax_rate_id: UUID | None = Field(None, alias="taxRateId")
    value: float | None = None
    valid_from: datetime | None = Field(None, alias="validFrom")
    valid_to: datetime | None = Field(None, alias="validTo")
    bu_number: int | None = Field(None, alias="buNumber")

class UpdateTaxRateRequest(BaseModel):
    number: int | None = None
    name: str | None = None

class UpdateTermsOfPaymentRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: int | None = None
    name: str | None = None
    cash_discount: float | None = Field(None, alias="cashDiscount")
    cash_discount_days: int | None = Field(None, alias="cashDiscountDays")
    payment_deadline_days: int | None = Field(None, alias="paymentDeadlineDays")
    states: list[str] | None = None
    formatted_text: str | None = Field(None, alias="formattedText")

class UpdateTransactionItemTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    deserialization_type: str | None = Field(None, alias="deserializationType")
    name: str | None = None
    number: int | None = None
    has_position_number: bool | None = Field(None, alias="hasPositionNumber")
    is_selectable: bool | None = Field(None, alias="isSelectable")
    detail_html: str | None = Field(None, alias="detailHtml")
    data_template: str | None = Field(None, alias="dataTemplate")
    article_gla_resolver: str | None = Field(None, alias="articleGLAResolver")
    code: str | None = None

class UpdateTransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    number: str | None = None
    reference: str | None = None
    type_id: UUID | None = Field(None, alias="typeId")
    subtype_id: UUID | None = Field(None, alias="subtypeId")
    date: datetime | None = None
    delivery_date: datetime | None = Field(None, alias="deliveryDate")
    terms_of_payment_id: UUID | None = Field(None, alias="termsOfPaymentId")
    payment_method_id: UUID | None = Field(None, alias="paymentMethodId")
    currency_id: UUID | None = Field(None, alias="currencyId")
    description: str | None = None
    financial_partner: TransactionContactRequest | None = Field(None, alias="financialPartner")
    delivery_address: TransactionContactRequest | None = Field(None, alias="deliveryAddress")
    invoice_recipient: TransactionContactRequest | None = Field(None, alias="invoiceRecipient")
    payer: TransactionContactRequest | None = None
    responsible: TransactionContactRequest | None = None
    representative: TransactionContactRequest | None = None
    items: list[TransactionItemRequest] | None = None
    alternative_payment_deadline: datetime | None = Field(None, alias="alternativePaymentDeadline")
    balance: float | None = None
    barcode: str | None = None
    bill_to_text: str | None = Field(None, alias="billToText")
    cash_discount_percent_value: float | None = Field(None, alias="cashDiscountPercentValue")
    cash_discount_total: float | None = Field(None, alias="cashDiscountTotal")
    financial_accounting_period_id: UUID | None = Field(None, alias="financialAccountingPeriodId")
    period_id: UUID | None = Field(None, alias="periodId")
    states: list[str] | None = None
    manual_vat: TransactionManualVatRequest | None = Field(None, alias="manualVAT")
    notes: str | None = None
    due_date: datetime | None = Field(None, alias="dueDate")
    reference_number: str | None = Field(None, alias="referenceNumber")
    tax_group_id: UUID | None = Field(None, alias="taxGroupId")
    operation_item_combination_mode: OperationItemCombinationModeModel | None = Field(None, alias="operationItemCombinationMode")
    is_gross: bool | None = Field(None, alias="isGross")
    financial_export_disabled: bool | None = Field(None, alias="financialExportDisabled")
    default_cost_centers: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostCenters")
    default_cost_objects: list[CostCenterAssignmentRequest] | None = Field(None, alias="defaultCostObjects")
    metadata_processing_data: MetadataProcessingDataRequest | None = Field(None, alias="metadataProcessingData")

class UpdateTransactionTypeRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = None
    number: int | None = None
    report_name: str | None = Field(None, alias="reportName")
    short_name: str | None = Field(None, alias="shortName")
    functions: list[str] | None = None
    subtypes: list[TransactionSubtypeRequest] | None = None
    code: str | None = None

class ValueOperator(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ValueOperatorModel(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1

class ZUGFeRDVersion(IntEnum):
    VALUE_100 = 100
    VALUE_200 = 200
    VALUE_220 = 220
