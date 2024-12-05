# OBBjectPriceTargetResultsInner


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
from openbb_client.models.ob_bject_price_target_results_inner import OBBjectPriceTargetResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPriceTargetResultsInner from a JSON string
ob_bject_price_target_results_inner_instance = OBBjectPriceTargetResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectPriceTargetResultsInner.to_json())

# convert the object into a dict
ob_bject_price_target_results_inner_dict = ob_bject_price_target_results_inner_instance.to_dict()
# create an instance of OBBjectPriceTargetResultsInner from a dict
ob_bject_price_target_results_inner_from_dict = OBBjectPriceTargetResultsInner.from_dict(ob_bject_price_target_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


