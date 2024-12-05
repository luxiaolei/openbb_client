# ImfAvailableIndicatorsData

IMF Available Indicators Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**iso** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**table** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.imf_available_indicators_data import ImfAvailableIndicatorsData

# TODO update the JSON string below
json = "{}"
# create an instance of ImfAvailableIndicatorsData from a JSON string
imf_available_indicators_data_instance = ImfAvailableIndicatorsData.from_json(json)
# print the JSON string representation of the object
print(ImfAvailableIndicatorsData.to_json())

# convert the object into a dict
imf_available_indicators_data_dict = imf_available_indicators_data_instance.to_dict()
# create an instance of ImfAvailableIndicatorsData from a dict
imf_available_indicators_data_from_dict = ImfAvailableIndicatorsData.from_dict(imf_available_indicators_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


