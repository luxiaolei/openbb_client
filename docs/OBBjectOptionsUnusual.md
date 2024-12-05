# OBBjectOptionsUnusual

OBBject with results of type OptionsUnusual

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioOptionsUnusualData]**](IntrinioOptionsUnusualData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_options_unusual import OBBjectOptionsUnusual

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOptionsUnusual from a JSON string
ob_bject_options_unusual_instance = OBBjectOptionsUnusual.from_json(json)
# print the JSON string representation of the object
print(OBBjectOptionsUnusual.to_json())

# convert the object into a dict
ob_bject_options_unusual_dict = ob_bject_options_unusual_instance.to_dict()
# create an instance of OBBjectOptionsUnusual from a dict
ob_bject_options_unusual_from_dict = OBBjectOptionsUnusual.from_dict(ob_bject_options_unusual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


