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

class FMPBalanceSheetGrowthData(BaseModel):
    """
    FMP Balance Sheet Growth Data.
    """ # noqa: E501
    period_ending: date = Field(description="The end date of the reporting period.")
    fiscal_period: Optional[StrictStr] = None
    fiscal_year: Optional[StrictInt] = None
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    growth_cash_and_cash_equivalents: Optional[Union[StrictFloat, StrictInt]] = None
    growth_short_term_investments: Optional[Union[StrictFloat, StrictInt]] = None
    growth_cash_and_short_term_investments: Optional[Union[StrictFloat, StrictInt]] = None
    growth_net_receivables: Optional[Union[StrictFloat, StrictInt]] = None
    growth_inventory: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_current_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_current_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_property_plant_equipment_net: Optional[Union[StrictFloat, StrictInt]]
    growth_goodwill: Optional[Union[StrictFloat, StrictInt]]
    growth_intangible_assets: Optional[Union[StrictFloat, StrictInt]]
    growth_goodwill_and_intangible_assets: Optional[Union[StrictFloat, StrictInt]]
    growth_long_term_investments: Optional[Union[StrictFloat, StrictInt]] = None
    growth_tax_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_non_current_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_non_current_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_assets: Optional[Union[StrictFloat, StrictInt]] = None
    growth_account_payables: Optional[Union[StrictFloat, StrictInt]] = None
    growth_short_term_debt: Optional[Union[StrictFloat, StrictInt]] = None
    growth_tax_payables: Optional[Union[StrictFloat, StrictInt]] = None
    growth_deferred_revenue: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_current_liabilities: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_current_liabilities: Optional[Union[StrictFloat, StrictInt]] = None
    growth_long_term_debt: Optional[Union[StrictFloat, StrictInt]] = None
    growth_deferred_revenue_non_current: Optional[Union[StrictFloat, StrictInt]] = None
    growth_deferrred_tax_liabilities_non_current: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_non_current_liabilities: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_non_current_liabilities: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_liabilities: Optional[Union[StrictFloat, StrictInt]]
    growth_total_liabilities: Optional[Union[StrictFloat, StrictInt]]
    growth_common_stock: Optional[Union[StrictFloat, StrictInt]]
    growth_retained_earnings: Optional[Union[StrictFloat, StrictInt]]
    growth_accumulated_other_comprehensive_income: Optional[Union[StrictFloat, StrictInt]]
    growth_other_total_shareholders_equity: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_shareholders_equity: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_liabilities_and_shareholders_equity: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_investments: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_debt: Optional[Union[StrictFloat, StrictInt]] = None
    growth_net_debt: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["period_ending", "fiscal_period", "fiscal_year", "symbol", "growth_cash_and_cash_equivalents", "growth_short_term_investments", "growth_cash_and_short_term_investments", "growth_net_receivables", "growth_inventory", "growth_other_current_assets", "growth_total_current_assets", "growth_property_plant_equipment_net", "growth_goodwill", "growth_intangible_assets", "growth_goodwill_and_intangible_assets", "growth_long_term_investments", "growth_tax_assets", "growth_other_non_current_assets", "growth_total_non_current_assets", "growth_other_assets", "growth_total_assets", "growth_account_payables", "growth_short_term_debt", "growth_tax_payables", "growth_deferred_revenue", "growth_other_current_liabilities", "growth_total_current_liabilities", "growth_long_term_debt", "growth_deferred_revenue_non_current", "growth_deferrred_tax_liabilities_non_current", "growth_other_non_current_liabilities", "growth_total_non_current_liabilities", "growth_other_liabilities", "growth_total_liabilities", "growth_common_stock", "growth_retained_earnings", "growth_accumulated_other_comprehensive_income", "growth_other_total_shareholders_equity", "growth_total_shareholders_equity", "growth_total_liabilities_and_shareholders_equity", "growth_total_investments", "growth_total_debt", "growth_net_debt"]

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
        """Create an instance of FMPBalanceSheetGrowthData from a JSON string"""
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

        # set to None if growth_cash_and_cash_equivalents (nullable) is None
        # and model_fields_set contains the field
        if self.growth_cash_and_cash_equivalents is None and "growth_cash_and_cash_equivalents" in self.model_fields_set:
            _dict['growth_cash_and_cash_equivalents'] = None

        # set to None if growth_short_term_investments (nullable) is None
        # and model_fields_set contains the field
        if self.growth_short_term_investments is None and "growth_short_term_investments" in self.model_fields_set:
            _dict['growth_short_term_investments'] = None

        # set to None if growth_cash_and_short_term_investments (nullable) is None
        # and model_fields_set contains the field
        if self.growth_cash_and_short_term_investments is None and "growth_cash_and_short_term_investments" in self.model_fields_set:
            _dict['growth_cash_and_short_term_investments'] = None

        # set to None if growth_net_receivables (nullable) is None
        # and model_fields_set contains the field
        if self.growth_net_receivables is None and "growth_net_receivables" in self.model_fields_set:
            _dict['growth_net_receivables'] = None

        # set to None if growth_inventory (nullable) is None
        # and model_fields_set contains the field
        if self.growth_inventory is None and "growth_inventory" in self.model_fields_set:
            _dict['growth_inventory'] = None

        # set to None if growth_other_current_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_current_assets is None and "growth_other_current_assets" in self.model_fields_set:
            _dict['growth_other_current_assets'] = None

        # set to None if growth_total_current_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_current_assets is None and "growth_total_current_assets" in self.model_fields_set:
            _dict['growth_total_current_assets'] = None

        # set to None if growth_property_plant_equipment_net (nullable) is None
        # and model_fields_set contains the field
        if self.growth_property_plant_equipment_net is None and "growth_property_plant_equipment_net" in self.model_fields_set:
            _dict['growth_property_plant_equipment_net'] = None

        # set to None if growth_goodwill (nullable) is None
        # and model_fields_set contains the field
        if self.growth_goodwill is None and "growth_goodwill" in self.model_fields_set:
            _dict['growth_goodwill'] = None

        # set to None if growth_intangible_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_intangible_assets is None and "growth_intangible_assets" in self.model_fields_set:
            _dict['growth_intangible_assets'] = None

        # set to None if growth_goodwill_and_intangible_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_goodwill_and_intangible_assets is None and "growth_goodwill_and_intangible_assets" in self.model_fields_set:
            _dict['growth_goodwill_and_intangible_assets'] = None

        # set to None if growth_long_term_investments (nullable) is None
        # and model_fields_set contains the field
        if self.growth_long_term_investments is None and "growth_long_term_investments" in self.model_fields_set:
            _dict['growth_long_term_investments'] = None

        # set to None if growth_tax_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_tax_assets is None and "growth_tax_assets" in self.model_fields_set:
            _dict['growth_tax_assets'] = None

        # set to None if growth_other_non_current_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_non_current_assets is None and "growth_other_non_current_assets" in self.model_fields_set:
            _dict['growth_other_non_current_assets'] = None

        # set to None if growth_total_non_current_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_non_current_assets is None and "growth_total_non_current_assets" in self.model_fields_set:
            _dict['growth_total_non_current_assets'] = None

        # set to None if growth_other_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_assets is None and "growth_other_assets" in self.model_fields_set:
            _dict['growth_other_assets'] = None

        # set to None if growth_total_assets (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_assets is None and "growth_total_assets" in self.model_fields_set:
            _dict['growth_total_assets'] = None

        # set to None if growth_account_payables (nullable) is None
        # and model_fields_set contains the field
        if self.growth_account_payables is None and "growth_account_payables" in self.model_fields_set:
            _dict['growth_account_payables'] = None

        # set to None if growth_short_term_debt (nullable) is None
        # and model_fields_set contains the field
        if self.growth_short_term_debt is None and "growth_short_term_debt" in self.model_fields_set:
            _dict['growth_short_term_debt'] = None

        # set to None if growth_tax_payables (nullable) is None
        # and model_fields_set contains the field
        if self.growth_tax_payables is None and "growth_tax_payables" in self.model_fields_set:
            _dict['growth_tax_payables'] = None

        # set to None if growth_deferred_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.growth_deferred_revenue is None and "growth_deferred_revenue" in self.model_fields_set:
            _dict['growth_deferred_revenue'] = None

        # set to None if growth_other_current_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_current_liabilities is None and "growth_other_current_liabilities" in self.model_fields_set:
            _dict['growth_other_current_liabilities'] = None

        # set to None if growth_total_current_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_current_liabilities is None and "growth_total_current_liabilities" in self.model_fields_set:
            _dict['growth_total_current_liabilities'] = None

        # set to None if growth_long_term_debt (nullable) is None
        # and model_fields_set contains the field
        if self.growth_long_term_debt is None and "growth_long_term_debt" in self.model_fields_set:
            _dict['growth_long_term_debt'] = None

        # set to None if growth_deferred_revenue_non_current (nullable) is None
        # and model_fields_set contains the field
        if self.growth_deferred_revenue_non_current is None and "growth_deferred_revenue_non_current" in self.model_fields_set:
            _dict['growth_deferred_revenue_non_current'] = None

        # set to None if growth_deferrred_tax_liabilities_non_current (nullable) is None
        # and model_fields_set contains the field
        if self.growth_deferrred_tax_liabilities_non_current is None and "growth_deferrred_tax_liabilities_non_current" in self.model_fields_set:
            _dict['growth_deferrred_tax_liabilities_non_current'] = None

        # set to None if growth_other_non_current_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_non_current_liabilities is None and "growth_other_non_current_liabilities" in self.model_fields_set:
            _dict['growth_other_non_current_liabilities'] = None

        # set to None if growth_total_non_current_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_non_current_liabilities is None and "growth_total_non_current_liabilities" in self.model_fields_set:
            _dict['growth_total_non_current_liabilities'] = None

        # set to None if growth_other_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_liabilities is None and "growth_other_liabilities" in self.model_fields_set:
            _dict['growth_other_liabilities'] = None

        # set to None if growth_total_liabilities (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_liabilities is None and "growth_total_liabilities" in self.model_fields_set:
            _dict['growth_total_liabilities'] = None

        # set to None if growth_common_stock (nullable) is None
        # and model_fields_set contains the field
        if self.growth_common_stock is None and "growth_common_stock" in self.model_fields_set:
            _dict['growth_common_stock'] = None

        # set to None if growth_retained_earnings (nullable) is None
        # and model_fields_set contains the field
        if self.growth_retained_earnings is None and "growth_retained_earnings" in self.model_fields_set:
            _dict['growth_retained_earnings'] = None

        # set to None if growth_accumulated_other_comprehensive_income (nullable) is None
        # and model_fields_set contains the field
        if self.growth_accumulated_other_comprehensive_income is None and "growth_accumulated_other_comprehensive_income" in self.model_fields_set:
            _dict['growth_accumulated_other_comprehensive_income'] = None

        # set to None if growth_other_total_shareholders_equity (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_total_shareholders_equity is None and "growth_other_total_shareholders_equity" in self.model_fields_set:
            _dict['growth_other_total_shareholders_equity'] = None

        # set to None if growth_total_shareholders_equity (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_shareholders_equity is None and "growth_total_shareholders_equity" in self.model_fields_set:
            _dict['growth_total_shareholders_equity'] = None

        # set to None if growth_total_liabilities_and_shareholders_equity (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_liabilities_and_shareholders_equity is None and "growth_total_liabilities_and_shareholders_equity" in self.model_fields_set:
            _dict['growth_total_liabilities_and_shareholders_equity'] = None

        # set to None if growth_total_investments (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_investments is None and "growth_total_investments" in self.model_fields_set:
            _dict['growth_total_investments'] = None

        # set to None if growth_total_debt (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_debt is None and "growth_total_debt" in self.model_fields_set:
            _dict['growth_total_debt'] = None

        # set to None if growth_net_debt (nullable) is None
        # and model_fields_set contains the field
        if self.growth_net_debt is None and "growth_net_debt" in self.model_fields_set:
            _dict['growth_net_debt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPBalanceSheetGrowthData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period_ending": obj.get("period_ending"),
            "fiscal_period": obj.get("fiscal_period"),
            "fiscal_year": obj.get("fiscal_year"),
            "symbol": obj.get("symbol"),
            "growth_cash_and_cash_equivalents": obj.get("growth_cash_and_cash_equivalents"),
            "growth_short_term_investments": obj.get("growth_short_term_investments"),
            "growth_cash_and_short_term_investments": obj.get("growth_cash_and_short_term_investments"),
            "growth_net_receivables": obj.get("growth_net_receivables"),
            "growth_inventory": obj.get("growth_inventory"),
            "growth_other_current_assets": obj.get("growth_other_current_assets"),
            "growth_total_current_assets": obj.get("growth_total_current_assets"),
            "growth_property_plant_equipment_net": obj.get("growth_property_plant_equipment_net"),
            "growth_goodwill": obj.get("growth_goodwill"),
            "growth_intangible_assets": obj.get("growth_intangible_assets"),
            "growth_goodwill_and_intangible_assets": obj.get("growth_goodwill_and_intangible_assets"),
            "growth_long_term_investments": obj.get("growth_long_term_investments"),
            "growth_tax_assets": obj.get("growth_tax_assets"),
            "growth_other_non_current_assets": obj.get("growth_other_non_current_assets"),
            "growth_total_non_current_assets": obj.get("growth_total_non_current_assets"),
            "growth_other_assets": obj.get("growth_other_assets"),
            "growth_total_assets": obj.get("growth_total_assets"),
            "growth_account_payables": obj.get("growth_account_payables"),
            "growth_short_term_debt": obj.get("growth_short_term_debt"),
            "growth_tax_payables": obj.get("growth_tax_payables"),
            "growth_deferred_revenue": obj.get("growth_deferred_revenue"),
            "growth_other_current_liabilities": obj.get("growth_other_current_liabilities"),
            "growth_total_current_liabilities": obj.get("growth_total_current_liabilities"),
            "growth_long_term_debt": obj.get("growth_long_term_debt"),
            "growth_deferred_revenue_non_current": obj.get("growth_deferred_revenue_non_current"),
            "growth_deferrred_tax_liabilities_non_current": obj.get("growth_deferrred_tax_liabilities_non_current"),
            "growth_other_non_current_liabilities": obj.get("growth_other_non_current_liabilities"),
            "growth_total_non_current_liabilities": obj.get("growth_total_non_current_liabilities"),
            "growth_other_liabilities": obj.get("growth_other_liabilities"),
            "growth_total_liabilities": obj.get("growth_total_liabilities"),
            "growth_common_stock": obj.get("growth_common_stock"),
            "growth_retained_earnings": obj.get("growth_retained_earnings"),
            "growth_accumulated_other_comprehensive_income": obj.get("growth_accumulated_other_comprehensive_income"),
            "growth_other_total_shareholders_equity": obj.get("growth_other_total_shareholders_equity"),
            "growth_total_shareholders_equity": obj.get("growth_total_shareholders_equity"),
            "growth_total_liabilities_and_shareholders_equity": obj.get("growth_total_liabilities_and_shareholders_equity"),
            "growth_total_investments": obj.get("growth_total_investments"),
            "growth_total_debt": obj.get("growth_total_debt"),
            "growth_net_debt": obj.get("growth_net_debt")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


