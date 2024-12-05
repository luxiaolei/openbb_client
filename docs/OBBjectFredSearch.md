# OBBjectFredSearch

OBBject with results of type FredSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredSearchData]**](FredSearchData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_fred_search import OBBjectFredSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFredSearch from a JSON string
ob_bject_fred_search_instance = OBBjectFredSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectFredSearch.to_json())

# convert the object into a dict
ob_bject_fred_search_dict = ob_bject_fred_search_instance.to_dict()
# create an instance of OBBjectFredSearch from a dict
ob_bject_fred_search_from_dict = OBBjectFredSearch.from_dict(ob_bject_fred_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


