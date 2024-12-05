# IntrinioForwardPeEstimatesData

Intrinio Forward PE Estimates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**name** | **str** |  | [optional] 
**year_1** | **float** |  | [optional] 
**year_2** | **float** |  | [optional] 
**year_3** | **float** |  | [optional] 
**year_4** | **float** |  | [optional] 
**year_5** | **float** |  | [optional] 
**peg_ratio_year_1** | **float** |  | [optional] 
**eps_ttm** | **float** |  | [optional] 
**last_updated** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_forward_pe_estimates_data import IntrinioForwardPeEstimatesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioForwardPeEstimatesData from a JSON string
intrinio_forward_pe_estimates_data_instance = IntrinioForwardPeEstimatesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioForwardPeEstimatesData.to_json())

# convert the object into a dict
intrinio_forward_pe_estimates_data_dict = intrinio_forward_pe_estimates_data_instance.to_dict()
# create an instance of IntrinioForwardPeEstimatesData from a dict
intrinio_forward_pe_estimates_data_from_dict = IntrinioForwardPeEstimatesData.from_dict(intrinio_forward_pe_estimates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


