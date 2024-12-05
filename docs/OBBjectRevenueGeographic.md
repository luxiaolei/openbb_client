# OBBjectRevenueGeographic

OBBject with results of type RevenueGeographic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPRevenueGeographicData]**](FMPRevenueGeographicData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_revenue_geographic import OBBjectRevenueGeographic

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectRevenueGeographic from a JSON string
ob_bject_revenue_geographic_instance = OBBjectRevenueGeographic.from_json(json)
# print the JSON string representation of the object
print(OBBjectRevenueGeographic.to_json())

# convert the object into a dict
ob_bject_revenue_geographic_dict = ob_bject_revenue_geographic_instance.to_dict()
# create an instance of OBBjectRevenueGeographic from a dict
ob_bject_revenue_geographic_from_dict = OBBjectRevenueGeographic.from_dict(ob_bject_revenue_geographic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


