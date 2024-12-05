# FMPMarketSnapshotsData

FMP Market Snapshots Data.

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

## Example

```python
from openbb_client.models.fmp_market_snapshots_data import FMPMarketSnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPMarketSnapshotsData from a JSON string
fmp_market_snapshots_data_instance = FMPMarketSnapshotsData.from_json(json)
# print the JSON string representation of the object
print(FMPMarketSnapshotsData.to_json())

# convert the object into a dict
fmp_market_snapshots_data_dict = fmp_market_snapshots_data_instance.to_dict()
# create an instance of FMPMarketSnapshotsData from a dict
fmp_market_snapshots_data_from_dict = FMPMarketSnapshotsData.from_dict(fmp_market_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


