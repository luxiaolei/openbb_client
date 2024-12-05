# FMPPriceTargetData

FMP Price Target Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published_date** | [**PublishedDate**](PublishedDate.md) |  | 
**published_time** | **str** |  | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**exchange** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**analyst_name** | **str** |  | [optional] 
**analyst_firm** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**price_target** | **float** |  | [optional] 
**adj_price_target** | **float** |  | [optional] 
**price_target_previous** | **float** |  | [optional] 
**previous_adj_price_target** | **float** |  | [optional] 
**price_when_posted** | **float** |  | [optional] 
**rating_current** | **str** |  | [optional] 
**rating_previous** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**news_url** | **str** |  | [optional] 
**news_title** | **str** |  | [optional] 
**news_publisher** | **str** |  | [optional] 
**news_base_url** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_price_target_data import FMPPriceTargetData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPPriceTargetData from a JSON string
fmp_price_target_data_instance = FMPPriceTargetData.from_json(json)
# print the JSON string representation of the object
print(FMPPriceTargetData.to_json())

# convert the object into a dict
fmp_price_target_data_dict = fmp_price_target_data_instance.to_dict()
# create an instance of FMPPriceTargetData from a dict
fmp_price_target_data_from_dict = FMPPriceTargetData.from_dict(fmp_price_target_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


