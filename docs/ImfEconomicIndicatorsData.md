# ImfEconomicIndicatorsData

IMF Economic Indicators Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol_root** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | [**Value**](Value.md) |  | [optional] 
**scale** | **str** |  | [optional] 
**table** | **str** |  | [optional] 
**level** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**reference_sector** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.imf_economic_indicators_data import ImfEconomicIndicatorsData

# TODO update the JSON string below
json = "{}"
# create an instance of ImfEconomicIndicatorsData from a JSON string
imf_economic_indicators_data_instance = ImfEconomicIndicatorsData.from_json(json)
# print the JSON string representation of the object
print(ImfEconomicIndicatorsData.to_json())

# convert the object into a dict
imf_economic_indicators_data_dict = imf_economic_indicators_data_instance.to_dict()
# create an instance of ImfEconomicIndicatorsData from a dict
imf_economic_indicators_data_from_dict = ImfEconomicIndicatorsData.from_dict(imf_economic_indicators_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


