# OBBjectAmeribor

OBBject with results of type Ameribor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredAmeriborData]**](FredAmeriborData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_ameribor import OBBjectAmeribor

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAmeribor from a JSON string
ob_bject_ameribor_instance = OBBjectAmeribor.from_json(json)
# print the JSON string representation of the object
print(OBBjectAmeribor.to_json())

# convert the object into a dict
ob_bject_ameribor_dict = ob_bject_ameribor_instance.to_dict()
# create an instance of OBBjectAmeribor from a dict
ob_bject_ameribor_from_dict = OBBjectAmeribor.from_dict(ob_bject_ameribor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


