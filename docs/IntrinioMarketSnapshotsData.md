# IntrinioMarketSnapshotsData

Intrinio Market Snapshots Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**prev_close** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**last_price** | **float** |  | [optional] 
**last_size** | **int** |  | [optional] 
**last_volume** | **int** |  | [optional] 
**last_trade_timestamp** | **datetime** |  | [optional] 
**bid_size** | **int** |  | [optional] 
**bid_price** | **float** |  | [optional] 
**ask_price** | **float** |  | [optional] 
**ask_size** | **int** |  | [optional] 
**last_bid_timestamp** | **datetime** |  | [optional] 
**last_ask_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_market_snapshots_data import IntrinioMarketSnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioMarketSnapshotsData from a JSON string
intrinio_market_snapshots_data_instance = IntrinioMarketSnapshotsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioMarketSnapshotsData.to_json())

# convert the object into a dict
intrinio_market_snapshots_data_dict = intrinio_market_snapshots_data_instance.to_dict()
# create an instance of IntrinioMarketSnapshotsData from a dict
intrinio_market_snapshots_data_from_dict = IntrinioMarketSnapshotsData.from_dict(intrinio_market_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


