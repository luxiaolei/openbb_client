# Intrinio2

The date of the data. Can be a datetime or an ISO datetime string. Data appears to go back to around 2022-06-01 Example: '2024-03-08T12:15:00+0400' (provider: intrinio)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.intrinio2 import Intrinio2

# TODO update the JSON string below
json = "{}"
# create an instance of Intrinio2 from a JSON string
intrinio2_instance = Intrinio2.from_json(json)
# print the JSON string representation of the object
print(Intrinio2.to_json())

# convert the object into a dict
intrinio2_dict = intrinio2_instance.to_dict()
# create an instance of Intrinio2 from a dict
intrinio2_from_dict = Intrinio2.from_dict(intrinio2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


