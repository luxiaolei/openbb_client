# FMPIndexHistoricalData

FMP Index Historical Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**Date6**](Date6.md) |  | 
**open** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**close** | **float** |  | [optional] 
**volume** | **int** |  | [optional] 
**vwap** | **float** |  | [optional] 
**change** | **float** |  | [optional] 
**change_percent** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_index_historical_data import FMPIndexHistoricalData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPIndexHistoricalData from a JSON string
fmp_index_historical_data_instance = FMPIndexHistoricalData.from_json(json)
# print the JSON string representation of the object
print(FMPIndexHistoricalData.to_json())

# convert the object into a dict
fmp_index_historical_data_dict = fmp_index_historical_data_instance.to_dict()
# create an instance of FMPIndexHistoricalData from a dict
fmp_index_historical_data_from_dict = FMPIndexHistoricalData.from_dict(fmp_index_historical_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


