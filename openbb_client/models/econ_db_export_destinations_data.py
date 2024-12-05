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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openbb_client.models.value1 import Value1
from typing import Optional, Set
from typing_extensions import Self

class EconDbExportDestinationsData(BaseModel):
    """
    EconDB Export Destinations Data.
    """ # noqa: E501
    origin_country: StrictStr = Field(description="The country of origin.")
    destination_country: StrictStr = Field(description="The destination country.")
    value: Value1
    units: StrictStr = Field(description="The units of measurement for the value.")
    title: StrictStr = Field(description="The title of the data.")
    footnote: Optional[StrictStr]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["origin_country", "destination_country", "value", "units", "title", "footnote"]

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
        """Create an instance of EconDbExportDestinationsData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if footnote (nullable) is None
        # and model_fields_set contains the field
        if self.footnote is None and "footnote" in self.model_fields_set:
            _dict['footnote'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EconDbExportDestinationsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "origin_country": obj.get("origin_country"),
            "destination_country": obj.get("destination_country"),
            "value": Value1.from_dict(obj["value"]) if obj.get("value") is not None else None,
            "units": obj.get("units"),
            "title": obj.get("title"),
            "footnote": obj.get("footnote")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


