# OBBjectInstitutionalOwnership

OBBject with results of type InstitutionalOwnership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPInstitutionalOwnershipData]**](FMPInstitutionalOwnershipData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_institutional_ownership import OBBjectInstitutionalOwnership

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectInstitutionalOwnership from a JSON string
ob_bject_institutional_ownership_instance = OBBjectInstitutionalOwnership.from_json(json)
# print the JSON string representation of the object
print(OBBjectInstitutionalOwnership.to_json())

# convert the object into a dict
ob_bject_institutional_ownership_dict = ob_bject_institutional_ownership_instance.to_dict()
# create an instance of OBBjectInstitutionalOwnership from a dict
ob_bject_institutional_ownership_from_dict = OBBjectInstitutionalOwnership.from_dict(ob_bject_institutional_ownership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


