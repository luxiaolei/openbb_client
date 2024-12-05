# OBBjectRevenueBusinessLine

OBBject with results of type RevenueBusinessLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPRevenueBusinessLineData]**](FMPRevenueBusinessLineData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_revenue_business_line import OBBjectRevenueBusinessLine

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectRevenueBusinessLine from a JSON string
ob_bject_revenue_business_line_instance = OBBjectRevenueBusinessLine.from_json(json)
# print the JSON string representation of the object
print(OBBjectRevenueBusinessLine.to_json())

# convert the object into a dict
ob_bject_revenue_business_line_dict = ob_bject_revenue_business_line_instance.to_dict()
# create an instance of OBBjectRevenueBusinessLine from a dict
ob_bject_revenue_business_line_from_dict = OBBjectRevenueBusinessLine.from_dict(ob_bject_revenue_business_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


