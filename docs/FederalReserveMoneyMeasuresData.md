# FederalReserveMoneyMeasuresData

FederalReserve Money Measures Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **date** | The date of the data. | 
**m1** | **float** | Value of the M1 money supply in billions. | 
**m2** | **float** | Value of the M2 money supply in billions. | 
**currency** | **float** |  | [optional] 
**demand_deposits** | **float** |  | [optional] 
**retail_money_market_funds** | **float** |  | [optional] 
**other_liquid_deposits** | **float** |  | [optional] 
**small_denomination_time_deposits** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.federal_reserve_money_measures_data import FederalReserveMoneyMeasuresData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveMoneyMeasuresData from a JSON string
federal_reserve_money_measures_data_instance = FederalReserveMoneyMeasuresData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveMoneyMeasuresData.to_json())

# convert the object into a dict
federal_reserve_money_measures_data_dict = federal_reserve_money_measures_data_instance.to_dict()
# create an instance of FederalReserveMoneyMeasuresData from a dict
federal_reserve_money_measures_data_from_dict = FederalReserveMoneyMeasuresData.from_dict(federal_reserve_money_measures_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


