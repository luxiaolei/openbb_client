# OBBjectEconomicIndicatorsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**scale** | **str** |  | [optional] 
**table** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**reference_sector** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_economic_indicators_results_inner import OBBjectEconomicIndicatorsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEconomicIndicatorsResultsInner from a JSON string
ob_bject_economic_indicators_results_inner_instance = OBBjectEconomicIndicatorsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEconomicIndicatorsResultsInner.to_json())

# convert the object into a dict
ob_bject_economic_indicators_results_inner_dict = ob_bject_economic_indicators_results_inner_instance.to_dict()
# create an instance of OBBjectEconomicIndicatorsResultsInner from a dict
ob_bject_economic_indicators_results_inner_from_dict = OBBjectEconomicIndicatorsResultsInner.from_dict(ob_bject_economic_indicators_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


