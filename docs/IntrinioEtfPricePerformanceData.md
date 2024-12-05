# IntrinioEtfPricePerformanceData

Intrinio ETF Performance Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**one_day** | **float** |  | [optional] 
**wtd** | **float** |  | [optional] 
**one_week** | **float** |  | [optional] 
**mtd** | **float** |  | [optional] 
**one_month** | **float** |  | [optional] 
**qtd** | **float** |  | [optional] 
**three_month** | **float** |  | [optional] 
**six_month** | **float** |  | [optional] 
**ytd** | **float** |  | [optional] 
**one_year** | **float** |  | [optional] 
**two_year** | **float** |  | [optional] 
**three_year** | **float** |  | [optional] 
**four_year** | **float** |  | [optional] 
**five_year** | **float** |  | [optional] 
**ten_year** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**max_annualized** | **float** |  | [optional] 
**volatility_one_year** | **float** |  | [optional] 
**volatility_three_year** | **float** |  | [optional] 
**volatility_five_year** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**volume_avg_30** | **float** |  | [optional] 
**volume_avg_90** | **float** |  | [optional] 
**volume_avg_180** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**nav** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**shares_outstanding** | **int** |  | [optional] 
**updated** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_etf_price_performance_data import IntrinioEtfPricePerformanceData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioEtfPricePerformanceData from a JSON string
intrinio_etf_price_performance_data_instance = IntrinioEtfPricePerformanceData.from_json(json)
# print the JSON string representation of the object
print(IntrinioEtfPricePerformanceData.to_json())

# convert the object into a dict
intrinio_etf_price_performance_data_dict = intrinio_etf_price_performance_data_instance.to_dict()
# create an instance of IntrinioEtfPricePerformanceData from a dict
intrinio_etf_price_performance_data_from_dict = IntrinioEtfPricePerformanceData.from_dict(intrinio_etf_price_performance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


