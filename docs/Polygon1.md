# Polygon1

Query by datetime, greater than. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour. (provider: polygon)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.polygon1 import Polygon1

# TODO update the JSON string below
json = "{}"
# create an instance of Polygon1 from a JSON string
polygon1_instance = Polygon1.from_json(json)
# print the JSON string representation of the object
print(Polygon1.to_json())

# convert the object into a dict
polygon1_dict = polygon1_instance.to_dict()
# create an instance of Polygon1 from a dict
polygon1_from_dict = Polygon1.from_dict(polygon1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


