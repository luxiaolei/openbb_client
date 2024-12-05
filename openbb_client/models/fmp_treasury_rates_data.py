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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class FMPTreasuryRatesData(BaseModel):
    """
    FMP Treasury Rates Data.
    """ # noqa: E501
    var_date: date = Field(description="The date of the data.", alias="date")
    week_4: Optional[Union[StrictFloat, StrictInt]] = None
    month_1: Optional[Union[StrictFloat, StrictInt]] = None
    month_2: Optional[Union[StrictFloat, StrictInt]] = None
    month_3: Optional[Union[StrictFloat, StrictInt]] = None
    month_6: Optional[Union[StrictFloat, StrictInt]] = None
    year_1: Optional[Union[StrictFloat, StrictInt]] = None
    year_2: Optional[Union[StrictFloat, StrictInt]] = None
    year_3: Optional[Union[StrictFloat, StrictInt]] = None
    year_5: Optional[Union[StrictFloat, StrictInt]] = None
    year_7: Optional[Union[StrictFloat, StrictInt]] = None
    year_10: Optional[Union[StrictFloat, StrictInt]] = None
    year_20: Optional[Union[StrictFloat, StrictInt]] = None
    year_30: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "week_4", "month_1", "month_2", "month_3", "month_6", "year_1", "year_2", "year_3", "year_5", "year_7", "year_10", "year_20", "year_30"]

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
        """Create an instance of FMPTreasuryRatesData from a JSON string"""
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

        # set to None if week_4 (nullable) is None
        # and model_fields_set contains the field
        if self.week_4 is None and "week_4" in self.model_fields_set:
            _dict['week_4'] = None

        # set to None if month_1 (nullable) is None
        # and model_fields_set contains the field
        if self.month_1 is None and "month_1" in self.model_fields_set:
            _dict['month_1'] = None

        # set to None if month_2 (nullable) is None
        # and model_fields_set contains the field
        if self.month_2 is None and "month_2" in self.model_fields_set:
            _dict['month_2'] = None

        # set to None if month_3 (nullable) is None
        # and model_fields_set contains the field
        if self.month_3 is None and "month_3" in self.model_fields_set:
            _dict['month_3'] = None

        # set to None if month_6 (nullable) is None
        # and model_fields_set contains the field
        if self.month_6 is None and "month_6" in self.model_fields_set:
            _dict['month_6'] = None

        # set to None if year_1 (nullable) is None
        # and model_fields_set contains the field
        if self.year_1 is None and "year_1" in self.model_fields_set:
            _dict['year_1'] = None

        # set to None if year_2 (nullable) is None
        # and model_fields_set contains the field
        if self.year_2 is None and "year_2" in self.model_fields_set:
            _dict['year_2'] = None

        # set to None if year_3 (nullable) is None
        # and model_fields_set contains the field
        if self.year_3 is None and "year_3" in self.model_fields_set:
            _dict['year_3'] = None

        # set to None if year_5 (nullable) is None
        # and model_fields_set contains the field
        if self.year_5 is None and "year_5" in self.model_fields_set:
            _dict['year_5'] = None

        # set to None if year_7 (nullable) is None
        # and model_fields_set contains the field
        if self.year_7 is None and "year_7" in self.model_fields_set:
            _dict['year_7'] = None

        # set to None if year_10 (nullable) is None
        # and model_fields_set contains the field
        if self.year_10 is None and "year_10" in self.model_fields_set:
            _dict['year_10'] = None

        # set to None if year_20 (nullable) is None
        # and model_fields_set contains the field
        if self.year_20 is None and "year_20" in self.model_fields_set:
            _dict['year_20'] = None

        # set to None if year_30 (nullable) is None
        # and model_fields_set contains the field
        if self.year_30 is None and "year_30" in self.model_fields_set:
            _dict['year_30'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPTreasuryRatesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "week_4": obj.get("week_4"),
            "month_1": obj.get("month_1"),
            "month_2": obj.get("month_2"),
            "month_3": obj.get("month_3"),
            "month_6": obj.get("month_6"),
            "year_1": obj.get("year_1"),
            "year_2": obj.get("year_2"),
            "year_3": obj.get("year_3"),
            "year_5": obj.get("year_5"),
            "year_7": obj.get("year_7"),
            "year_10": obj.get("year_10"),
            "year_20": obj.get("year_20"),
            "year_30": obj.get("year_30")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


