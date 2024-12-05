# FMPHistoricalSplitsData

FMP Historical Splits Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**numerator** | **float** |  | [optional] 
**denominator** | **float** |  | [optional] 
**split_ratio** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_historical_splits_data import FMPHistoricalSplitsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPHistoricalSplitsData from a JSON string
fmp_historical_splits_data_instance = FMPHistoricalSplitsData.from_json(json)
# print the JSON string representation of the object
print(FMPHistoricalSplitsData.to_json())

# convert the object into a dict
fmp_historical_splits_data_dict = fmp_historical_splits_data_instance.to_dict()
# create an instance of FMPHistoricalSplitsData from a dict
fmp_historical_splits_data_from_dict = FMPHistoricalSplitsData.from_dict(fmp_historical_splits_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


