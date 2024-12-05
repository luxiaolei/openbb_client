# OBBjectFederalFundsRateResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Effective federal funds rate. | 
**target_range_upper** | **float** |  | [optional] 
**target_range_lower** | **float** |  | [optional] 
**percentile_1** | **float** |  | [optional] 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 
**percentile_99** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**intraday_low** | **float** |  | [optional] 
**intraday_high** | **float** |  | [optional] 
**standard_deviation** | **float** |  | [optional] 
**revision_indicator** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_federal_funds_rate_results_inner import OBBjectFederalFundsRateResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectFederalFundsRateResultsInner from a JSON string
ob_bject_federal_funds_rate_results_inner_instance = OBBjectFederalFundsRateResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectFederalFundsRateResultsInner.to_json())

# convert the object into a dict
ob_bject_federal_funds_rate_results_inner_dict = ob_bject_federal_funds_rate_results_inner_instance.to_dict()
# create an instance of OBBjectFederalFundsRateResultsInner from a dict
ob_bject_federal_funds_rate_results_inner_from_dict = OBBjectFederalFundsRateResultsInner.from_dict(ob_bject_federal_funds_rate_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


