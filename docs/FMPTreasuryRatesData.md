# FMPTreasuryRatesData

FMP Treasury Rates Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**week_4** | **float** |  | [optional] 
**month_1** | **float** |  | [optional] 
**month_2** | **float** |  | [optional] 
**month_3** | **float** |  | [optional] 
**month_6** | **float** |  | [optional] 
**year_1** | **float** |  | [optional] 
**year_2** | **float** |  | [optional] 
**year_3** | **float** |  | [optional] 
**year_5** | **float** |  | [optional] 
**year_7** | **float** |  | [optional] 
**year_10** | **float** |  | [optional] 
**year_20** | **float** |  | [optional] 
**year_30** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_treasury_rates_data import FMPTreasuryRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPTreasuryRatesData from a JSON string
fmp_treasury_rates_data_instance = FMPTreasuryRatesData.from_json(json)
# print the JSON string representation of the object
print(FMPTreasuryRatesData.to_json())

# convert the object into a dict
fmp_treasury_rates_data_dict = fmp_treasury_rates_data_instance.to_dict()
# create an instance of FMPTreasuryRatesData from a dict
fmp_treasury_rates_data_from_dict = FMPTreasuryRatesData.from_dict(fmp_treasury_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


