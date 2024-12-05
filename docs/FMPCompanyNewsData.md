# FMPCompanyNewsData

FMP Company News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. Here it is the published date of the article. | 
**title** | **str** | Title of the article. | 
**text** | **str** |  | [optional] 
**images** | **List[Dict[str, str]]** |  | [optional] 
**url** | **str** | URL to the article. | 
**symbols** | **str** |  | [optional] 
**source** | **str** | Name of the news source. | 

## Example

```python
from openbb_client.models.fmp_company_news_data import FMPCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPCompanyNewsData from a JSON string
fmp_company_news_data_instance = FMPCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(FMPCompanyNewsData.to_json())

# convert the object into a dict
fmp_company_news_data_dict = fmp_company_news_data_instance.to_dict()
# create an instance of FMPCompanyNewsData from a dict
fmp_company_news_data_from_dict = FMPCompanyNewsData.from_dict(fmp_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


