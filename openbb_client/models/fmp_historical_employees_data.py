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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class FMPHistoricalEmployeesData(BaseModel):
    """
    FMP Historical Employees Data.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    cik: StrictInt = Field(description="Central Index Key (CIK) for the requested entity.")
    acceptance_time: datetime = Field(description="Time of acceptance of the company employee.")
    period_of_report: date = Field(description="Date of reporting of the company employee.")
    company_name: StrictStr = Field(description="Registered name of the company to retrieve the historical employees of.")
    form_type: StrictStr = Field(description="Form type of the company employee.")
    filing_date: date = Field(description="Filing date of the company employee")
    employee_count: StrictInt = Field(description="Count of employees of the company.")
    source: StrictStr = Field(description="Source URL which retrieves this data for the company.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "cik", "acceptance_time", "period_of_report", "company_name", "form_type", "filing_date", "employee_count", "source"]

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
        """Create an instance of FMPHistoricalEmployeesData from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPHistoricalEmployeesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "cik": obj.get("cik"),
            "acceptance_time": obj.get("acceptance_time"),
            "period_of_report": obj.get("period_of_report"),
            "company_name": obj.get("company_name"),
            "form_type": obj.get("form_type"),
            "filing_date": obj.get("filing_date"),
            "employee_count": obj.get("employee_count"),
            "source": obj.get("source")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


