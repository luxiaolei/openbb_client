# OBBjectCryptoHistoricalResultsInner


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
**transactions** | **int** |  | [optional] 
**adj_close** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**volume_notional** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_crypto_historical_results_inner import OBBjectCryptoHistoricalResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCryptoHistoricalResultsInner from a JSON string
ob_bject_crypto_historical_results_inner_instance = OBBjectCryptoHistoricalResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectCryptoHistoricalResultsInner.to_json())

# convert the object into a dict
ob_bject_crypto_historical_results_inner_dict = ob_bject_crypto_historical_results_inner_instance.to_dict()
# create an instance of OBBjectCryptoHistoricalResultsInner from a dict
ob_bject_crypto_historical_results_inner_from_dict = OBBjectCryptoHistoricalResultsInner.from_dict(ob_bject_crypto_historical_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


