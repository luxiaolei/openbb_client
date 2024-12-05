# Oecd

Country to get the CLI for, default is G20. Multiple comma separated items allowed. (provider: oecd)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.oecd import Oecd

# TODO update the JSON string below
json = "{}"
# create an instance of Oecd from a JSON string
oecd_instance = Oecd.from_json(json)
# print the JSON string representation of the object
print(Oecd.to_json())

# convert the object into a dict
oecd_dict = oecd_instance.to_dict()
# create an instance of Oecd from a dict
oecd_from_dict = Oecd.from_dict(oecd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


