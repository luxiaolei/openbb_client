# OBBjectExecutiveCompensation

OBBject with results of type ExecutiveCompensation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPExecutiveCompensationData]**](FMPExecutiveCompensationData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_executive_compensation import OBBjectExecutiveCompensation

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectExecutiveCompensation from a JSON string
ob_bject_executive_compensation_instance = OBBjectExecutiveCompensation.from_json(json)
# print the JSON string representation of the object
print(OBBjectExecutiveCompensation.to_json())

# convert the object into a dict
ob_bject_executive_compensation_dict = ob_bject_executive_compensation_instance.to_dict()
# create an instance of OBBjectExecutiveCompensation from a dict
ob_bject_executive_compensation_from_dict = OBBjectExecutiveCompensation.from_dict(ob_bject_executive_compensation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


