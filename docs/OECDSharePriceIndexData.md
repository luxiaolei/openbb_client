# OECDSharePriceIndexData

OECD Share Price Index Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.oecd_share_price_index_data import OECDSharePriceIndexData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDSharePriceIndexData from a JSON string
oecd_share_price_index_data_instance = OECDSharePriceIndexData.from_json(json)
# print the JSON string representation of the object
print(OECDSharePriceIndexData.to_json())

# convert the object into a dict
oecd_share_price_index_data_dict = oecd_share_price_index_data_instance.to_dict()
# create an instance of OECDSharePriceIndexData from a dict
oecd_share_price_index_data_from_dict = OECDSharePriceIndexData.from_dict(oecd_share_price_index_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


