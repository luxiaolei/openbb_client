# OBBjectBlsSeries

OBBject with results of type BlsSeries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[BlsSeriesData]**](BlsSeriesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_bls_series import OBBjectBlsSeries

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectBlsSeries from a JSON string
ob_bject_bls_series_instance = OBBjectBlsSeries.from_json(json)
# print the JSON string representation of the object
print(OBBjectBlsSeries.to_json())

# convert the object into a dict
ob_bject_bls_series_dict = ob_bject_bls_series_instance.to_dict()
# create an instance of OBBjectBlsSeries from a dict
ob_bject_bls_series_from_dict = OBBjectBlsSeries.from_dict(ob_bject_bls_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


