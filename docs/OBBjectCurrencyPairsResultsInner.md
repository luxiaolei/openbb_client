# OBBjectCurrencyPairsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**currency_symbol** | **str** |  | [optional] 
**base_currency_symbol** | **str** |  | [optional] 
**base_currency_name** | **str** |  | [optional] 
**market** | **str** | Name of the trading market. Always &#39;fx&#39;. | 
**locale** | **str** | Locale of the currency pair. | 
**last_updated** | **date** |  | [optional] 
**delisted** | **date** |  | [optional] 
**currency** | **str** | Base currency of the currency pair. | 
**stock_exchange** | **str** |  | [optional] 
**exchange_short_name** | **str** |  | [optional] 
**base_currency** | **str** | ISO 4217 currency code of the base currency. | 
**quote_currency** | **str** | ISO 4217 currency code of the quote currency. | 

## Example

```python
from openbb_client.models.ob_bject_currency_pairs_results_inner import OBBjectCurrencyPairsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCurrencyPairsResultsInner from a JSON string
ob_bject_currency_pairs_results_inner_instance = OBBjectCurrencyPairsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectCurrencyPairsResultsInner.to_json())

# convert the object into a dict
ob_bject_currency_pairs_results_inner_dict = ob_bject_currency_pairs_results_inner_instance.to_dict()
# create an instance of OBBjectCurrencyPairsResultsInner from a dict
ob_bject_currency_pairs_results_inner_from_dict = OBBjectCurrencyPairsResultsInner.from_dict(ob_bject_currency_pairs_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


