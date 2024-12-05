# OBBjectForwardEbitdaEstimatesResultsInner


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
from openbb_client.models.ob_bject_forward_ebitda_estimates_results_inner import OBBjectForwardEbitdaEstimatesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectForwardEbitdaEstimatesResultsInner from a JSON string
ob_bject_forward_ebitda_estimates_results_inner_instance = OBBjectForwardEbitdaEstimatesResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectForwardEbitdaEstimatesResultsInner.to_json())

# convert the object into a dict
ob_bject_forward_ebitda_estimates_results_inner_dict = ob_bject_forward_ebitda_estimates_results_inner_instance.to_dict()
# create an instance of OBBjectForwardEbitdaEstimatesResultsInner from a dict
ob_bject_forward_ebitda_estimates_results_inner_from_dict = OBBjectForwardEbitdaEstimatesResultsInner.from_dict(ob_bject_forward_ebitda_estimates_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


