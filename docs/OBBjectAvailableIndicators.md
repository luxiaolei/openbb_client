# OBBjectAvailableIndicators

OBBject with results of type AvailableIndicators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectAvailableIndicatorsResultsInner]**](OBBjectAvailableIndicatorsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_available_indicators import OBBjectAvailableIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAvailableIndicators from a JSON string
ob_bject_available_indicators_instance = OBBjectAvailableIndicators.from_json(json)
# print the JSON string representation of the object
print(OBBjectAvailableIndicators.to_json())

# convert the object into a dict
ob_bject_available_indicators_dict = ob_bject_available_indicators_instance.to_dict()
# create an instance of OBBjectAvailableIndicators from a dict
ob_bject_available_indicators_from_dict = OBBjectAvailableIndicators.from_dict(ob_bject_available_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


