# YFGainersData

Yahoo Finance Gainers Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**price** | **float** | Last price. | 
**change** | **float** | Change in price. | 
**percent_change** | **float** | Percent change. | 
**volume** | [**Volume1**](Volume1.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**previous_close** | **float** |  | [optional] 
**ma_50** | **float** |  | [optional] 
**ma_200** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**shares_outstanding** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**price_to_book** | **float** |  | [optional] 
**eps_ttm** | **float** |  | [optional] 
**eps_forward** | **float** |  | [optional] 
**pe_forward** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_timezone** | **str** |  | [optional] 
**earnings_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.yf_gainers_data import YFGainersData

# TODO update the JSON string below
json = "{}"
# create an instance of YFGainersData from a JSON string
yf_gainers_data_instance = YFGainersData.from_json(json)
# print the JSON string representation of the object
print(YFGainersData.to_json())

# convert the object into a dict
yf_gainers_data_dict = yf_gainers_data_instance.to_dict()
# create an instance of YFGainersData from a dict
yf_gainers_data_from_dict = YFGainersData.from_dict(yf_gainers_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


