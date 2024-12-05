# IntrinioCompany

Intrinio Company Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Intrinio ID of the Company. | 
**ticker** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**lei** | **str** |  | [optional] 
**cik** | **str** |  | 

## Example

```python
from openbb_client.models.intrinio_company import IntrinioCompany

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioCompany from a JSON string
intrinio_company_instance = IntrinioCompany.from_json(json)
# print the JSON string representation of the object
print(IntrinioCompany.to_json())

# convert the object into a dict
intrinio_company_dict = intrinio_company_instance.to_dict()
# create an instance of IntrinioCompany from a dict
intrinio_company_from_dict = IntrinioCompany.from_dict(intrinio_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


