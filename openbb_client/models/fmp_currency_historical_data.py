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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from openbb_client.models.date6 import Date6
from typing import Optional, Set
from typing_extensions import Self

class FMPCurrencyHistoricalData(BaseModel):
    """
    FMP Currency Historical Price Data.
    """ # noqa: E501
    var_date: Date6 = Field(alias="date")
    open: Union[StrictFloat, StrictInt] = Field(description="The open price.")
    high: Union[StrictFloat, StrictInt] = Field(description="The high price.")
    low: Union[StrictFloat, StrictInt] = Field(description="The low price.")
    close: Union[StrictFloat, StrictInt] = Field(description="The close price.")
    volume: Optional[Union[StrictFloat, StrictInt]] = None
    vwap: Optional[Union[StrictFloat, StrictInt]] = None
    adj_close: Optional[Union[StrictFloat, StrictInt]] = None
    change: Optional[Union[StrictFloat, StrictInt]] = None
    change_percent: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "open", "high", "low", "close", "volume", "vwap", "adj_close", "change", "change_percent"]

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
        """Create an instance of FMPCurrencyHistoricalData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_date
        if self.var_date:
            _dict['date'] = self.var_date.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if volume (nullable) is None
        # and model_fields_set contains the field
        if self.volume is None and "volume" in self.model_fields_set:
            _dict['volume'] = None

        # set to None if vwap (nullable) is None
        # and model_fields_set contains the field
        if self.vwap is None and "vwap" in self.model_fields_set:
            _dict['vwap'] = None

        # set to None if adj_close (nullable) is None
        # and model_fields_set contains the field
        if self.adj_close is None and "adj_close" in self.model_fields_set:
            _dict['adj_close'] = None

        # set to None if change (nullable) is None
        # and model_fields_set contains the field
        if self.change is None and "change" in self.model_fields_set:
            _dict['change'] = None

        # set to None if change_percent (nullable) is None
        # and model_fields_set contains the field
        if self.change_percent is None and "change_percent" in self.model_fields_set:
            _dict['change_percent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPCurrencyHistoricalData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": Date6.from_dict(obj["date"]) if obj.get("date") is not None else None,
            "open": obj.get("open"),
            "high": obj.get("high"),
            "low": obj.get("low"),
            "close": obj.get("close"),
            "volume": obj.get("volume"),
            "vwap": obj.get("vwap"),
            "adj_close": obj.get("adj_close"),
            "change": obj.get("change"),
            "change_percent": obj.get("change_percent")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


