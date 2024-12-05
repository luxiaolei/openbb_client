# OBBjectBondIndices

OBBject with results of type BondIndices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredBondIndicesData]**](FredBondIndicesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_bond_indices import OBBjectBondIndices

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBondIndices from a JSON string
ob_bject_bond_indices_instance = OBBjectBondIndices.from_json(json)
# print the JSON string representation of the object
print(OBBjectBondIndices.to_json())

# convert the object into a dict
ob_bject_bond_indices_dict = ob_bject_bond_indices_instance.to_dict()
# create an instance of OBBjectBondIndices from a dict
ob_bject_bond_indices_from_dict = OBBjectBondIndices.from_dict(ob_bject_bond_indices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


