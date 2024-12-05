# BenzingaCompanyNewsData

Benzinga Company News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. Here it is the published date of the article. | 
**title** | **str** | Title of the article. | 
**text** | **str** |  | [optional] 
**images** | **List[Dict[str, str]]** |  | [optional] 
**url** | **str** | URL to the article. | 
**symbols** | **str** |  | [optional] 
**id** | **str** | Article ID. | 
**author** | **str** |  | [optional] 
**teaser** | **str** |  | [optional] 
**channels** | **str** |  | [optional] 
**stocks** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from openbb_client.models.benzinga_company_news_data import BenzingaCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of BenzingaCompanyNewsData from a JSON string
benzinga_company_news_data_instance = BenzingaCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(BenzingaCompanyNewsData.to_json())

# convert the object into a dict
benzinga_company_news_data_dict = benzinga_company_news_data_instance.to_dict()
# create an instance of BenzingaCompanyNewsData from a dict
benzinga_company_news_data_from_dict = BenzingaCompanyNewsData.from_dict(benzinga_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


