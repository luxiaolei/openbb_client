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
from openbb_client.models.actual import Actual
from openbb_client.models.consensus import Consensus
from openbb_client.models.forecast import Forecast
from openbb_client.models.previous import Previous
from openbb_client.models.revised import Revised
from typing import Optional, Set
from typing_extensions import Self

class TEEconomicCalendarData(BaseModel):
    """
    Trading Economics Economic Calendar Data.
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, alias="date")
    country: Optional[StrictStr] = None
    category: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    importance: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    unit: Optional[StrictStr] = None
    consensus: Optional[Consensus] = None
    previous: Optional[Previous] = None
    revised: Optional[Revised] = None
    actual: Optional[Actual] = None
    forecast: Optional[Forecast] = None
    reference: Optional[StrictStr] = None
    reference_date: Optional[date] = None
    calendar_id: Optional[StrictInt] = None
    date_span: Optional[StrictInt] = None
    symbol: Optional[StrictStr] = None
    ticker: Optional[StrictStr] = None
    te_url: Optional[StrictStr] = None
    source_url: Optional[StrictStr] = None
    last_updated: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["date", "country", "category", "event", "importance", "source", "currency", "unit", "consensus", "previous", "revised", "actual", "forecast", "reference", "reference_date", "calendar_id", "date_span", "symbol", "ticker", "te_url", "source_url", "last_updated"]

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
        """Create an instance of TEEconomicCalendarData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of consensus
        if self.consensus:
            _dict['consensus'] = self.consensus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous
        if self.previous:
            _dict['previous'] = self.previous.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revised
        if self.revised:
            _dict['revised'] = self.revised.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actual
        if self.actual:
            _dict['actual'] = self.actual.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forecast
        if self.forecast:
            _dict['forecast'] = self.forecast.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if var_date (nullable) is None
        # and model_fields_set contains the field
        if self.var_date is None and "var_date" in self.model_fields_set:
            _dict['date'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if event (nullable) is None
        # and model_fields_set contains the field
        if self.event is None and "event" in self.model_fields_set:
            _dict['event'] = None

        # set to None if importance (nullable) is None
        # and model_fields_set contains the field
        if self.importance is None and "importance" in self.model_fields_set:
            _dict['importance'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if consensus (nullable) is None
        # and model_fields_set contains the field
        if self.consensus is None and "consensus" in self.model_fields_set:
            _dict['consensus'] = None

        # set to None if previous (nullable) is None
        # and model_fields_set contains the field
        if self.previous is None and "previous" in self.model_fields_set:
            _dict['previous'] = None

        # set to None if revised (nullable) is None
        # and model_fields_set contains the field
        if self.revised is None and "revised" in self.model_fields_set:
            _dict['revised'] = None

        # set to None if actual (nullable) is None
        # and model_fields_set contains the field
        if self.actual is None and "actual" in self.model_fields_set:
            _dict['actual'] = None

        # set to None if forecast (nullable) is None
        # and model_fields_set contains the field
        if self.forecast is None and "forecast" in self.model_fields_set:
            _dict['forecast'] = None

        # set to None if reference (nullable) is None
        # and model_fields_set contains the field
        if self.reference is None and "reference" in self.model_fields_set:
            _dict['reference'] = None

        # set to None if reference_date (nullable) is None
        # and model_fields_set contains the field
        if self.reference_date is None and "reference_date" in self.model_fields_set:
            _dict['reference_date'] = None

        # set to None if calendar_id (nullable) is None
        # and model_fields_set contains the field
        if self.calendar_id is None and "calendar_id" in self.model_fields_set:
            _dict['calendar_id'] = None

        # set to None if date_span (nullable) is None
        # and model_fields_set contains the field
        if self.date_span is None and "date_span" in self.model_fields_set:
            _dict['date_span'] = None

        # set to None if symbol (nullable) is None
        # and model_fields_set contains the field
        if self.symbol is None and "symbol" in self.model_fields_set:
            _dict['symbol'] = None

        # set to None if ticker (nullable) is None
        # and model_fields_set contains the field
        if self.ticker is None and "ticker" in self.model_fields_set:
            _dict['ticker'] = None

        # set to None if te_url (nullable) is None
        # and model_fields_set contains the field
        if self.te_url is None and "te_url" in self.model_fields_set:
            _dict['te_url'] = None

        # set to None if source_url (nullable) is None
        # and model_fields_set contains the field
        if self.source_url is None and "source_url" in self.model_fields_set:
            _dict['source_url'] = None

        # set to None if last_updated (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated is None and "last_updated" in self.model_fields_set:
            _dict['last_updated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TEEconomicCalendarData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "country": obj.get("country"),
            "category": obj.get("category"),
            "event": obj.get("event"),
            "importance": obj.get("importance"),
            "source": obj.get("source"),
            "currency": obj.get("currency"),
            "unit": obj.get("unit"),
            "consensus": Consensus.from_dict(obj["consensus"]) if obj.get("consensus") is not None else None,
            "previous": Previous.from_dict(obj["previous"]) if obj.get("previous") is not None else None,
            "revised": Revised.from_dict(obj["revised"]) if obj.get("revised") is not None else None,
            "actual": Actual.from_dict(obj["actual"]) if obj.get("actual") is not None else None,
            "forecast": Forecast.from_dict(obj["forecast"]) if obj.get("forecast") is not None else None,
            "reference": obj.get("reference"),
            "reference_date": obj.get("reference_date"),
            "calendar_id": obj.get("calendar_id"),
            "date_span": obj.get("date_span"),
            "symbol": obj.get("symbol"),
            "ticker": obj.get("ticker"),
            "te_url": obj.get("te_url"),
            "source_url": obj.get("source_url"),
            "last_updated": obj.get("last_updated")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


