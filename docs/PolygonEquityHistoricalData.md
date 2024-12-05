# PolygonEquityHistoricalData

Polygon Equity Historical Price Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** | The open price. | 
**high** | **float** | The high price. | 
**low** | **float** | The low price. | 
**close** | **float** | The close price. | 
**volume** | [**Volume**](Volume.md) |  | [optional] 
**vwap** | **float** |  | [optional] 
**transactions** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_equity_historical_data import PolygonEquityHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonEquityHistoricalData from a JSON string
polygon_equity_historical_data_instance = PolygonEquityHistoricalData.from_json(json)
# print the JSON string representation of the object
print(PolygonEquityHistoricalData.to_json())

# convert the object into a dict
polygon_equity_historical_data_dict = polygon_equity_historical_data_instance.to_dict()
# create an instance of PolygonEquityHistoricalData from a dict
polygon_equity_historical_data_from_dict = PolygonEquityHistoricalData.from_dict(polygon_equity_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


