# FMPEquityHistoricalData

FMP Equity Historical Price Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | [**Volume**](Volume.md) |  | [optional] 
**vwap** | **float** |  | [optional] 
**adj_close** | **float** |  | [optional] 
**unadjusted_volume** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_equity_historical_data import FMPEquityHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityHistoricalData from a JSON string
fmp_equity_historical_data_instance = FMPEquityHistoricalData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityHistoricalData.to_json())

# convert the object into a dict
fmp_equity_historical_data_dict = fmp_equity_historical_data_instance.to_dict()
# create an instance of FMPEquityHistoricalData from a dict
fmp_equity_historical_data_from_dict = FMPEquityHistoricalData.from_dict(fmp_equity_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


