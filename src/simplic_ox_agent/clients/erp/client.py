"""Typed client generated from the OpenAPI spec."""

from __future__ import annotations

from uuid import UUID

from ...core.http_client import SimplicOxHttpClient
from .models import (
    AddonFieldResponse,
    BillingLineModel,
    BillingLineResultModel,
    ConvertResultModel,
    CurrencyModel,
    DistributeBillingLinesToDraftTransactionsResultModel,
    DraftTransactionsResultModel,
    ElectronicInvoiceCreateResult,
    ElectronicInvoiceImportResult,
    EndpointContract,
    FiscalYearModel,
    FiscalYearResultModel,
    LockBillingLineResultModel,
    OrganizationSettingResult,
    OxQLQueryResult,
    PaymentMethodModel,
    PersonalAccountGroupModel,
    PersonalAccountModel,
    PreviewTransactionModel,
    ServiceObject,
    SplitConfigurationModel,
    TaxGroupModel,
    TaxKeyModel,
    TaxRateModel,
    TermsOfPaymentModel,
    TransactionItemTypeModel,
    TransactionModel,
    TransactionResultModel,
    TransactionTypeModel,
    UnlockBillingLineResultModel,
)

_PREFIX = "erp-api/v1"


class ErpClient:
    """Typed client for ``erp-api/v1``.

    Wraps a :class:`~simplic_ox_agent.core.http_client.SimplicOxHttpClient`
    and exposes one async method per endpoint.  Responses are parsed into
    typed Pydantic models; HTTP errors raise via ``raise_for_status()``.

    Example::

        from simplic_ox_agent.clients.erp import ErpClient

        client = ErpClient(context.http)
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

    async def get_billing_line(
        self,
    ) -> None:
        """Gets all billing lines."""
        response = await self._http.get(
            f"{_PREFIX}/BillingLine",
        )
        response.raise_for_status()

    async def create_billing_line(
        self,
        financial_partner: TransactionContactRequest | None = None,
        date: str | None = None,
        delivery_date: str | None = None,
        text: str | None = None,
        source_text: str | None = None,
        quantity: BillingLineQuantityRequest | None = None,
        single_price: float | None = None,
        total_price: float | None = None,
        is_gross: bool | None = None,
        tax_rate_id: UUID | None = None,
        cost_centers: list[CostCenterAssignmentRequest] | None = None,
        cost_objects: list[CostCenterAssignmentRequest] | None = None,
        general_ledger_account_group_id: UUID | None = None,
        reference: str | None = None,
        references: list[BillingLineReferenceRequest] | None = None,
        is_manual_billing_line: bool | None = None,
        addon: dict[str, object] | None = None,
        source_billing_line_reference: SourceBillingLineReferenceRequest | None = None,
    ) -> BillingLineResultModel:
        """Creates a new billing line."""
        _body: dict[str, object] = {
        }
        if financial_partner is not None:
            _body["financialPartner"] = financial_partner
        if date is not None:
            _body["date"] = date
        if delivery_date is not None:
            _body["deliveryDate"] = delivery_date
        if text is not None:
            _body["text"] = text
        if source_text is not None:
            _body["sourceText"] = source_text
        if quantity is not None:
            _body["quantity"] = quantity
        if single_price is not None:
            _body["singlePrice"] = single_price
        if total_price is not None:
            _body["totalPrice"] = total_price
        if is_gross is not None:
            _body["isGross"] = is_gross
        if tax_rate_id is not None:
            _body["taxRateId"] = str(tax_rate_id)
        if cost_centers is not None:
            _body["costCenters"] = cost_centers
        if cost_objects is not None:
            _body["costObjects"] = cost_objects
        if general_ledger_account_group_id is not None:
            _body["generalLedgerAccountGroupId"] = str(general_ledger_account_group_id)
        if reference is not None:
            _body["reference"] = reference
        if references is not None:
            _body["references"] = references
        if is_manual_billing_line is not None:
            _body["isManualBillingLine"] = is_manual_billing_line
        if addon is not None:
            _body["addon"] = addon
        if source_billing_line_reference is not None:
            _body["sourceBillingLineReference"] = source_billing_line_reference
        response = await self._http.post(
            f"{_PREFIX}/BillingLine",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineResultModel.model_validate(response.json())

    async def get_billing_line_by_id(
        self,
        id: UUID,
    ) -> BillingLineModel:
        """Gets a billing line by ID."""
        response = await self._http.get(
            f"{_PREFIX}/BillingLine/{id}",
        )
        response.raise_for_status()
        return BillingLineModel.model_validate(response.json())

    async def update_billing_line_by_id(
        self,
        id: UUID,
        financial_partner: TransactionContactRequest | None = None,
        date: str | None = None,
        delivery_date: str | None = None,
        text: str | None = None,
        source_text: str | None = None,
        quantity: BillingLineQuantityRequest | None = None,
        single_price: float | None = None,
        total_price: float | None = None,
        is_gross: bool | None = None,
        tax_rate_id: UUID | None = None,
        cost_centers: list[CostCenterAssignmentRequest] | None = None,
        cost_objects: list[CostCenterAssignmentRequest] | None = None,
        general_ledger_account_group_id: UUID | None = None,
        reference: str | None = None,
        references: list[BillingLineReferenceRequest] | None = None,
        is_manual_billing_line: bool | None = None,
        addon: dict[str, object] | None = None,
        source_billing_line_reference: SourceBillingLineReferenceRequest | None = None,
    ) -> BillingLineResultModel:
        """Patches a billing line."""
        _body: dict[str, object] = {
        }
        if financial_partner is not None:
            _body["financialPartner"] = financial_partner
        if date is not None:
            _body["date"] = date
        if delivery_date is not None:
            _body["deliveryDate"] = delivery_date
        if text is not None:
            _body["text"] = text
        if source_text is not None:
            _body["sourceText"] = source_text
        if quantity is not None:
            _body["quantity"] = quantity
        if single_price is not None:
            _body["singlePrice"] = single_price
        if total_price is not None:
            _body["totalPrice"] = total_price
        if is_gross is not None:
            _body["isGross"] = is_gross
        if tax_rate_id is not None:
            _body["taxRateId"] = str(tax_rate_id)
        if cost_centers is not None:
            _body["costCenters"] = cost_centers
        if cost_objects is not None:
            _body["costObjects"] = cost_objects
        if general_ledger_account_group_id is not None:
            _body["generalLedgerAccountGroupId"] = str(general_ledger_account_group_id)
        if reference is not None:
            _body["reference"] = reference
        if references is not None:
            _body["references"] = references
        if is_manual_billing_line is not None:
            _body["isManualBillingLine"] = is_manual_billing_line
        if addon is not None:
            _body["addon"] = addon
        if source_billing_line_reference is not None:
            _body["sourceBillingLineReference"] = source_billing_line_reference
        response = await self._http.patch(
            f"{_PREFIX}/BillingLine/{id}",
            json=_body,
        )
        response.raise_for_status()
        return BillingLineResultModel.model_validate(response.json())

    async def delete_billing_line_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a billing line."""
        response = await self._http.delete(
            f"{_PREFIX}/BillingLine/{id}",
        )
        response.raise_for_status()

    async def get_by_state(
        self,
        state: BillingLineState,
    ) -> None:
        """Gets all billing lines with a given state."""
        response = await self._http.get(
            f"{_PREFIX}/BillingLine/get-by-state/{state}",
        )
        response.raise_for_status()

    async def lock(
        self,
        id: UUID,
    ) -> LockBillingLineResultModel:
        """Locks a billing line."""
        response = await self._http.patch(
            f"{_PREFIX}/BillingLine/{id}/lock",
        )
        response.raise_for_status()
        return LockBillingLineResultModel.model_validate(response.json())

    async def unlock(
        self,
        id: UUID,
    ) -> UnlockBillingLineResultModel:
        """Unlocks a billing line."""
        response = await self._http.patch(
            f"{_PREFIX}/BillingLine/{id}/unlock",
        )
        response.raise_for_status()
        return UnlockBillingLineResultModel.model_validate(response.json())

    async def create_currency(
        self,
        number: int,
        name: str,
        short_name: str,
        symbol: str,
    ) -> CurrencyModel:
        """Creates a new currency."""
        response = await self._http.post(
            f"{_PREFIX}/Currency",
            json={"number": number, "name": name, "shortName": short_name, "symbol": symbol},
        )
        response.raise_for_status()
        return CurrencyModel.model_validate(response.json())

    async def get_currency_by_id(
        self,
        id: UUID,
    ) -> CurrencyModel:
        """Gets a currency by ID."""
        response = await self._http.get(
            f"{_PREFIX}/Currency/{id}",
        )
        response.raise_for_status()
        return CurrencyModel.model_validate(response.json())

    async def update_currency_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
        short_name: str | None = None,
        symbol: str | None = None,
    ) -> CurrencyModel:
        """Patches a currency."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if short_name is not None:
            _body["shortName"] = short_name
        if symbol is not None:
            _body["symbol"] = symbol
        response = await self._http.patch(
            f"{_PREFIX}/Currency/{id}",
            json=_body,
        )
        response.raise_for_status()
        return CurrencyModel.model_validate(response.json())

    async def delete_currency_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a currency."""
        response = await self._http.delete(
            f"{_PREFIX}/Currency/{id}",
        )
        response.raise_for_status()

    async def create(
        self,
        pdf: str | None = None,
        profile: Profile | None = None,
        version: ZUGFeRDVersion | None = None,
        rounding_mode: RoundingMode | None = None,
        electronic_invoice_type: ElectronicInvoiceType | None = None,
        add_peppol_address: bool | None = None,
        leitweg_id_required: bool | None = None,
        invoice_data: InvoiceDataRequest | None = None,
    ) -> ElectronicInvoiceCreateResult:
        """Creates a PDF file that constitutes a hybrid electronic invoice according to the ZUGFeRD standard from an invoice PDF file and the relevant invoice data."""
        _body: dict[str, object] = {
        }
        if pdf is not None:
            _body["pdf"] = pdf
        if profile is not None:
            _body["profile"] = profile
        if version is not None:
            _body["version"] = version
        if rounding_mode is not None:
            _body["roundingMode"] = rounding_mode
        if electronic_invoice_type is not None:
            _body["electronicInvoiceType"] = electronic_invoice_type
        if add_peppol_address is not None:
            _body["addPeppolAddress"] = add_peppol_address
        if leitweg_id_required is not None:
            _body["leitwegIdRequired"] = leitweg_id_required
        if invoice_data is not None:
            _body["invoiceData"] = invoice_data
        response = await self._http.post(
            f"{_PREFIX}/ElectronicInvoicing/create",
            json=_body,
        )
        response.raise_for_status()
        return ElectronicInvoiceCreateResult.model_validate(response.json())

    async def import(
        self,
        file_to_import: str | None = None,
    ) -> ElectronicInvoiceImportResult:
        """Extracts the invoice data from an electronic invoice (either ZUGFeRD hybrid electronic invoice PDF or XRechnung XML) and validates it."""
        _body: dict[str, object] = {
        }
        if file_to_import is not None:
            _body["fileToImport"] = file_to_import
        response = await self._http.post(
            f"{_PREFIX}/ElectronicInvoicing/import",
            json=_body,
        )
        response.raise_for_status()
        return ElectronicInvoiceImportResult.model_validate(response.json())

    async def create_fiscal_year(
        self,
        number: int,
        name: str,
        from_: str,
        to: str,
        periods: list[PeriodRequest],
    ) -> FiscalYearResultModel:
        """Creates a new fiscal year."""
        response = await self._http.post(
            f"{_PREFIX}/FiscalYear",
            json={"number": number, "name": name, "from": from_, "to": to, "periods": periods},
        )
        response.raise_for_status()
        return FiscalYearResultModel.model_validate(response.json())

    async def get_fiscal_year_by_id(
        self,
        id: UUID,
    ) -> FiscalYearModel:
        """Gets a fiscal year by ID."""
        response = await self._http.get(
            f"{_PREFIX}/FiscalYear/{id}",
        )
        response.raise_for_status()
        return FiscalYearModel.model_validate(response.json())

    async def update_fiscal_year_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        periods: list[PeriodRequest] | None = None,
    ) -> FiscalYearResultModel:
        """Patches a fiscal year."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if from_ is not None:
            _body["from"] = from_
        if to is not None:
            _body["to"] = to
        if periods is not None:
            _body["periods"] = periods
        response = await self._http.patch(
            f"{_PREFIX}/FiscalYear/{id}",
            json=_body,
        )
        response.raise_for_status()
        return FiscalYearResultModel.model_validate(response.json())

    async def delete_fiscal_year_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a fiscal year."""
        response = await self._http.delete(
            f"{_PREFIX}/FiscalYear/{id}",
        )
        response.raise_for_status()

    async def internal_currency_get_by_id(
        self,
        id: UUID | None = None,
    ) -> CurrencyModel:
        """Get a currency by id"""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalCurrency/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return CurrencyModel.model_validate(response.json())

    async def internal_personal_account_get_by_id(
        self,
        id: UUID | None = None,
    ) -> PersonalAccountModel:
        """Gets a personal account by ID."""
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalPersonalAccount/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def internal_tax_rate_get_by_id(
        self,
        id: UUID | None = None,
    ) -> TaxRateModel:
        _params: dict[str, object] = {}
        if id is not None:
            _params["id"] = str(id)
        response = await self._http.get(
            f"{_PREFIX}/internal/InternalTaxRate/get-by-id",
            params=_params,
        )
        response.raise_for_status()
        return TaxRateModel.model_validate(response.json())

    async def add_billing_lines(
        self,
        transaction_id: UUID | None = None,
        billing_lines: list[CreateBillingLineRequest] | None = None,
    ) -> TransactionModel:
        """Creates a set of billing lines and adds them to an existing transaction."""
        _body: dict[str, object] = {
        }
        if transaction_id is not None:
            _body["transactionId"] = str(transaction_id)
        if billing_lines is not None:
            _body["billingLines"] = billing_lines
        response = await self._http.post(
            f"{_PREFIX}/internal/InternalTransaction/add-billing-lines",
            json=_body,
        )
        response.raise_for_status()
        return TransactionModel.model_validate(response.json())

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

    async def create_payment_method(
        self,
        number: int,
        name: str,
    ) -> PaymentMethodModel:
        """Creates a new payment method."""
        response = await self._http.post(
            f"{_PREFIX}/PaymentMethod",
            json={"number": number, "name": name},
        )
        response.raise_for_status()
        return PaymentMethodModel.model_validate(response.json())

    async def get_payment_method_by_id(
        self,
        id: UUID,
    ) -> PaymentMethodModel:
        """Gets a payment method by ID."""
        response = await self._http.get(
            f"{_PREFIX}/PaymentMethod/{id}",
        )
        response.raise_for_status()
        return PaymentMethodModel.model_validate(response.json())

    async def update_payment_method_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
    ) -> PaymentMethodModel:
        """Patches a payment method."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        response = await self._http.patch(
            f"{_PREFIX}/PaymentMethod/{id}",
            json=_body,
        )
        response.raise_for_status()
        return PaymentMethodModel.model_validate(response.json())

    async def delete_payment_method_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a payment method."""
        response = await self._http.delete(
            f"{_PREFIX}/PaymentMethod/{id}",
        )
        response.raise_for_status()

    async def create_personal_account(
        self,
        address_contact_ids: list[UUID] | None = None,
        sale_terms_of_payment_id: UUID | None = None,
        purchase_terms_of_payment_id: UUID | None = None,
        tax_group_id: UUID | None = None,
        personal_account_group_id: UUID | None = None,
        number: str | None = None,
        vat_id: str | None = None,
        type: str | None = None,
        credit_limit: CreditLimitModel | None = None,
    ) -> PersonalAccountModel:
        """Creates a new personal account."""
        _body: dict[str, object] = {
        }
        if address_contact_ids is not None:
            _body["addressContactIds"] = str(address_contact_ids)
        if sale_terms_of_payment_id is not None:
            _body["saleTermsOfPaymentId"] = str(sale_terms_of_payment_id)
        if purchase_terms_of_payment_id is not None:
            _body["purchaseTermsOfPaymentId"] = str(purchase_terms_of_payment_id)
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if personal_account_group_id is not None:
            _body["personalAccountGroupId"] = str(personal_account_group_id)
        if number is not None:
            _body["number"] = number
        if vat_id is not None:
            _body["vatId"] = vat_id
        if type is not None:
            _body["type"] = type
        if credit_limit is not None:
            _body["creditLimit"] = credit_limit
        response = await self._http.post(
            f"{_PREFIX}/PersonalAccount",
            json=_body,
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def get_personal_account_by_id(
        self,
        id: UUID,
    ) -> PersonalAccountModel:
        """Gets a personal account by ID."""
        response = await self._http.get(
            f"{_PREFIX}/PersonalAccount/{id}",
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def update_personal_account_by_id(
        self,
        id: UUID,
        id: UUID | None = None,
        number: str | None = None,
        vat_id: str | None = None,
        type: str | None = None,
        credit_limit: CreditLimitModel | None = None,
        address_contact_ids: list[UUID] | None = None,
        sale_terms_of_payment_id: UUID | None = None,
        purchase_terms_of_payment_id: UUID | None = None,
        tax_group_id: UUID | None = None,
        personal_account_group_id: UUID | None = None,
    ) -> PersonalAccountModel:
        """Patches a personal account."""
        _body: dict[str, object] = {
        }
        if id is not None:
            _body["id"] = str(id)
        if number is not None:
            _body["number"] = number
        if vat_id is not None:
            _body["vatId"] = vat_id
        if type is not None:
            _body["type"] = type
        if credit_limit is not None:
            _body["creditLimit"] = credit_limit
        if address_contact_ids is not None:
            _body["addressContactIds"] = str(address_contact_ids)
        if sale_terms_of_payment_id is not None:
            _body["saleTermsOfPaymentId"] = str(sale_terms_of_payment_id)
        if purchase_terms_of_payment_id is not None:
            _body["purchaseTermsOfPaymentId"] = str(purchase_terms_of_payment_id)
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if personal_account_group_id is not None:
            _body["personalAccountGroupId"] = str(personal_account_group_id)
        response = await self._http.patch(
            f"{_PREFIX}/PersonalAccount/{id}",
            json=_body,
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def delete_personal_account_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a personal account."""
        response = await self._http.delete(
            f"{_PREFIX}/PersonalAccount/{id}",
        )
        response.raise_for_status()

    async def get_by_contact_id(
        self,
        contact_id: UUID,
    ) -> None:
        """Get all personal accounts, attached to a contact"""
        response = await self._http.get(
            f"{_PREFIX}/PersonalAccount/get-by-contact-id/{contact_id}",
        )
        response.raise_for_status()

    async def add_address(
        self,
        id: UUID,
        contact_id: UUID,
    ) -> PersonalAccountModel:
        """Adds an address given by ID to a personal account."""
        response = await self._http.put(
            f"{_PREFIX}/PersonalAccount/add-address/{id}/{contact_id}",
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def remove_address(
        self,
        id: UUID,
        contact_id: UUID,
    ) -> PersonalAccountModel:
        """Removes an address given by ID from a personal account."""
        response = await self._http.put(
            f"{_PREFIX}/PersonalAccount/remove-address/{id}/{contact_id}",
        )
        response.raise_for_status()
        return PersonalAccountModel.model_validate(response.json())

    async def search(
        self,
        text: str | None = None,
        skip: int | None = None,
        limit: int | None = None,
    ) -> None:
        """Retrieves a data page of personal accounts for comboboxes."""
        _params: dict[str, object] = {}
        if text is not None:
            _params["text"] = text
        if skip is not None:
            _params["skip"] = skip
        if limit is not None:
            _params["limit"] = limit
        response = await self._http.get(
            f"{_PREFIX}/PersonalAccount/search",
            params=_params,
        )
        response.raise_for_status()

    async def reindex(
        self,
    ) -> None:
        """Retrieves a data page of personal accounts for comboboxes."""
        response = await self._http.post(
            f"{_PREFIX}/PersonalAccount/reindex",
        )
        response.raise_for_status()

    async def get_personal_account_group(
        self,
    ) -> None:
        """Gets all personal account groups."""
        response = await self._http.get(
            f"{_PREFIX}/PersonalAccountGroup",
        )
        response.raise_for_status()

    async def create_personal_account_group(
        self,
        number: str | None = None,
        name: str | None = None,
    ) -> PersonalAccountGroupModel:
        """Creates a new personal account group."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        response = await self._http.post(
            f"{_PREFIX}/PersonalAccountGroup",
            json=_body,
        )
        response.raise_for_status()
        return PersonalAccountGroupModel.model_validate(response.json())

    async def get_personal_account_group_by_id(
        self,
        id: UUID,
    ) -> PersonalAccountGroupModel:
        """Gets a personal account group by ID."""
        response = await self._http.get(
            f"{_PREFIX}/PersonalAccountGroup/{id}",
        )
        response.raise_for_status()
        return PersonalAccountGroupModel.model_validate(response.json())

    async def update_personal_account_group_by_id(
        self,
        id: UUID,
        number: str | None = None,
        name: str | None = None,
    ) -> PersonalAccountGroupModel:
        """Patches a personal account group."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        response = await self._http.patch(
            f"{_PREFIX}/PersonalAccountGroup/{id}",
            json=_body,
        )
        response.raise_for_status()
        return PersonalAccountGroupModel.model_validate(response.json())

    async def delete_personal_account_group_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a personal account group."""
        response = await self._http.delete(
            f"{_PREFIX}/PersonalAccountGroup/{id}",
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

    async def get_split_configuration(
        self,
    ) -> None:
        """Gets all split configurations."""
        response = await self._http.get(
            f"{_PREFIX}/SplitConfiguration",
        )
        response.raise_for_status()

    async def create_split_configuration(
        self,
        number: str | None = None,
        name: str | None = None,
        split_definitions: list[SplitDefinition] | None = None,
    ) -> SplitConfigurationModel:
        """Creates a new split configuration."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if split_definitions is not None:
            _body["splitDefinitions"] = split_definitions
        response = await self._http.post(
            f"{_PREFIX}/SplitConfiguration",
            json=_body,
        )
        response.raise_for_status()
        return SplitConfigurationModel.model_validate(response.json())

    async def get_split_configuration_by_id(
        self,
        id: UUID,
    ) -> SplitConfigurationModel:
        """Gets a split configuration by ID."""
        response = await self._http.get(
            f"{_PREFIX}/SplitConfiguration/{id}",
        )
        response.raise_for_status()
        return SplitConfigurationModel.model_validate(response.json())

    async def update_split_configuration_by_id(
        self,
        id: UUID,
        number: str | None = None,
        name: str | None = None,
        split_definitions: list[SplitDefinition] | None = None,
    ) -> SplitConfigurationModel:
        """Patches a split configuration."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if split_definitions is not None:
            _body["splitDefinitions"] = split_definitions
        response = await self._http.patch(
            f"{_PREFIX}/SplitConfiguration/{id}",
            json=_body,
        )
        response.raise_for_status()
        return SplitConfigurationModel.model_validate(response.json())

    async def delete_split_configuration_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a split configuration."""
        response = await self._http.delete(
            f"{_PREFIX}/SplitConfiguration/{id}",
        )
        response.raise_for_status()

    async def create_tax_group(
        self,
        number: int,
        name: str,
        countries: list[TaxGroupCountryIsoRequest],
    ) -> TaxGroupModel:
        """Creates a new tax group."""
        response = await self._http.post(
            f"{_PREFIX}/TaxGroup",
            json={"number": number, "name": name, "countries": countries},
        )
        response.raise_for_status()
        return TaxGroupModel.model_validate(response.json())

    async def get_tax_group_by_id(
        self,
        id: UUID,
    ) -> TaxGroupModel:
        """Gets a tax group by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TaxGroup/{id}",
        )
        response.raise_for_status()
        return TaxGroupModel.model_validate(response.json())

    async def update_tax_group_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
        countries: list[TaxGroupCountryIsoRequest] | None = None,
    ) -> TaxGroupModel:
        """Patches a tax group."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if countries is not None:
            _body["countries"] = countries
        response = await self._http.patch(
            f"{_PREFIX}/TaxGroup/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TaxGroupModel.model_validate(response.json())

    async def delete_tax_group_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a tax group."""
        response = await self._http.delete(
            f"{_PREFIX}/TaxGroup/{id}",
        )
        response.raise_for_status()

    async def create_tax_key(
        self,
        name: str,
        value: float,
        valid_from: str,
        tax_group_id: UUID | None = None,
        tax_rate_id: UUID | None = None,
        valid_to: str | None = None,
        bu_number: int | None = None,
    ) -> TaxKeyModel:
        """Creates a new tax key."""
        _body: dict[str, object] = {
            "name": name,
            "value": value,
            "validFrom": valid_from,
        }
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if tax_rate_id is not None:
            _body["taxRateId"] = str(tax_rate_id)
        if valid_to is not None:
            _body["validTo"] = valid_to
        if bu_number is not None:
            _body["buNumber"] = bu_number
        response = await self._http.post(
            f"{_PREFIX}/TaxKey",
            json=_body,
        )
        response.raise_for_status()
        return TaxKeyModel.model_validate(response.json())

    async def get_tax_key_by_id(
        self,
        id: UUID,
    ) -> TaxKeyModel:
        """Gets a tax key by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TaxKey/{id}",
        )
        response.raise_for_status()
        return TaxKeyModel.model_validate(response.json())

    async def update_tax_key_by_id(
        self,
        id: UUID,
        name: str | None = None,
        tax_group_id: UUID | None = None,
        tax_rate_id: UUID | None = None,
        value: float | None = None,
        valid_from: str | None = None,
        valid_to: str | None = None,
        bu_number: int | None = None,
    ) -> TaxKeyModel:
        """Patches a tax key."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if tax_rate_id is not None:
            _body["taxRateId"] = str(tax_rate_id)
        if value is not None:
            _body["value"] = value
        if valid_from is not None:
            _body["validFrom"] = valid_from
        if valid_to is not None:
            _body["validTo"] = valid_to
        if bu_number is not None:
            _body["buNumber"] = bu_number
        response = await self._http.patch(
            f"{_PREFIX}/TaxKey/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TaxKeyModel.model_validate(response.json())

    async def delete_tax_key_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a tax key."""
        response = await self._http.delete(
            f"{_PREFIX}/TaxKey/{id}",
        )
        response.raise_for_status()

    async def create_tax_rate(
        self,
        number: int,
        name: str,
    ) -> TaxRateModel:
        """Creates a new tax rate."""
        response = await self._http.post(
            f"{_PREFIX}/TaxRate",
            json={"number": number, "name": name},
        )
        response.raise_for_status()
        return TaxRateModel.model_validate(response.json())

    async def get_tax_rate_by_id(
        self,
        id: UUID,
    ) -> TaxRateModel:
        """Gets a tax rate by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TaxRate/{id}",
        )
        response.raise_for_status()
        return TaxRateModel.model_validate(response.json())

    async def update_tax_rate_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
    ) -> TaxRateModel:
        """Patches a tax rate."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        response = await self._http.patch(
            f"{_PREFIX}/TaxRate/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TaxRateModel.model_validate(response.json())

    async def delete_tax_rate_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a tax rate."""
        response = await self._http.delete(
            f"{_PREFIX}/TaxRate/{id}",
        )
        response.raise_for_status()

    async def create_terms_of_payment(
        self,
        number: int,
        name: str,
        payment_deadline_days: int,
        cash_discount: float | None = None,
        cash_discount_days: int | None = None,
        states: list[str] | None = None,
        formatted_text: str | None = None,
    ) -> TermsOfPaymentModel:
        """Creates a new terms of payment configuration."""
        _body: dict[str, object] = {
            "number": number,
            "name": name,
            "paymentDeadlineDays": payment_deadline_days,
        }
        if cash_discount is not None:
            _body["cashDiscount"] = cash_discount
        if cash_discount_days is not None:
            _body["cashDiscountDays"] = cash_discount_days
        if states is not None:
            _body["states"] = states
        if formatted_text is not None:
            _body["formattedText"] = formatted_text
        response = await self._http.post(
            f"{_PREFIX}/TermsOfPayment",
            json=_body,
        )
        response.raise_for_status()
        return TermsOfPaymentModel.model_validate(response.json())

    async def get_terms_of_payment_by_id(
        self,
        id: UUID,
    ) -> TermsOfPaymentModel:
        """Gets a terms of payment configuration by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TermsOfPayment/{id}",
        )
        response.raise_for_status()
        return TermsOfPaymentModel.model_validate(response.json())

    async def update_terms_of_payment_by_id(
        self,
        id: UUID,
        number: int | None = None,
        name: str | None = None,
        cash_discount: float | None = None,
        cash_discount_days: int | None = None,
        payment_deadline_days: int | None = None,
        states: list[str] | None = None,
        formatted_text: str | None = None,
    ) -> TermsOfPaymentModel:
        """Patches a terms of payment configuration."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if name is not None:
            _body["name"] = name
        if cash_discount is not None:
            _body["cashDiscount"] = cash_discount
        if cash_discount_days is not None:
            _body["cashDiscountDays"] = cash_discount_days
        if payment_deadline_days is not None:
            _body["paymentDeadlineDays"] = payment_deadline_days
        if states is not None:
            _body["states"] = states
        if formatted_text is not None:
            _body["formattedText"] = formatted_text
        response = await self._http.patch(
            f"{_PREFIX}/TermsOfPayment/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TermsOfPaymentModel.model_validate(response.json())

    async def delete_terms_of_payment_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a terms of payment configuration."""
        response = await self._http.delete(
            f"{_PREFIX}/TermsOfPayment/{id}",
        )
        response.raise_for_status()

    async def create_transaction(
        self,
        number: str,
        type_id: UUID,
        subtype_id: UUID,
        is_gross: bool,
        creator: TransactionContactRequest | None = None,
        reference: str | None = None,
        date: str | None = None,
        delivery_date: str | None = None,
        terms_of_payment_id: UUID | None = None,
        payment_method_id: UUID | None = None,
        currency_id: UUID | None = None,
        description: str | None = None,
        financial_partner: TransactionContactRequest | None = None,
        delivery_address: TransactionContactRequest | None = None,
        invoice_recipient: TransactionContactRequest | None = None,
        payer: TransactionContactRequest | None = None,
        responsible: TransactionContactRequest | None = None,
        representative: TransactionContactRequest | None = None,
        items: list[TransactionItemRequest] | None = None,
        alternative_payment_deadline: str | None = None,
        balance: float | None = None,
        barcode: str | None = None,
        bill_to_text: str | None = None,
        cash_discount_percent_value: float | None = None,
        cash_discount_total: float | None = None,
        financial_accounting_period_id: UUID | None = None,
        period_id: UUID | None = None,
        manual_vat: TransactionManualVatRequest | None = None,
        notes: str | None = None,
        due_date: str | None = None,
        reference_number: str | None = None,
        tax_group_id: UUID | None = None,
        operation_item_combination_mode: OperationItemCombinationModeModel | None = None,
        financial_export_disabled: bool | None = None,
        default_cost_centers: list[CostCenterAssignmentRequest] | None = None,
        default_cost_objects: list[CostCenterAssignmentRequest] | None = None,
        metadata_processing_data: MetadataProcessingDataRequest | None = None,
    ) -> TransactionResultModel:
        """Creates a new transaction."""
        _body: dict[str, object] = {
            "number": number,
            "typeId": str(type_id),
            "subtypeId": str(subtype_id),
            "isGross": is_gross,
        }
        if creator is not None:
            _body["creator"] = creator
        if reference is not None:
            _body["reference"] = reference
        if date is not None:
            _body["date"] = date
        if delivery_date is not None:
            _body["deliveryDate"] = delivery_date
        if terms_of_payment_id is not None:
            _body["termsOfPaymentId"] = str(terms_of_payment_id)
        if payment_method_id is not None:
            _body["paymentMethodId"] = str(payment_method_id)
        if currency_id is not None:
            _body["currencyId"] = str(currency_id)
        if description is not None:
            _body["description"] = description
        if financial_partner is not None:
            _body["financialPartner"] = financial_partner
        if delivery_address is not None:
            _body["deliveryAddress"] = delivery_address
        if invoice_recipient is not None:
            _body["invoiceRecipient"] = invoice_recipient
        if payer is not None:
            _body["payer"] = payer
        if responsible is not None:
            _body["responsible"] = responsible
        if representative is not None:
            _body["representative"] = representative
        if items is not None:
            _body["items"] = items
        if alternative_payment_deadline is not None:
            _body["alternativePaymentDeadline"] = alternative_payment_deadline
        if balance is not None:
            _body["balance"] = balance
        if barcode is not None:
            _body["barcode"] = barcode
        if bill_to_text is not None:
            _body["billToText"] = bill_to_text
        if cash_discount_percent_value is not None:
            _body["cashDiscountPercentValue"] = cash_discount_percent_value
        if cash_discount_total is not None:
            _body["cashDiscountTotal"] = cash_discount_total
        if financial_accounting_period_id is not None:
            _body["financialAccountingPeriodId"] = str(financial_accounting_period_id)
        if period_id is not None:
            _body["periodId"] = str(period_id)
        if manual_vat is not None:
            _body["manualVAT"] = manual_vat
        if notes is not None:
            _body["notes"] = notes
        if due_date is not None:
            _body["dueDate"] = due_date
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if operation_item_combination_mode is not None:
            _body["operationItemCombinationMode"] = operation_item_combination_mode
        if financial_export_disabled is not None:
            _body["financialExportDisabled"] = financial_export_disabled
        if default_cost_centers is not None:
            _body["defaultCostCenters"] = default_cost_centers
        if default_cost_objects is not None:
            _body["defaultCostObjects"] = default_cost_objects
        if metadata_processing_data is not None:
            _body["metadataProcessingData"] = metadata_processing_data
        response = await self._http.post(
            f"{_PREFIX}/Transaction",
            json=_body,
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def get_drafts(
        self,
    ) -> None:
        """Gets all draft transactions."""
        response = await self._http.get(
            f"{_PREFIX}/Transaction/drafts",
        )
        response.raise_for_status()

    async def drafts(
        self,
        billing_line_ids: list[UUID] | None = None,
        target: SplitTarget | None = None,
        split_configuration_id: UUID | None = None,
    ) -> DraftTransactionsResultModel:
        """Creates a set of draft transactions resulting from a set of billing lines."""
        _body: dict[str, object] = {
        }
        if billing_line_ids is not None:
            _body["billingLineIds"] = str(billing_line_ids)
        if target is not None:
            _body["target"] = target
        if split_configuration_id is not None:
            _body["splitConfigurationId"] = str(split_configuration_id)
        response = await self._http.post(
            f"{_PREFIX}/Transaction/drafts",
            json=_body,
        )
        response.raise_for_status()
        return DraftTransactionsResultModel.model_validate(response.json())

    async def drafts_billing_lines(
        self,
        id: UUID,
        draft_transaction_id: UUID | None = None,
        billing_line_ids: list[UUID] | None = None,
    ) -> TransactionResultModel:
        """Adds a set of billing lines to an existing draft transaction."""
        _body: dict[str, object] = {
        }
        if draft_transaction_id is not None:
            _body["draftTransactionId"] = str(draft_transaction_id)
        if billing_line_ids is not None:
            _body["billingLineIds"] = str(billing_line_ids)
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/drafts/{id}/billing-lines",
            json=_body,
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def drafts_billing_lines_remove(
        self,
        billing_line_ids: list[UUID] | None = None,
    ) -> DraftTransactionsResultModel:
        """Removes a set of billing line transaction items from their respective assigned draft transaction by billing line IDs.
Billing lines may belong to different draft transactions; each is updated independently."""
        _body: dict[str, object] = {
        }
        if billing_line_ids is not None:
            _body["billingLineIds"] = str(billing_line_ids)
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/drafts/billing-lines/remove",
            json=_body,
        )
        response.raise_for_status()
        return DraftTransactionsResultModel.model_validate(response.json())

    async def preview(
        self,
        creator: TransactionContactRequest | None = None,
        number: str | None = None,
        reference: str | None = None,
        type_id: UUID | None = None,
        subtype_id: UUID | None = None,
        date: str | None = None,
        delivery_date: str | None = None,
        terms_of_payment_id: UUID | None = None,
        payment_method_id: UUID | None = None,
        currency_id: UUID | None = None,
        description: str | None = None,
        financial_partner: TransactionContactRequest | None = None,
        delivery_address: TransactionContactRequest | None = None,
        invoice_recipient: TransactionContactRequest | None = None,
        payer: TransactionContactRequest | None = None,
        responsible: TransactionContactRequest | None = None,
        representative: TransactionContactRequest | None = None,
        items: list[PreviewTransactionItemRequest] | None = None,
        alternative_payment_deadline: str | None = None,
        balance: float | None = None,
        barcode: str | None = None,
        bill_to_text: str | None = None,
        cash_discount_percent_value: float | None = None,
        cash_discount_total: float | None = None,
        financial_accounting_period_id: UUID | None = None,
        period_id: UUID | None = None,
        manual_vat: TransactionManualVatRequest | None = None,
        notes: str | None = None,
        due_date: str | None = None,
        reference_number: str | None = None,
        tax_group_id: UUID | None = None,
        operation_item_combination_mode: OperationItemCombinationModeModel | None = None,
        is_gross: bool | None = None,
        financial_export_disabled: bool | None = None,
        default_cost_centers: list[CostCenterAssignmentRequest] | None = None,
        default_cost_objects: list[CostCenterAssignmentRequest] | None = None,
        metadata_processing_data: MetadataProcessingDataRequest | None = None,
        validate_price_input: bool | None = None,
    ) -> PreviewTransactionModel:
        """Validates and creates a preview for a transaction."""
        _body: dict[str, object] = {
        }
        if creator is not None:
            _body["creator"] = creator
        if number is not None:
            _body["number"] = number
        if reference is not None:
            _body["reference"] = reference
        if type_id is not None:
            _body["typeId"] = str(type_id)
        if subtype_id is not None:
            _body["subtypeId"] = str(subtype_id)
        if date is not None:
            _body["date"] = date
        if delivery_date is not None:
            _body["deliveryDate"] = delivery_date
        if terms_of_payment_id is not None:
            _body["termsOfPaymentId"] = str(terms_of_payment_id)
        if payment_method_id is not None:
            _body["paymentMethodId"] = str(payment_method_id)
        if currency_id is not None:
            _body["currencyId"] = str(currency_id)
        if description is not None:
            _body["description"] = description
        if financial_partner is not None:
            _body["financialPartner"] = financial_partner
        if delivery_address is not None:
            _body["deliveryAddress"] = delivery_address
        if invoice_recipient is not None:
            _body["invoiceRecipient"] = invoice_recipient
        if payer is not None:
            _body["payer"] = payer
        if responsible is not None:
            _body["responsible"] = responsible
        if representative is not None:
            _body["representative"] = representative
        if items is not None:
            _body["items"] = items
        if alternative_payment_deadline is not None:
            _body["alternativePaymentDeadline"] = alternative_payment_deadline
        if balance is not None:
            _body["balance"] = balance
        if barcode is not None:
            _body["barcode"] = barcode
        if bill_to_text is not None:
            _body["billToText"] = bill_to_text
        if cash_discount_percent_value is not None:
            _body["cashDiscountPercentValue"] = cash_discount_percent_value
        if cash_discount_total is not None:
            _body["cashDiscountTotal"] = cash_discount_total
        if financial_accounting_period_id is not None:
            _body["financialAccountingPeriodId"] = str(financial_accounting_period_id)
        if period_id is not None:
            _body["periodId"] = str(period_id)
        if manual_vat is not None:
            _body["manualVAT"] = manual_vat
        if notes is not None:
            _body["notes"] = notes
        if due_date is not None:
            _body["dueDate"] = due_date
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if operation_item_combination_mode is not None:
            _body["operationItemCombinationMode"] = operation_item_combination_mode
        if is_gross is not None:
            _body["isGross"] = is_gross
        if financial_export_disabled is not None:
            _body["financialExportDisabled"] = financial_export_disabled
        if default_cost_centers is not None:
            _body["defaultCostCenters"] = default_cost_centers
        if default_cost_objects is not None:
            _body["defaultCostObjects"] = default_cost_objects
        if metadata_processing_data is not None:
            _body["metadataProcessingData"] = metadata_processing_data
        if validate_price_input is not None:
            _body["validatePriceInput"] = validate_price_input
        response = await self._http.post(
            f"{_PREFIX}/Transaction/preview",
            json=_body,
        )
        response.raise_for_status()
        return PreviewTransactionModel.model_validate(response.json())

    async def get_transaction_by_id(
        self,
        id: UUID,
        lock_resource: bool | None = None,
    ) -> TransactionModel:
        """Gets a transaction by ID."""
        _params: dict[str, object] = {}
        if lock_resource is not None:
            _params["lockResource"] = lock_resource
        response = await self._http.get(
            f"{_PREFIX}/Transaction/{id}",
            params=_params,
        )
        response.raise_for_status()
        return TransactionModel.model_validate(response.json())

    async def update_transaction_by_id(
        self,
        id: UUID,
        number: str | None = None,
        reference: str | None = None,
        type_id: UUID | None = None,
        subtype_id: UUID | None = None,
        date: str | None = None,
        delivery_date: str | None = None,
        terms_of_payment_id: UUID | None = None,
        payment_method_id: UUID | None = None,
        currency_id: UUID | None = None,
        description: str | None = None,
        financial_partner: TransactionContactRequest | None = None,
        delivery_address: TransactionContactRequest | None = None,
        invoice_recipient: TransactionContactRequest | None = None,
        payer: TransactionContactRequest | None = None,
        responsible: TransactionContactRequest | None = None,
        representative: TransactionContactRequest | None = None,
        items: list[TransactionItemRequest] | None = None,
        alternative_payment_deadline: str | None = None,
        balance: float | None = None,
        barcode: str | None = None,
        bill_to_text: str | None = None,
        cash_discount_percent_value: float | None = None,
        cash_discount_total: float | None = None,
        financial_accounting_period_id: UUID | None = None,
        period_id: UUID | None = None,
        states: list[str] | None = None,
        manual_vat: TransactionManualVatRequest | None = None,
        notes: str | None = None,
        due_date: str | None = None,
        reference_number: str | None = None,
        tax_group_id: UUID | None = None,
        operation_item_combination_mode: OperationItemCombinationModeModel | None = None,
        is_gross: bool | None = None,
        financial_export_disabled: bool | None = None,
        default_cost_centers: list[CostCenterAssignmentRequest] | None = None,
        default_cost_objects: list[CostCenterAssignmentRequest] | None = None,
        metadata_processing_data: MetadataProcessingDataRequest | None = None,
    ) -> TransactionResultModel:
        """Patches a transaction."""
        _body: dict[str, object] = {
        }
        if number is not None:
            _body["number"] = number
        if reference is not None:
            _body["reference"] = reference
        if type_id is not None:
            _body["typeId"] = str(type_id)
        if subtype_id is not None:
            _body["subtypeId"] = str(subtype_id)
        if date is not None:
            _body["date"] = date
        if delivery_date is not None:
            _body["deliveryDate"] = delivery_date
        if terms_of_payment_id is not None:
            _body["termsOfPaymentId"] = str(terms_of_payment_id)
        if payment_method_id is not None:
            _body["paymentMethodId"] = str(payment_method_id)
        if currency_id is not None:
            _body["currencyId"] = str(currency_id)
        if description is not None:
            _body["description"] = description
        if financial_partner is not None:
            _body["financialPartner"] = financial_partner
        if delivery_address is not None:
            _body["deliveryAddress"] = delivery_address
        if invoice_recipient is not None:
            _body["invoiceRecipient"] = invoice_recipient
        if payer is not None:
            _body["payer"] = payer
        if responsible is not None:
            _body["responsible"] = responsible
        if representative is not None:
            _body["representative"] = representative
        if items is not None:
            _body["items"] = items
        if alternative_payment_deadline is not None:
            _body["alternativePaymentDeadline"] = alternative_payment_deadline
        if balance is not None:
            _body["balance"] = balance
        if barcode is not None:
            _body["barcode"] = barcode
        if bill_to_text is not None:
            _body["billToText"] = bill_to_text
        if cash_discount_percent_value is not None:
            _body["cashDiscountPercentValue"] = cash_discount_percent_value
        if cash_discount_total is not None:
            _body["cashDiscountTotal"] = cash_discount_total
        if financial_accounting_period_id is not None:
            _body["financialAccountingPeriodId"] = str(financial_accounting_period_id)
        if period_id is not None:
            _body["periodId"] = str(period_id)
        if states is not None:
            _body["states"] = states
        if manual_vat is not None:
            _body["manualVAT"] = manual_vat
        if notes is not None:
            _body["notes"] = notes
        if due_date is not None:
            _body["dueDate"] = due_date
        if reference_number is not None:
            _body["referenceNumber"] = reference_number
        if tax_group_id is not None:
            _body["taxGroupId"] = str(tax_group_id)
        if operation_item_combination_mode is not None:
            _body["operationItemCombinationMode"] = operation_item_combination_mode
        if is_gross is not None:
            _body["isGross"] = is_gross
        if financial_export_disabled is not None:
            _body["financialExportDisabled"] = financial_export_disabled
        if default_cost_centers is not None:
            _body["defaultCostCenters"] = default_cost_centers
        if default_cost_objects is not None:
            _body["defaultCostObjects"] = default_cost_objects
        if metadata_processing_data is not None:
            _body["metadataProcessingData"] = metadata_processing_data
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def delete_transaction_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a transaction."""
        response = await self._http.delete(
            f"{_PREFIX}/Transaction/{id}",
        )
        response.raise_for_status()

    async def convert_transactions(
        self,
        transaction_subsets: dict[str, dict[str, float]],
        target_type_id: UUID,
        commit: bool,
        target_subtype_id: UUID | None = None,
        check_compatible_properties: list[str] | None = None,
    ) -> ConvertResultModel:
        """Converts a set of transactions."""
        _body: dict[str, object] = {
            "transactionSubsets": transaction_subsets,
            "targetTypeId": str(target_type_id),
            "commit": commit,
        }
        if target_subtype_id is not None:
            _body["targetSubtypeId"] = str(target_subtype_id)
        if check_compatible_properties is not None:
            _body["checkCompatibleProperties"] = check_compatible_properties
        response = await self._http.post(
            f"{_PREFIX}/Transaction/convert-transactions",
            json=_body,
        )
        response.raise_for_status()
        return ConvertResultModel.model_validate(response.json())

    async def cancel(
        self,
        id: UUID,
    ) -> TransactionResultModel:
        """Cancels a transaction."""
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/cancel/{id}",
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def get_by_barcode(
        self,
        barcode: str,
    ) -> TransactionModel:
        """Gets a transaction by barcode."""
        response = await self._http.get(
            f"{_PREFIX}/Transaction/by-barcode/{barcode}",
        )
        response.raise_for_status()
        return TransactionModel.model_validate(response.json())

    async def get_by_date(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> None:
        """Gets a set of transactions occuring between two points in time."""
        _params: dict[str, object] = {}
        if from_ is not None:
            _params["from"] = from_
        if to is not None:
            _params["to"] = to
        response = await self._http.get(
            f"{_PREFIX}/Transaction/by-date",
            params=_params,
        )
        response.raise_for_status()

    async def get_by_number(
        self,
        number: str,
    ) -> None:
        """Gets a set of transactions by number."""
        response = await self._http.get(
            f"{_PREFIX}/Transaction/by-number/{number}",
        )
        response.raise_for_status()

    async def drafts_convert(
        self,
        id: UUID,
        target_type_id: UUID | None = None,
        target_subtype_id: UUID | None = None,
    ) -> TransactionResultModel:
        """Converts a draft transaction to a regular, non-draft transaction."""
        _body: dict[str, object] = {
        }
        if target_type_id is not None:
            _body["targetTypeId"] = str(target_type_id)
        if target_subtype_id is not None:
            _body["targetSubtypeId"] = str(target_subtype_id)
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/drafts/{id}/convert",
            json=_body,
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def revert_to_draft(
        self,
        id: UUID,
    ) -> TransactionResultModel:
        """Reverts a non-draft transaction back to draft state."""
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/{id}/revert-to-draft",
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def drafts_billing_lines_distribute(
        self,
        billing_line_ids: list[UUID] | None = None,
        pinned_transaction_ids: dict[str, UUID] | None = None,
        split_configuration_id: UUID | None = None,
    ) -> DistributeBillingLinesToDraftTransactionsResultModel:
        """Distributes a set of billing lines onto existing draft transactions according to a split configuration.
Billing lines with a pinned transaction ID are assigned directly; all others are matched via the split configuration.
When multiple draft transactions are eligible for a billing line it is reported as ambiguous."""
        _body: dict[str, object] = {
        }
        if billing_line_ids is not None:
            _body["billingLineIds"] = str(billing_line_ids)
        if pinned_transaction_ids is not None:
            _body["pinnedTransactionIds"] = str(pinned_transaction_ids)
        if split_configuration_id is not None:
            _body["splitConfigurationId"] = str(split_configuration_id)
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/drafts/billing-lines/distribute",
            json=_body,
        )
        response.raise_for_status()
        return DistributeBillingLinesToDraftTransactionsResultModel.model_validate(response.json())

    async def print(
        self,
        id: UUID,
    ) -> TransactionResultModel:
        """Prints a transaction by rendering its report, uploading it to the CDN
and creating a linked document entry."""
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/print/{id}",
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def revert_print(
        self,
        id: UUID,
    ) -> TransactionResultModel:
        """Reverts the printed state of a transaction."""
        response = await self._http.patch(
            f"{_PREFIX}/Transaction/revert-print/{id}",
        )
        response.raise_for_status()
        return TransactionResultModel.model_validate(response.json())

    async def create_transaction_item_type(
        self,
        name: str,
        number: int,
        has_position_number: bool,
        is_selectable: bool,
        deserialization_type: str | None = None,
        detail_html: str | None = None,
        data_template: str | None = None,
        article_gla_resolver: str | None = None,
        code: str | None = None,
    ) -> TransactionItemTypeModel:
        """Creates a new transaction item type."""
        _body: dict[str, object] = {
            "name": name,
            "number": number,
            "hasPositionNumber": has_position_number,
            "isSelectable": is_selectable,
        }
        if deserialization_type is not None:
            _body["deserializationType"] = deserialization_type
        if detail_html is not None:
            _body["detailHtml"] = detail_html
        if data_template is not None:
            _body["dataTemplate"] = data_template
        if article_gla_resolver is not None:
            _body["articleGLAResolver"] = article_gla_resolver
        if code is not None:
            _body["code"] = code
        response = await self._http.post(
            f"{_PREFIX}/TransactionItemType",
            json=_body,
        )
        response.raise_for_status()
        return TransactionItemTypeModel.model_validate(response.json())

    async def get_transaction_item_type_by_id(
        self,
        id: UUID,
    ) -> TransactionItemTypeModel:
        """Gets a transaction item type by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TransactionItemType/{id}",
        )
        response.raise_for_status()
        return TransactionItemTypeModel.model_validate(response.json())

    async def update_transaction_item_type_by_id(
        self,
        id: UUID,
        deserialization_type: str | None = None,
        name: str | None = None,
        number: int | None = None,
        has_position_number: bool | None = None,
        is_selectable: bool | None = None,
        detail_html: str | None = None,
        data_template: str | None = None,
        article_gla_resolver: str | None = None,
        code: str | None = None,
    ) -> TransactionItemTypeModel:
        """Patches a transaction item type."""
        _body: dict[str, object] = {
        }
        if deserialization_type is not None:
            _body["deserializationType"] = deserialization_type
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if has_position_number is not None:
            _body["hasPositionNumber"] = has_position_number
        if is_selectable is not None:
            _body["isSelectable"] = is_selectable
        if detail_html is not None:
            _body["detailHtml"] = detail_html
        if data_template is not None:
            _body["dataTemplate"] = data_template
        if article_gla_resolver is not None:
            _body["articleGLAResolver"] = article_gla_resolver
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/TransactionItemType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TransactionItemTypeModel.model_validate(response.json())

    async def delete_transaction_item_type_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a transaction item type."""
        response = await self._http.delete(
            f"{_PREFIX}/TransactionItemType/{id}",
        )
        response.raise_for_status()

    async def create_transaction_type(
        self,
        name: str,
        number: int,
        subtypes: list[TransactionSubtypeRequest],
        report_name: str | None = None,
        short_name: str | None = None,
        functions: list[str] | None = None,
        code: str | None = None,
    ) -> TransactionTypeModel:
        """Creates a new transaction type."""
        _body: dict[str, object] = {
            "name": name,
            "number": number,
            "subtypes": subtypes,
        }
        if report_name is not None:
            _body["reportName"] = report_name
        if short_name is not None:
            _body["shortName"] = short_name
        if functions is not None:
            _body["functions"] = functions
        if code is not None:
            _body["code"] = code
        response = await self._http.post(
            f"{_PREFIX}/TransactionType",
            json=_body,
        )
        response.raise_for_status()
        return TransactionTypeModel.model_validate(response.json())

    async def get_transaction_type_by_id(
        self,
        id: UUID,
    ) -> TransactionTypeModel:
        """Gets a transaction type by ID."""
        response = await self._http.get(
            f"{_PREFIX}/TransactionType/{id}",
        )
        response.raise_for_status()
        return TransactionTypeModel.model_validate(response.json())

    async def update_transaction_type_by_id(
        self,
        id: UUID,
        name: str | None = None,
        number: int | None = None,
        report_name: str | None = None,
        short_name: str | None = None,
        functions: list[str] | None = None,
        subtypes: list[TransactionSubtypeRequest] | None = None,
        code: str | None = None,
    ) -> TransactionTypeModel:
        """Patches a transaction type."""
        _body: dict[str, object] = {
        }
        if name is not None:
            _body["name"] = name
        if number is not None:
            _body["number"] = number
        if report_name is not None:
            _body["reportName"] = report_name
        if short_name is not None:
            _body["shortName"] = short_name
        if functions is not None:
            _body["functions"] = functions
        if subtypes is not None:
            _body["subtypes"] = subtypes
        if code is not None:
            _body["code"] = code
        response = await self._http.patch(
            f"{_PREFIX}/TransactionType/{id}",
            json=_body,
        )
        response.raise_for_status()
        return TransactionTypeModel.model_validate(response.json())

    async def delete_transaction_type_by_id(
        self,
        id: UUID,
    ) -> None:
        """Deletes a transaction type."""
        response = await self._http.delete(
            f"{_PREFIX}/TransactionType/{id}",
        )
        response.raise_for_status()
