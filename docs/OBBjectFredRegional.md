# OBBjectFredRegional

OBBject with results of type FredRegional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredRegionalData]**](FredRegionalData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_fred_regional import OBBjectFredRegional

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFredRegional from a JSON string
ob_bject_fred_regional_instance = OBBjectFredRegional.from_json(json)
# print the JSON string representation of the object
print(OBBjectFredRegional.to_json())

# convert the object into a dict
ob_bject_fred_regional_dict = ob_bject_fred_regional_instance.to_dict()
# create an instance of OBBjectFredRegional from a dict
ob_bject_fred_regional_from_dict = OBBjectFredRegional.from_dict(ob_bject_fred_regional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


