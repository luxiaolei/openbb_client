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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class YFinanceKeyMetricsData(BaseModel):
    """
    YFinance Key Metrics Data.
    """ # noqa: E501
    symbol: Optional[StrictStr] = None
    market_cap: Optional[Union[StrictFloat, StrictInt]] = None
    pe_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    forward_pe: Optional[Union[StrictFloat, StrictInt]] = None
    peg_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    peg_ratio_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    eps_ttm: Optional[Union[StrictFloat, StrictInt]] = None
    eps_forward: Optional[Union[StrictFloat, StrictInt]] = None
    enterprise_to_ebitda: Optional[Union[StrictFloat, StrictInt]] = None
    earnings_growth: Optional[Union[StrictFloat, StrictInt]] = None
    earnings_growth_quarterly: Optional[Union[StrictFloat, StrictInt]] = None
    revenue_per_share: Optional[Union[StrictFloat, StrictInt]] = None
    revenue_growth: Optional[Union[StrictFloat, StrictInt]] = None
    enterprise_to_revenue: Optional[Union[StrictFloat, StrictInt]] = None
    cash_per_share: Optional[Union[StrictFloat, StrictInt]] = None
    quick_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    current_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    debt_to_equity: Optional[Union[StrictFloat, StrictInt]] = None
    gross_margin: Optional[Union[StrictFloat, StrictInt]] = None
    operating_margin: Optional[Union[StrictFloat, StrictInt]] = None
    ebitda_margin: Optional[Union[StrictFloat, StrictInt]] = None
    profit_margin: Optional[Union[StrictFloat, StrictInt]] = None
    return_on_assets: Optional[Union[StrictFloat, StrictInt]] = None
    return_on_equity: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_yield: Optional[Union[StrictFloat, StrictInt]] = None
    dividend_yield_5y_avg: Optional[Union[StrictFloat, StrictInt]] = None
    payout_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    book_value: Optional[Union[StrictFloat, StrictInt]] = None
    price_to_book: Optional[Union[StrictFloat, StrictInt]] = None
    enterprise_value: Optional[StrictInt] = None
    overall_risk: Optional[Union[StrictFloat, StrictInt]] = None
    audit_risk: Optional[Union[StrictFloat, StrictInt]] = None
    board_risk: Optional[Union[StrictFloat, StrictInt]] = None
    compensation_risk: Optional[Union[StrictFloat, StrictInt]] = None
    shareholder_rights_risk: Optional[Union[StrictFloat, StrictInt]] = None
    beta: Optional[Union[StrictFloat, StrictInt]] = None
    price_return_1y: Optional[Union[StrictFloat, StrictInt]] = None
    currency: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "market_cap", "pe_ratio", "forward_pe", "peg_ratio", "peg_ratio_ttm", "eps_ttm", "eps_forward", "enterprise_to_ebitda", "earnings_growth", "earnings_growth_quarterly", "revenue_per_share", "revenue_growth", "enterprise_to_revenue", "cash_per_share", "quick_ratio", "current_ratio", "debt_to_equity", "gross_margin", "operating_margin", "ebitda_margin", "profit_margin", "return_on_assets", "return_on_equity", "dividend_yield", "dividend_yield_5y_avg", "payout_ratio", "book_value", "price_to_book", "enterprise_value", "overall_risk", "audit_risk", "board_risk", "compensation_risk", "shareholder_rights_risk", "beta", "price_return_1y", "currency"]

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
        """Create an instance of YFinanceKeyMetricsData from a JSON string"""
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

        # set to None if symbol (nullable) is None
        # and model_fields_set contains the field
        if self.symbol is None and "symbol" in self.model_fields_set:
            _dict['symbol'] = None

        # set to None if market_cap (nullable) is None
        # and model_fields_set contains the field
        if self.market_cap is None and "market_cap" in self.model_fields_set:
            _dict['market_cap'] = None

        # set to None if pe_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.pe_ratio is None and "pe_ratio" in self.model_fields_set:
            _dict['pe_ratio'] = None

        # set to None if forward_pe (nullable) is None
        # and model_fields_set contains the field
        if self.forward_pe is None and "forward_pe" in self.model_fields_set:
            _dict['forward_pe'] = None

        # set to None if peg_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.peg_ratio is None and "peg_ratio" in self.model_fields_set:
            _dict['peg_ratio'] = None

        # set to None if peg_ratio_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.peg_ratio_ttm is None and "peg_ratio_ttm" in self.model_fields_set:
            _dict['peg_ratio_ttm'] = None

        # set to None if eps_ttm (nullable) is None
        # and model_fields_set contains the field
        if self.eps_ttm is None and "eps_ttm" in self.model_fields_set:
            _dict['eps_ttm'] = None

        # set to None if eps_forward (nullable) is None
        # and model_fields_set contains the field
        if self.eps_forward is None and "eps_forward" in self.model_fields_set:
            _dict['eps_forward'] = None

        # set to None if enterprise_to_ebitda (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_to_ebitda is None and "enterprise_to_ebitda" in self.model_fields_set:
            _dict['enterprise_to_ebitda'] = None

        # set to None if earnings_growth (nullable) is None
        # and model_fields_set contains the field
        if self.earnings_growth is None and "earnings_growth" in self.model_fields_set:
            _dict['earnings_growth'] = None

        # set to None if earnings_growth_quarterly (nullable) is None
        # and model_fields_set contains the field
        if self.earnings_growth_quarterly is None and "earnings_growth_quarterly" in self.model_fields_set:
            _dict['earnings_growth_quarterly'] = None

        # set to None if revenue_per_share (nullable) is None
        # and model_fields_set contains the field
        if self.revenue_per_share is None and "revenue_per_share" in self.model_fields_set:
            _dict['revenue_per_share'] = None

        # set to None if revenue_growth (nullable) is None
        # and model_fields_set contains the field
        if self.revenue_growth is None and "revenue_growth" in self.model_fields_set:
            _dict['revenue_growth'] = None

        # set to None if enterprise_to_revenue (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_to_revenue is None and "enterprise_to_revenue" in self.model_fields_set:
            _dict['enterprise_to_revenue'] = None

        # set to None if cash_per_share (nullable) is None
        # and model_fields_set contains the field
        if self.cash_per_share is None and "cash_per_share" in self.model_fields_set:
            _dict['cash_per_share'] = None

        # set to None if quick_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.quick_ratio is None and "quick_ratio" in self.model_fields_set:
            _dict['quick_ratio'] = None

        # set to None if current_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.current_ratio is None and "current_ratio" in self.model_fields_set:
            _dict['current_ratio'] = None

        # set to None if debt_to_equity (nullable) is None
        # and model_fields_set contains the field
        if self.debt_to_equity is None and "debt_to_equity" in self.model_fields_set:
            _dict['debt_to_equity'] = None

        # set to None if gross_margin (nullable) is None
        # and model_fields_set contains the field
        if self.gross_margin is None and "gross_margin" in self.model_fields_set:
            _dict['gross_margin'] = None

        # set to None if operating_margin (nullable) is None
        # and model_fields_set contains the field
        if self.operating_margin is None and "operating_margin" in self.model_fields_set:
            _dict['operating_margin'] = None

        # set to None if ebitda_margin (nullable) is None
        # and model_fields_set contains the field
        if self.ebitda_margin is None and "ebitda_margin" in self.model_fields_set:
            _dict['ebitda_margin'] = None

        # set to None if profit_margin (nullable) is None
        # and model_fields_set contains the field
        if self.profit_margin is None and "profit_margin" in self.model_fields_set:
            _dict['profit_margin'] = None

        # set to None if return_on_assets (nullable) is None
        # and model_fields_set contains the field
        if self.return_on_assets is None and "return_on_assets" in self.model_fields_set:
            _dict['return_on_assets'] = None

        # set to None if return_on_equity (nullable) is None
        # and model_fields_set contains the field
        if self.return_on_equity is None and "return_on_equity" in self.model_fields_set:
            _dict['return_on_equity'] = None

        # set to None if dividend_yield (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_yield is None and "dividend_yield" in self.model_fields_set:
            _dict['dividend_yield'] = None

        # set to None if dividend_yield_5y_avg (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_yield_5y_avg is None and "dividend_yield_5y_avg" in self.model_fields_set:
            _dict['dividend_yield_5y_avg'] = None

        # set to None if payout_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.payout_ratio is None and "payout_ratio" in self.model_fields_set:
            _dict['payout_ratio'] = None

        # set to None if book_value (nullable) is None
        # and model_fields_set contains the field
        if self.book_value is None and "book_value" in self.model_fields_set:
            _dict['book_value'] = None

        # set to None if price_to_book (nullable) is None
        # and model_fields_set contains the field
        if self.price_to_book is None and "price_to_book" in self.model_fields_set:
            _dict['price_to_book'] = None

        # set to None if enterprise_value (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise_value is None and "enterprise_value" in self.model_fields_set:
            _dict['enterprise_value'] = None

        # set to None if overall_risk (nullable) is None
        # and model_fields_set contains the field
        if self.overall_risk is None and "overall_risk" in self.model_fields_set:
            _dict['overall_risk'] = None

        # set to None if audit_risk (nullable) is None
        # and model_fields_set contains the field
        if self.audit_risk is None and "audit_risk" in self.model_fields_set:
            _dict['audit_risk'] = None

        # set to None if board_risk (nullable) is None
        # and model_fields_set contains the field
        if self.board_risk is None and "board_risk" in self.model_fields_set:
            _dict['board_risk'] = None

        # set to None if compensation_risk (nullable) is None
        # and model_fields_set contains the field
        if self.compensation_risk is None and "compensation_risk" in self.model_fields_set:
            _dict['compensation_risk'] = None

        # set to None if shareholder_rights_risk (nullable) is None
        # and model_fields_set contains the field
        if self.shareholder_rights_risk is None and "shareholder_rights_risk" in self.model_fields_set:
            _dict['shareholder_rights_risk'] = None

        # set to None if beta (nullable) is None
        # and model_fields_set contains the field
        if self.beta is None and "beta" in self.model_fields_set:
            _dict['beta'] = None

        # set to None if price_return_1y (nullable) is None
        # and model_fields_set contains the field
        if self.price_return_1y is None and "price_return_1y" in self.model_fields_set:
            _dict['price_return_1y'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of YFinanceKeyMetricsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "market_cap": obj.get("market_cap"),
            "pe_ratio": obj.get("pe_ratio"),
            "forward_pe": obj.get("forward_pe"),
            "peg_ratio": obj.get("peg_ratio"),
            "peg_ratio_ttm": obj.get("peg_ratio_ttm"),
            "eps_ttm": obj.get("eps_ttm"),
            "eps_forward": obj.get("eps_forward"),
            "enterprise_to_ebitda": obj.get("enterprise_to_ebitda"),
            "earnings_growth": obj.get("earnings_growth"),
            "earnings_growth_quarterly": obj.get("earnings_growth_quarterly"),
            "revenue_per_share": obj.get("revenue_per_share"),
            "revenue_growth": obj.get("revenue_growth"),
            "enterprise_to_revenue": obj.get("enterprise_to_revenue"),
            "cash_per_share": obj.get("cash_per_share"),
            "quick_ratio": obj.get("quick_ratio"),
            "current_ratio": obj.get("current_ratio"),
            "debt_to_equity": obj.get("debt_to_equity"),
            "gross_margin": obj.get("gross_margin"),
            "operating_margin": obj.get("operating_margin"),
            "ebitda_margin": obj.get("ebitda_margin"),
            "profit_margin": obj.get("profit_margin"),
            "return_on_assets": obj.get("return_on_assets"),
            "return_on_equity": obj.get("return_on_equity"),
            "dividend_yield": obj.get("dividend_yield"),
            "dividend_yield_5y_avg": obj.get("dividend_yield_5y_avg"),
            "payout_ratio": obj.get("payout_ratio"),
            "book_value": obj.get("book_value"),
            "price_to_book": obj.get("price_to_book"),
            "enterprise_value": obj.get("enterprise_value"),
            "overall_risk": obj.get("overall_risk"),
            "audit_risk": obj.get("audit_risk"),
            "board_risk": obj.get("board_risk"),
            "compensation_risk": obj.get("compensation_risk"),
            "shareholder_rights_risk": obj.get("shareholder_rights_risk"),
            "beta": obj.get("beta"),
            "price_return_1y": obj.get("price_return_1y"),
            "currency": obj.get("currency")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


