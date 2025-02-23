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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BenzingaAnalystSearchData(BaseModel):
    """
    Benzinga Analyst Search Data.
    """ # noqa: E501
    last_updated: Optional[datetime] = None
    firm_name: Optional[StrictStr] = None
    name_first: Optional[StrictStr] = None
    name_last: Optional[StrictStr] = None
    name_full: StrictStr = Field(description="Analyst full name.")
    analyst_id: Optional[StrictStr] = None
    firm_id: Optional[StrictStr] = None
    smart_score: Optional[Union[StrictFloat, StrictInt]] = None
    overall_success_rate: Optional[Union[StrictFloat, StrictInt]] = None
    overall_avg_return_percentile: Optional[Union[StrictFloat, StrictInt]] = None
    total_ratings_percentile: Optional[Union[StrictFloat, StrictInt]] = None
    total_ratings: Optional[StrictInt] = None
    overall_gain_count: Optional[StrictInt] = None
    overall_loss_count: Optional[StrictInt] = None
    overall_average_return: Optional[Union[StrictFloat, StrictInt]] = None
    overall_std_dev: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_1m: Optional[StrictInt] = None
    loss_count_1m: Optional[StrictInt] = None
    average_return_1m: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_1m: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_1m: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_1m: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_3m: Optional[StrictInt] = None
    loss_count_3m: Optional[StrictInt] = None
    average_return_3m: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_3m: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_3m: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_3m: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_6m: Optional[StrictInt] = None
    loss_count_6m: Optional[StrictInt] = None
    average_return_6m: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_6m: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_9m: Optional[StrictInt] = None
    loss_count_9m: Optional[StrictInt] = None
    average_return_9m: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_9m: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_9m: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_9m: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_1y: Optional[StrictInt] = None
    loss_count_1y: Optional[StrictInt] = None
    average_return_1y: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_1y: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_1y: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_1y: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_2y: Optional[StrictInt] = None
    loss_count_2y: Optional[StrictInt] = None
    average_return_2y: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_2y: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_2y: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_2y: Optional[Union[StrictFloat, StrictInt]] = None
    gain_count_3y: Optional[StrictInt] = None
    loss_count_3y: Optional[StrictInt] = None
    average_return_3y: Optional[Union[StrictFloat, StrictInt]] = None
    std_dev_3y: Optional[Union[StrictFloat, StrictInt]] = None
    smart_score_3y: Optional[Union[StrictFloat, StrictInt]] = None
    success_rate_3y: Optional[Union[StrictFloat, StrictInt]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["last_updated", "firm_name", "name_first", "name_last", "name_full", "analyst_id", "firm_id", "smart_score", "overall_success_rate", "overall_avg_return_percentile", "total_ratings_percentile", "total_ratings", "overall_gain_count", "overall_loss_count", "overall_average_return", "overall_std_dev", "gain_count_1m", "loss_count_1m", "average_return_1m", "std_dev_1m", "smart_score_1m", "success_rate_1m", "gain_count_3m", "loss_count_3m", "average_return_3m", "std_dev_3m", "smart_score_3m", "success_rate_3m", "gain_count_6m", "loss_count_6m", "average_return_6m", "std_dev_6m", "gain_count_9m", "loss_count_9m", "average_return_9m", "std_dev_9m", "smart_score_9m", "success_rate_9m", "gain_count_1y", "loss_count_1y", "average_return_1y", "std_dev_1y", "smart_score_1y", "success_rate_1y", "gain_count_2y", "loss_count_2y", "average_return_2y", "std_dev_2y", "smart_score_2y", "success_rate_2y", "gain_count_3y", "loss_count_3y", "average_return_3y", "std_dev_3y", "smart_score_3y", "success_rate_3y"]

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
        """Create an instance of BenzingaAnalystSearchData from a JSON string"""
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

        # set to None if last_updated (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated is None and "last_updated" in self.model_fields_set:
            _dict['last_updated'] = None

        # set to None if firm_name (nullable) is None
        # and model_fields_set contains the field
        if self.firm_name is None and "firm_name" in self.model_fields_set:
            _dict['firm_name'] = None

        # set to None if name_first (nullable) is None
        # and model_fields_set contains the field
        if self.name_first is None and "name_first" in self.model_fields_set:
            _dict['name_first'] = None

        # set to None if name_last (nullable) is None
        # and model_fields_set contains the field
        if self.name_last is None and "name_last" in self.model_fields_set:
            _dict['name_last'] = None

        # set to None if analyst_id (nullable) is None
        # and model_fields_set contains the field
        if self.analyst_id is None and "analyst_id" in self.model_fields_set:
            _dict['analyst_id'] = None

        # set to None if firm_id (nullable) is None
        # and model_fields_set contains the field
        if self.firm_id is None and "firm_id" in self.model_fields_set:
            _dict['firm_id'] = None

        # set to None if smart_score (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score is None and "smart_score" in self.model_fields_set:
            _dict['smart_score'] = None

        # set to None if overall_success_rate (nullable) is None
        # and model_fields_set contains the field
        if self.overall_success_rate is None and "overall_success_rate" in self.model_fields_set:
            _dict['overall_success_rate'] = None

        # set to None if overall_avg_return_percentile (nullable) is None
        # and model_fields_set contains the field
        if self.overall_avg_return_percentile is None and "overall_avg_return_percentile" in self.model_fields_set:
            _dict['overall_avg_return_percentile'] = None

        # set to None if total_ratings_percentile (nullable) is None
        # and model_fields_set contains the field
        if self.total_ratings_percentile is None and "total_ratings_percentile" in self.model_fields_set:
            _dict['total_ratings_percentile'] = None

        # set to None if total_ratings (nullable) is None
        # and model_fields_set contains the field
        if self.total_ratings is None and "total_ratings" in self.model_fields_set:
            _dict['total_ratings'] = None

        # set to None if overall_gain_count (nullable) is None
        # and model_fields_set contains the field
        if self.overall_gain_count is None and "overall_gain_count" in self.model_fields_set:
            _dict['overall_gain_count'] = None

        # set to None if overall_loss_count (nullable) is None
        # and model_fields_set contains the field
        if self.overall_loss_count is None and "overall_loss_count" in self.model_fields_set:
            _dict['overall_loss_count'] = None

        # set to None if overall_average_return (nullable) is None
        # and model_fields_set contains the field
        if self.overall_average_return is None and "overall_average_return" in self.model_fields_set:
            _dict['overall_average_return'] = None

        # set to None if overall_std_dev (nullable) is None
        # and model_fields_set contains the field
        if self.overall_std_dev is None and "overall_std_dev" in self.model_fields_set:
            _dict['overall_std_dev'] = None

        # set to None if gain_count_1m (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_1m is None and "gain_count_1m" in self.model_fields_set:
            _dict['gain_count_1m'] = None

        # set to None if loss_count_1m (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_1m is None and "loss_count_1m" in self.model_fields_set:
            _dict['loss_count_1m'] = None

        # set to None if average_return_1m (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_1m is None and "average_return_1m" in self.model_fields_set:
            _dict['average_return_1m'] = None

        # set to None if std_dev_1m (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_1m is None and "std_dev_1m" in self.model_fields_set:
            _dict['std_dev_1m'] = None

        # set to None if smart_score_1m (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_1m is None and "smart_score_1m" in self.model_fields_set:
            _dict['smart_score_1m'] = None

        # set to None if success_rate_1m (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_1m is None and "success_rate_1m" in self.model_fields_set:
            _dict['success_rate_1m'] = None

        # set to None if gain_count_3m (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_3m is None and "gain_count_3m" in self.model_fields_set:
            _dict['gain_count_3m'] = None

        # set to None if loss_count_3m (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_3m is None and "loss_count_3m" in self.model_fields_set:
            _dict['loss_count_3m'] = None

        # set to None if average_return_3m (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_3m is None and "average_return_3m" in self.model_fields_set:
            _dict['average_return_3m'] = None

        # set to None if std_dev_3m (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_3m is None and "std_dev_3m" in self.model_fields_set:
            _dict['std_dev_3m'] = None

        # set to None if smart_score_3m (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_3m is None and "smart_score_3m" in self.model_fields_set:
            _dict['smart_score_3m'] = None

        # set to None if success_rate_3m (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_3m is None and "success_rate_3m" in self.model_fields_set:
            _dict['success_rate_3m'] = None

        # set to None if gain_count_6m (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_6m is None and "gain_count_6m" in self.model_fields_set:
            _dict['gain_count_6m'] = None

        # set to None if loss_count_6m (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_6m is None and "loss_count_6m" in self.model_fields_set:
            _dict['loss_count_6m'] = None

        # set to None if average_return_6m (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_6m is None and "average_return_6m" in self.model_fields_set:
            _dict['average_return_6m'] = None

        # set to None if std_dev_6m (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_6m is None and "std_dev_6m" in self.model_fields_set:
            _dict['std_dev_6m'] = None

        # set to None if gain_count_9m (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_9m is None and "gain_count_9m" in self.model_fields_set:
            _dict['gain_count_9m'] = None

        # set to None if loss_count_9m (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_9m is None and "loss_count_9m" in self.model_fields_set:
            _dict['loss_count_9m'] = None

        # set to None if average_return_9m (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_9m is None and "average_return_9m" in self.model_fields_set:
            _dict['average_return_9m'] = None

        # set to None if std_dev_9m (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_9m is None and "std_dev_9m" in self.model_fields_set:
            _dict['std_dev_9m'] = None

        # set to None if smart_score_9m (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_9m is None and "smart_score_9m" in self.model_fields_set:
            _dict['smart_score_9m'] = None

        # set to None if success_rate_9m (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_9m is None and "success_rate_9m" in self.model_fields_set:
            _dict['success_rate_9m'] = None

        # set to None if gain_count_1y (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_1y is None and "gain_count_1y" in self.model_fields_set:
            _dict['gain_count_1y'] = None

        # set to None if loss_count_1y (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_1y is None and "loss_count_1y" in self.model_fields_set:
            _dict['loss_count_1y'] = None

        # set to None if average_return_1y (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_1y is None and "average_return_1y" in self.model_fields_set:
            _dict['average_return_1y'] = None

        # set to None if std_dev_1y (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_1y is None and "std_dev_1y" in self.model_fields_set:
            _dict['std_dev_1y'] = None

        # set to None if smart_score_1y (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_1y is None and "smart_score_1y" in self.model_fields_set:
            _dict['smart_score_1y'] = None

        # set to None if success_rate_1y (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_1y is None and "success_rate_1y" in self.model_fields_set:
            _dict['success_rate_1y'] = None

        # set to None if gain_count_2y (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_2y is None and "gain_count_2y" in self.model_fields_set:
            _dict['gain_count_2y'] = None

        # set to None if loss_count_2y (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_2y is None and "loss_count_2y" in self.model_fields_set:
            _dict['loss_count_2y'] = None

        # set to None if average_return_2y (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_2y is None and "average_return_2y" in self.model_fields_set:
            _dict['average_return_2y'] = None

        # set to None if std_dev_2y (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_2y is None and "std_dev_2y" in self.model_fields_set:
            _dict['std_dev_2y'] = None

        # set to None if smart_score_2y (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_2y is None and "smart_score_2y" in self.model_fields_set:
            _dict['smart_score_2y'] = None

        # set to None if success_rate_2y (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_2y is None and "success_rate_2y" in self.model_fields_set:
            _dict['success_rate_2y'] = None

        # set to None if gain_count_3y (nullable) is None
        # and model_fields_set contains the field
        if self.gain_count_3y is None and "gain_count_3y" in self.model_fields_set:
            _dict['gain_count_3y'] = None

        # set to None if loss_count_3y (nullable) is None
        # and model_fields_set contains the field
        if self.loss_count_3y is None and "loss_count_3y" in self.model_fields_set:
            _dict['loss_count_3y'] = None

        # set to None if average_return_3y (nullable) is None
        # and model_fields_set contains the field
        if self.average_return_3y is None and "average_return_3y" in self.model_fields_set:
            _dict['average_return_3y'] = None

        # set to None if std_dev_3y (nullable) is None
        # and model_fields_set contains the field
        if self.std_dev_3y is None and "std_dev_3y" in self.model_fields_set:
            _dict['std_dev_3y'] = None

        # set to None if smart_score_3y (nullable) is None
        # and model_fields_set contains the field
        if self.smart_score_3y is None and "smart_score_3y" in self.model_fields_set:
            _dict['smart_score_3y'] = None

        # set to None if success_rate_3y (nullable) is None
        # and model_fields_set contains the field
        if self.success_rate_3y is None and "success_rate_3y" in self.model_fields_set:
            _dict['success_rate_3y'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BenzingaAnalystSearchData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "last_updated": obj.get("last_updated"),
            "firm_name": obj.get("firm_name"),
            "name_first": obj.get("name_first"),
            "name_last": obj.get("name_last"),
            "name_full": obj.get("name_full"),
            "analyst_id": obj.get("analyst_id"),
            "firm_id": obj.get("firm_id"),
            "smart_score": obj.get("smart_score"),
            "overall_success_rate": obj.get("overall_success_rate"),
            "overall_avg_return_percentile": obj.get("overall_avg_return_percentile"),
            "total_ratings_percentile": obj.get("total_ratings_percentile"),
            "total_ratings": obj.get("total_ratings"),
            "overall_gain_count": obj.get("overall_gain_count"),
            "overall_loss_count": obj.get("overall_loss_count"),
            "overall_average_return": obj.get("overall_average_return"),
            "overall_std_dev": obj.get("overall_std_dev"),
            "gain_count_1m": obj.get("gain_count_1m"),
            "loss_count_1m": obj.get("loss_count_1m"),
            "average_return_1m": obj.get("average_return_1m"),
            "std_dev_1m": obj.get("std_dev_1m"),
            "smart_score_1m": obj.get("smart_score_1m"),
            "success_rate_1m": obj.get("success_rate_1m"),
            "gain_count_3m": obj.get("gain_count_3m"),
            "loss_count_3m": obj.get("loss_count_3m"),
            "average_return_3m": obj.get("average_return_3m"),
            "std_dev_3m": obj.get("std_dev_3m"),
            "smart_score_3m": obj.get("smart_score_3m"),
            "success_rate_3m": obj.get("success_rate_3m"),
            "gain_count_6m": obj.get("gain_count_6m"),
            "loss_count_6m": obj.get("loss_count_6m"),
            "average_return_6m": obj.get("average_return_6m"),
            "std_dev_6m": obj.get("std_dev_6m"),
            "gain_count_9m": obj.get("gain_count_9m"),
            "loss_count_9m": obj.get("loss_count_9m"),
            "average_return_9m": obj.get("average_return_9m"),
            "std_dev_9m": obj.get("std_dev_9m"),
            "smart_score_9m": obj.get("smart_score_9m"),
            "success_rate_9m": obj.get("success_rate_9m"),
            "gain_count_1y": obj.get("gain_count_1y"),
            "loss_count_1y": obj.get("loss_count_1y"),
            "average_return_1y": obj.get("average_return_1y"),
            "std_dev_1y": obj.get("std_dev_1y"),
            "smart_score_1y": obj.get("smart_score_1y"),
            "success_rate_1y": obj.get("success_rate_1y"),
            "gain_count_2y": obj.get("gain_count_2y"),
            "loss_count_2y": obj.get("loss_count_2y"),
            "average_return_2y": obj.get("average_return_2y"),
            "std_dev_2y": obj.get("std_dev_2y"),
            "smart_score_2y": obj.get("smart_score_2y"),
            "success_rate_2y": obj.get("success_rate_2y"),
            "gain_count_3y": obj.get("gain_count_3y"),
            "loss_count_3y": obj.get("loss_count_3y"),
            "average_return_3y": obj.get("average_return_3y"),
            "std_dev_3y": obj.get("std_dev_3y"),
            "smart_score_3y": obj.get("smart_score_3y"),
            "success_rate_3y": obj.get("success_rate_3y")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


