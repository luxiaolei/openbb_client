# OBBjectCompositeLeadingIndicator

OBBject with results of type CompositeLeadingIndicator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDCompositeLeadingIndicatorData]**](OECDCompositeLeadingIndicatorData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_composite_leading_indicator import OBBjectCompositeLeadingIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectCompositeLeadingIndicator from a JSON string
ob_bject_composite_leading_indicator_instance = OBBjectCompositeLeadingIndicator.from_json(json)
# print the JSON string representation of the object
print(OBBjectCompositeLeadingIndicator.to_json())

# convert the object into a dict
ob_bject_composite_leading_indicator_dict = ob_bject_composite_leading_indicator_instance.to_dict()
# create an instance of OBBjectCompositeLeadingIndicator from a dict
ob_bject_composite_leading_indicator_from_dict = OBBjectCompositeLeadingIndicator.from_dict(ob_bject_composite_leading_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


