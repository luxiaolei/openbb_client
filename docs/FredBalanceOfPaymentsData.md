# FredBalanceOfPaymentsData

FRED Balance Of Payments Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **date** | The date representing the beginning of the reporting period. | [optional] 
**balance_percent_of_gdp** | **float** |  | [optional] 
**balance_total** | **float** |  | [optional] 
**balance_total_services** | **float** |  | [optional] 
**balance_total_secondary_income** | **float** |  | [optional] 
**balance_total_goods** | **float** |  | [optional] 
**balance_total_primary_income** | **float** |  | [optional] 
**credits_services_percent_of_goods_and_services** | **float** |  | [optional] 
**credits_services_percent_of_current_account** | **float** |  | [optional] 
**credits_total_services** | **float** |  | [optional] 
**credits_total_goods** | **float** |  | [optional] 
**credits_total_primary_income** | **float** |  | [optional] 
**credits_total_secondary_income** | **float** |  | [optional] 
**credits_total** | **float** |  | [optional] 
**debits_services_percent_of_goods_and_services** | **float** |  | [optional] 
**debits_services_percent_of_current_account** | **float** |  | [optional] 
**debits_total_services** | **float** |  | [optional] 
**debits_total_goods** | **float** |  | [optional] 
**debits_total_primary_income** | **float** |  | [optional] 
**debits_total** | **float** |  | [optional] 
**debits_total_secondary_income** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_balance_of_payments_data import FredBalanceOfPaymentsData

# TODO update the JSON string below
json = "{}"
# create an instance of FredBalanceOfPaymentsData from a JSON string
fred_balance_of_payments_data_instance = FredBalanceOfPaymentsData.from_json(json)
# print the JSON string representation of the object
print(FredBalanceOfPaymentsData.to_json())

# convert the object into a dict
fred_balance_of_payments_data_dict = fred_balance_of_payments_data_instance.to_dict()
# create an instance of FredBalanceOfPaymentsData from a dict
fred_balance_of_payments_data_from_dict = FredBalanceOfPaymentsData.from_dict(fred_balance_of_payments_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


