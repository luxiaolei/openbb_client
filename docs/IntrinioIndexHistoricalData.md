# IntrinioIndexHistoricalData

Intrinio Index Historical Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_index_historical_data import IntrinioIndexHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioIndexHistoricalData from a JSON string
intrinio_index_historical_data_instance = IntrinioIndexHistoricalData.from_json(json)
# print the JSON string representation of the object
print(IntrinioIndexHistoricalData.to_json())

# convert the object into a dict
intrinio_index_historical_data_dict = intrinio_index_historical_data_instance.to_dict()
# create an instance of IntrinioIndexHistoricalData from a dict
intrinio_index_historical_data_from_dict = IntrinioIndexHistoricalData.from_dict(intrinio_index_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


