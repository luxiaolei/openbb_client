# OBBjectInstitutionsSearch

OBBject with results of type InstitutionsSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[SecInstitutionsSearchData]**](SecInstitutionsSearchData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_institutions_search import OBBjectInstitutionsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectInstitutionsSearch from a JSON string
ob_bject_institutions_search_instance = OBBjectInstitutionsSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectInstitutionsSearch.to_json())

# convert the object into a dict
ob_bject_institutions_search_dict = ob_bject_institutions_search_instance.to_dict()
# create an instance of OBBjectInstitutionsSearch from a dict
ob_bject_institutions_search_from_dict = OBBjectInstitutionsSearch.from_dict(ob_bject_institutions_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


