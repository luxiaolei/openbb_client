# FREDPROJECTIONData

FRED PROJECTION Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**range_high** | **float** |  | 
**central_tendency_high** | **float** |  | 
**median** | **float** |  | 
**range_midpoint** | **float** |  | 
**central_tendency_midpoint** | **float** |  | 
**range_low** | **float** |  | 
**central_tendency_low** | **float** |  | 

## Example

```python
from openbb_client.models.fredprojection_data import FREDPROJECTIONData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDPROJECTIONData from a JSON string
fredprojection_data_instance = FREDPROJECTIONData.from_json(json)
# print the JSON string representation of the object
print(FREDPROJECTIONData.to_json())

# convert the object into a dict
fredprojection_data_dict = fredprojection_data_instance.to_dict()
# create an instance of FREDPROJECTIONData from a dict
fredprojection_data_from_dict = FREDPROJECTIONData.from_dict(fredprojection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


