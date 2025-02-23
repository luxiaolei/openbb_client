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

class FMPHistoricalEpsData(BaseModel):
    """
    FMP Historical EPS Data.
    """ # noqa: E501
    var_date: Optional[date] = Field(default=None, description="The date of the data.", alias="date")
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    announce_time: Optional[StrictStr] = None
    eps_actual: Optional[Union[StrictFloat, StrictInt]] = None
    eps_estimated: Optional[Union[StrictFloat, StrictInt]] = None
    revenue_estimated: Optional[Union[StrictFloat, StrictInt]] = None
    revenue_actual: Optional[Union[StrictFloat, StrictInt]] = None
    reporting_time: Optional[StrictStr] = None
    updated_at: Optional[date] = None
    period_ending: Optional[date] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "symbol", "announce_time", "eps_actual", "eps_estimated", "revenue_estimated", "revenue_actual", "reporting_time", "updated_at", "period_ending"]

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
        """Create an instance of FMPHistoricalEpsData from a JSON string"""
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

        # set to None if announce_time (nullable) is None
        # and model_fields_set contains the field
        if self.announce_time is None and "announce_time" in self.model_fields_set:
            _dict['announce_time'] = None

        # set to None if eps_actual (nullable) is None
        # and model_fields_set contains the field
        if self.eps_actual is None and "eps_actual" in self.model_fields_set:
            _dict['eps_actual'] = None

        # set to None if eps_estimated (nullable) is None
        # and model_fields_set contains the field
        if self.eps_estimated is None and "eps_estimated" in self.model_fields_set:
            _dict['eps_estimated'] = None

        # set to None if revenue_estimated (nullable) is None
        # and model_fields_set contains the field
        if self.revenue_estimated is None and "revenue_estimated" in self.model_fields_set:
            _dict['revenue_estimated'] = None

        # set to None if revenue_actual (nullable) is None
        # and model_fields_set contains the field
        if self.revenue_actual is None and "revenue_actual" in self.model_fields_set:
            _dict['revenue_actual'] = None

        # set to None if reporting_time (nullable) is None
        # and model_fields_set contains the field
        if self.reporting_time is None and "reporting_time" in self.model_fields_set:
            _dict['reporting_time'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if period_ending (nullable) is None
        # and model_fields_set contains the field
        if self.period_ending is None and "period_ending" in self.model_fields_set:
            _dict['period_ending'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPHistoricalEpsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "symbol": obj.get("symbol"),
            "announce_time": obj.get("announce_time"),
            "eps_actual": obj.get("eps_actual"),
            "eps_estimated": obj.get("eps_estimated"),
            "revenue_estimated": obj.get("revenue_estimated"),
            "revenue_actual": obj.get("revenue_actual"),
            "reporting_time": obj.get("reporting_time"),
            "updated_at": obj.get("updated_at"),
            "period_ending": obj.get("period_ending")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


