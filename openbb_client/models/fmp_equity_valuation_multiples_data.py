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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class FMPEquityValuationMultiplesData(BaseModel):
    """
    FMP Equity Valuation Multiples Data.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    revenue_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    net_income_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    operating_cash_flow_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    free_cash_flow_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    cash_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    book_value_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    tangible_book_value_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    shareholders_equity_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    interest_debt_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    market_cap_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    enterprise_value_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    pe_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    price_to_sales_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    pocf_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    pfcf_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    pb_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    ptb_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    ev_to_sales_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    enterprise_value_over_ebitda_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    ev_to_operating_cash_flow_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    ev_to_free_cash_flow_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    earnings_yield_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    free_cash_flow_yield_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    debt_to_equity_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    debt_to_assets_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    net_debt_to_ebitda_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    current_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    interest_coverage_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    income_quality_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_yield_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_yield_percentage_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_to_market_cap_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    payout_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    sales_general_and_administrative_to_revenue_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    research_and_development_to_revenue_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    intangibles_to_total_assets_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    capex_to_operating_cash_flow_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    capex_to_revenue_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    capex_to_depreciation_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    stock_based_compensation_to_revenue_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    graham_number_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    roic_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    return_on_tangible_assets_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    graham_net_net_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    working_capital_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    tangible_asset_value_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    net_current_asset_value_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    invested_capital_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    average_receivables_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    average_payables_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    average_inventory_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    days_sales_outstanding_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    days_payables_outstanding_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    days_of_inventory_on_hand_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    receivables_turnover_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    payables_turnover_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    inventory_turnover_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    roe_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    capex_per_share_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "revenue_per_share_ttm", "net_income_per_share_ttm", "operating_cash_flow_per_share_ttm", "free_cash_flow_per_share_ttm", "cash_per_share_ttm", "book_value_per_share_ttm", "tangible_book_value_per_share_ttm", "shareholders_equity_per_share_ttm", "interest_debt_per_share_ttm", "market_cap_ttm", "enterprise_value_ttm", "pe_ratio_ttm", "price_to_sales_ratio_ttm", "pocf_ratio_ttm", "pfcf_ratio_ttm", "pb_ratio_ttm", "ptb_ratio_ttm", "ev_to_sales_ttm", "enterprise_value_over_ebitda_ttm", "ev_to_operating_cash_flow_ttm", "ev_to_free_cash_flow_ttm", "earnings_yield_ttm", "free_cash_flow_yield_ttm", "debt_to_equity_ttm", "debt_to_assets_ttm", "net_debt_to_ebitda_ttm", "current_ratio_ttm", "interest_coverage_ttm", "income_quality_ttm", "dividend_yield_ttm", "dividend_yield_percentage_ttm", "dividend_to_market_cap_ttm", "dividend_per_share_ttm", "payout_ratio_ttm", "sales_general_and_administrative_to_revenue_ttm", "research_and_development_to_revenue_ttm", "intangibles_to_total_assets_ttm", "capex_to_operating_cash_flow_ttm", "capex_to_revenue_ttm", "capex_to_depreciation_ttm", "stock_based_compensation_to_revenue_ttm", "graham_number_ttm", "roic_ttm", "return_on_tangible_assets_ttm", "graham_net_net_ttm", "working_capital_ttm", "tangible_asset_value_ttm", "net_current_asset_value_ttm", "invested_capital_ttm", "average_receivables_ttm", "average_payables_ttm", "average_inventory_ttm", "days_sales_outstanding_ttm", "days_payables_outstanding_ttm", "days_of_inventory_on_hand_ttm", "receivables_turnover_ttm", "payables_turnover_ttm", "inventory_turnover_ttm", "roe_ttm", "capex_per_share_ttm"]

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
        """Create an instance of FMPEquityValuationMultiplesData from a JSON string"""
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

        # set to None if revenue_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.revenue_per_share_ttm is None and "revenue_per_share_ttm" in self.model_fields_set:
            _dict['revenue_per_share_ttm'] = None

        # set to None if net_income_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.net_income_per_share_ttm is None and "net_income_per_share_ttm" in self.model_fields_set:
            _dict['net_income_per_share_ttm'] = None

        # set to None if operating_cash_flow_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.operating_cash_flow_per_share_ttm is None and "operating_cash_flow_per_share_ttm" in self.model_fields_set:
            _dict['operating_cash_flow_per_share_ttm'] = None

        # set to None if free_cash_flow_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.free_cash_flow_per_share_ttm is None and "free_cash_flow_per_share_ttm" in self.model_fields_set:
            _dict['free_cash_flow_per_share_ttm'] = None

        # set to None if cash_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.cash_per_share_ttm is None and "cash_per_share_ttm" in self.model_fields_set:
            _dict['cash_per_share_ttm'] = None

        # set to None if book_value_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.book_value_per_share_ttm is None and "book_value_per_share_ttm" in self.model_fields_set:
            _dict['book_value_per_share_ttm'] = None

        # set to None if tangible_book_value_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.tangible_book_value_per_share_ttm is None and "tangible_book_value_per_share_ttm" in self.model_fields_set:
            _dict['tangible_book_value_per_share_ttm'] = None

        # set to None if shareholders_equity_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.shareholders_equity_per_share_ttm is None and "shareholders_equity_per_share_ttm" in self.model_fields_set:
            _dict['shareholders_equity_per_share_ttm'] = None

        # set to None if interest_debt_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.interest_debt_per_share_ttm is None and "interest_debt_per_share_ttm" in self.model_fields_set:
            _dict['interest_debt_per_share_ttm'] = None

        # set to None if market_cap_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.market_cap_ttm is None and "market_cap_ttm" in self.model_fields_set:
            _dict['market_cap_ttm'] = None

        # set to None if enterprise_value_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_value_ttm is None and "enterprise_value_ttm" in self.model_fields_set:
            _dict['enterprise_value_ttm'] = None

        # set to None if pe_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.pe_ratio_ttm is None and "pe_ratio_ttm" in self.model_fields_set:
            _dict['pe_ratio_ttm'] = None

        # set to None if price_to_sales_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.price_to_sales_ratio_ttm is None and "price_to_sales_ratio_ttm" in self.model_fields_set:
            _dict['price_to_sales_ratio_ttm'] = None

        # set to None if pocf_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.pocf_ratio_ttm is None and "pocf_ratio_ttm" in self.model_fields_set:
            _dict['pocf_ratio_ttm'] = None

        # set to None if pfcf_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.pfcf_ratio_ttm is None and "pfcf_ratio_ttm" in self.model_fields_set:
            _dict['pfcf_ratio_ttm'] = None

        # set to None if pb_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.pb_ratio_ttm is None and "pb_ratio_ttm" in self.model_fields_set:
            _dict['pb_ratio_ttm'] = None

        # set to None if ptb_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.ptb_ratio_ttm is None and "ptb_ratio_ttm" in self.model_fields_set:
            _dict['ptb_ratio_ttm'] = None

        # set to None if ev_to_sales_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.ev_to_sales_ttm is None and "ev_to_sales_ttm" in self.model_fields_set:
            _dict['ev_to_sales_ttm'] = None

        # set to None if enterprise_value_over_ebitda_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_value_over_ebitda_ttm is None and "enterprise_value_over_ebitda_ttm" in self.model_fields_set:
            _dict['enterprise_value_over_ebitda_ttm'] = None

        # set to None if ev_to_operating_cash_flow_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.ev_to_operating_cash_flow_ttm is None and "ev_to_operating_cash_flow_ttm" in self.model_fields_set:
            _dict['ev_to_operating_cash_flow_ttm'] = None

        # set to None if ev_to_free_cash_flow_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.ev_to_free_cash_flow_ttm is None and "ev_to_free_cash_flow_ttm" in self.model_fields_set:
            _dict['ev_to_free_cash_flow_ttm'] = None

        # set to None if earnings_yield_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.earnings_yield_ttm is None and "earnings_yield_ttm" in self.model_fields_set:
            _dict['earnings_yield_ttm'] = None

        # set to None if free_cash_flow_yield_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.free_cash_flow_yield_ttm is None and "free_cash_flow_yield_ttm" in self.model_fields_set:
            _dict['free_cash_flow_yield_ttm'] = None

        # set to None if debt_to_equity_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.debt_to_equity_ttm is None and "debt_to_equity_ttm" in self.model_fields_set:
            _dict['debt_to_equity_ttm'] = None

        # set to None if debt_to_assets_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.debt_to_assets_ttm is None and "debt_to_assets_ttm" in self.model_fields_set:
            _dict['debt_to_assets_ttm'] = None

        # set to None if net_debt_to_ebitda_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.net_debt_to_ebitda_ttm is None and "net_debt_to_ebitda_ttm" in self.model_fields_set:
            _dict['net_debt_to_ebitda_ttm'] = None

        # set to None if current_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.current_ratio_ttm is None and "current_ratio_ttm" in self.model_fields_set:
            _dict['current_ratio_ttm'] = None

        # set to None if interest_coverage_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.interest_coverage_ttm is None and "interest_coverage_ttm" in self.model_fields_set:
            _dict['interest_coverage_ttm'] = None

        # set to None if income_quality_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.income_quality_ttm is None and "income_quality_ttm" in self.model_fields_set:
            _dict['income_quality_ttm'] = None

        # set to None if dividend_yield_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_yield_ttm is None and "dividend_yield_ttm" in self.model_fields_set:
            _dict['dividend_yield_ttm'] = None

        # set to None if dividend_yield_percentage_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_yield_percentage_ttm is None and "dividend_yield_percentage_ttm" in self.model_fields_set:
            _dict['dividend_yield_percentage_ttm'] = None

        # set to None if dividend_to_market_cap_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_to_market_cap_ttm is None and "dividend_to_market_cap_ttm" in self.model_fields_set:
            _dict['dividend_to_market_cap_ttm'] = None

        # set to None if dividend_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_per_share_ttm is None and "dividend_per_share_ttm" in self.model_fields_set:
            _dict['dividend_per_share_ttm'] = None

        # set to None if payout_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.payout_ratio_ttm is None and "payout_ratio_ttm" in self.model_fields_set:
            _dict['payout_ratio_ttm'] = None

        # set to None if sales_general_and_administrative_to_revenue_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.sales_general_and_administrative_to_revenue_ttm is None and "sales_general_and_administrative_to_revenue_ttm" in self.model_fields_set:
            _dict['sales_general_and_administrative_to_revenue_ttm'] = None

        # set to None if research_and_development_to_revenue_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.research_and_development_to_revenue_ttm is None and "research_and_development_to_revenue_ttm" in self.model_fields_set:
            _dict['research_and_development_to_revenue_ttm'] = None

        # set to None if intangibles_to_total_assets_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.intangibles_to_total_assets_ttm is None and "intangibles_to_total_assets_ttm" in self.model_fields_set:
            _dict['intangibles_to_total_assets_ttm'] = None

        # set to None if capex_to_operating_cash_flow_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.capex_to_operating_cash_flow_ttm is None and "capex_to_operating_cash_flow_ttm" in self.model_fields_set:
            _dict['capex_to_operating_cash_flow_ttm'] = None

        # set to None if capex_to_revenue_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.capex_to_revenue_ttm is None and "capex_to_revenue_ttm" in self.model_fields_set:
            _dict['capex_to_revenue_ttm'] = None

        # set to None if capex_to_depreciation_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.capex_to_depreciation_ttm is None and "capex_to_depreciation_ttm" in self.model_fields_set:
            _dict['capex_to_depreciation_ttm'] = None

        # set to None if stock_based_compensation_to_revenue_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.stock_based_compensation_to_revenue_ttm is None and "stock_based_compensation_to_revenue_ttm" in self.model_fields_set:
            _dict['stock_based_compensation_to_revenue_ttm'] = None

        # set to None if graham_number_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.graham_number_ttm is None and "graham_number_ttm" in self.model_fields_set:
            _dict['graham_number_ttm'] = None

        # set to None if roic_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.roic_ttm is None and "roic_ttm" in self.model_fields_set:
            _dict['roic_ttm'] = None

        # set to None if return_on_tangible_assets_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.return_on_tangible_assets_ttm is None and "return_on_tangible_assets_ttm" in self.model_fields_set:
            _dict['return_on_tangible_assets_ttm'] = None

        # set to None if graham_net_net_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.graham_net_net_ttm is None and "graham_net_net_ttm" in self.model_fields_set:
            _dict['graham_net_net_ttm'] = None

        # set to None if working_capital_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.working_capital_ttm is None and "working_capital_ttm" in self.model_fields_set:
            _dict['working_capital_ttm'] = None

        # set to None if tangible_asset_value_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.tangible_asset_value_ttm is None and "tangible_asset_value_ttm" in self.model_fields_set:
            _dict['tangible_asset_value_ttm'] = None

        # set to None if net_current_asset_value_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.net_current_asset_value_ttm is None and "net_current_asset_value_ttm" in self.model_fields_set:
            _dict['net_current_asset_value_ttm'] = None

        # set to None if invested_capital_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.invested_capital_ttm is None and "invested_capital_ttm" in self.model_fields_set:
            _dict['invested_capital_ttm'] = None

        # set to None if average_receivables_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.average_receivables_ttm is None and "average_receivables_ttm" in self.model_fields_set:
            _dict['average_receivables_ttm'] = None

        # set to None if average_payables_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.average_payables_ttm is None and "average_payables_ttm" in self.model_fields_set:
            _dict['average_payables_ttm'] = None

        # set to None if average_inventory_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.average_inventory_ttm is None and "average_inventory_ttm" in self.model_fields_set:
            _dict['average_inventory_ttm'] = None

        # set to None if days_sales_outstanding_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.days_sales_outstanding_ttm is None and "days_sales_outstanding_ttm" in self.model_fields_set:
            _dict['days_sales_outstanding_ttm'] = None

        # set to None if days_payables_outstanding_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.days_payables_outstanding_ttm is None and "days_payables_outstanding_ttm" in self.model_fields_set:
            _dict['days_payables_outstanding_ttm'] = None

        # set to None if days_of_inventory_on_hand_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.days_of_inventory_on_hand_ttm is None and "days_of_inventory_on_hand_ttm" in self.model_fields_set:
            _dict['days_of_inventory_on_hand_ttm'] = None

        # set to None if receivables_turnover_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.receivables_turnover_ttm is None and "receivables_turnover_ttm" in self.model_fields_set:
            _dict['receivables_turnover_ttm'] = None

        # set to None if payables_turnover_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.payables_turnover_ttm is None and "payables_turnover_ttm" in self.model_fields_set:
            _dict['payables_turnover_ttm'] = None

        # set to None if inventory_turnover_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.inventory_turnover_ttm is None and "inventory_turnover_ttm" in self.model_fields_set:
            _dict['inventory_turnover_ttm'] = None

        # set to None if roe_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.roe_ttm is None and "roe_ttm" in self.model_fields_set:
            _dict['roe_ttm'] = None

        # set to None if capex_per_share_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.capex_per_share_ttm is None and "capex_per_share_ttm" in self.model_fields_set:
            _dict['capex_per_share_ttm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPEquityValuationMultiplesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "revenue_per_share_ttm": obj.get("revenue_per_share_ttm"),
            "net_income_per_share_ttm": obj.get("net_income_per_share_ttm"),
            "operating_cash_flow_per_share_ttm": obj.get("operating_cash_flow_per_share_ttm"),
            "free_cash_flow_per_share_ttm": obj.get("free_cash_flow_per_share_ttm"),
            "cash_per_share_ttm": obj.get("cash_per_share_ttm"),
            "book_value_per_share_ttm": obj.get("book_value_per_share_ttm"),
            "tangible_book_value_per_share_ttm": obj.get("tangible_book_value_per_share_ttm"),
            "shareholders_equity_per_share_ttm": obj.get("shareholders_equity_per_share_ttm"),
            "interest_debt_per_share_ttm": obj.get("interest_debt_per_share_ttm"),
            "market_cap_ttm": obj.get("market_cap_ttm"),
            "enterprise_value_ttm": obj.get("enterprise_value_ttm"),
            "pe_ratio_ttm": obj.get("pe_ratio_ttm"),
            "price_to_sales_ratio_ttm": obj.get("price_to_sales_ratio_ttm"),
            "pocf_ratio_ttm": obj.get("pocf_ratio_ttm"),
            "pfcf_ratio_ttm": obj.get("pfcf_ratio_ttm"),
            "pb_ratio_ttm": obj.get("pb_ratio_ttm"),
            "ptb_ratio_ttm": obj.get("ptb_ratio_ttm"),
            "ev_to_sales_ttm": obj.get("ev_to_sales_ttm"),
            "enterprise_value_over_ebitda_ttm": obj.get("enterprise_value_over_ebitda_ttm"),
            "ev_to_operating_cash_flow_ttm": obj.get("ev_to_operating_cash_flow_ttm"),
            "ev_to_free_cash_flow_ttm": obj.get("ev_to_free_cash_flow_ttm"),
            "earnings_yield_ttm": obj.get("earnings_yield_ttm"),
            "free_cash_flow_yield_ttm": obj.get("free_cash_flow_yield_ttm"),
            "debt_to_equity_ttm": obj.get("debt_to_equity_ttm"),
            "debt_to_assets_ttm": obj.get("debt_to_assets_ttm"),
            "net_debt_to_ebitda_ttm": obj.get("net_debt_to_ebitda_ttm"),
            "current_ratio_ttm": obj.get("current_ratio_ttm"),
            "interest_coverage_ttm": obj.get("interest_coverage_ttm"),
            "income_quality_ttm": obj.get("income_quality_ttm"),
            "dividend_yield_ttm": obj.get("dividend_yield_ttm"),
            "dividend_yield_percentage_ttm": obj.get("dividend_yield_percentage_ttm"),
            "dividend_to_market_cap_ttm": obj.get("dividend_to_market_cap_ttm"),
            "dividend_per_share_ttm": obj.get("dividend_per_share_ttm"),
            "payout_ratio_ttm": obj.get("payout_ratio_ttm"),
            "sales_general_and_administrative_to_revenue_ttm": obj.get("sales_general_and_administrative_to_revenue_ttm"),
            "research_and_development_to_revenue_ttm": obj.get("research_and_development_to_revenue_ttm"),
            "intangibles_to_total_assets_ttm": obj.get("intangibles_to_total_assets_ttm"),
            "capex_to_operating_cash_flow_ttm": obj.get("capex_to_operating_cash_flow_ttm"),
            "capex_to_revenue_ttm": obj.get("capex_to_revenue_ttm"),
            "capex_to_depreciation_ttm": obj.get("capex_to_depreciation_ttm"),
            "stock_based_compensation_to_revenue_ttm": obj.get("stock_based_compensation_to_revenue_ttm"),
            "graham_number_ttm": obj.get("graham_number_ttm"),
            "roic_ttm": obj.get("roic_ttm"),
            "return_on_tangible_assets_ttm": obj.get("return_on_tangible_assets_ttm"),
            "graham_net_net_ttm": obj.get("graham_net_net_ttm"),
            "working_capital_ttm": obj.get("working_capital_ttm"),
            "tangible_asset_value_ttm": obj.get("tangible_asset_value_ttm"),
            "net_current_asset_value_ttm": obj.get("net_current_asset_value_ttm"),
            "invested_capital_ttm": obj.get("invested_capital_ttm"),
            "average_receivables_ttm": obj.get("average_receivables_ttm"),
            "average_payables_ttm": obj.get("average_payables_ttm"),
            "average_inventory_ttm": obj.get("average_inventory_ttm"),
            "days_sales_outstanding_ttm": obj.get("days_sales_outstanding_ttm"),
            "days_payables_outstanding_ttm": obj.get("days_payables_outstanding_ttm"),
            "days_of_inventory_on_hand_ttm": obj.get("days_of_inventory_on_hand_ttm"),
            "receivables_turnover_ttm": obj.get("receivables_turnover_ttm"),
            "payables_turnover_ttm": obj.get("payables_turnover_ttm"),
            "inventory_turnover_ttm": obj.get("inventory_turnover_ttm"),
            "roe_ttm": obj.get("roe_ttm"),
            "capex_per_share_ttm": obj.get("capex_per_share_ttm")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


