# OBBjectMarketSnapshotsResultsInner


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
**last_price_timestamp** | [**LastPriceTimestamp**](LastPriceTimestamp.md) |  | [optional] 
**ma_50** | **float** |  | [optional] 
**ma_200** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**volume_avg** | **int** |  | [optional] 
**market_cap** | **int** |  | [optional] 
**eps** | **float** |  | [optional] 
**pe** | **float** |  | [optional] 
**shares_outstanding** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**earnings_date** | [**EarningsDate**](EarningsDate.md) |  | [optional] 
**vwap** | **float** |  | [optional] 
**prev_open** | **float** |  | [optional] 
**prev_high** | **float** |  | [optional] 
**prev_low** | **float** |  | [optional] 
**prev_volume** | **float** |  | [optional] 
**prev_vwap** | **float** |  | [optional] 
**last_updated** | **datetime** |  | 
**bid** | **float** |  | [optional] 
**ask** | **float** |  | [optional] 
**quote_timestamp** | **datetime** |  | [optional] 
**last_trade_price** | **float** |  | [optional] 
**last_trade_size** | **int** |  | [optional] 
**last_trade_conditions** | **List[int]** |  | [optional] 
**last_trade_exchange** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_market_snapshots_results_inner import OBBjectMarketSnapshotsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectMarketSnapshotsResultsInner from a JSON string
ob_bject_market_snapshots_results_inner_instance = OBBjectMarketSnapshotsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectMarketSnapshotsResultsInner.to_json())

# convert the object into a dict
ob_bject_market_snapshots_results_inner_dict = ob_bject_market_snapshots_results_inner_instance.to_dict()
# create an instance of OBBjectMarketSnapshotsResultsInner from a dict
ob_bject_market_snapshots_results_inner_from_dict = OBBjectMarketSnapshotsResultsInner.from_dict(ob_bject_market_snapshots_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


