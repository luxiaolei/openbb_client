# IntrinioOptionsSnapshotsData

Intrinio Options Snapshots Data. Warning: This is a large file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_symbol** | **List[str]** | Ticker symbol of the underlying asset. | 
**contract_symbol** | **List[str]** | Symbol of the options contract. | 
**expiration** | **List[date]** | Expiration date of the options contract. | 
**dte** | **List[Optional[int]]** | Number of days to expiration of the options contract. | [optional] 
**strike** | **List[float]** | Strike price of the options contract. | 
**option_type** | **List[str]** | The type of option. | 
**volume** | **List[Optional[int]]** | The trading volume. | [optional] 
**open_interest** | **List[Optional[int]]** | Open interest at the time. | [optional] 
**last_price** | **List[Optional[float]]** | Last trade price at the time. | [optional] 
**last_size** | **List[Optional[int]]** | Lot size of the last trade. | [optional] 
**last_timestamp** | **List[Optional[datetime]]** | Timestamp of the last price. | [optional] 
**open** | **List[Optional[float]]** | The open price. | [optional] 
**high** | **List[Optional[float]]** | The high price. | [optional] 
**low** | **List[Optional[float]]** | The low price. | [optional] 
**close** | **List[Optional[float]]** | The close price. | [optional] 
**bid** | **List[Optional[float]]** | The last bid price at the time. | [optional] 
**bid_size** | **List[Optional[int]]** | The size of the last bid price. | [optional] 
**bid_timestamp** | **List[Optional[datetime]]** | The timestamp of the last bid price. | [optional] 
**ask** | **List[Optional[float]]** | The last ask price at the time. | [optional] 
**ask_size** | **List[Optional[int]]** | The size of the last ask price. | [optional] 
**ask_timestamp** | **List[Optional[datetime]]** | The timestamp of the last ask price. | [optional] 
**total_bid_volume** | **List[Optional[int]]** | Total volume of bids. | [optional] 
**bid_high** | **List[Optional[float]]** | The highest bid price. | [optional] 
**bid_low** | **List[Optional[float]]** | The lowest bid price. | [optional] 
**total_ask_volume** | **List[Optional[int]]** | Total volume of asks. | [optional] 
**ask_high** | **List[Optional[float]]** | The highest ask price. | [optional] 
**ask_low** | **List[Optional[float]]** | The lowest ask price. | [optional] 

## Example

```python
from openbb_client.models.intrinio_options_snapshots_data import IntrinioOptionsSnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioOptionsSnapshotsData from a JSON string
intrinio_options_snapshots_data_instance = IntrinioOptionsSnapshotsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioOptionsSnapshotsData.to_json())

# convert the object into a dict
intrinio_options_snapshots_data_dict = intrinio_options_snapshots_data_instance.to_dict()
# create an instance of IntrinioOptionsSnapshotsData from a dict
intrinio_options_snapshots_data_from_dict = IntrinioOptionsSnapshotsData.from_dict(intrinio_options_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


