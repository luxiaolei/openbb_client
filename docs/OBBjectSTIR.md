# OBBjectSTIR

OBBject with results of type STIR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDSTIRData]**](OECDSTIRData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_stir import OBBjectSTIR

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectSTIR from a JSON string
ob_bject_stir_instance = OBBjectSTIR.from_json(json)
# print the JSON string representation of the object
print(OBBjectSTIR.to_json())

# convert the object into a dict
ob_bject_stir_dict = ob_bject_stir_instance.to_dict()
# create an instance of OBBjectSTIR from a dict
ob_bject_stir_from_dict = OBBjectSTIR.from_dict(ob_bject_stir_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


