# OBBjectEquityOwnership

OBBject with results of type EquityOwnership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPEquityOwnershipData]**](FMPEquityOwnershipData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_ownership import OBBjectEquityOwnership

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityOwnership from a JSON string
ob_bject_equity_ownership_instance = OBBjectEquityOwnership.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityOwnership.to_json())

# convert the object into a dict
ob_bject_equity_ownership_dict = ob_bject_equity_ownership_instance.to_dict()
# create an instance of OBBjectEquityOwnership from a dict
ob_bject_equity_ownership_from_dict = OBBjectEquityOwnership.from_dict(ob_bject_equity_ownership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


