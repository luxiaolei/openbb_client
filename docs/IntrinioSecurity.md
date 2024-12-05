# IntrinioSecurity

Intrinio Security Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Intrinio ID for Security. | 
**company_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 
**composite_ticker** | **str** |  | [optional] 
**figi** | **str** |  | [optional] 
**composite_figi** | **str** |  | [optional] 
**share_class_figi** | **str** |  | [optional] 
**primary_listing** | **bool** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_security import IntrinioSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioSecurity from a JSON string
intrinio_security_instance = IntrinioSecurity.from_json(json)
# print the JSON string representation of the object
print(IntrinioSecurity.to_json())

# convert the object into a dict
intrinio_security_dict = intrinio_security_instance.to_dict()
# create an instance of IntrinioSecurity from a dict
intrinio_security_from_dict = IntrinioSecurity.from_dict(intrinio_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


