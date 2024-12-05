# OBBjectCommoditySpotPrices

OBBject with results of type CommoditySpotPrices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredCommoditySpotPricesData]**](FredCommoditySpotPricesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_commodity_spot_prices import OBBjectCommoditySpotPrices

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCommoditySpotPrices from a JSON string
ob_bject_commodity_spot_prices_instance = OBBjectCommoditySpotPrices.from_json(json)
# print the JSON string representation of the object
print(OBBjectCommoditySpotPrices.to_json())

# convert the object into a dict
ob_bject_commodity_spot_prices_dict = ob_bject_commodity_spot_prices_instance.to_dict()
# create an instance of OBBjectCommoditySpotPrices from a dict
ob_bject_commodity_spot_prices_from_dict = OBBjectCommoditySpotPrices.from_dict(ob_bject_commodity_spot_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


