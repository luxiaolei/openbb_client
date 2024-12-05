# IntrinioForwardSalesEstimatesData

Intrinio Forward Sales Estimates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**var_date** | **date** | The date of the data. | 
**fiscal_year** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**calendar_year** | **int** |  | [optional] 
**calendar_period** | **str** |  | [optional] 
**low_estimate** | **int** |  | [optional] 
**high_estimate** | **int** |  | [optional] 
**mean** | **int** |  | [optional] 
**median** | **int** |  | [optional] 
**standard_deviation** | **int** |  | [optional] 
**number_of_analysts** | **int** |  | [optional] 
**revisions_1w_up** | **int** |  | [optional] 
**revisions_1w_down** | **int** |  | [optional] 
**revisions_1w_change_percent** | **float** |  | [optional] 
**revisions_1m_up** | **int** |  | [optional] 
**revisions_1m_down** | **int** |  | [optional] 
**revisions_1m_change_percent** | **float** |  | [optional] 
**revisions_3m_up** | **int** |  | [optional] 
**revisions_3m_down** | **int** |  | [optional] 
**revisions_3m_change_percent** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_forward_sales_estimates_data import IntrinioForwardSalesEstimatesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioForwardSalesEstimatesData from a JSON string
intrinio_forward_sales_estimates_data_instance = IntrinioForwardSalesEstimatesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioForwardSalesEstimatesData.to_json())

# convert the object into a dict
intrinio_forward_sales_estimates_data_dict = intrinio_forward_sales_estimates_data_instance.to_dict()
# create an instance of IntrinioForwardSalesEstimatesData from a dict
intrinio_forward_sales_estimates_data_from_dict = IntrinioForwardSalesEstimatesData.from_dict(intrinio_forward_sales_estimates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


