# coding: utf-8

"""
    OpenBB Platform API

    Investment research for everyone, anywhere.

    The version of the OpenAPI document: 1
    Contact: hello@openbb.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class IntrinioCashFlowStatementData(BaseModel):
    """
    Intrinio Cash Flow Statement Data.
    """ # noqa: E501
    period_ending: date = Field(description="The end date of the reporting period.")
    fiscal_period: Optional[StrictStr] = None
    fiscal_year: Optional[StrictInt] = None
    reported_currency: Optional[StrictStr] = None
    net_income_continuing_operations: Optional[Union[StrictFloat, StrictInt]] = None
    net_income_discontinued_operations: Optional[Union[StrictFloat, StrictInt]] = None
    net_income: Optional[Union[StrictFloat, StrictInt]] = None
    provision_for_loan_losses: Optional[Union[StrictFloat, StrictInt]] = None
    provision_for_credit_losses: Optional[Union[StrictFloat, StrictInt]] = None
    depreciation_expense: Optional[Union[StrictFloat, StrictInt]] = None
    amortization_expense: Optional[Union[StrictFloat, StrictInt]] = None
    share_based_compensation: Optional[Union[StrictFloat, StrictInt]] = None
    non_cash_adjustments_to_reconcile_net_income: Optional[Union[StrictFloat, StrictInt]] = None
    changes_in_operating_assets_and_liabilities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_continuing_operating_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_discontinued_operating_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_operating_activities: Optional[Union[StrictFloat, StrictInt]] = None
    divestitures: Optional[Union[StrictFloat, StrictInt]] = None
    sale_of_property_plant_and_equipment: Optional[Union[StrictFloat, StrictInt]] = None
    acquisitions: Optional[Union[StrictFloat, StrictInt]] = None
    purchase_of_investments: Optional[Union[StrictFloat, StrictInt]] = None
    purchase_of_investment_securities: Optional[Union[StrictFloat, StrictInt]] = None
    sale_and_maturity_of_investments: Optional[Union[StrictFloat, StrictInt]] = None
    loans_held_for_sale: Optional[Union[StrictFloat, StrictInt]] = None
    purchase_of_property_plant_and_equipment: Optional[Union[StrictFloat, StrictInt]] = None
    other_investing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_continuing_investing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_discontinued_investing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_investing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    payment_of_dividends: Optional[Union[StrictFloat, StrictInt]] = None
    repurchase_of_common_equity: Optional[Union[StrictFloat, StrictInt]] = None
    repurchase_of_preferred_equity: Optional[Union[StrictFloat, StrictInt]] = None
    issuance_of_common_equity: Optional[Union[StrictFloat, StrictInt]] = None
    issuance_of_preferred_equity: Optional[Union[StrictFloat, StrictInt]] = None
    issuance_of_debt: Optional[Union[StrictFloat, StrictInt]] = None
    repayment_of_debt: Optional[Union[StrictFloat, StrictInt]] = None
    other_financing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    cash_interest_received: Optional[Union[StrictFloat, StrictInt]] = None
    net_change_in_deposits: Optional[Union[StrictFloat, StrictInt]] = None
    net_increase_in_fed_funds_sold: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_continuing_financing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_discontinued_financing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    net_cash_from_financing_activities: Optional[Union[StrictFloat, StrictInt]] = None
    effect_of_exchange_rate_changes: Optional[Union[StrictFloat, StrictInt]] = None
    other_net_changes_in_cash: Optional[Union[StrictFloat, StrictInt]] = None
    net_change_in_cash_and_equivalents: Optional[Union[StrictFloat, StrictInt]] = None
    cash_income_taxes_paid: Optional[Union[StrictFloat, StrictInt]] = None
    cash_interest_paid: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["period_ending", "fiscal_period", "fiscal_year", "reported_currency", "net_income_continuing_operations", "net_income_discontinued_operations", "net_income", "provision_for_loan_losses", "provision_for_credit_losses", "depreciation_expense", "amortization_expense", "share_based_compensation", "non_cash_adjustments_to_reconcile_net_income", "changes_in_operating_assets_and_liabilities", "net_cash_from_continuing_operating_activities", "net_cash_from_discontinued_operating_activities", "net_cash_from_operating_activities", "divestitures", "sale_of_property_plant_and_equipment", "acquisitions", "purchase_of_investments", "purchase_of_investment_securities", "sale_and_maturity_of_investments", "loans_held_for_sale", "purchase_of_property_plant_and_equipment", "other_investing_activities", "net_cash_from_continuing_investing_activities", "net_cash_from_discontinued_investing_activities", "net_cash_from_investing_activities", "payment_of_dividends", "repurchase_of_common_equity", "repurchase_of_preferred_equity", "issuance_of_common_equity", "issuance_of_preferred_equity", "issuance_of_debt", "repayment_of_debt", "other_financing_activities", "cash_interest_received", "net_change_in_deposits", "net_increase_in_fed_funds_sold", "net_cash_from_continuing_financing_activities", "net_cash_from_discontinued_financing_activities", "net_cash_from_financing_activities", "effect_of_exchange_rate_changes", "other_net_changes_in_cash", "net_change_in_cash_and_equivalents", "cash_income_taxes_paid", "cash_interest_paid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IntrinioCashFlowStatementData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if fiscal_period (nullable) is None
        # and model_fields_set contains the field
        if self.fiscal_period is None and "fiscal_period" in self.model_fields_set:
            _dict['fiscal_period'] = None

        # set to None if fiscal_year (nullable) is None
        # and model_fields_set contains the field
        if self.fiscal_year is None and "fiscal_year" in self.model_fields_set:
            _dict['fiscal_year'] = None

        # set to None if reported_currency (nullable) is None
        # and model_fields_set contains the field
        if self.reported_currency is None and "reported_currency" in self.model_fields_set:
            _dict['reported_currency'] = None

        # set to None if net_income_continuing_operations (nullable) is None
        # and model_fields_set contains the field
        if self.net_income_continuing_operations is None and "net_income_continuing_operations" in self.model_fields_set:
            _dict['net_income_continuing_operations'] = None

        # set to None if net_income_discontinued_operations (nullable) is None
        # and model_fields_set contains the field
        if self.net_income_discontinued_operations is None and "net_income_discontinued_operations" in self.model_fields_set:
            _dict['net_income_discontinued_operations'] = None

        # set to None if net_income (nullable) is None
        # and model_fields_set contains the field
        if self.net_income is None and "net_income" in self.model_fields_set:
            _dict['net_income'] = None

        # set to None if provision_for_loan_losses (nullable) is None
        # and model_fields_set contains the field
        if self.provision_for_loan_losses is None and "provision_for_loan_losses" in self.model_fields_set:
            _dict['provision_for_loan_losses'] = None

        # set to None if provision_for_credit_losses (nullable) is None
        # and model_fields_set contains the field
        if self.provision_for_credit_losses is None and "provision_for_credit_losses" in self.model_fields_set:
            _dict['provision_for_credit_losses'] = None

        # set to None if depreciation_expense (nullable) is None
        # and model_fields_set contains the field
        if self.depreciation_expense is None and "depreciation_expense" in self.model_fields_set:
            _dict['depreciation_expense'] = None

        # set to None if amortization_expense (nullable) is None
        # and model_fields_set contains the field
        if self.amortization_expense is None and "amortization_expense" in self.model_fields_set:
            _dict['amortization_expense'] = None

        # set to None if share_based_compensation (nullable) is None
        # and model_fields_set contains the field
        if self.share_based_compensation is None and "share_based_compensation" in self.model_fields_set:
            _dict['share_based_compensation'] = None

        # set to None if non_cash_adjustments_to_reconcile_net_income (nullable) is None
        # and model_fields_set contains the field
        if self.non_cash_adjustments_to_reconcile_net_income is None and "non_cash_adjustments_to_reconcile_net_income" in self.model_fields_set:
            _dict['non_cash_adjustments_to_reconcile_net_income'] = None

        # set to None if changes_in_operating_assets_and_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.changes_in_operating_assets_and_liabilities is None and "changes_in_operating_assets_and_liabilities" in self.model_fields_set:
            _dict['changes_in_operating_assets_and_liabilities'] = None

        # set to None if net_cash_from_continuing_operating_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_continuing_operating_activities is None and "net_cash_from_continuing_operating_activities" in self.model_fields_set:
            _dict['net_cash_from_continuing_operating_activities'] = None

        # set to None if net_cash_from_discontinued_operating_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_discontinued_operating_activities is None and "net_cash_from_discontinued_operating_activities" in self.model_fields_set:
            _dict['net_cash_from_discontinued_operating_activities'] = None

        # set to None if net_cash_from_operating_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_operating_activities is None and "net_cash_from_operating_activities" in self.model_fields_set:
            _dict['net_cash_from_operating_activities'] = None

        # set to None if divestitures (nullable) is None
        # and model_fields_set contains the field
        if self.divestitures is None and "divestitures" in self.model_fields_set:
            _dict['divestitures'] = None

        # set to None if sale_of_property_plant_and_equipment (nullable) is None
        # and model_fields_set contains the field
        if self.sale_of_property_plant_and_equipment is None and "sale_of_property_plant_and_equipment" in self.model_fields_set:
            _dict['sale_of_property_plant_and_equipment'] = None

        # set to None if acquisitions (nullable) is None
        # and model_fields_set contains the field
        if self.acquisitions is None and "acquisitions" in self.model_fields_set:
            _dict['acquisitions'] = None

        # set to None if purchase_of_investments (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_of_investments is None and "purchase_of_investments" in self.model_fields_set:
            _dict['purchase_of_investments'] = None

        # set to None if purchase_of_investment_securities (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_of_investment_securities is None and "purchase_of_investment_securities" in self.model_fields_set:
            _dict['purchase_of_investment_securities'] = None

        # set to None if sale_and_maturity_of_investments (nullable) is None
        # and model_fields_set contains the field
        if self.sale_and_maturity_of_investments is None and "sale_and_maturity_of_investments" in self.model_fields_set:
            _dict['sale_and_maturity_of_investments'] = None

        # set to None if loans_held_for_sale (nullable) is None
        # and model_fields_set contains the field
        if self.loans_held_for_sale is None and "loans_held_for_sale" in self.model_fields_set:
            _dict['loans_held_for_sale'] = None

        # set to None if purchase_of_property_plant_and_equipment (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_of_property_plant_and_equipment is None and "purchase_of_property_plant_and_equipment" in self.model_fields_set:
            _dict['purchase_of_property_plant_and_equipment'] = None

        # set to None if other_investing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.other_investing_activities is None and "other_investing_activities" in self.model_fields_set:
            _dict['other_investing_activities'] = None

        # set to None if net_cash_from_continuing_investing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_continuing_investing_activities is None and "net_cash_from_continuing_investing_activities" in self.model_fields_set:
            _dict['net_cash_from_continuing_investing_activities'] = None

        # set to None if net_cash_from_discontinued_investing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_discontinued_investing_activities is None and "net_cash_from_discontinued_investing_activities" in self.model_fields_set:
            _dict['net_cash_from_discontinued_investing_activities'] = None

        # set to None if net_cash_from_investing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_investing_activities is None and "net_cash_from_investing_activities" in self.model_fields_set:
            _dict['net_cash_from_investing_activities'] = None

        # set to None if payment_of_dividends (nullable) is None
        # and model_fields_set contains the field
        if self.payment_of_dividends is None and "payment_of_dividends" in self.model_fields_set:
            _dict['payment_of_dividends'] = None

        # set to None if repurchase_of_common_equity (nullable) is None
        # and model_fields_set contains the field
        if self.repurchase_of_common_equity is None and "repurchase_of_common_equity" in self.model_fields_set:
            _dict['repurchase_of_common_equity'] = None

        # set to None if repurchase_of_preferred_equity (nullable) is None
        # and model_fields_set contains the field
        if self.repurchase_of_preferred_equity is None and "repurchase_of_preferred_equity" in self.model_fields_set:
            _dict['repurchase_of_preferred_equity'] = None

        # set to None if issuance_of_common_equity (nullable) is None
        # and model_fields_set contains the field
        if self.issuance_of_common_equity is None and "issuance_of_common_equity" in self.model_fields_set:
            _dict['issuance_of_common_equity'] = None

        # set to None if issuance_of_preferred_equity (nullable) is None
        # and model_fields_set contains the field
        if self.issuance_of_preferred_equity is None and "issuance_of_preferred_equity" in self.model_fields_set:
            _dict['issuance_of_preferred_equity'] = None

        # set to None if issuance_of_debt (nullable) is None
        # and model_fields_set contains the field
        if self.issuance_of_debt is None and "issuance_of_debt" in self.model_fields_set:
            _dict['issuance_of_debt'] = None

        # set to None if repayment_of_debt (nullable) is None
        # and model_fields_set contains the field
        if self.repayment_of_debt is None and "repayment_of_debt" in self.model_fields_set:
            _dict['repayment_of_debt'] = None

        # set to None if other_financing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.other_financing_activities is None and "other_financing_activities" in self.model_fields_set:
            _dict['other_financing_activities'] = None

        # set to None if cash_interest_received (nullable) is None
        # and model_fields_set contains the field
        if self.cash_interest_received is None and "cash_interest_received" in self.model_fields_set:
            _dict['cash_interest_received'] = None

        # set to None if net_change_in_deposits (nullable) is None
        # and model_fields_set contains the field
        if self.net_change_in_deposits is None and "net_change_in_deposits" in self.model_fields_set:
            _dict['net_change_in_deposits'] = None

        # set to None if net_increase_in_fed_funds_sold (nullable) is None
        # and model_fields_set contains the field
        if self.net_increase_in_fed_funds_sold is None and "net_increase_in_fed_funds_sold" in self.model_fields_set:
            _dict['net_increase_in_fed_funds_sold'] = None

        # set to None if net_cash_from_continuing_financing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_continuing_financing_activities is None and "net_cash_from_continuing_financing_activities" in self.model_fields_set:
            _dict['net_cash_from_continuing_financing_activities'] = None

        # set to None if net_cash_from_discontinued_financing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_discontinued_financing_activities is None and "net_cash_from_discontinued_financing_activities" in self.model_fields_set:
            _dict['net_cash_from_discontinued_financing_activities'] = None

        # set to None if net_cash_from_financing_activities (nullable) is None
        # and model_fields_set contains the field
        if self.net_cash_from_financing_activities is None and "net_cash_from_financing_activities" in self.model_fields_set:
            _dict['net_cash_from_financing_activities'] = None

        # set to None if effect_of_exchange_rate_changes (nullable) is None
        # and model_fields_set contains the field
        if self.effect_of_exchange_rate_changes is None and "effect_of_exchange_rate_changes" in self.model_fields_set:
            _dict['effect_of_exchange_rate_changes'] = None

        # set to None if other_net_changes_in_cash (nullable) is None
        # and model_fields_set contains the field
        if self.other_net_changes_in_cash is None and "other_net_changes_in_cash" in self.model_fields_set:
            _dict['other_net_changes_in_cash'] = None

        # set to None if net_change_in_cash_and_equivalents (nullable) is None
        # and model_fields_set contains the field
        if self.net_change_in_cash_and_equivalents is None and "net_change_in_cash_and_equivalents" in self.model_fields_set:
            _dict['net_change_in_cash_and_equivalents'] = None

        # set to None if cash_income_taxes_paid (nullable) is None
        # and model_fields_set contains the field
        if self.cash_income_taxes_paid is None and "cash_income_taxes_paid" in self.model_fields_set:
            _dict['cash_income_taxes_paid'] = None

        # set to None if cash_interest_paid (nullable) is None
        # and model_fields_set contains the field
        if self.cash_interest_paid is None and "cash_interest_paid" in self.model_fields_set:
            _dict['cash_interest_paid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntrinioCashFlowStatementData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period_ending": obj.get("period_ending"),
            "fiscal_period": obj.get("fiscal_period"),
            "fiscal_year": obj.get("fiscal_year"),
            "reported_currency": obj.get("reported_currency"),
            "net_income_continuing_operations": obj.get("net_income_continuing_operations"),
            "net_income_discontinued_operations": obj.get("net_income_discontinued_operations"),
            "net_income": obj.get("net_income"),
            "provision_for_loan_losses": obj.get("provision_for_loan_losses"),
            "provision_for_credit_losses": obj.get("provision_for_credit_losses"),
            "depreciation_expense": obj.get("depreciation_expense"),
            "amortization_expense": obj.get("amortization_expense"),
            "share_based_compensation": obj.get("share_based_compensation"),
            "non_cash_adjustments_to_reconcile_net_income": obj.get("non_cash_adjustments_to_reconcile_net_income"),
            "changes_in_operating_assets_and_liabilities": obj.get("changes_in_operating_assets_and_liabilities"),
            "net_cash_from_continuing_operating_activities": obj.get("net_cash_from_continuing_operating_activities"),
            "net_cash_from_discontinued_operating_activities": obj.get("net_cash_from_discontinued_operating_activities"),
            "net_cash_from_operating_activities": obj.get("net_cash_from_operating_activities"),
            "divestitures": obj.get("divestitures"),
            "sale_of_property_plant_and_equipment": obj.get("sale_of_property_plant_and_equipment"),
            "acquisitions": obj.get("acquisitions"),
            "purchase_of_investments": obj.get("purchase_of_investments"),
            "purchase_of_investment_securities": obj.get("purchase_of_investment_securities"),
            "sale_and_maturity_of_investments": obj.get("sale_and_maturity_of_investments"),
            "loans_held_for_sale": obj.get("loans_held_for_sale"),
            "purchase_of_property_plant_and_equipment": obj.get("purchase_of_property_plant_and_equipment"),
            "other_investing_activities": obj.get("other_investing_activities"),
            "net_cash_from_continuing_investing_activities": obj.get("net_cash_from_continuing_investing_activities"),
            "net_cash_from_discontinued_investing_activities": obj.get("net_cash_from_discontinued_investing_activities"),
            "net_cash_from_investing_activities": obj.get("net_cash_from_investing_activities"),
            "payment_of_dividends": obj.get("payment_of_dividends"),
            "repurchase_of_common_equity": obj.get("repurchase_of_common_equity"),
            "repurchase_of_preferred_equity": obj.get("repurchase_of_preferred_equity"),
            "issuance_of_common_equity": obj.get("issuance_of_common_equity"),
            "issuance_of_preferred_equity": obj.get("issuance_of_preferred_equity"),
            "issuance_of_debt": obj.get("issuance_of_debt"),
            "repayment_of_debt": obj.get("repayment_of_debt"),
            "other_financing_activities": obj.get("other_financing_activities"),
            "cash_interest_received": obj.get("cash_interest_received"),
            "net_change_in_deposits": obj.get("net_change_in_deposits"),
            "net_increase_in_fed_funds_sold": obj.get("net_increase_in_fed_funds_sold"),
            "net_cash_from_continuing_financing_activities": obj.get("net_cash_from_continuing_financing_activities"),
            "net_cash_from_discontinued_financing_activities": obj.get("net_cash_from_discontinued_financing_activities"),
            "net_cash_from_financing_activities": obj.get("net_cash_from_financing_activities"),
            "effect_of_exchange_rate_changes": obj.get("effect_of_exchange_rate_changes"),
            "other_net_changes_in_cash": obj.get("other_net_changes_in_cash"),
            "net_change_in_cash_and_equivalents": obj.get("net_change_in_cash_and_equivalents"),
            "cash_income_taxes_paid": obj.get("cash_income_taxes_paid"),
            "cash_interest_paid": obj.get("cash_interest_paid")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


