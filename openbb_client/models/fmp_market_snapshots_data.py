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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openbb_client.models.earnings_date import EarningsDate
from openbb_client.models.last_price_timestamp import LastPriceTimestamp
from typing import Optional, Set
from typing_extensions import Self

class FMPMarketSnapshotsData(BaseModel):
    """
    FMP Market Snapshots Data.
    """ # noqa: E501
    symbol: StrictStr = Field(description="Symbol representing the entity requested in the data.")
    open: Optional[Union[StrictFloat, StrictInt]] = None
    high: Optional[Union[StrictFloat, StrictInt]] = None
    low: Optional[Union[StrictFloat, StrictInt]] = None
    close: Optional[Union[StrictFloat, StrictInt]] = None
    volume: Optional[StrictInt] = None
    prev_close: Optional[Union[StrictFloat, StrictInt]] = None
    change: Optional[Union[StrictFloat, StrictInt]] = None
    change_percent: Optional[Union[StrictFloat, StrictInt]] = None
    last_price: Optional[Union[StrictFloat, StrictInt]] = None
    last_price_timestamp: Optional[LastPriceTimestamp] = None
    ma_50: Optional[Union[StrictFloat, StrictInt]] = None
    ma_200: Optional[Union[StrictFloat, StrictInt]] = None
    year_high: Optional[Union[StrictFloat, StrictInt]] = None
    year_low: Optional[Union[StrictFloat, StrictInt]] = None
    volume_avg: Optional[StrictInt] = None
    market_cap: Optional[StrictInt] = None
    eps: Optional[Union[StrictFloat, StrictInt]] = None
    pe: Optional[Union[StrictFloat, StrictInt]] = None
    shares_outstanding: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    exchange: Optional[StrictStr] = None
    earnings_date: Optional[EarningsDate] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["symbol", "open", "high", "low", "close", "volume", "prev_close", "change", "change_percent", "last_price", "last_price_timestamp", "ma_50", "ma_200", "year_high", "year_low", "volume_avg", "market_cap", "eps", "pe", "shares_outstanding", "name", "exchange", "earnings_date"]

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
        """Create an instance of FMPMarketSnapshotsData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_price_timestamp
        if self.last_price_timestamp:
            _dict['last_price_timestamp'] = self.last_price_timestamp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of earnings_date
        if self.earnings_date:
            _dict['earnings_date'] = self.earnings_date.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if open (nullable) is None
        # and model_fields_set contains the field
        if self.open is None and "open" in self.model_fields_set:
            _dict['open'] = None

        # set to None if high (nullable) is None
        # and model_fields_set contains the field
        if self.high is None and "high" in self.model_fields_set:
            _dict['high'] = None

        # set to None if low (nullable) is None
        # and model_fields_set contains the field
        if self.low is None and "low" in self.model_fields_set:
            _dict['low'] = None

        # set to None if close (nullable) is None
        # and model_fields_set contains the field
        if self.close is None and "close" in self.model_fields_set:
            _dict['close'] = None

        # set to None if volume (nullable) is None
        # and model_fields_set contains the field
        if self.volume is None and "volume" in self.model_fields_set:
            _dict['volume'] = None

        # set to None if prev_close (nullable) is None
        # and model_fields_set contains the field
        if self.prev_close is None and "prev_close" in self.model_fields_set:
            _dict['prev_close'] = None

        # set to None if change (nullable) is None
        # and model_fields_set contains the field
        if self.change is None and "change" in self.model_fields_set:
            _dict['change'] = None

        # set to None if change_percent (nullable) is None
        # and model_fields_set contains the field
        if self.change_percent is None and "change_percent" in self.model_fields_set:
            _dict['change_percent'] = None

        # set to None if last_price (nullable) is None
        # and model_fields_set contains the field
        if self.last_price is None and "last_price" in self.model_fields_set:
            _dict['last_price'] = None

        # set to None if last_price_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.last_price_timestamp is None and "last_price_timestamp" in self.model_fields_set:
            _dict['last_price_timestamp'] = None

        # set to None if ma_50 (nullable) is None
        # and model_fields_set contains the field
        if self.ma_50 is None and "ma_50" in self.model_fields_set:
            _dict['ma_50'] = None

        # set to None if ma_200 (nullable) is None
        # and model_fields_set contains the field
        if self.ma_200 is None and "ma_200" in self.model_fields_set:
            _dict['ma_200'] = None

        # set to None if year_high (nullable) is None
        # and model_fields_set contains the field
        if self.year_high is None and "year_high" in self.model_fields_set:
            _dict['year_high'] = None

        # set to None if year_low (nullable) is None
        # and model_fields_set contains the field
        if self.year_low is None and "year_low" in self.model_fields_set:
            _dict['year_low'] = None

        # set to None if volume_avg (nullable) is None
        # and model_fields_set contains the field
        if self.volume_avg is None and "volume_avg" in self.model_fields_set:
            _dict['volume_avg'] = None

        # set to None if market_cap (nullable) is None
        # and model_fields_set contains the field
        if self.market_cap is None and "market_cap" in self.model_fields_set:
            _dict['market_cap'] = None

        # set to None if eps (nullable) is None
        # and model_fields_set contains the field
        if self.eps is None and "eps" in self.model_fields_set:
            _dict['eps'] = None

        # set to None if pe (nullable) is None
        # and model_fields_set contains the field
        if self.pe is None and "pe" in self.model_fields_set:
            _dict['pe'] = None

        # set to None if shares_outstanding (nullable) is None
        # and model_fields_set contains the field
        if self.shares_outstanding is None and "shares_outstanding" in self.model_fields_set:
            _dict['shares_outstanding'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if exchange (nullable) is None
        # and model_fields_set contains the field
        if self.exchange is None and "exchange" in self.model_fields_set:
            _dict['exchange'] = None

        # set to None if earnings_date (nullable) is None
        # and model_fields_set contains the field
        if self.earnings_date is None and "earnings_date" in self.model_fields_set:
            _dict['earnings_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FMPMarketSnapshotsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "open": obj.get("open"),
            "high": obj.get("high"),
            "low": obj.get("low"),
            "close": obj.get("close"),
            "volume": obj.get("volume"),
            "prev_close": obj.get("prev_close"),
            "change": obj.get("change"),
            "change_percent": obj.get("change_percent"),
            "last_price": obj.get("last_price"),
            "last_price_timestamp": LastPriceTimestamp.from_dict(obj["last_price_timestamp"]) if obj.get("last_price_timestamp") is not None else None,
            "ma_50": obj.get("ma_50"),
            "ma_200": obj.get("ma_200"),
            "year_high": obj.get("year_high"),
            "year_low": obj.get("year_low"),
            "volume_avg": obj.get("volume_avg"),
            "market_cap": obj.get("market_cap"),
            "eps": obj.get("eps"),
            "pe": obj.get("pe"),
            "shares_outstanding": obj.get("shares_outstanding"),
            "name": obj.get("name"),
            "exchange": obj.get("exchange"),
            "earnings_date": EarningsDate.from_dict(obj["earnings_date"]) if obj.get("earnings_date") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


