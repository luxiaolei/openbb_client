# YFinanceCompanyNewsData

YFinance Company News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. Here it is the published date of the article. | 
**title** | **str** | Title of the article. | 
**text** | **str** |  | [optional] 
**images** | **List[Dict[str, str]]** |  | [optional] 
**url** | **str** | URL to the article. | 
**symbols** | **str** |  | [optional] 
**source** | **str** | Source of the news article | 

## Example

```python
from openbb_client.models.y_finance_company_news_data import YFinanceCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceCompanyNewsData from a JSON string
y_finance_company_news_data_instance = YFinanceCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(YFinanceCompanyNewsData.to_json())

# convert the object into a dict
y_finance_company_news_data_dict = y_finance_company_news_data_instance.to_dict()
# create an instance of YFinanceCompanyNewsData from a dict
y_finance_company_news_data_from_dict = YFinanceCompanyNewsData.from_dict(y_finance_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


