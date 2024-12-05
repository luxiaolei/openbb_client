# FredRegionalData

FRED Regional Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**region** | **str** | The name of the region. | 
**code** | [**Code**](Code.md) |  | 
**value** | [**Value6**](Value6.md) |  | [optional] 
**series_id** | **str** | The individual series ID for the region. | 

## Example

```python
from openbb_client.models.fred_regional_data import FredRegionalData

# TODO update the JSON string below
json = "{}"
# create an instance of FredRegionalData from a JSON string
fred_regional_data_instance = FredRegionalData.from_json(json)
# print the JSON string representation of the object
print(FredRegionalData.to_json())

# convert the object into a dict
fred_regional_data_dict = fred_regional_data_instance.to_dict()
# create an instance of FredRegionalData from a dict
fred_regional_data_from_dict = FredRegionalData.from_dict(fred_regional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


