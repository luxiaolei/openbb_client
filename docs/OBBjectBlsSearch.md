# OBBjectBlsSearch

OBBject with results of type BlsSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[BlsSearchData]**](BlsSearchData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_bls_search import OBBjectBlsSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBlsSearch from a JSON string
ob_bject_bls_search_instance = OBBjectBlsSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectBlsSearch.to_json())

# convert the object into a dict
ob_bject_bls_search_dict = ob_bject_bls_search_instance.to_dict()
# create an instance of OBBjectBlsSearch from a dict
ob_bject_bls_search_from_dict = OBBjectBlsSearch.from_dict(ob_bject_bls_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


