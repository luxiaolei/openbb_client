# FMPEtfSearchData

FMP ETF Search Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data.(ETF) | 
**name** | **str** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**sector** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**beta** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**last_annual_dividend** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**actively_trading** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_etf_search_data import FMPEtfSearchData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfSearchData from a JSON string
fmp_etf_search_data_instance = FMPEtfSearchData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfSearchData.to_json())

# convert the object into a dict
fmp_etf_search_data_dict = fmp_etf_search_data_instance.to_dict()
# create an instance of FMPEtfSearchData from a dict
fmp_etf_search_data_from_dict = FMPEtfSearchData.from_dict(fmp_etf_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


