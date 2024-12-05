# YFinanceEtfInfoData

YFinance ETF Info Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. (ETF) | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**inception_date** | **str** |  | 
**fund_type** | **str** |  | [optional] 
**fund_family** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**exchange** | **str** |  | [optional] 
**exchange_timezone** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**nav_price** | **float** |  | [optional] 
**total_assets** | **int** |  | [optional] 
**trailing_pe** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**dividend_rate_ttm** | **float** |  | [optional] 
**dividend_yield_ttm** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**ma_50d** | **float** |  | [optional] 
**ma_200d** | **float** |  | [optional] 
**return_ytd** | **float** |  | [optional] 
**return_3y_avg** | **float** |  | [optional] 
**return_5y_avg** | **float** |  | [optional] 
**beta_3y_avg** | **float** |  | [optional] 
**volume_avg** | **float** |  | [optional] 
**volume_avg_10d** | **float** |  | [optional] 
**bid** | **float** |  | [optional] 
**bid_size** | **float** |  | [optional] 
**ask** | **float** |  | [optional] 
**ask_size** | **float** |  | [optional] 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**prev_close** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.y_finance_etf_info_data import YFinanceEtfInfoData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceEtfInfoData from a JSON string
y_finance_etf_info_data_instance = YFinanceEtfInfoData.from_json(json)
# print the JSON string representation of the object
print(YFinanceEtfInfoData.to_json())

# convert the object into a dict
y_finance_etf_info_data_dict = y_finance_etf_info_data_instance.to_dict()
# create an instance of YFinanceEtfInfoData from a dict
y_finance_etf_info_data_from_dict = YFinanceEtfInfoData.from_dict(y_finance_etf_info_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


