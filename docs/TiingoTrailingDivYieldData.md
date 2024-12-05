# TiingoTrailingDivYieldData

Tiingo Trailing Dividend Yield Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**trailing_dividend_yield** | **float** | Trailing dividend yield. | 

## Example

```python
from openbb_client.models.tiingo_trailing_div_yield_data import TiingoTrailingDivYieldData

# TODO update the JSON string below
json = "{}"
# create an instance of TiingoTrailingDivYieldData from a JSON string
tiingo_trailing_div_yield_data_instance = TiingoTrailingDivYieldData.from_json(json)
# print the JSON string representation of the object
print(TiingoTrailingDivYieldData.to_json())

# convert the object into a dict
tiingo_trailing_div_yield_data_dict = tiingo_trailing_div_yield_data_instance.to_dict()
# create an instance of TiingoTrailingDivYieldData from a dict
tiingo_trailing_div_yield_data_from_dict = TiingoTrailingDivYieldData.from_dict(tiingo_trailing_div_yield_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


