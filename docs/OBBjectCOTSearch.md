# OBBjectCOTSearch

OBBject with results of type COTSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[CftcCotSearchData]**](CftcCotSearchData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_cot_search import OBBjectCOTSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCOTSearch from a JSON string
ob_bject_cot_search_instance = OBBjectCOTSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectCOTSearch.to_json())

# convert the object into a dict
ob_bject_cot_search_dict = ob_bject_cot_search_instance.to_dict()
# create an instance of OBBjectCOTSearch from a dict
ob_bject_cot_search_from_dict = OBBjectCOTSearch.from_dict(ob_bject_cot_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


