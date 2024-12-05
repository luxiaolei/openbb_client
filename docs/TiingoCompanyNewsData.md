# TiingoCompanyNewsData

Tiingo Company News data.

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
**source** | **str** | News source. | 
**crawl_date** | **datetime** | Date the news article was crawled. | 

## Example

```python
from openbb_client.models.tiingo_company_news_data import TiingoCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of TiingoCompanyNewsData from a JSON string
tiingo_company_news_data_instance = TiingoCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(TiingoCompanyNewsData.to_json())

# convert the object into a dict
tiingo_company_news_data_dict = tiingo_company_news_data_instance.to_dict()
# create an instance of TiingoCompanyNewsData from a dict
tiingo_company_news_data_from_dict = TiingoCompanyNewsData.from_dict(tiingo_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


