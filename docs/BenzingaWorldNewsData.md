# BenzingaWorldNewsData

Benzinga World News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. The published date of the article. | 
**title** | **str** | Title of the article. | 
**images** | **List[Dict[str, str]]** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**id** | **str** | Article ID. | 
**author** | **str** |  | [optional] 
**teaser** | **str** |  | [optional] 
**channels** | **str** |  | [optional] 
**stocks** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.benzinga_world_news_data import BenzingaWorldNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of BenzingaWorldNewsData from a JSON string
benzinga_world_news_data_instance = BenzingaWorldNewsData.from_json(json)
# print the JSON string representation of the object
print(BenzingaWorldNewsData.to_json())

# convert the object into a dict
benzinga_world_news_data_dict = benzinga_world_news_data_instance.to_dict()
# create an instance of BenzingaWorldNewsData from a dict
benzinga_world_news_data_from_dict = BenzingaWorldNewsData.from_dict(benzinga_world_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


