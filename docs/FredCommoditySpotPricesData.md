# FredCommoditySpotPricesData

FRED Commodity Spot Prices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**commodity** | **str** |  | [optional] 
**price** | **float** | Price of the commodity. | 
**unit** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fred_commodity_spot_prices_data import FredCommoditySpotPricesData

# TODO update the JSON string below
json = "{}"
# create an instance of FredCommoditySpotPricesData from a JSON string
fred_commodity_spot_prices_data_instance = FredCommoditySpotPricesData.from_json(json)
# print the JSON string representation of the object
print(FredCommoditySpotPricesData.to_json())

# convert the object into a dict
fred_commodity_spot_prices_data_dict = fred_commodity_spot_prices_data_instance.to_dict()
# create an instance of FredCommoditySpotPricesData from a dict
fred_commodity_spot_prices_data_from_dict = FredCommoditySpotPricesData.from_dict(fred_commodity_spot_prices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


