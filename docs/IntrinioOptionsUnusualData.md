# IntrinioOptionsUnusualData

Intrinio Unusual Options Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_symbol** | **str** |  | [optional] 
**contract_symbol** | **str** | Contract symbol for the option. | 
**trade_timestamp** | **datetime** | The datetime of order placement. | 
**trade_type** | **str** | The type of unusual trade. | 
**sentiment** | **str** | Bullish, Bearish, or Neutral Sentiment is estimated based on whether the trade was executed at the bid, ask, or mark price. | 
**bid_at_execution** | **float** | Bid price at execution. | 
**ask_at_execution** | **float** | Ask price at execution. | 
**average_price** | **float** | The average premium paid per option contract. | 
**underlying_price_at_execution** | **float** |  | [optional] 
**total_size** | **int** | The total number of contracts involved in a single transaction. | 
**total_value** | [**TotalValue**](TotalValue.md) |  | 

## Example

```python
from openbb_client.models.intrinio_options_unusual_data import IntrinioOptionsUnusualData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioOptionsUnusualData from a JSON string
intrinio_options_unusual_data_instance = IntrinioOptionsUnusualData.from_json(json)
# print the JSON string representation of the object
print(IntrinioOptionsUnusualData.to_json())

# convert the object into a dict
intrinio_options_unusual_data_dict = intrinio_options_unusual_data_instance.to_dict()
# create an instance of IntrinioOptionsUnusualData from a dict
intrinio_options_unusual_data_from_dict = IntrinioOptionsUnusualData.from_dict(intrinio_options_unusual_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


