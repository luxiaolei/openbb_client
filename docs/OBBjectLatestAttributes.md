# OBBjectLatestAttributes

OBBject with results of type LatestAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioLatestAttributesData]**](IntrinioLatestAttributesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_latest_attributes import OBBjectLatestAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectLatestAttributes from a JSON string
ob_bject_latest_attributes_instance = OBBjectLatestAttributes.from_json(json)
# print the JSON string representation of the object
print(OBBjectLatestAttributes.to_json())

# convert the object into a dict
ob_bject_latest_attributes_dict = ob_bject_latest_attributes_instance.to_dict()
# create an instance of OBBjectLatestAttributes from a dict
ob_bject_latest_attributes_from_dict = OBBjectLatestAttributes.from_dict(ob_bject_latest_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


