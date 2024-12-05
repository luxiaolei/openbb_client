# IntrinioForwardEbitdaEstimatesData

Intrinio Forward EBITDA Estimates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**last_updated** | **date** |  | [optional] 
**period_ending** | **date** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**fiscal_period** | **str** |  | [optional] 
**calendar_year** | **int** |  | [optional] 
**calendar_period** | [**CalendarPeriod**](CalendarPeriod.md) |  | [optional] 
**low_estimate** | **int** |  | [optional] 
**high_estimate** | **int** |  | [optional] 
**mean** | **int** |  | [optional] 
**median** | **int** |  | [optional] 
**standard_deviation** | **int** |  | [optional] 
**number_of_analysts** | **int** |  | [optional] 
**conensus_type** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_forward_ebitda_estimates_data import IntrinioForwardEbitdaEstimatesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioForwardEbitdaEstimatesData from a JSON string
intrinio_forward_ebitda_estimates_data_instance = IntrinioForwardEbitdaEstimatesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioForwardEbitdaEstimatesData.to_json())

# convert the object into a dict
intrinio_forward_ebitda_estimates_data_dict = intrinio_forward_ebitda_estimates_data_instance.to_dict()
# create an instance of IntrinioForwardEbitdaEstimatesData from a dict
intrinio_forward_ebitda_estimates_data_from_dict = IntrinioForwardEbitdaEstimatesData.from_dict(intrinio_forward_ebitda_estimates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


