# OBBjectPriceTarget

OBBject with results of type PriceTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectPriceTargetResultsInner]**](OBBjectPriceTargetResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_price_target import OBBjectPriceTarget

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPriceTarget from a JSON string
ob_bject_price_target_instance = OBBjectPriceTarget.from_json(json)
# print the JSON string representation of the object
print(OBBjectPriceTarget.to_json())

# convert the object into a dict
ob_bject_price_target_dict = ob_bject_price_target_instance.to_dict()
# create an instance of OBBjectPriceTarget from a dict
ob_bject_price_target_from_dict = OBBjectPriceTarget.from_dict(ob_bject_price_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


