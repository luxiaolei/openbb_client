# OBBjectAvailableIndicatorsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**iso** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**table** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**scale** | **str** |  | [optional] 
**multiplier** | **int** |  | 
**transformation** | **str** | Transformation type. | 
**source** | **str** |  | [optional] 
**first_date** | **date** |  | [optional] 
**last_date** | **date** |  | [optional] 
**last_insert_timestamp** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_available_indicators_results_inner import OBBjectAvailableIndicatorsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAvailableIndicatorsResultsInner from a JSON string
ob_bject_available_indicators_results_inner_instance = OBBjectAvailableIndicatorsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectAvailableIndicatorsResultsInner.to_json())

# convert the object into a dict
ob_bject_available_indicators_results_inner_dict = ob_bject_available_indicators_results_inner_instance.to_dict()
# create an instance of OBBjectAvailableIndicatorsResultsInner from a dict
ob_bject_available_indicators_results_inner_from_dict = OBBjectAvailableIndicatorsResultsInner.from_dict(ob_bject_available_indicators_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


