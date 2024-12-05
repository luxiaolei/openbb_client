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

class IntrinioPriceTargetConsensusData(BaseModel):
    """
    Intrinio Price Target Consensus  Data.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    name: Optional[StrictStr] = None
    target_high: Optional[Union[StrictFloat, StrictInt]] = None
    target_low: Optional[Union[StrictFloat, StrictInt]] = None
    target_consensus: Optional[Union[StrictFloat, StrictInt]] = None
    target_median: Optional[Union[StrictFloat, StrictInt]] = None
    standard_deviation: Optional[Union[StrictFloat, StrictInt]] = None
    total_anaylsts: Optional[StrictInt] = None
    raised: Optional[StrictInt] = None
    lowered: Optional[StrictInt] = None
    most_recent_date: Optional[date] = None
    industry_group_number: Optional[StrictInt] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "name", "target_high", "target_low", "target_consensus", "target_median", "standard_deviation", "total_anaylsts", "raised", "lowered", "most_recent_date", "industry_group_number"]

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
        """Create an instance of IntrinioPriceTargetConsensusData from a JSON string"""
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

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if target_high (nullable) is None
        # and model_fields_set contains the field
        if self.target_high is None and "target_high" in self.model_fields_set:
            _dict['target_high'] = None

        # set to None if target_low (nullable) is None
        # and model_fields_set contains the field
        if self.target_low is None and "target_low" in self.model_fields_set:
            _dict['target_low'] = None

        # set to None if target_consensus (nullable) is None
        # and model_fields_set contains the field
        if self.target_consensus is None and "target_consensus" in self.model_fields_set:
            _dict['target_consensus'] = None

        # set to None if target_median (nullable) is None
        # and model_fields_set contains the field
        if self.target_median is None and "target_median" in self.model_fields_set:
            _dict['target_median'] = None

        # set to None if standard_deviation (nullable) is None
        # and model_fields_set contains the field
        if self.standard_deviation is None and "standard_deviation" in self.model_fields_set:
            _dict['standard_deviation'] = None

        # set to None if total_anaylsts (nullable) is None
        # and model_fields_set contains the field
        if self.total_anaylsts is None and "total_anaylsts" in self.model_fields_set:
            _dict['total_anaylsts'] = None

        # set to None if raised (nullable) is None
        # and model_fields_set contains the field
        if self.raised is None and "raised" in self.model_fields_set:
            _dict['raised'] = None

        # set to None if lowered (nullable) is None
        # and model_fields_set contains the field
        if self.lowered is None and "lowered" in self.model_fields_set:
            _dict['lowered'] = None

        # set to None if most_recent_date (nullable) is None
        # and model_fields_set contains the field
        if self.most_recent_date is None and "most_recent_date" in self.model_fields_set:
            _dict['most_recent_date'] = None

        # set to None if industry_group_number (nullable) is None
        # and model_fields_set contains the field
        if self.industry_group_number is None and "industry_group_number" in self.model_fields_set:
            _dict['industry_group_number'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntrinioPriceTargetConsensusData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "target_high": obj.get("target_high"),
            "target_low": obj.get("target_low"),
            "target_consensus": obj.get("target_consensus"),
            "target_median": obj.get("target_median"),
            "standard_deviation": obj.get("standard_deviation"),
            "total_anaylsts": obj.get("total_anaylsts"),
            "raised": obj.get("raised"),
            "lowered": obj.get("lowered"),
            "most_recent_date": obj.get("most_recent_date"),
            "industry_group_number": obj.get("industry_group_number")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


