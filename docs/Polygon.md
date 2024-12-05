# Polygon

Query by datetime, less than. Either a date with the format 'YYYY-MM-DD' or a TZ-aware timestamp string, 'YYYY-MM-DDTH:M:S.000000000-04:00'. Include all nanoseconds and the 'T' between the day and hour. (provider: polygon)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.polygon import Polygon

# TODO update the JSON string below
json = "{}"
# create an instance of Polygon from a JSON string
polygon_instance = Polygon.from_json(json)
# print the JSON string representation of the object
print(Polygon.to_json())

# convert the object into a dict
polygon_dict = polygon_instance.to_dict()
# create an instance of Polygon from a dict
polygon_from_dict = Polygon.from_dict(polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


