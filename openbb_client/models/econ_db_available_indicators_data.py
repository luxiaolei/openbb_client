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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EconDbAvailableIndicatorsData(BaseModel):
    """
    EconDB Available Indicators Data.
    """ # noqa: E501
    symbol_root: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    iso: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    frequency: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    scale: Optional[StrictStr] = None
    multiplier: Optional[StrictInt]
    transformation: StrictStr = Field(description="Transformation type.")
    source: Optional[StrictStr] = None
    first_date: Optional[date] = None
    last_date: Optional[date] = None
    last_insert_timestamp: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol_root", "symbol", "country", "iso", "description", "frequency", "currency", "scale", "multiplier", "transformation", "source", "first_date", "last_date", "last_insert_timestamp"]

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
        """Create an instance of EconDbAvailableIndicatorsData from a JSON string"""
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

        # set to None if symbol_root (nullable) is None
        # and model_fields_set contains the field
        if self.symbol_root is None and "symbol_root" in self.model_fields_set:
            _dict['symbol_root'] = None

        # set to None if symbol (nullable) is None
        # and model_fields_set contains the field
        if self.symbol is None and "symbol" in self.model_fields_set:
            _dict['symbol'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if iso (nullable) is None
        # and model_fields_set contains the field
        if self.iso is None and "iso" in self.model_fields_set:
            _dict['iso'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if frequency (nullable) is None
        # and model_fields_set contains the field
        if self.frequency is None and "frequency" in self.model_fields_set:
            _dict['frequency'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if scale (nullable) is None
        # and model_fields_set contains the field
        if self.scale is None and "scale" in self.model_fields_set:
            _dict['scale'] = None

        # set to None if multiplier (nullable) is None
        # and model_fields_set contains the field
        if self.multiplier is None and "multiplier" in self.model_fields_set:
            _dict['multiplier'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if first_date (nullable) is None
        # and model_fields_set contains the field
        if self.first_date is None and "first_date" in self.model_fields_set:
            _dict['first_date'] = None

        # set to None if last_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_date is None and "last_date" in self.model_fields_set:
            _dict['last_date'] = None

        # set to None if last_insert_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.last_insert_timestamp is None and "last_insert_timestamp" in self.model_fields_set:
            _dict['last_insert_timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EconDbAvailableIndicatorsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol_root": obj.get("symbol_root"),
            "symbol": obj.get("symbol"),
            "country": obj.get("country"),
            "iso": obj.get("iso"),
            "description": obj.get("description"),
            "frequency": obj.get("frequency"),
            "currency": obj.get("currency"),
            "scale": obj.get("scale"),
            "multiplier": obj.get("multiplier"),
            "transformation": obj.get("transformation"),
            "source": obj.get("source"),
            "first_date": obj.get("first_date"),
            "last_date": obj.get("last_date"),
            "last_insert_timestamp": obj.get("last_insert_timestamp")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


