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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IntrinioSearchAttributesData(BaseModel):
    """
    Intrinio Search Attributes Data.
    """ # noqa: E501
    id: StrictStr = Field(description="ID of the financial attribute.")
    name: StrictStr = Field(description="Name of the financial attribute.")
    tag: StrictStr = Field(description="Tag of the financial attribute.")
    statement_code: StrictStr = Field(description="Code of the financial statement.")
    statement_type: Optional[StrictStr] = None
    parent_name: Optional[StrictStr] = None
    sequence: Optional[StrictInt] = None
    factor: Optional[StrictStr] = None
    transaction: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    unit: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "tag", "statement_code", "statement_type", "parent_name", "sequence", "factor", "transaction", "type", "unit"]

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
        """Create an instance of IntrinioSearchAttributesData from a JSON string"""
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

        # set to None if statement_type (nullable) is None
        # and model_fields_set contains the field
        if self.statement_type is None and "statement_type" in self.model_fields_set:
            _dict['statement_type'] = None

        # set to None if parent_name (nullable) is None
        # and model_fields_set contains the field
        if self.parent_name is None and "parent_name" in self.model_fields_set:
            _dict['parent_name'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['sequence'] = None

        # set to None if factor (nullable) is None
        # and model_fields_set contains the field
        if self.factor is None and "factor" in self.model_fields_set:
            _dict['factor'] = None

        # set to None if transaction (nullable) is None
        # and model_fields_set contains the field
        if self.transaction is None and "transaction" in self.model_fields_set:
            _dict['transaction'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntrinioSearchAttributesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "tag": obj.get("tag"),
            "statement_code": obj.get("statement_code"),
            "statement_type": obj.get("statement_type"),
            "parent_name": obj.get("parent_name"),
            "sequence": obj.get("sequence"),
            "factor": obj.get("factor"),
            "transaction": obj.get("transaction"),
            "type": obj.get("type"),
            "unit": obj.get("unit")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


