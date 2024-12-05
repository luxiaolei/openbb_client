# YFinanceOptionsChainsData

Options Chains Data.  Note: The attached properties and methods are available only when working with an instance of this class, initialized with validated provider data. The items below bind to the `results` object in the function's output.  Properties ---------- dataframe: DataFrame     Return all data as a Pandas DataFrame, with additional computed columns (Breakeven, GEX, DEX) if available. expirations: List[str]     Return a list of unique expiration dates, as strings. strikes: List[float]     Return a list of unique strike prices. has_iv: bool     Return True if the data contains implied volatility. has_greeks: bool     Return True if the data contains greeks. total_oi: Dict     Return open interest stats as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_volume: Dict     Return volume stats as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_dex: Dict     Return Delta Dollars (DEX), if available, as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. total_gex: Dict     Return Gamma Exposure (GEX), if available, as a nested dictionary with keys: total, expiration, strike.     Both, \"expiration\" and \"strike\", contain a list of records with fields: Calls, Puts, Total, Net Percent, PCR. last_price: float     Manually set the underlying price by assigning a float value to this property.     Certain provider/symbol combinations may not return the underlying price,     and it may be necessary, or desirable, to set it post-initialization.     This property can be used to override the underlying price returned by the provider.     It is not set automatically, and this property will return None if it is not set.  Methods ------- filter_data(     date: Optional[Union[str, int]] = None,     column: Optional[str] = None,     option_type: Optional[Literal[\"call\", \"put\"]] = None,     moneyness: Optional[Literal[\"otm\", \"itm\"]] = None,     value_min: Optional[float] = None,     value_max: Optional[float] = None,     stat: Optional[Literal[\"open_interest\", \"volume\", \"dex\", \"gex\"]] = None,     by: Literal[\"expiration\", \"strike\"] = \"expiration\", ) -> DataFrame:     Return statistics by strike or expiration; or, the filtered chains data. skew(     date: Optional[Union[int, str]] = None, underlying_price: Optional[float] = None) -> DataFrame:     Return skewness of the options, either vertical or horizontal, by nearest DTE. straddle(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a straddle, by nearest DTE. Use a negative strike price for short options. strangle(     days: Optional[int] = None, moneyness: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a strangle, by nearest DTE and % moneyness.     Use a negative value for moneyness for short options. synthetic_long(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a synthetic long position, by nearest DTE and strike price. synthetic_short(     days: Optional[int] = None, strike: Optional[float] = None, underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a synthetic short position, by nearest DTE and strike price. vertical_call(     days: Optional[int] = None, sold: Optional[float] = None, bought: Optional[float] = None,     underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a vertical call spread, by nearest DTE and strike price to sold and bought levels. vertical_put(     days: Optional[int] = None, sold: Optional[float] = None, bought: Optional[float] = None,     underlying_price: Optional[float] = None ) -> DataFrame:     Calculates the cost of a vertical put spread, by nearest DTE and strike price to sold and bought levels. strategies(     days: Optional[int] = None,     straddle_strike: Optional[float] = None,     strangle_moneyness: Optional[List[float]] = None,     synthetic_longs: Optional[List[float]] = None,     synthetic_shorts: Optional[List[float]] = None,     vertical_calls: Optional[List[tuple]] = None,     vertical_puts: Optional[List[tuple]] = None,     underlying_price: Optional[float] = None, ) -> DataFrame:     Method for combining multiple strategies and parameters in a single DataFrame.     To get all expirations, set days to -1.  Raises ------ OpenBBError     OpenBBError will raise when accessing properties and methods if required, specific, data was not found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_symbol** | **List[Optional[str]]** | Underlying symbol for the option. | [optional] 
**underlying_price** | **List[Optional[float]]** | Price of the underlying stock. | [optional] 
**contract_symbol** | **List[str]** | Contract symbol for the option. | 
**eod_date** | **List[Optional[date]]** | Date for which the options chains are returned. | [optional] 
**expiration** | **List[date]** | Expiration date of the contract. | 
**dte** | **List[Optional[int]]** | Days to expiration of the contract. | [optional] 
**strike** | **List[float]** | Strike price of the contract. | 
**option_type** | **List[str]** | Call or Put. | 
**open_interest** | **List[Optional[int]]** | Open interest on the contract. | [optional] 
**volume** | **List[Optional[int]]** | The trading volume. | [optional] 
**theoretical_price** | **List[Optional[float]]** | Theoretical value of the option. | [optional] 
**last_trade_price** | **List[Optional[float]]** | Last trade price of the option. | [optional] 
**last_trade_size** | **List[Optional[int]]** | Last trade size of the option. | [optional] 
**last_trade_time** | **List[Optional[datetime]]** | The timestamp of the last trade. | [optional] 
**tick** | **List[Optional[str]]** | Whether the last tick was up or down in price. | [optional] 
**bid** | **List[Optional[float]]** | Current bid price for the option. | [optional] 
**bid_size** | **List[Optional[int]]** | Bid size for the option. | [optional] 
**bid_time** | **List[Optional[datetime]]** | The timestamp of the bid price. | [optional] 
**bid_exchange** | **List[Optional[str]]** | The exchange of the bid price. | [optional] 
**ask** | **List[Optional[float]]** | Current ask price for the option. | [optional] 
**ask_size** | **List[Optional[int]]** | Ask size for the option. | [optional] 
**ask_time** | **List[Optional[datetime]]** | The timestamp of the ask price. | [optional] 
**ask_exchange** | **List[Optional[str]]** | The exchange of the ask price. | [optional] 
**mark** | **List[Optional[float]]** | The mid-price between the latest bid and ask. | [optional] 
**open** | **List[Optional[float]]** | The open price. | [optional] 
**open_bid** | **List[Optional[float]]** | The opening bid price for the option that day. | [optional] 
**open_ask** | **List[Optional[float]]** | The opening ask price for the option that day. | [optional] 
**high** | **List[Optional[float]]** | The high price. | [optional] 
**bid_high** | **List[Optional[float]]** | The highest bid price for the option that day. | [optional] 
**ask_high** | **List[Optional[float]]** | The highest ask price for the option that day. | [optional] 
**low** | **List[Optional[float]]** | The low price. | [optional] 
**bid_low** | **List[Optional[float]]** | The lowest bid price for the option that day. | [optional] 
**ask_low** | **List[Optional[float]]** | The lowest ask price for the option that day. | [optional] 
**close** | **List[Optional[float]]** | The close price. | [optional] 
**close_size** | **List[Optional[int]]** | The closing trade size for the option that day. | [optional] 
**close_time** | **List[Optional[datetime]]** | The time of the closing price for the option that day. | [optional] 
**close_bid** | **List[Optional[float]]** | The closing bid price for the option that day. | [optional] 
**close_bid_size** | **List[Optional[int]]** | The closing bid size for the option that day. | [optional] 
**close_bid_time** | **List[Optional[datetime]]** | The time of the bid closing price for the option that day. | [optional] 
**close_ask** | **List[Optional[float]]** | The closing ask price for the option that day. | [optional] 
**close_ask_size** | **List[Optional[int]]** | The closing ask size for the option that day. | [optional] 
**close_ask_time** | **List[Optional[datetime]]** | The time of the ask closing price for the option that day. | [optional] 
**prev_close** | **List[Optional[float]]** | The previous close price. | [optional] 
**change** | **List[Optional[float]]** | The change in the price of the option. | [optional] 
**change_percent** | **List[Optional[float]]** | Change, in normalized percentage points, of the option. | [optional] 
**implied_volatility** | **List[Optional[float]]** | Implied volatility of the option. | [optional] 
**delta** | **List[Optional[float]]** | Delta of the option. | [optional] 
**gamma** | **List[Optional[float]]** | Gamma of the option. | [optional] 
**theta** | **List[Optional[float]]** | Theta of the option. | [optional] 
**vega** | **List[Optional[float]]** | Vega of the option. | [optional] 
**rho** | **List[Optional[float]]** | Rho of the option. | [optional] 
**in_the_money** | **List[Optional[bool]]** | Whether the option is in the money. | [optional] 
**currency** | **List[Optional[str]]** | Currency of the option. | [optional] 

## Example

```python
from openbb_client.models.y_finance_options_chains_data import YFinanceOptionsChainsData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceOptionsChainsData from a JSON string
y_finance_options_chains_data_instance = YFinanceOptionsChainsData.from_json(json)
# print the JSON string representation of the object
print(YFinanceOptionsChainsData.to_json())

# convert the object into a dict
y_finance_options_chains_data_dict = y_finance_options_chains_data_instance.to_dict()
# create an instance of YFinanceOptionsChainsData from a dict
y_finance_options_chains_data_from_dict = YFinanceOptionsChainsData.from_dict(y_finance_options_chains_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


