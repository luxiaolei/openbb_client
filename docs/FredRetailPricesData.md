# FredRetailPricesData

FRED Retail Prices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**description** | **str** | Description of the item. | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_retail_prices_data import FredRetailPricesData

# TODO update the JSON string below
json = "{}"
# create an instance of FredRetailPricesData from a JSON string
fred_retail_prices_data_instance = FredRetailPricesData.from_json(json)
# print the JSON string representation of the object
print(FredRetailPricesData.to_json())

# convert the object into a dict
fred_retail_prices_data_dict = fred_retail_prices_data_instance.to_dict()
# create an instance of FredRetailPricesData from a dict
fred_retail_prices_data_from_dict = FredRetailPricesData.from_dict(fred_retail_prices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


