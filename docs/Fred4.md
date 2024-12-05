# Fred4

The specific index, or index group, to query. Default is the 'primary' group. Multiple comma separated items allowed. (provider: fred)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.fred4 import Fred4

# TODO update the JSON string below
json = "{}"
# create an instance of Fred4 from a JSON string
fred4_instance = Fred4.from_json(json)
# print the JSON string representation of the object
print(Fred4.to_json())

# convert the object into a dict
fred4_dict = fred4_instance.to_dict()
# create an instance of Fred4 from a dict
fred4_from_dict = Fred4.from_dict(fred4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


