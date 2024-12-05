# OBBjectEtfSearchResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data.(ETF) | 
**name** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**figi_ticker** | **str** |  | [optional] 
**ric** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**sedol** | **str** |  | [optional] 
**intrinio_id** | **str** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**sector** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**beta** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**last_annual_dividend** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**exchange_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**actively_trading** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_search_results_inner import OBBjectEtfSearchResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfSearchResultsInner from a JSON string
ob_bject_etf_search_results_inner_instance = OBBjectEtfSearchResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfSearchResultsInner.to_json())

# convert the object into a dict
ob_bject_etf_search_results_inner_dict = ob_bject_etf_search_results_inner_instance.to_dict()
# create an instance of OBBjectEtfSearchResultsInner from a dict
ob_bject_etf_search_results_inner_from_dict = OBBjectEtfSearchResultsInner.from_dict(ob_bject_etf_search_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


