# TiingoEquityHistoricalData

Tiingo Equity Historical Price Data.

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
**adj_open** | **float** |  | [optional] 
**adj_high** | **float** |  | [optional] 
**adj_low** | **float** |  | [optional] 
**adj_close** | **float** |  | [optional] 
**adj_volume** | **float** |  | [optional] 
**split_ratio** | **float** |  | [optional] 
**dividend** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.tiingo_equity_historical_data import TiingoEquityHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of TiingoEquityHistoricalData from a JSON string
tiingo_equity_historical_data_instance = TiingoEquityHistoricalData.from_json(json)
# print the JSON string representation of the object
print(TiingoEquityHistoricalData.to_json())

# convert the object into a dict
tiingo_equity_historical_data_dict = tiingo_equity_historical_data_instance.to_dict()
# create an instance of TiingoEquityHistoricalData from a dict
tiingo_equity_historical_data_from_dict = TiingoEquityHistoricalData.from_dict(tiingo_equity_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


