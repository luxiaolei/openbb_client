# FREDIORBData

FRED IORB Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.frediorb_data import FREDIORBData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDIORBData from a JSON string
frediorb_data_instance = FREDIORBData.from_json(json)
# print the JSON string representation of the object
print(FREDIORBData.to_json())

# convert the object into a dict
frediorb_data_dict = frediorb_data_instance.to_dict()
# create an instance of FREDIORBData from a dict
frediorb_data_from_dict = FREDIORBData.from_dict(frediorb_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


