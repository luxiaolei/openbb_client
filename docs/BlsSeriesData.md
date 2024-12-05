# BlsSeriesData

BLS Series Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**title** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**change_1_m** | **float** |  | [optional] 
**change_3_m** | **float** |  | [optional] 
**change_6_m** | **float** |  | [optional] 
**change_12_m** | **float** |  | [optional] 
**change_percent_1_m** | **float** |  | [optional] 
**change_percent_3_m** | **float** |  | [optional] 
**change_percent_6_m** | **float** |  | [optional] 
**change_percent_12_m** | **float** |  | [optional] 
**latest** | **bool** |  | [optional] 
**footnotes** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.bls_series_data import BlsSeriesData

# TODO update the JSON string below
json = "{}"
# create an instance of BlsSeriesData from a JSON string
bls_series_data_instance = BlsSeriesData.from_json(json)
# print the JSON string representation of the object
print(BlsSeriesData.to_json())

# convert the object into a dict
bls_series_data_dict = bls_series_data_instance.to_dict()
# create an instance of BlsSeriesData from a dict
bls_series_data_from_dict = BlsSeriesData.from_dict(bls_series_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


