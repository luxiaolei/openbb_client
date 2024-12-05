# FederalReservePrimaryDealerPositioningData

Federal Reserve Primary Dealer Positioning Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**value** | **int** | The reported value of the net position (long - short), in millions of $USD. | 
**name** | **str** | Short name for the series. | 
**title** | **str** | Title of the series. | 

## Example

```python
from openbb_client.models.federal_reserve_primary_dealer_positioning_data import FederalReservePrimaryDealerPositioningData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReservePrimaryDealerPositioningData from a JSON string
federal_reserve_primary_dealer_positioning_data_instance = FederalReservePrimaryDealerPositioningData.from_json(json)
# print the JSON string representation of the object
print(FederalReservePrimaryDealerPositioningData.to_json())

# convert the object into a dict
federal_reserve_primary_dealer_positioning_data_dict = federal_reserve_primary_dealer_positioning_data_instance.to_dict()
# create an instance of FederalReservePrimaryDealerPositioningData from a dict
federal_reserve_primary_dealer_positioning_data_from_dict = FederalReservePrimaryDealerPositioningData.from_dict(federal_reserve_primary_dealer_positioning_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


