# Benzinga3

Comma-separated list of fields to include in the response. See https://docs.benzinga.io/benzinga-apis/calendar/get-ratings to learn about the available fields. Multiple comma separated items allowed. (provider: benzinga)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.benzinga3 import Benzinga3

# TODO update the JSON string below
json = "{}"
# create an instance of Benzinga3 from a JSON string
benzinga3_instance = Benzinga3.from_json(json)
# print the JSON string representation of the object
print(Benzinga3.to_json())

# convert the object into a dict
benzinga3_dict = benzinga3_instance.to_dict()
# create an instance of Benzinga3 from a dict
benzinga3_from_dict = Benzinga3.from_dict(benzinga3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


