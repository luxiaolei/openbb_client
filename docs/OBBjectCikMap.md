# OBBjectCikMap

OBBject with results of type CikMap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**SecCikMapData**](SecCikMapData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_cik_map import OBBjectCikMap

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCikMap from a JSON string
ob_bject_cik_map_instance = OBBjectCikMap.from_json(json)
# print the JSON string representation of the object
print(OBBjectCikMap.to_json())

# convert the object into a dict
ob_bject_cik_map_dict = ob_bject_cik_map_instance.to_dict()
# create an instance of OBBjectCikMap from a dict
ob_bject_cik_map_from_dict = OBBjectCikMap.from_dict(ob_bject_cik_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


