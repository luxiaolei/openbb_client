# PolygonMarketSnapshotsData

Polygon Market Snapshots Data.

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
**vwap** | **float** |  | [optional] 
**prev_open** | **float** |  | [optional] 
**prev_high** | **float** |  | [optional] 
**prev_low** | **float** |  | [optional] 
**prev_volume** | **float** |  | [optional] 
**prev_vwap** | **float** |  | [optional] 
**last_updated** | **datetime** |  | 
**bid** | **float** |  | [optional] 
**bid_size** | **int** |  | [optional] 
**ask_size** | **int** |  | [optional] 
**ask** | **float** |  | [optional] 
**quote_timestamp** | **datetime** |  | [optional] 
**last_trade_price** | **float** |  | [optional] 
**last_trade_size** | **int** |  | [optional] 
**last_trade_conditions** | **List[int]** |  | [optional] 
**last_trade_exchange** | **int** |  | [optional] 
**last_trade_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_market_snapshots_data import PolygonMarketSnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonMarketSnapshotsData from a JSON string
polygon_market_snapshots_data_instance = PolygonMarketSnapshotsData.from_json(json)
# print the JSON string representation of the object
print(PolygonMarketSnapshotsData.to_json())

# convert the object into a dict
polygon_market_snapshots_data_dict = polygon_market_snapshots_data_instance.to_dict()
# create an instance of PolygonMarketSnapshotsData from a dict
polygon_market_snapshots_data_from_dict = PolygonMarketSnapshotsData.from_dict(polygon_market_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


