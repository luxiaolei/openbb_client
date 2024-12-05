# OBBjectIndexHistoricalResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**vwap** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**transactions** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_index_historical_results_inner import OBBjectIndexHistoricalResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectIndexHistoricalResultsInner from a JSON string
ob_bject_index_historical_results_inner_instance = OBBjectIndexHistoricalResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectIndexHistoricalResultsInner.to_json())

# convert the object into a dict
ob_bject_index_historical_results_inner_dict = ob_bject_index_historical_results_inner_instance.to_dict()
# create an instance of OBBjectIndexHistoricalResultsInner from a dict
ob_bject_index_historical_results_inner_from_dict = OBBjectIndexHistoricalResultsInner.from_dict(ob_bject_index_historical_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


