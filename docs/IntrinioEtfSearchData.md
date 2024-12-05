# IntrinioEtfSearchData

Intrinio ETF Search Data.

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

## Example

```python
from openbb_client.models.intrinio_etf_search_data import IntrinioEtfSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEtfSearchData from a JSON string
intrinio_etf_search_data_instance = IntrinioEtfSearchData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEtfSearchData.to_json())

# convert the object into a dict
intrinio_etf_search_data_dict = intrinio_etf_search_data_instance.to_dict()
# create an instance of IntrinioEtfSearchData from a dict
intrinio_etf_search_data_from_dict = IntrinioEtfSearchData.from_dict(intrinio_etf_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


