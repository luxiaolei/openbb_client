# FederalReserveTreasuryRatesData

FederalReserve Treasury Rates Data.

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
from openbb_client.models.federal_reserve_treasury_rates_data import FederalReserveTreasuryRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveTreasuryRatesData from a JSON string
federal_reserve_treasury_rates_data_instance = FederalReserveTreasuryRatesData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveTreasuryRatesData.to_json())

# convert the object into a dict
federal_reserve_treasury_rates_data_dict = federal_reserve_treasury_rates_data_instance.to_dict()
# create an instance of FederalReserveTreasuryRatesData from a dict
federal_reserve_treasury_rates_data_from_dict = FederalReserveTreasuryRatesData.from_dict(federal_reserve_treasury_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


