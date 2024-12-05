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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class IntrinioOptionsChainsData(BaseModel):
    """
    Options Chains Data.  Note: The attached properties and methods are available only when working with an instance of this class, initialized with validated provider data. The items below bind to the `results` object in the function's output.  Properties ---------- dataframe: DataFrame     Return all data as a Pandas DataFrame, with additional computed columns (Breakeven, GEX, DEX) if available. expirations: List[str]     Return a list of unique expiration dates, as strings. strikes: List[float]     Return a list of unique strike prices. has_iv: bool     Return True if the data contains implied volatility. has_greeks: bool     Return True if the data contains greeks. total_oi: Dict     Return open interest stats as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_volume: Dict     Return volume stats as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_dex: Dict     Return Delta Dollars (DEX), if available, as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_gex: Dict     Return Gamma Exposure (GEX), if available, as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. last_price: float     Manually set the underlying price by assigning a float value to this property.     Certain provider/symbol combinations may not return the underlying price,     and it may be necessary, or desirable, to set it post-initialization.     This property can be used to override the underlying price returned by the provider.     It is not set automatically, and this property will return None if it is not set.  Methods ------- filter_data(     date: Optional[Union[str, int]] = None,     column: Optional[str] = None,     option_type: Optional[Literal[\"call\", \"put\"]] = None,     moneyness: Optional[Literal[\"otm\", \"itm\"]] = None,     value_min: Optional[float] = None,     value_max: Optional[float] = None,     stat: Optional[Literal[\"open_interest\", \"volume\", \"dex\", \"gex\"]] = None,     by: Literal[\"expiration\", \"strike\"] = \"expiration\", ) -> DataFrame:     Return statistics by strike or expiration; or, the filtered chains data. skew(     date: Optional[Union[int, str]] = None, underlying_price: Optional[float] = None) -> DataFrame:     Return skewness of the options, either vertical or horizontal, by nearest DTE. straddle(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a straddle, by nearest DTE. Use a negative strike price for short options. strangle(     days: Optional[int] = None, moneyness: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a strangle, by nearest DTE and % moneyness.     Use a negative value for moneyness for short options. synthetic_long(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a synthetic long position, by nearest DTE and strike price. synthetic_short(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a synthetic short position, by nearest DTE and strike price. vertical_call(     days: Optional[int] = None, sold: Optional[float] = None, bought: Optional[float] = None,     underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a vertical call spread, by nearest DTE and strike price to sold and bought levels. vertical_put(     days: Optional[int] = None, sold: Optional[float] = None, bought: Optional[float] = None,     underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a vertical put spread, by nearest DTE and strike price to sold and bought levels. strategies(     days: Optional[int] = None,     straddle_strike: Optional[float] = None,     strangle_moneyness: Optional[List[float]] = None,     synthetic_longs: Optional[List[float]] = None,     synthetic_shorts: Optional[List[float]] = None,     vertical_calls: Optional[List[tuple]] = None,     vertical_puts: Optional[List[tuple]] = None,     underlying_price: Optional[float] = None, ) -> DataFrame:     Method for combining multiple strategies and parameters in a single DataFrame.     To get all expirations, set days to -1.  Raises ------ OpenBBError     OpenBBError will raise when accessing properties and methods if required, specific, data was not found.
    """ # noqa: E501
    underlying_symbol: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Underlying symbol for the option.")
    underlying_price: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Price of the underlying stock.")
    contract_symbol: List[StrictStr] = Field(description="Contract symbol for the option.")
    eod_date: Optional[List[Optional[date]]] = Field(default=None, description="Date for which the options chains are returned.")
    expiration: List[date] = Field(description="Expiration date of the contract.")
    dte: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Days to expiration of the contract.")
    strike: List[Union[StrictFloat, StrictInt]] = Field(description="Strike price of the contract.")
    option_type: List[StrictStr] = Field(description="Call or Put.")
    open_interest: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Open interest on the contract.")
    volume: Optional[List[Optional[StrictInt]]] = Field(default=None, description="The trading volume.")
    theoretical_price: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Theoretical value of the option.")
    last_trade_price: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Last trade price of the option.")
    last_trade_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Last trade size of the option.")
    last_trade_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The timestamp of the last trade.")
    tick: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Whether the last tick was up or down in price.")
    bid: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Current bid price for the option.")
    bid_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Bid size for the option.")
    bid_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The timestamp of the bid price.")
    bid_exchange: Optional[List[Optional[StrictStr]]] = Field(default=None, description="The exchange of the bid price.")
    ask: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Current ask price for the option.")
    ask_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Ask size for the option.")
    ask_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The timestamp of the ask price.")
    ask_exchange: Optional[List[Optional[StrictStr]]] = Field(default=None, description="The exchange of the ask price.")
    mark: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The mid-price between the latest bid and ask.")
    open: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The open price.")
    open_bid: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The opening bid price for the option that day.")
    open_ask: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The opening ask price for the option that day.")
    high: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The high price.")
    bid_high: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The highest bid price for the option that day.")
    ask_high: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The highest ask price for the option that day.")
    low: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The low price.")
    bid_low: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The lowest bid price for the option that day.")
    ask_low: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The lowest ask price for the option that day.")
    close: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The close price.")
    close_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="The closing trade size for the option that day.")
    close_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The time of the closing price for the option that day.")
    close_bid: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The closing bid price for the option that day.")
    close_bid_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="The closing bid size for the option that day.")
    close_bid_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The time of the bid closing price for the option that day.")
    close_ask: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The closing ask price for the option that day.")
    close_ask_size: Optional[List[Optional[StrictInt]]] = Field(default=None, description="The closing ask size for the option that day.")
    close_ask_time: Optional[List[Optional[datetime]]] = Field(default=None, description="The time of the ask closing price for the option that day.")
    prev_close: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The previous close price.")
    change: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="The change in the price of the option.")
    change_percent: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Change, in normalized percentage points, of the option.")
    implied_volatility: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Implied volatility of the option.")
    delta: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Delta of the option.")
    gamma: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Gamma of the option.")
    theta: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Theta of the option.")
    vega: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Vega of the option.")
    rho: Optional[List[Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Rho of the option.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["underlying_symbol", "underlying_price", "contract_symbol", "eod_date", "expiration", "dte", "strike", "option_type", "open_interest", "volume", "theoretical_price", "last_trade_price", "last_trade_size", "last_trade_time", "tick", "bid", "bid_size", "bid_time", "bid_exchange", "ask", "ask_size", "ask_time", "ask_exchange", "mark", "open", "open_bid", "open_ask", "high", "bid_high", "ask_high", "low", "bid_low", "ask_low", "close", "close_size", "close_time", "close_bid", "close_bid_size", "close_bid_time", "close_ask", "close_ask_size", "close_ask_time", "prev_close", "change", "change_percent", "implied_volatility", "delta", "gamma", "theta", "vega", "rho"]

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
        """Create an instance of IntrinioOptionsChainsData from a JSON string"""
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
        """Create an instance of IntrinioOptionsChainsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "underlying_symbol": obj.get("underlying_symbol"),
            "underlying_price": obj.get("underlying_price"),
            "contract_symbol": obj.get("contract_symbol"),
            "eod_date": obj.get("eod_date"),
            "expiration": obj.get("expiration"),
            "dte": obj.get("dte"),
            "strike": obj.get("strike"),
            "option_type": obj.get("option_type"),
            "open_interest": obj.get("open_interest"),
            "volume": obj.get("volume"),
            "theoretical_price": obj.get("theoretical_price"),
            "last_trade_price": obj.get("last_trade_price"),
            "last_trade_size": obj.get("last_trade_size"),
            "last_trade_time": obj.get("last_trade_time"),
            "tick": obj.get("tick"),
            "bid": obj.get("bid"),
            "bid_size": obj.get("bid_size"),
            "bid_time": obj.get("bid_time"),
            "bid_exchange": obj.get("bid_exchange"),
            "ask": obj.get("ask"),
            "ask_size": obj.get("ask_size"),
            "ask_time": obj.get("ask_time"),
            "ask_exchange": obj.get("ask_exchange"),
            "mark": obj.get("mark"),
            "open": obj.get("open"),
            "open_bid": obj.get("open_bid"),
            "open_ask": obj.get("open_ask"),
            "high": obj.get("high"),
            "bid_high": obj.get("bid_high"),
            "ask_high": obj.get("ask_high"),
            "low": obj.get("low"),
            "bid_low": obj.get("bid_low"),
            "ask_low": obj.get("ask_low"),
            "close": obj.get("close"),
            "close_size": obj.get("close_size"),
            "close_time": obj.get("close_time"),
            "close_bid": obj.get("close_bid"),
            "close_bid_size": obj.get("close_bid_size"),
            "close_bid_time": obj.get("close_bid_time"),
            "close_ask": obj.get("close_ask"),
            "close_ask_size": obj.get("close_ask_size"),
            "close_ask_time": obj.get("close_ask_time"),
            "prev_close": obj.get("prev_close"),
            "change": obj.get("change"),
            "change_percent": obj.get("change_percent"),
            "implied_volatility": obj.get("implied_volatility"),
            "delta": obj.get("delta"),
            "gamma": obj.get("gamma"),
            "theta": obj.get("theta"),
            "vega": obj.get("vega"),
            "rho": obj.get("rho")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


