# PolygonPublisher

PolygonPublisher Data Model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favicon_url** | **str** | Favicon URL. | 
**homepage_url** | **str** | Homepage URL. | 
**logo_url** | **str** | Logo URL. | 
**name** | **str** | Publisher Name. | 

## Example

```python
from openbb_client.models.polygon_publisher import PolygonPublisher

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonPublisher from a JSON string
polygon_publisher_instance = PolygonPublisher.from_json(json)
# print the JSON string representation of the object
print(PolygonPublisher.to_json())

# convert the object into a dict
polygon_publisher_dict = polygon_publisher_instance.to_dict()
# create an instance of PolygonPublisher from a dict
polygon_publisher_from_dict = PolygonPublisher.from_dict(polygon_publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


