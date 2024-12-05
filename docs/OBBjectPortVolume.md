# OBBjectPortVolume

OBBject with results of type PortVolume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[EconDbPortVolumeData]**](EconDbPortVolumeData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_port_volume import OBBjectPortVolume

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPortVolume from a JSON string
ob_bject_port_volume_instance = OBBjectPortVolume.from_json(json)
# print the JSON string representation of the object
print(OBBjectPortVolume.to_json())

# convert the object into a dict
ob_bject_port_volume_dict = ob_bject_port_volume_instance.to_dict()
# create an instance of OBBjectPortVolume from a dict
ob_bject_port_volume_from_dict = OBBjectPortVolume.from_dict(ob_bject_port_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


