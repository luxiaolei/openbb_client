# FREDConsumerPriceIndexData

FRED Consumer Price Index Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** |  | 
**value** | **float** | CPI index value or period change. | 

## Example

```python
from openbb_client.models.fred_consumer_price_index_data import FREDConsumerPriceIndexData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDConsumerPriceIndexData from a JSON string
fred_consumer_price_index_data_instance = FREDConsumerPriceIndexData.from_json(json)
# print the JSON string representation of the object
print(FREDConsumerPriceIndexData.to_json())

# convert the object into a dict
fred_consumer_price_index_data_dict = fred_consumer_price_index_data_instance.to_dict()
# create an instance of FREDConsumerPriceIndexData from a dict
fred_consumer_price_index_data_from_dict = FREDConsumerPriceIndexData.from_dict(fred_consumer_price_index_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


