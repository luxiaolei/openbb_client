# FMPRevenueBusinessLineData

FMP Revenue By Business Line Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**business_line** | **str** |  | [optional] 
**revenue** | [**Revenue**](Revenue.md) |  | 

## Example

```python
from openbb_client.models.fmp_revenue_business_line_data import FMPRevenueBusinessLineData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPRevenueBusinessLineData from a JSON string
fmp_revenue_business_line_data_instance = FMPRevenueBusinessLineData.from_json(json)
# print the JSON string representation of the object
print(FMPRevenueBusinessLineData.to_json())

# convert the object into a dict
fmp_revenue_business_line_data_dict = fmp_revenue_business_line_data_instance.to_dict()
# create an instance of FMPRevenueBusinessLineData from a dict
fmp_revenue_business_line_data_from_dict = FMPRevenueBusinessLineData.from_dict(fmp_revenue_business_line_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


