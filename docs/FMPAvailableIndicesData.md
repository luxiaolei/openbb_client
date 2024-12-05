# FMPAvailableIndicesData

FMP Available Indices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**stock_exchange** | **str** | Stock exchange where the index is listed. | 
**exchange_short_name** | **str** | Short name of the stock exchange where the index is listed. | 

## Example

```python
from openbb_client.models.fmp_available_indices_data import FMPAvailableIndicesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPAvailableIndicesData from a JSON string
fmp_available_indices_data_instance = FMPAvailableIndicesData.from_json(json)
# print the JSON string representation of the object
print(FMPAvailableIndicesData.to_json())

# convert the object into a dict
fmp_available_indices_data_dict = fmp_available_indices_data_instance.to_dict()
# create an instance of FMPAvailableIndicesData from a dict
fmp_available_indices_data_from_dict = FMPAvailableIndicesData.from_dict(fmp_available_indices_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


