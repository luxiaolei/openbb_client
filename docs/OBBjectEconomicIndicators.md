# OBBjectEconomicIndicators

OBBject with results of type EconomicIndicators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEconomicIndicatorsResultsInner]**](OBBjectEconomicIndicatorsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_economic_indicators import OBBjectEconomicIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEconomicIndicators from a JSON string
ob_bject_economic_indicators_instance = OBBjectEconomicIndicators.from_json(json)
# print the JSON string representation of the object
print(OBBjectEconomicIndicators.to_json())

# convert the object into a dict
ob_bject_economic_indicators_dict = ob_bject_economic_indicators_instance.to_dict()
# create an instance of OBBjectEconomicIndicators from a dict
ob_bject_economic_indicators_from_dict = OBBjectEconomicIndicators.from_dict(ob_bject_economic_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


