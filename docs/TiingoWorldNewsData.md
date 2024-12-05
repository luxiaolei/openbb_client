# TiingoWorldNewsData

Tiingo World News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. The published date of the article. | 
**title** | **str** | Title of the article. | 
**images** | **List[Dict[str, str]]** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**symbols** | **str** |  | [optional] 
**article_id** | **int** | Unique ID of the news article. | 
**site** | **str** | News source. | 
**tags** | **str** |  | [optional] 
**crawl_date** | **datetime** | Date the news article was crawled. | 

## Example

```python
from openbb_client.models.tiingo_world_news_data import TiingoWorldNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of TiingoWorldNewsData from a JSON string
tiingo_world_news_data_instance = TiingoWorldNewsData.from_json(json)
# print the JSON string representation of the object
print(TiingoWorldNewsData.to_json())

# convert the object into a dict
tiingo_world_news_data_dict = tiingo_world_news_data_instance.to_dict()
# create an instance of TiingoWorldNewsData from a dict
tiingo_world_news_data_from_dict = TiingoWorldNewsData.from_dict(tiingo_world_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


