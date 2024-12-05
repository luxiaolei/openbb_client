# OBBjectRetailPrices

OBBject with results of type RetailPrices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredRetailPricesData]**](FredRetailPricesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_retail_prices import OBBjectRetailPrices

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectRetailPrices from a JSON string
ob_bject_retail_prices_instance = OBBjectRetailPrices.from_json(json)
# print the JSON string representation of the object
print(OBBjectRetailPrices.to_json())

# convert the object into a dict
ob_bject_retail_prices_dict = ob_bject_retail_prices_instance.to_dict()
# create an instance of OBBjectRetailPrices from a dict
ob_bject_retail_prices_from_dict = OBBjectRetailPrices.from_dict(ob_bject_retail_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


