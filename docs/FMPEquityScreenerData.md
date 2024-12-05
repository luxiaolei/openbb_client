# FMPEquityScreenerData

FMP Equity Screener Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**market_cap** | **int** |  | [optional] 
**sector** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**beta** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**last_annual_dividend** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_etf** | **bool** |  | [optional] 
**actively_trading** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_equity_screener_data import FMPEquityScreenerData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityScreenerData from a JSON string
fmp_equity_screener_data_instance = FMPEquityScreenerData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityScreenerData.to_json())

# convert the object into a dict
fmp_equity_screener_data_dict = fmp_equity_screener_data_instance.to_dict()
# create an instance of FMPEquityScreenerData from a dict
fmp_equity_screener_data_from_dict = FMPEquityScreenerData.from_dict(fmp_equity_screener_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


