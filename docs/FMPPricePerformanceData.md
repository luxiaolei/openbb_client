# FMPPricePerformanceData

FMP Price Performance Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The ticker symbol. | 
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

## Example

```python
from openbb_client.models.fmp_price_performance_data import FMPPricePerformanceData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPPricePerformanceData from a JSON string
fmp_price_performance_data_instance = FMPPricePerformanceData.from_json(json)
# print the JSON string representation of the object
print(FMPPricePerformanceData.to_json())

# convert the object into a dict
fmp_price_performance_data_dict = fmp_price_performance_data_instance.to_dict()
# create an instance of FMPPricePerformanceData from a dict
fmp_price_performance_data_from_dict = FMPPricePerformanceData.from_dict(fmp_price_performance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


