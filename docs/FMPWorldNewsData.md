# FMPWorldNewsData

FMP World News Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the data. The published date of the article. | 
**title** | **str** | Title of the article. | 
**images** | **List[Dict[str, str]]** |  | [optional] 
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**site** | **str** | News source. | 

## Example

```python
from openbb_client.models.fmp_world_news_data import FMPWorldNewsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPWorldNewsData from a JSON string
fmp_world_news_data_instance = FMPWorldNewsData.from_json(json)
# print the JSON string representation of the object
print(FMPWorldNewsData.to_json())

# convert the object into a dict
fmp_world_news_data_dict = fmp_world_news_data_instance.to_dict()
# create an instance of FMPWorldNewsData from a dict
fmp_world_news_data_from_dict = FMPWorldNewsData.from_dict(fmp_world_news_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


