# FMPKeyExecutivesData

FMP Key Executives Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Designation of the key executive. | 
**name** | **str** | Name of the key executive. | 
**pay** | **int** |  | [optional] 
**currency_pay** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**year_born** | **int** |  | [optional] 
**title_since** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_key_executives_data import FMPKeyExecutivesData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPKeyExecutivesData from a JSON string
fmp_key_executives_data_instance = FMPKeyExecutivesData.from_json(json)
# print the JSON string representation of the object
print(FMPKeyExecutivesData.to_json())

# convert the object into a dict
fmp_key_executives_data_dict = fmp_key_executives_data_instance.to_dict()
# create an instance of FMPKeyExecutivesData from a dict
fmp_key_executives_data_from_dict = FMPKeyExecutivesData.from_dict(fmp_key_executives_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


