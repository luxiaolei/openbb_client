# OBBjectPROJECTIONS

OBBject with results of type PROJECTIONS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDPROJECTIONData]**](FREDPROJECTIONData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_projections import OBBjectPROJECTIONS

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPROJECTIONS from a JSON string
ob_bject_projections_instance = OBBjectPROJECTIONS.from_json(json)
# print the JSON string representation of the object
print(OBBjectPROJECTIONS.to_json())

# convert the object into a dict
ob_bject_projections_dict = ob_bject_projections_instance.to_dict()
# create an instance of OBBjectPROJECTIONS from a dict
ob_bject_projections_from_dict = OBBjectPROJECTIONS.from_dict(ob_bject_projections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


