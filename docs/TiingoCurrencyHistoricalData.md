# TiingoCurrencyHistoricalData

Tiingo Currency Historical Price Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | **float** |  | [optional] 
**vwap** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.tiingo_currency_historical_data import TiingoCurrencyHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of TiingoCurrencyHistoricalData from a JSON string
tiingo_currency_historical_data_instance = TiingoCurrencyHistoricalData.from_json(json)
# print the JSON string representation of the object
print(TiingoCurrencyHistoricalData.to_json())

# convert the object into a dict
tiingo_currency_historical_data_dict = tiingo_currency_historical_data_instance.to_dict()
# create an instance of TiingoCurrencyHistoricalData from a dict
tiingo_currency_historical_data_from_dict = TiingoCurrencyHistoricalData.from_dict(tiingo_currency_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


