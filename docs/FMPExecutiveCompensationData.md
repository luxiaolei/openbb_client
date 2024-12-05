# FMPExecutiveCompensationData

FMP Executive Compensation Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**cik** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**industry** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**name_and_position** | **str** |  | [optional] 
**salary** | **float** |  | [optional] 
**bonus** | **float** |  | [optional] 
**stock_award** | **float** |  | [optional] 
**incentive_plan_compensation** | **float** |  | [optional] 
**all_other_compensation** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**accepted_date** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_executive_compensation_data import FMPExecutiveCompensationData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPExecutiveCompensationData from a JSON string
fmp_executive_compensation_data_instance = FMPExecutiveCompensationData.from_json(json)
# print the JSON string representation of the object
print(FMPExecutiveCompensationData.to_json())

# convert the object into a dict
fmp_executive_compensation_data_dict = fmp_executive_compensation_data_instance.to_dict()
# create an instance of FMPExecutiveCompensationData from a dict
fmp_executive_compensation_data_from_dict = FMPExecutiveCompensationData.from_dict(fmp_executive_compensation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


