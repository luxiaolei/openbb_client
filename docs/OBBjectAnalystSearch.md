# OBBjectAnalystSearch

OBBject with results of type AnalystSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[BenzingaAnalystSearchData]**](BenzingaAnalystSearchData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_analyst_search import OBBjectAnalystSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectAnalystSearch from a JSON string
ob_bject_analyst_search_instance = OBBjectAnalystSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectAnalystSearch.to_json())

# convert the object into a dict
ob_bject_analyst_search_dict = ob_bject_analyst_search_instance.to_dict()
# create an instance of OBBjectAnalystSearch from a dict
ob_bject_analyst_search_from_dict = OBBjectAnalystSearch.from_dict(ob_bject_analyst_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


