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

class FMPIncomeStatementGrowthData(BaseModel):
    """
    FMP Income Statement Growth Data.
    """ # noqa: E501
    period_ending: date = Field(description="The end date of the reporting period.")
    fiscal_period: Optional[StrictStr] = None
    fiscal_year: Optional[StrictInt] = None
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    growth_revenue: Optional[Union[StrictFloat, StrictInt]] = None
    growth_cost_of_revenue: Optional[Union[StrictFloat, StrictInt]] = None
    growth_gross_profit: Optional[Union[StrictFloat, StrictInt]] = None
    growth_gross_profit_margin: Optional[Union[StrictFloat, StrictInt]] = None
    growth_general_and_admin_expense: Optional[Union[StrictFloat, StrictInt]] = None
    growth_research_and_development_expense: Optional[Union[StrictFloat, StrictInt]] = None
    growth_selling_and_marketing_expense: Optional[Union[StrictFloat, StrictInt]] = None
    growth_other_expenses: Optional[Union[StrictFloat, StrictInt]] = None
    growth_operating_expenses: Optional[Union[StrictFloat, StrictInt]] = None
    growth_cost_and_expenses: Optional[Union[StrictFloat, StrictInt]] = None
    growth_interest_expense: Optional[Union[StrictFloat, StrictInt]] = None
    growth_depreciation_and_amortization: Optional[Union[StrictFloat, StrictInt]] = None
    growth_ebitda: Optional[Union[StrictFloat, StrictInt]] = None
    growth_ebitda_margin: Optional[Union[StrictFloat, StrictInt]] = None
    growth_operating_income: Optional[Union[StrictFloat, StrictInt]] = None
    growth_operating_income_margin: Optional[Union[StrictFloat, StrictInt]] = None
    growth_total_other_income_expenses_net: Optional[Union[StrictFloat, StrictInt]] = None
    growth_income_before_tax: Optional[Union[StrictFloat, StrictInt]] = None
    growth_income_before_tax_margin: Optional[Union[StrictFloat, StrictInt]] = None
    growth_income_tax_expense: Optional[Union[StrictFloat, StrictInt]] = None
    growth_consolidated_net_income: Optional[Union[StrictFloat, StrictInt]] = None
    growth_net_income_margin: Optional[Union[StrictFloat, StrictInt]] = None
    growth_basic_earings_per_share: Optional[Union[StrictFloat, StrictInt]] = None
    growth_diluted_earnings_per_share: Optional[Union[StrictFloat, StrictInt]] = None
    growth_weighted_average_basic_shares_outstanding: Optional[Union[StrictFloat, StrictInt]] = None
    growth_weighted_average_diluted_shares_outstanding: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["period_ending", "fiscal_period", "fiscal_year", "symbol", "growth_revenue", "growth_cost_of_revenue", "growth_gross_profit", "growth_gross_profit_margin", "growth_general_and_admin_expense", "growth_research_and_development_expense", "growth_selling_and_marketing_expense", "growth_other_expenses", "growth_operating_expenses", "growth_cost_and_expenses", "growth_interest_expense", "growth_depreciation_and_amortization", "growth_ebitda", "growth_ebitda_margin", "growth_operating_income", "growth_operating_income_margin", "growth_total_other_income_expenses_net", "growth_income_before_tax", "growth_income_before_tax_margin", "growth_income_tax_expense", "growth_consolidated_net_income", "growth_net_income_margin", "growth_basic_earings_per_share", "growth_diluted_earnings_per_share", "growth_weighted_average_basic_shares_outstanding", "growth_weighted_average_diluted_shares_outstanding"]

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
        """Create an instance of FMPIncomeStatementGrowthData from a JSON string"""
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

        # set to None if growth_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.growth_revenue is None and "growth_revenue" in self.model_fields_set:
            _dict['growth_revenue'] = None

        # set to None if growth_cost_of_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.growth_cost_of_revenue is None and "growth_cost_of_revenue" in self.model_fields_set:
            _dict['growth_cost_of_revenue'] = None

        # set to None if growth_gross_profit (nullable) is None
        # and model_fields_set contains the field
        if self.growth_gross_profit is None and "growth_gross_profit" in self.model_fields_set:
            _dict['growth_gross_profit'] = None

        # set to None if growth_gross_profit_margin (nullable) is None
        # and model_fields_set contains the field
        if self.growth_gross_profit_margin is None and "growth_gross_profit_margin" in self.model_fields_set:
            _dict['growth_gross_profit_margin'] = None

        # set to None if growth_general_and_admin_expense (nullable) is None
        # and model_fields_set contains the field
        if self.growth_general_and_admin_expense is None and "growth_general_and_admin_expense" in self.model_fields_set:
            _dict['growth_general_and_admin_expense'] = None

        # set to None if growth_research_and_development_expense (nullable) is None
        # and model_fields_set contains the field
        if self.growth_research_and_development_expense is None and "growth_research_and_development_expense" in self.model_fields_set:
            _dict['growth_research_and_development_expense'] = None

        # set to None if growth_selling_and_marketing_expense (nullable) is None
        # and model_fields_set contains the field
        if self.growth_selling_and_marketing_expense is None and "growth_selling_and_marketing_expense" in self.model_fields_set:
            _dict['growth_selling_and_marketing_expense'] = None

        # set to None if growth_other_expenses (nullable) is None
        # and model_fields_set contains the field
        if self.growth_other_expenses is None and "growth_other_expenses" in self.model_fields_set:
            _dict['growth_other_expenses'] = None

        # set to None if growth_operating_expenses (nullable) is None
        # and model_fields_set contains the field
        if self.growth_operating_expenses is None and "growth_operating_expenses" in self.model_fields_set:
            _dict['growth_operating_expenses'] = None

        # set to None if growth_cost_and_expenses (nullable) is None
        # and model_fields_set contains the field
        if self.growth_cost_and_expenses is None and "growth_cost_and_expenses" in self.model_fields_set:
            _dict['growth_cost_and_expenses'] = None

        # set to None if growth_interest_expense (nullable) is None
        # and model_fields_set contains the field
        if self.growth_interest_expense is None and "growth_interest_expense" in self.model_fields_set:
            _dict['growth_interest_expense'] = None

        # set to None if growth_depreciation_and_amortization (nullable) is None
        # and model_fields_set contains the field
        if self.growth_depreciation_and_amortization is None and "growth_depreciation_and_amortization" in self.model_fields_set:
            _dict['growth_depreciation_and_amortization'] = None

        # set to None if growth_ebitda (nullable) is None
        # and model_fields_set contains the field
        if self.growth_ebitda is None and "growth_ebitda" in self.model_fields_set:
            _dict['growth_ebitda'] = None

        # set to None if growth_ebitda_margin (nullable) is None
        # and model_fields_set contains the field
        if self.growth_ebitda_margin is None and "growth_ebitda_margin" in self.model_fields_set:
            _dict['growth_ebitda_margin'] = None

        # set to None if growth_operating_income (nullable) is None
        # and model_fields_set contains the field
        if self.growth_operating_income is None and "growth_operating_income" in self.model_fields_set:
            _dict['growth_operating_income'] = None

        # set to None if growth_operating_income_margin (nullable) is None
        # and model_fields_set contains the field
        if self.growth_operating_income_margin is None and "growth_operating_income_margin" in self.model_fields_set:
            _dict['growth_operating_income_margin'] = None

        # set to None if growth_total_other_income_expenses_net (nullable) is None
        # and model_fields_set contains the field
        if self.growth_total_other_income_expenses_net is None and "growth_total_other_income_expenses_net" in self.model_fields_set:
            _dict['growth_total_other_income_expenses_net'] = None

        # set to None if growth_income_before_tax (nullable) is None
        # and model_fields_set contains the field
        if self.growth_income_before_tax is None and "growth_income_before_tax" in self.model_fields_set:
            _dict['growth_income_before_tax'] = None

        # set to None if growth_income_before_tax_margin (nullable) is None
        # and model_fields_set contains the field
        if self.growth_income_before_tax_margin is None and "growth_income_before_tax_margin" in self.model_fields_set:
            _dict['growth_income_before_tax_margin'] = None

        # set to None if growth_income_tax_expense (nullable) is None
        # and model_fields_set contains the field
        if self.growth_income_tax_expense is None and "growth_income_tax_expense" in self.model_fields_set:
            _dict['growth_income_tax_expense'] = None

        # set to None if growth_consolidated_net_income (nullable) is None
        # and model_fields_set contains the field
        if self.growth_consolidated_net_income is None and "growth_consolidated_net_income" in self.model_fields_set:
            _dict['growth_consolidated_net_income'] = None

        # set to None if growth_net_income_margin (nullable) is None
        # and model_fields_set contains the field
        if self.growth_net_income_margin is None and "growth_net_income_margin" in self.model_fields_set:
            _dict['growth_net_income_margin'] = None

        # set to None if growth_basic_earings_per_share (nullable) is None
        # and model_fields_set contains the field
        if self.growth_basic_earings_per_share is None and "growth_basic_earings_per_share" in self.model_fields_set:
            _dict['growth_basic_earings_per_share'] = None

        # set to None if growth_diluted_earnings_per_share (nullable) is None
        # and model_fields_set contains the field
        if self.growth_diluted_earnings_per_share is None and "growth_diluted_earnings_per_share" in self.model_fields_set:
            _dict['growth_diluted_earnings_per_share'] = None

        # set to None if growth_weighted_average_basic_shares_outstanding (nullable) is None
        # and model_fields_set contains the field
        if self.growth_weighted_average_basic_shares_outstanding is None and "growth_weighted_average_basic_shares_outstanding" in self.model_fields_set:
            _dict['growth_weighted_average_basic_shares_outstanding'] = None

        # set to None if growth_weighted_average_diluted_shares_outstanding (nullable) is None
        # and model_fields_set contains the field
        if self.growth_weighted_average_diluted_shares_outstanding is None and "growth_weighted_average_diluted_shares_outstanding" in self.model_fields_set:
            _dict['growth_weighted_average_diluted_shares_outstanding'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPIncomeStatementGrowthData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period_ending": obj.get("period_ending"),
            "fiscal_period": obj.get("fiscal_period"),
            "fiscal_year": obj.get("fiscal_year"),
            "symbol": obj.get("symbol"),
            "growth_revenue": obj.get("growth_revenue"),
            "growth_cost_of_revenue": obj.get("growth_cost_of_revenue"),
            "growth_gross_profit": obj.get("growth_gross_profit"),
            "growth_gross_profit_margin": obj.get("growth_gross_profit_margin"),
            "growth_general_and_admin_expense": obj.get("growth_general_and_admin_expense"),
            "growth_research_and_development_expense": obj.get("growth_research_and_development_expense"),
            "growth_selling_and_marketing_expense": obj.get("growth_selling_and_marketing_expense"),
            "growth_other_expenses": obj.get("growth_other_expenses"),
            "growth_operating_expenses": obj.get("growth_operating_expenses"),
            "growth_cost_and_expenses": obj.get("growth_cost_and_expenses"),
            "growth_interest_expense": obj.get("growth_interest_expense"),
            "growth_depreciation_and_amortization": obj.get("growth_depreciation_and_amortization"),
            "growth_ebitda": obj.get("growth_ebitda"),
            "growth_ebitda_margin": obj.get("growth_ebitda_margin"),
            "growth_operating_income": obj.get("growth_operating_income"),
            "growth_operating_income_margin": obj.get("growth_operating_income_margin"),
            "growth_total_other_income_expenses_net": obj.get("growth_total_other_income_expenses_net"),
            "growth_income_before_tax": obj.get("growth_income_before_tax"),
            "growth_income_before_tax_margin": obj.get("growth_income_before_tax_margin"),
            "growth_income_tax_expense": obj.get("growth_income_tax_expense"),
            "growth_consolidated_net_income": obj.get("growth_consolidated_net_income"),
            "growth_net_income_margin": obj.get("growth_net_income_margin"),
            "growth_basic_earings_per_share": obj.get("growth_basic_earings_per_share"),
            "growth_diluted_earnings_per_share": obj.get("growth_diluted_earnings_per_share"),
            "growth_weighted_average_basic_shares_outstanding": obj.get("growth_weighted_average_basic_shares_outstanding"),
            "growth_weighted_average_diluted_shares_outstanding": obj.get("growth_weighted_average_diluted_shares_outstanding")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


