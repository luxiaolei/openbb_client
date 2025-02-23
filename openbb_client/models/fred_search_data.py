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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FredSearchData(BaseModel):
    """
    FRED Search Data.
    """ # noqa: E501
    release_id: Optional[StrictStr] = None
    series_id: Optional[StrictStr] = None
    series_group: Optional[StrictStr] = None
    region_type: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    observation_start: Optional[date] = None
    observation_end: Optional[date] = None
    frequency: Optional[StrictStr] = None
    frequency_short: Optional[StrictStr] = None
    units: Optional[StrictStr] = None
    units_short: Optional[StrictStr] = None
    seasonal_adjustment: Optional[StrictStr] = None
    seasonal_adjustment_short: Optional[StrictStr] = None
    last_updated: Optional[datetime] = None
    popularity: Optional[StrictInt] = None
    group_popularity: Optional[StrictInt] = None
    realtime_start: Optional[date] = None
    realtime_end: Optional[date] = None
    notes: Optional[StrictStr] = None
    press_release: Optional[StrictBool] = None
    url: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["release_id", "series_id", "series_group", "region_type", "name", "title", "observation_start", "observation_end", "frequency", "frequency_short", "units", "units_short", "seasonal_adjustment", "seasonal_adjustment_short", "last_updated", "popularity", "group_popularity", "realtime_start", "realtime_end", "notes", "press_release", "url"]

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
        """Create an instance of FredSearchData from a JSON string"""
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

        # set to None if release_id (nullable) is None
        # and model_fields_set contains the field
        if self.release_id is None and "release_id" in self.model_fields_set:
            _dict['release_id'] = None

        # set to None if series_id (nullable) is None
        # and model_fields_set contains the field
        if self.series_id is None and "series_id" in self.model_fields_set:
            _dict['series_id'] = None

        # set to None if series_group (nullable) is None
        # and model_fields_set contains the field
        if self.series_group is None and "series_group" in self.model_fields_set:
            _dict['series_group'] = None

        # set to None if region_type (nullable) is None
        # and model_fields_set contains the field
        if self.region_type is None and "region_type" in self.model_fields_set:
            _dict['region_type'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if observation_start (nullable) is None
        # and model_fields_set contains the field
        if self.observation_start is None and "observation_start" in self.model_fields_set:
            _dict['observation_start'] = None

        # set to None if observation_end (nullable) is None
        # and model_fields_set contains the field
        if self.observation_end is None and "observation_end" in self.model_fields_set:
            _dict['observation_end'] = None

        # set to None if frequency (nullable) is None
        # and model_fields_set contains the field
        if self.frequency is None and "frequency" in self.model_fields_set:
            _dict['frequency'] = None

        # set to None if frequency_short (nullable) is None
        # and model_fields_set contains the field
        if self.frequency_short is None and "frequency_short" in self.model_fields_set:
            _dict['frequency_short'] = None

        # set to None if units (nullable) is None
        # and model_fields_set contains the field
        if self.units is None and "units" in self.model_fields_set:
            _dict['units'] = None

        # set to None if units_short (nullable) is None
        # and model_fields_set contains the field
        if self.units_short is None and "units_short" in self.model_fields_set:
            _dict['units_short'] = None

        # set to None if seasonal_adjustment (nullable) is None
        # and model_fields_set contains the field
        if self.seasonal_adjustment is None and "seasonal_adjustment" in self.model_fields_set:
            _dict['seasonal_adjustment'] = None

        # set to None if seasonal_adjustment_short (nullable) is None
        # and model_fields_set contains the field
        if self.seasonal_adjustment_short is None and "seasonal_adjustment_short" in self.model_fields_set:
            _dict['seasonal_adjustment_short'] = None

        # set to None if last_updated (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated is None and "last_updated" in self.model_fields_set:
            _dict['last_updated'] = None

        # set to None if popularity (nullable) is None
        # and model_fields_set contains the field
        if self.popularity is None and "popularity" in self.model_fields_set:
            _dict['popularity'] = None

        # set to None if group_popularity (nullable) is None
        # and model_fields_set contains the field
        if self.group_popularity is None and "group_popularity" in self.model_fields_set:
            _dict['group_popularity'] = None

        # set to None if realtime_start (nullable) is None
        # and model_fields_set contains the field
        if self.realtime_start is None and "realtime_start" in self.model_fields_set:
            _dict['realtime_start'] = None

        # set to None if realtime_end (nullable) is None
        # and model_fields_set contains the field
        if self.realtime_end is None and "realtime_end" in self.model_fields_set:
            _dict['realtime_end'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if press_release (nullable) is None
        # and model_fields_set contains the field
        if self.press_release is None and "press_release" in self.model_fields_set:
            _dict['press_release'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FredSearchData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "release_id": obj.get("release_id"),
            "series_id": obj.get("series_id"),
            "series_group": obj.get("series_group"),
            "region_type": obj.get("region_type"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "observation_start": obj.get("observation_start"),
            "observation_end": obj.get("observation_end"),
            "frequency": obj.get("frequency"),
            "frequency_short": obj.get("frequency_short"),
            "units": obj.get("units"),
            "units_short": obj.get("units_short"),
            "seasonal_adjustment": obj.get("seasonal_adjustment"),
            "seasonal_adjustment_short": obj.get("seasonal_adjustment_short"),
            "last_updated": obj.get("last_updated"),
            "popularity": obj.get("popularity"),
            "group_popularity": obj.get("group_popularity"),
            "realtime_start": obj.get("realtime_start"),
            "realtime_end": obj.get("realtime_end"),
            "notes": obj.get("notes"),
            "press_release": obj.get("press_release"),
            "url": obj.get("url")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


