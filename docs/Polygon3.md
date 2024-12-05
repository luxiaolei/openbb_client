# Polygon3

Query by datetime, greater than or equal to. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour. (provider: polygon)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.polygon3 import Polygon3

# TODO update the JSON string below
json = "{}"
# create an instance of Polygon3 from a JSON string
polygon3_instance = Polygon3.from_json(json)
# print the JSON string representation of the object
print(Polygon3.to_json())

# convert the object into a dict
polygon3_dict = polygon3_instance.to_dict()
# create an instance of Polygon3 from a dict
polygon3_from_dict = Polygon3.from_dict(polygon3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


