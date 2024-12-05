# OBBjectIORB

OBBject with results of type IORB

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDIORBData]**](FREDIORBData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_iorb import OBBjectIORB

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectIORB from a JSON string
ob_bject_iorb_instance = OBBjectIORB.from_json(json)
# print the JSON string representation of the object
print(OBBjectIORB.to_json())

# convert the object into a dict
ob_bject_iorb_dict = ob_bject_iorb_instance.to_dict()
# create an instance of OBBjectIORB from a dict
ob_bject_iorb_from_dict = OBBjectIORB.from_dict(ob_bject_iorb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


