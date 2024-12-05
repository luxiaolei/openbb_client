# OBBjectDiscountWindowPrimaryCreditRate

OBBject with results of type DiscountWindowPrimaryCreditRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDDiscountWindowPrimaryCreditRateData]**](FREDDiscountWindowPrimaryCreditRateData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_discount_window_primary_credit_rate import OBBjectDiscountWindowPrimaryCreditRate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectDiscountWindowPrimaryCreditRate from a JSON string
ob_bject_discount_window_primary_credit_rate_instance = OBBjectDiscountWindowPrimaryCreditRate.from_json(json)
# print the JSON string representation of the object
print(OBBjectDiscountWindowPrimaryCreditRate.to_json())

# convert the object into a dict
ob_bject_discount_window_primary_credit_rate_dict = ob_bject_discount_window_primary_credit_rate_instance.to_dict()
# create an instance of OBBjectDiscountWindowPrimaryCreditRate from a dict
ob_bject_discount_window_primary_credit_rate_from_dict = OBBjectDiscountWindowPrimaryCreditRate.from_dict(ob_bject_discount_window_primary_credit_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


