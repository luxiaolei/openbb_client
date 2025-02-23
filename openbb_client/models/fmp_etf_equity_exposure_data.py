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
from openbb_client.models.market_value import MarketValue
from typing import Optional, Set
from typing_extensions import Self

class FMPEtfEquityExposureData(BaseModel):
    """
    FMP ETF Equity Exposure Data.
    """ # noqa: E501
    equity_symbol: StrictStr = Field(description="The symbol of the equity requested.")
    etf_symbol: StrictStr = Field(description="The symbol of the ETF with exposure to the requested equity.")
    shares: Optional[Union[StrictFloat, StrictInt]] = None
    weight: Optional[Union[StrictFloat, StrictInt]] = None
    market_value: Optional[MarketValue] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["equity_symbol", "etf_symbol", "shares", "weight", "market_value"]

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
        """Create an instance of FMPEtfEquityExposureData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of market_value
        if self.market_value:
            _dict['market_value'] = self.market_value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if shares (nullable) is None
        # and model_fields_set contains the field
        if self.shares is None and "shares" in self.model_fields_set:
            _dict['shares'] = None

        # set to None if weight (nullable) is None
        # and model_fields_set contains the field
        if self.weight is None and "weight" in self.model_fields_set:
            _dict['weight'] = None

        # set to None if market_value (nullable) is None
        # and model_fields_set contains the field
        if self.market_value is None and "market_value" in self.model_fields_set:
            _dict['market_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPEtfEquityExposureData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "equity_symbol": obj.get("equity_symbol"),
            "etf_symbol": obj.get("etf_symbol"),
            "shares": obj.get("shares"),
            "weight": obj.get("weight"),
            "market_value": MarketValue.from_dict(obj["market_value"]) if obj.get("market_value") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


