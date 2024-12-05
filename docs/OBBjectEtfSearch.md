# OBBjectEtfSearch

OBBject with results of type EtfSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectEtfSearchResultsInner]**](OBBjectEtfSearchResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_search import OBBjectEtfSearch

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfSearch from a JSON string
ob_bject_etf_search_instance = OBBjectEtfSearch.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfSearch.to_json())

# convert the object into a dict
ob_bject_etf_search_dict = ob_bject_etf_search_instance.to_dict()
# create an instance of OBBjectEtfSearch from a dict
ob_bject_etf_search_from_dict = OBBjectEtfSearch.from_dict(ob_bject_etf_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


