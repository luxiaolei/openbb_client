# FederalReservePrimaryDealerFailsData

Federal Reserve Primary Dealer Fails Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**title** | **str** | Title of the series&#39; symbol. | 
**value** | [**Value5**](Value5.md) |  | 

## Example

```python
from openbb_client.models.federal_reserve_primary_dealer_fails_data import FederalReservePrimaryDealerFailsData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReservePrimaryDealerFailsData from a JSON string
federal_reserve_primary_dealer_fails_data_instance = FederalReservePrimaryDealerFailsData.from_json(json)
# print the JSON string representation of the object
print(FederalReservePrimaryDealerFailsData.to_json())

# convert the object into a dict
federal_reserve_primary_dealer_fails_data_dict = federal_reserve_primary_dealer_fails_data_instance.to_dict()
# create an instance of FederalReservePrimaryDealerFailsData from a dict
federal_reserve_primary_dealer_fails_data_from_dict = FederalReservePrimaryDealerFailsData.from_dict(federal_reserve_primary_dealer_fails_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


