# OBBjectLTIR

OBBject with results of type LTIR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDLTIRData]**](OECDLTIRData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_ltir import OBBjectLTIR

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectLTIR from a JSON string
ob_bject_ltir_instance = OBBjectLTIR.from_json(json)
# print the JSON string representation of the object
print(OBBjectLTIR.to_json())

# convert the object into a dict
ob_bject_ltir_dict = ob_bject_ltir_instance.to_dict()
# create an instance of OBBjectLTIR from a dict
ob_bject_ltir_from_dict = OBBjectLTIR.from_dict(ob_bject_ltir_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


