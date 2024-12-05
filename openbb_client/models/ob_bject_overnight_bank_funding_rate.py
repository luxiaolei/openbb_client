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
from openbb_client.models.chart import Chart
from openbb_client.models.ob_bject_overnight_bank_funding_rate_results_inner import OBBjectOvernightBankFundingRateResultsInner
from openbb_client.models.warning import Warning
from typing import Optional, Set
from typing_extensions import Self

class OBBjectOvernightBankFundingRate(BaseModel):
    """
    OBBject with results of type OvernightBankFundingRate
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    results: Optional[List[OBBjectOvernightBankFundingRateResultsInner]] = None
    provider: Optional[StrictStr] = None
    warnings: Optional[List[Warning]] = None
    chart: Optional[Chart] = None
    extra: Optional[Dict[str, Any]] = Field(default=None, description="Extra info.")
    __properties: ClassVar[List[str]] = ["_id", "results", "provider", "warnings", "chart", "extra"]

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
        """Create an instance of OBBjectOvernightBankFundingRate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of chart
        if self.chart:
            _dict['chart'] = self.chart.to_dict()
        # set to None if results (nullable) is None
        # and model_fields_set contains the field
        if self.results is None and "results" in self.model_fields_set:
            _dict['results'] = None

        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        # set to None if chart (nullable) is None
        # and model_fields_set contains the field
        if self.chart is None and "chart" in self.model_fields_set:
            _dict['chart'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OBBjectOvernightBankFundingRate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_id": obj.get("_id"),
            "results": [OBBjectOvernightBankFundingRateResultsInner.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "provider": obj.get("provider"),
            "warnings": [Warning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "chart": Chart.from_dict(obj["chart"]) if obj.get("chart") is not None else None,
            "extra": obj.get("extra")
        })
        return _obj


