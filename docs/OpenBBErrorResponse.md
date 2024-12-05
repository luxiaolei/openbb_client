# OpenBBErrorResponse

OpenBB Error Response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**error_kind** | **str** |  | 

## Example

```python
from openbb_client.models.open_bb_error_response import OpenBBErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenBBErrorResponse from a JSON string
open_bb_error_response_instance = OpenBBErrorResponse.from_json(json)
# print the JSON string representation of the object
print(OpenBBErrorResponse.to_json())

# convert the object into a dict
open_bb_error_response_dict = open_bb_error_response_instance.to_dict()
# create an instance of OpenBBErrorResponse from a dict
open_bb_error_response_from_dict = OpenBBErrorResponse.from_dict(open_bb_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


