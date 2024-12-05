# OECDHousePriceIndexData

OECD House Price Index Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.oecd_house_price_index_data import OECDHousePriceIndexData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDHousePriceIndexData from a JSON string
oecd_house_price_index_data_instance = OECDHousePriceIndexData.from_json(json)
# print the JSON string representation of the object
print(OECDHousePriceIndexData.to_json())

# convert the object into a dict
oecd_house_price_index_data_dict = oecd_house_price_index_data_instance.to_dict()
# create an instance of OECDHousePriceIndexData from a dict
oecd_house_price_index_data_from_dict = OECDHousePriceIndexData.from_dict(oecd_house_price_index_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


