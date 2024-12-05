# OBBjectOptionsChainsResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_symbol** | **List[str]** | Underlying symbol for the option. | [optional] 
**underlying_price** | **List[float]** | Price of the underlying stock. | [optional] 
**contract_symbol** | **List[str]** | Contract symbol for the option. | 
**eod_date** | **List[date]** | Date for which the options chains are returned. | [optional] 
**expiration** | **List[date]** | Expiration date of the contract. | 
**dte** | **List[int]** | Days to expiration of the contract. | [optional] 
**strike** | **List[float]** | Strike price of the contract. | 
**option_type** | **List[str]** | Call or Put. | 
**open_interest** | **List[int]** | Open interest on the contract. | [optional] 
**volume** | **List[int]** | The trading volume. | [optional] 
**theoretical_price** | **List[float]** | Theoretical value of the option. | [optional] 
**last_trade_price** | **List[float]** | Last trade price of the option. | [optional] 
**last_trade_size** | **List[int]** | Last trade size of the option. | [optional] 
**last_trade_time** | **List[datetime]** | The timestamp of the last trade. | [optional] 
**tick** | **List[str]** | Whether the last tick was up or down in price. | [optional] 
**bid** | **List[float]** | Current bid price for the option. | [optional] 
**bid_size** | **List[int]** | Bid size for the option. | [optional] 
**bid_time** | **List[datetime]** | The timestamp of the bid price. | [optional] 
**bid_exchange** | **List[str]** | The exchange of the bid price. | [optional] 
**ask** | **List[float]** | Current ask price for the option. | [optional] 
**ask_size** | **List[int]** | Ask size for the option. | [optional] 
**ask_time** | **List[datetime]** | The timestamp of the ask price. | [optional] 
**ask_exchange** | **List[str]** | The exchange of the ask price. | [optional] 
**mark** | **List[float]** | The mid-price between the latest bid and ask. | [optional] 
**open** | **List[float]** | The open price. | [optional] 
**open_bid** | **List[float]** | The opening bid price for the option that day. | [optional] 
**open_ask** | **List[float]** | The opening ask price for the option that day. | [optional] 
**high** | **List[float]** | The high price. | [optional] 
**bid_high** | **List[float]** | The highest bid price for the option that day. | [optional] 
**ask_high** | **List[float]** | The highest ask price for the option that day. | [optional] 
**low** | **List[float]** | The low price. | [optional] 
**bid_low** | **List[float]** | The lowest bid price for the option that day. | [optional] 
**ask_low** | **List[float]** | The lowest ask price for the option that day. | [optional] 
**close** | **List[float]** | The close price. | [optional] 
**close_size** | **List[int]** | The closing trade size for the option that day. | [optional] 
**close_time** | **List[datetime]** | The time of the closing price for the option that day. | [optional] 
**close_bid** | **List[float]** | The closing bid price for the option that day. | [optional] 
**close_bid_size** | **List[int]** | The closing bid size for the option that day. | [optional] 
**close_bid_time** | **List[datetime]** | The time of the bid closing price for the option that day. | [optional] 
**close_ask** | **List[float]** | The closing ask price for the option that day. | [optional] 
**close_ask_size** | **List[int]** | The closing ask size for the option that day. | [optional] 
**close_ask_time** | **List[datetime]** | The time of the ask closing price for the option that day. | [optional] 
**prev_close** | **List[float]** | The previous close price. | [optional] 
**change** | **List[float]** | The change in the price of the option. | [optional] 
**change_percent** | **List[float]** | Change, in normalized percentage points, of the option. | [optional] 
**implied_volatility** | **List[float]** | Implied volatility of the option. | [optional] 
**delta** | **List[float]** | Delta of the option. | [optional] 
**gamma** | **List[float]** | Gamma of the option. | [optional] 
**theta** | **List[float]** | Theta of the option. | [optional] 
**vega** | **List[float]** | Vega of the option. | [optional] 
**rho** | **List[float]** | Rho of the option. | [optional] 
**in_the_money** | **List[bool]** | Whether the option is in the money. | [optional] 
**currency** | **List[str]** | Currency of the option. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_options_chains_results import OBBjectOptionsChainsResults

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOptionsChainsResults from a JSON string
ob_bject_options_chains_results_instance = OBBjectOptionsChainsResults.from_json(json)
# print the JSON string representation of the object
print(OBBjectOptionsChainsResults.to_json())

# convert the object into a dict
ob_bject_options_chains_results_dict = ob_bject_options_chains_results_instance.to_dict()
# create an instance of OBBjectOptionsChainsResults from a dict
ob_bject_options_chains_results_from_dict = OBBjectOptionsChainsResults.from_dict(ob_bject_options_chains_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


