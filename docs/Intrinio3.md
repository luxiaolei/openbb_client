# Intrinio3

The date of the data. Can be a datetime or an ISO datetime string. Historical data appears to go back to mid-June 2022. Example: '2024-03-08T12:15:00+0400' (provider: intrinio)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.intrinio3 import Intrinio3

# TODO update the JSON string below
json = "{}"
# create an instance of Intrinio3 from a JSON string
intrinio3_instance = Intrinio3.from_json(json)
# print the JSON string representation of the object
print(Intrinio3.to_json())

# convert the object into a dict
intrinio3_dict = intrinio3_instance.to_dict()
# create an instance of Intrinio3 from a dict
intrinio3_from_dict = Intrinio3.from_dict(intrinio3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


