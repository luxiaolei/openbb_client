# FREDSONIAData

FRED SONIA Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fredsonia_data import FREDSONIAData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDSONIAData from a JSON string
fredsonia_data_instance = FREDSONIAData.from_json(json)
# print the JSON string representation of the object
print(FREDSONIAData.to_json())

# convert the object into a dict
fredsonia_data_dict = fredsonia_data_instance.to_dict()
# create an instance of FREDSONIAData from a dict
fredsonia_data_from_dict = FREDSONIAData.from_dict(fredsonia_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


