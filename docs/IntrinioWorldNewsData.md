# IntrinioWorldNewsData

Intrinio World News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. The published date of the article. | 
**title** | **str** | Title of the article. | 
**images** | **List[Dict[str, str]]** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**topics** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**business_relevance** | **float** |  | [optional] 
**sentiment** | **str** |  | [optional] 
**sentiment_confidence** | **float** |  | [optional] 
**language** | **str** |  | [optional] 
**spam** | **bool** |  | [optional] 
**copyright** | **str** |  | [optional] 
**id** | **str** | Article ID. | 
**company** | [**IntrinioCompany**](IntrinioCompany.md) |  | [optional] 
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_world_news_data import IntrinioWorldNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioWorldNewsData from a JSON string
intrinio_world_news_data_instance = IntrinioWorldNewsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioWorldNewsData.to_json())

# convert the object into a dict
intrinio_world_news_data_dict = intrinio_world_news_data_instance.to_dict()
# create an instance of IntrinioWorldNewsData from a dict
intrinio_world_news_data_from_dict = IntrinioWorldNewsData.from_dict(intrinio_world_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


