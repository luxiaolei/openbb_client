# FMPCryptoHistoricalData

FMP Crypto Historical Price Data.

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
**adj_close** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_crypto_historical_data import FMPCryptoHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCryptoHistoricalData from a JSON string
fmp_crypto_historical_data_instance = FMPCryptoHistoricalData.from_json(json)
# print the JSON string representation of the object
print(FMPCryptoHistoricalData.to_json())

# convert the object into a dict
fmp_crypto_historical_data_dict = fmp_crypto_historical_data_instance.to_dict()
# create an instance of FMPCryptoHistoricalData from a dict
fmp_crypto_historical_data_from_dict = FMPCryptoHistoricalData.from_dict(fmp_crypto_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


