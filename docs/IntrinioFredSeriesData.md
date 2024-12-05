# IntrinioFredSeriesData

Intrinio FRED Series Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_fred_series_data import IntrinioFredSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioFredSeriesData from a JSON string
intrinio_fred_series_data_instance = IntrinioFredSeriesData.from_json(json)
# print the JSON string representation of the object
print(IntrinioFredSeriesData.to_json())

# convert the object into a dict
intrinio_fred_series_data_dict = intrinio_fred_series_data_instance.to_dict()
# create an instance of IntrinioFredSeriesData from a dict
intrinio_fred_series_data_from_dict = IntrinioFredSeriesData.from_dict(intrinio_fred_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


