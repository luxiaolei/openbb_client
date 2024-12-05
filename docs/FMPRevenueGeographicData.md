# FMPRevenueGeographicData

FMP Revenue Geographic Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**filing_date** | **date** |  | [optional] 
**region** | **str** |  | [optional] 
**revenue** | [**Revenue1**](Revenue1.md) |  | 

## Example

```python
from openbb_client.models.fmp_revenue_geographic_data import FMPRevenueGeographicData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPRevenueGeographicData from a JSON string
fmp_revenue_geographic_data_instance = FMPRevenueGeographicData.from_json(json)
# print the JSON string representation of the object
print(FMPRevenueGeographicData.to_json())

# convert the object into a dict
fmp_revenue_geographic_data_dict = fmp_revenue_geographic_data_instance.to_dict()
# create an instance of FMPRevenueGeographicData from a dict
fmp_revenue_geographic_data_from_dict = FMPRevenueGeographicData.from_dict(fmp_revenue_geographic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


