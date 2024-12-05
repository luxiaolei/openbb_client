# OBBjectWorldNewsResultsInner


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
**id** | **str** | Article ID. | 
**author** | **str** |  | [optional] 
**teaser** | **str** |  | [optional] 
**channels** | **str** |  | [optional] 
**stocks** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
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
**company** | [**IntrinioCompany**](IntrinioCompany.md) |  | [optional] 
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_world_news_results_inner import OBBjectWorldNewsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectWorldNewsResultsInner from a JSON string
ob_bject_world_news_results_inner_instance = OBBjectWorldNewsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectWorldNewsResultsInner.to_json())

# convert the object into a dict
ob_bject_world_news_results_inner_dict = ob_bject_world_news_results_inner_instance.to_dict()
# create an instance of OBBjectWorldNewsResultsInner from a dict
ob_bject_world_news_results_inner_from_dict = OBBjectWorldNewsResultsInner.from_dict(ob_bject_world_news_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


