# OBBjectCompanyNewsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. Here it is the published date of the article. | 
**title** | **str** | Title of the article. | 
**text** | **str** |  | [optional] 
**images** | **List[Dict[str, str]]** |  | [optional] 
**url** | **str** | URL to the article. | 
**symbols** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**article_id** | **int** | Unique ID of the news article. | 
**source** | **str** | Name of the news source. | 
**crawl_date** | **datetime** | Date the news article was crawled. | 
**id** | **str** | Article ID. | 
**author** | **str** |  | [optional] 
**teaser** | **str** |  | [optional] 
**channels** | **str** |  | [optional] 
**stocks** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**amp_url** | **str** |  | [optional] 
**publisher** | [**PolygonPublisher**](PolygonPublisher.md) | Publisher of the article. | 
**summary** | **str** |  | [optional] 
**topics** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**business_relevance** | **float** |  | [optional] 
**sentiment** | **str** |  | [optional] 
**sentiment_confidence** | **float** |  | [optional] 
**language** | **str** |  | [optional] 
**spam** | **bool** |  | [optional] 
**copyright** | **str** |  | [optional] 
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_company_news_results_inner import OBBjectCompanyNewsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompanyNewsResultsInner from a JSON string
ob_bject_company_news_results_inner_instance = OBBjectCompanyNewsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompanyNewsResultsInner.to_json())

# convert the object into a dict
ob_bject_company_news_results_inner_dict = ob_bject_company_news_results_inner_instance.to_dict()
# create an instance of OBBjectCompanyNewsResultsInner from a dict
ob_bject_company_news_results_inner_from_dict = OBBjectCompanyNewsResultsInner.from_dict(ob_bject_company_news_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


