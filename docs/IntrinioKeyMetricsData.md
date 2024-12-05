# IntrinioKeyMetricsData

Intrinio Key Metrics Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**market_cap** | **float** |  | [optional] 
**pe_ratio** | **float** |  | [optional] 
**price_to_book** | **float** |  | [optional] 
**price_to_tangible_book** | **float** |  | [optional] 
**price_to_revenue** | **float** |  | [optional] 
**quick_ratio** | **float** |  | [optional] 
**gross_margin** | **float** |  | [optional] 
**ebit_margin** | **float** |  | [optional] 
**profit_margin** | **float** |  | [optional] 
**eps** | **float** |  | [optional] 
**eps_growth** | **float** |  | [optional] 
**revenue_growth** | **float** |  | [optional] 
**ebitda_growth** | **float** |  | [optional] 
**ebit_growth** | **float** |  | [optional] 
**net_income_growth** | **float** |  | [optional] 
**free_cash_flow_to_firm_growth** | **float** |  | [optional] 
**invested_capital_growth** | **float** |  | [optional] 
**return_on_assets** | **float** |  | [optional] 
**return_on_equity** | **float** |  | [optional] 
**return_on_invested_capital** | **float** |  | [optional] 
**ebitda** | **int** |  | [optional] 
**ebit** | **int** |  | [optional] 
**long_term_debt** | **int** |  | [optional] 
**total_debt** | **int** |  | [optional] 
**total_capital** | **int** |  | [optional] 
**enterprise_value** | **int** |  | [optional] 
**free_cash_flow_to_firm** | **int** |  | [optional] 
**altman_z_score** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**dividend_yield** | **float** |  | [optional] 
**earnings_yield** | **float** |  | [optional] 
**last_price** | **float** |  | [optional] 
**year_high** | **float** |  | [optional] 
**year_low** | **float** | 52 week low | [optional] 
**volume_avg** | **int** |  | [optional] 
**short_interest** | **int** |  | [optional] 
**shares_outstanding** | **int** |  | [optional] 
**days_to_cover** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_key_metrics_data import IntrinioKeyMetricsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioKeyMetricsData from a JSON string
intrinio_key_metrics_data_instance = IntrinioKeyMetricsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioKeyMetricsData.to_json())

# convert the object into a dict
intrinio_key_metrics_data_dict = intrinio_key_metrics_data_instance.to_dict()
# create an instance of IntrinioKeyMetricsData from a dict
intrinio_key_metrics_data_from_dict = IntrinioKeyMetricsData.from_dict(intrinio_key_metrics_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


