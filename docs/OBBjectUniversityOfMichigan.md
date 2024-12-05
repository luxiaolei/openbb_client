# OBBjectUniversityOfMichigan

OBBject with results of type UniversityOfMichigan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredUofMichiganData]**](FredUofMichiganData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_university_of_michigan import OBBjectUniversityOfMichigan

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectUniversityOfMichigan from a JSON string
ob_bject_university_of_michigan_instance = OBBjectUniversityOfMichigan.from_json(json)
# print the JSON string representation of the object
print(OBBjectUniversityOfMichigan.to_json())

# convert the object into a dict
ob_bject_university_of_michigan_dict = ob_bject_university_of_michigan_instance.to_dict()
# create an instance of OBBjectUniversityOfMichigan from a dict
ob_bject_university_of_michigan_from_dict = OBBjectUniversityOfMichigan.from_dict(ob_bject_university_of_michigan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


