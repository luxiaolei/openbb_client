# PolygonCurrencySnapshotsData

Polygon Currency Snapshots Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | The base, or domestic, currency. | 
**counter_currency** | **str** | The counter, or foreign, currency. | 
**last_rate** | **float** | The exchange rate, relative to the base currency. Rates are expressed as the amount of foreign currency received from selling one unit of the base currency, or the quantity of foreign currency required to purchase one unit of the domestic currency. To inverse the perspective, set the &#39;quote_type&#39; parameter as &#39;direct&#39;. | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**prev_close** | **float** |  | [optional] 
**vwap** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 
**prev_open** | **float** |  | [optional] 
**prev_high** | **float** |  | [optional] 
**prev_low** | **float** |  | [optional] 
**prev_volume** | **float** |  | [optional] 
**prev_vwap** | **float** |  | [optional] 
**bid** | **float** |  | [optional] 
**ask** | **float** |  | [optional] 
**minute_open** | **float** |  | [optional] 
**minute_high** | **float** |  | [optional] 
**minute_low** | **float** |  | [optional] 
**minute_close** | **float** |  | [optional] 
**minute_volume** | **float** |  | [optional] 
**minute_vwap** | **float** |  | [optional] 
**minute_transactions** | **float** |  | [optional] 
**quote_timestamp** | **datetime** |  | [optional] 
**minute_timestamp** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | 

## Example

```python
from openbb_client.models.polygon_currency_snapshots_data import PolygonCurrencySnapshotsData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonCurrencySnapshotsData from a JSON string
polygon_currency_snapshots_data_instance = PolygonCurrencySnapshotsData.from_json(json)
# print the JSON string representation of the object
print(PolygonCurrencySnapshotsData.to_json())

# convert the object into a dict
polygon_currency_snapshots_data_dict = polygon_currency_snapshots_data_instance.to_dict()
# create an instance of PolygonCurrencySnapshotsData from a dict
polygon_currency_snapshots_data_from_dict = PolygonCurrencySnapshotsData.from_dict(polygon_currency_snapshots_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


