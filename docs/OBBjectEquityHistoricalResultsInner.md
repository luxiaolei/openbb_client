# OBBjectEquityHistoricalResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | [**Volume**](Volume.md) |  | [optional] 
**vwap** | **float** |  | [optional] 
**average** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**adj_open** | **float** |  | [optional] 
**adj_high** | **float** |  | [optional] 
**adj_low** | **float** |  | [optional] 
**adj_close** | **float** |  | [optional] 
**adj_volume** | **float** |  | [optional] 
**fifty_two_week_high** | **float** |  | [optional] 
**fifty_two_week_low** | **float** |  | [optional] 
**factor** | **float** |  | [optional] 
**split_ratio** | **float** |  | [optional] 
**dividend** | **float** |  | [optional] 
**close_time** | **datetime** |  | [optional] 
**interval** | **str** |  | [optional] 
**intra_period** | **bool** |  | [optional] 
**transactions** | **int** |  | [optional] 
**unadjusted_volume** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_historical_results_inner import OBBjectEquityHistoricalResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityHistoricalResultsInner from a JSON string
ob_bject_equity_historical_results_inner_instance = OBBjectEquityHistoricalResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityHistoricalResultsInner.to_json())

# convert the object into a dict
ob_bject_equity_historical_results_inner_dict = ob_bject_equity_historical_results_inner_instance.to_dict()
# create an instance of OBBjectEquityHistoricalResultsInner from a dict
ob_bject_equity_historical_results_inner_from_dict = OBBjectEquityHistoricalResultsInner.from_dict(ob_bject_equity_historical_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


