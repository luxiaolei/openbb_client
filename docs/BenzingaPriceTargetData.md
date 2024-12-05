# BenzingaPriceTargetData

Benzinga Price Target Data.

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
**action_change** | **str** |  | [optional] 
**importance** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**analyst_id** | **str** |  | [optional] 
**url_news** | **str** |  | [optional] 
**url_analyst** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.benzinga_price_target_data import BenzingaPriceTargetData

# TODO update the JSON string below
json = "{}"
# create an instance of BenzingaPriceTargetData from a JSON string
benzinga_price_target_data_instance = BenzingaPriceTargetData.from_json(json)
# print the JSON string representation of the object
print(BenzingaPriceTargetData.to_json())

# convert the object into a dict
benzinga_price_target_data_dict = benzinga_price_target_data_instance.to_dict()
# create an instance of BenzingaPriceTargetData from a dict
benzinga_price_target_data_from_dict = BenzingaPriceTargetData.from_dict(benzinga_price_target_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


