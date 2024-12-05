# OBBjectForwardEpsEstimatesResultsInner


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
**low_estimate** | **float** |  | [optional] 
**high_estimate** | **float** |  | [optional] 
**mean** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**standard_deviation** | **float** |  | [optional] 
**number_of_analysts** | **int** |  | [optional] 
**revisions_change_percent** | **float** |  | [optional] 
**mean_1w** | **float** |  | [optional] 
**mean_1m** | **float** |  | [optional] 
**mean_2m** | **float** |  | [optional] 
**mean_3m** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_forward_eps_estimates_results_inner import OBBjectForwardEpsEstimatesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectForwardEpsEstimatesResultsInner from a JSON string
ob_bject_forward_eps_estimates_results_inner_instance = OBBjectForwardEpsEstimatesResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectForwardEpsEstimatesResultsInner.to_json())

# convert the object into a dict
ob_bject_forward_eps_estimates_results_inner_dict = ob_bject_forward_eps_estimates_results_inner_instance.to_dict()
# create an instance of OBBjectForwardEpsEstimatesResultsInner from a dict
ob_bject_forward_eps_estimates_results_inner_from_dict = OBBjectForwardEpsEstimatesResultsInner.from_dict(ob_bject_forward_eps_estimates_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


