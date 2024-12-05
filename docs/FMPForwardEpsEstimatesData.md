# FMPForwardEpsEstimatesData

FMP Forward EPS Data.

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

## Example

```python
from openbb_client.models.fmp_forward_eps_estimates_data import FMPForwardEpsEstimatesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPForwardEpsEstimatesData from a JSON string
fmp_forward_eps_estimates_data_instance = FMPForwardEpsEstimatesData.from_json(json)
# print the JSON string representation of the object
print(FMPForwardEpsEstimatesData.to_json())

# convert the object into a dict
fmp_forward_eps_estimates_data_dict = fmp_forward_eps_estimates_data_instance.to_dict()
# create an instance of FMPForwardEpsEstimatesData from a dict
fmp_forward_eps_estimates_data_from_dict = FMPForwardEpsEstimatesData.from_dict(fmp_forward_eps_estimates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


