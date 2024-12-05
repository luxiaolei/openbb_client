# FMPAnalystEstimatesData

FMP Analyst Estimates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**var_date** | **date** | The date of the data. | 
**estimated_revenue_low** | **int** |  | [optional] 
**estimated_revenue_high** | **int** |  | [optional] 
**estimated_revenue_avg** | **int** |  | [optional] 
**estimated_sga_expense_low** | **int** |  | [optional] 
**estimated_sga_expense_high** | **int** |  | [optional] 
**estimated_sga_expense_avg** | **int** |  | [optional] 
**estimated_ebitda_low** | **int** |  | [optional] 
**estimated_ebitda_high** | **int** |  | [optional] 
**estimated_ebitda_avg** | **int** |  | [optional] 
**estimated_ebit_low** | **int** |  | [optional] 
**estimated_ebit_high** | **int** |  | [optional] 
**estimated_ebit_avg** | **int** |  | [optional] 
**estimated_net_income_low** | **int** |  | [optional] 
**estimated_net_income_high** | **int** |  | [optional] 
**estimated_net_income_avg** | **int** |  | [optional] 
**estimated_eps_avg** | **float** |  | [optional] 
**estimated_eps_high** | **float** |  | [optional] 
**estimated_eps_low** | **float** |  | [optional] 
**number_analyst_estimated_revenue** | **int** |  | [optional] 
**number_analysts_estimated_eps** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_analyst_estimates_data import FMPAnalystEstimatesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPAnalystEstimatesData from a JSON string
fmp_analyst_estimates_data_instance = FMPAnalystEstimatesData.from_json(json)
# print the JSON string representation of the object
print(FMPAnalystEstimatesData.to_json())

# convert the object into a dict
fmp_analyst_estimates_data_dict = fmp_analyst_estimates_data_instance.to_dict()
# create an instance of FMPAnalystEstimatesData from a dict
fmp_analyst_estimates_data_from_dict = FMPAnalystEstimatesData.from_dict(fmp_analyst_estimates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


