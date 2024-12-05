# OBBjectMoodyCorporateBondIndex

OBBject with results of type MoodyCorporateBondIndex

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDMoodyCorporateBondIndexData]**](FREDMoodyCorporateBondIndexData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_moody_corporate_bond_index import OBBjectMoodyCorporateBondIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectMoodyCorporateBondIndex from a JSON string
ob_bject_moody_corporate_bond_index_instance = OBBjectMoodyCorporateBondIndex.from_json(json)
# print the JSON string representation of the object
print(OBBjectMoodyCorporateBondIndex.to_json())

# convert the object into a dict
ob_bject_moody_corporate_bond_index_dict = ob_bject_moody_corporate_bond_index_instance.to_dict()
# create an instance of OBBjectMoodyCorporateBondIndex from a dict
ob_bject_moody_corporate_bond_index_from_dict = OBBjectMoodyCorporateBondIndex.from_dict(ob_bject_moody_corporate_bond_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


