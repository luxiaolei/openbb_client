# YFinanceCryptoHistoricalData

Yahoo Finance Crypto Historical Price Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | **float** | The trading volume. | 
**vwap** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_crypto_historical_data import YFinanceCryptoHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceCryptoHistoricalData from a JSON string
y_finance_crypto_historical_data_instance = YFinanceCryptoHistoricalData.from_json(json)
# print the JSON string representation of the object
print(YFinanceCryptoHistoricalData.to_json())

# convert the object into a dict
y_finance_crypto_historical_data_dict = y_finance_crypto_historical_data_instance.to_dict()
# create an instance of YFinanceCryptoHistoricalData from a dict
y_finance_crypto_historical_data_from_dict = YFinanceCryptoHistoricalData.from_dict(y_finance_crypto_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


