# Date4

A specific date to get data for. By default is the current data. Multiple comma separated items allowed for provider(s): econdb, federal_reserve, fmp, fred.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.date4 import Date4

# TODO update the JSON string below
json = "{}"
# create an instance of Date4 from a JSON string
date4_instance = Date4.from_json(json)
# print the JSON string representation of the object
print(Date4.to_json())

# convert the object into a dict
date4_dict = date4_instance.to_dict()
# create an instance of Date4 from a dict
date4_from_dict = Date4.from_dict(date4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


