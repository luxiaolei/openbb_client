# OBBjectEquitySearchResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cik** | **str** |  | 
**lei** | **str** |  | 
**intrinio_id** | **str** | The Intrinio ID of the company. | 

## Example

```python
from openbb_client.models.ob_bject_equity_search_results_inner import OBBjectEquitySearchResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquitySearchResultsInner from a JSON string
ob_bject_equity_search_results_inner_instance = OBBjectEquitySearchResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquitySearchResultsInner.to_json())

# convert the object into a dict
ob_bject_equity_search_results_inner_dict = ob_bject_equity_search_results_inner_instance.to_dict()
# create an instance of OBBjectEquitySearchResultsInner from a dict
ob_bject_equity_search_results_inner_from_dict = OBBjectEquitySearchResultsInner.from_dict(ob_bject_equity_search_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


