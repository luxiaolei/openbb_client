# OBBjectAnalystEstimates

OBBject with results of type AnalystEstimates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPAnalystEstimatesData]**](FMPAnalystEstimatesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_analyst_estimates import OBBjectAnalystEstimates

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAnalystEstimates from a JSON string
ob_bject_analyst_estimates_instance = OBBjectAnalystEstimates.from_json(json)
# print the JSON string representation of the object
print(OBBjectAnalystEstimates.to_json())

# convert the object into a dict
ob_bject_analyst_estimates_dict = ob_bject_analyst_estimates_instance.to_dict()
# create an instance of OBBjectAnalystEstimates from a dict
ob_bject_analyst_estimates_from_dict = OBBjectAnalystEstimates.from_dict(ob_bject_analyst_estimates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


