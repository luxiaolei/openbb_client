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
from openbb_client.models.volume import Volume
from typing import Optional, Set
from typing_extensions import Self

class TiingoEquityHistoricalData(BaseModel):
    """
    Tiingo Equity Historical Price Data.
    """ # noqa: E501
    var_date: Date6 = Field(alias="date")
    open: Union[StrictFloat, StrictInt] = Field(description="The open price.")
    high: Union[StrictFloat, StrictInt] = Field(description="The high price.")
    low: Union[StrictFloat, StrictInt] = Field(description="The low price.")
    close: Union[StrictFloat, StrictInt] = Field(description="The close price.")
    volume: Optional[Volume] = None
    vwap: Optional[Union[StrictFloat, StrictInt]] = None
    adj_open: Optional[Union[StrictFloat, StrictInt]] = None
    adj_high: Optional[Union[StrictFloat, StrictInt]] = None
    adj_low: Optional[Union[StrictFloat, StrictInt]] = None
    adj_close: Optional[Union[StrictFloat, StrictInt]] = None
    adj_volume: Optional[Union[StrictFloat, StrictInt]] = None
    split_ratio: Optional[Union[StrictFloat, StrictInt]] = None
    dividend: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "open", "high", "low", "close", "volume", "vwap", "adj_open", "adj_high", "adj_low", "adj_close", "adj_volume", "split_ratio", "dividend"]

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
        """Create an instance of TiingoEquityHistoricalData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of volume
        if self.volume:
            _dict['volume'] = self.volume.to_dict()
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

        # set to None if adj_open (nullable) is None
        # and model_fields_set contains the field
        if self.adj_open is None and "adj_open" in self.model_fields_set:
            _dict['adj_open'] = None

        # set to None if adj_high (nullable) is None
        # and model_fields_set contains the field
        if self.adj_high is None and "adj_high" in self.model_fields_set:
            _dict['adj_high'] = None

        # set to None if adj_low (nullable) is None
        # and model_fields_set contains the field
        if self.adj_low is None and "adj_low" in self.model_fields_set:
            _dict['adj_low'] = None

        # set to None if adj_close (nullable) is None
        # and model_fields_set contains the field
        if self.adj_close is None and "adj_close" in self.model_fields_set:
            _dict['adj_close'] = None

        # set to None if adj_volume (nullable) is None
        # and model_fields_set contains the field
        if self.adj_volume is None and "adj_volume" in self.model_fields_set:
            _dict['adj_volume'] = None

        # set to None if split_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.split_ratio is None and "split_ratio" in self.model_fields_set:
            _dict['split_ratio'] = None

        # set to None if dividend (nullable) is None
        # and model_fields_set contains the field
        if self.dividend is None and "dividend" in self.model_fields_set:
            _dict['dividend'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TiingoEquityHistoricalData from a dict"""
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
            "volume": Volume.from_dict(obj["volume"]) if obj.get("volume") is not None else None,
            "vwap": obj.get("vwap"),
            "adj_open": obj.get("adj_open"),
            "adj_high": obj.get("adj_high"),
            "adj_low": obj.get("adj_low"),
            "adj_close": obj.get("adj_close"),
            "adj_volume": obj.get("adj_volume"),
            "split_ratio": obj.get("split_ratio"),
            "dividend": obj.get("dividend")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


