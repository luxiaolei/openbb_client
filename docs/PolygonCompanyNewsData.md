# PolygonCompanyNewsData

Polygon Company News Data.

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
**tags** | **str** |  | [optional] 
**id** | **str** | Article ID. | 
**amp_url** | **str** |  | [optional] 
**publisher** | [**PolygonPublisher**](PolygonPublisher.md) | Publisher of the article. | 

## Example

```python
from openbb_client.models.polygon_company_news_data import PolygonCompanyNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonCompanyNewsData from a JSON string
polygon_company_news_data_instance = PolygonCompanyNewsData.from_json(json)
# print the JSON string representation of the object
print(PolygonCompanyNewsData.to_json())

# convert the object into a dict
polygon_company_news_data_dict = polygon_company_news_data_instance.to_dict()
# create an instance of PolygonCompanyNewsData from a dict
polygon_company_news_data_from_dict = PolygonCompanyNewsData.from_dict(polygon_company_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


