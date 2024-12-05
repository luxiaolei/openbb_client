# IntrinioCompanyNewsData

Intrinio Company News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. Here it is the published date of the article. | 
**title** | **str** | Title of the article. | 
**text** | **str** |  | [optional] 
**images** | **List[Dict[str, str]]** |  | [optional] 
**url** | **str** | URL to the article. | 
**symbols** | **str** |  | [optional] 
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
**security** | [**IntrinioSecurity**](IntrinioSecurity.md) |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_company_news_data import IntrinioCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCompanyNewsData from a JSON string
intrinio_company_news_data_instance = IntrinioCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioCompanyNewsData.to_json())

# convert the object into a dict
intrinio_company_news_data_dict = intrinio_company_news_data_instance.to_dict()
# create an instance of IntrinioCompanyNewsData from a dict
intrinio_company_news_data_from_dict = IntrinioCompanyNewsData.from_dict(intrinio_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


