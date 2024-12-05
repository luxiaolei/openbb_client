# PolygonIndexHistoricalData

Polygon Index Historical Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**transactions** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_index_historical_data import PolygonIndexHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonIndexHistoricalData from a JSON string
polygon_index_historical_data_instance = PolygonIndexHistoricalData.from_json(json)
# print the JSON string representation of the object
print(PolygonIndexHistoricalData.to_json())

# convert the object into a dict
polygon_index_historical_data_dict = polygon_index_historical_data_instance.to_dict()
# create an instance of PolygonIndexHistoricalData from a dict
polygon_index_historical_data_from_dict = PolygonIndexHistoricalData.from_dict(polygon_index_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


