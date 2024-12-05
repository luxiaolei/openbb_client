# OBBjectCompanyNews

OBBject with results of type CompanyNews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectCompanyNewsResultsInner]**](OBBjectCompanyNewsResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_company_news import OBBjectCompanyNews

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompanyNews from a JSON string
ob_bject_company_news_instance = OBBjectCompanyNews.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompanyNews.to_json())

# convert the object into a dict
ob_bject_company_news_dict = ob_bject_company_news_instance.to_dict()
# create an instance of OBBjectCompanyNews from a dict
ob_bject_company_news_from_dict = OBBjectCompanyNews.from_dict(ob_bject_company_news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


