# FredSeriesData

FRED Series Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 

## Example

```python
from openbb_client.models.fred_series_data import FredSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of FredSeriesData from a JSON string
fred_series_data_instance = FredSeriesData.from_json(json)
# print the JSON string representation of the object
print(FredSeriesData.to_json())

# convert the object into a dict
fred_series_data_dict = fred_series_data_instance.to_dict()
# create an instance of FredSeriesData from a dict
fred_series_data_from_dict = FredSeriesData.from_dict(fred_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


