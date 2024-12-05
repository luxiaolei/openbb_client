# OBBjectEuroShortTermRate

OBBject with results of type EuroShortTermRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredEuroShortTermRateData]**](FredEuroShortTermRateData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_euro_short_term_rate import OBBjectEuroShortTermRate

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEuroShortTermRate from a JSON string
ob_bject_euro_short_term_rate_instance = OBBjectEuroShortTermRate.from_json(json)
# print the JSON string representation of the object
print(OBBjectEuroShortTermRate.to_json())

# convert the object into a dict
ob_bject_euro_short_term_rate_dict = ob_bject_euro_short_term_rate_instance.to_dict()
# create an instance of OBBjectEuroShortTermRate from a dict
ob_bject_euro_short_term_rate_from_dict = OBBjectEuroShortTermRate.from_dict(ob_bject_euro_short_term_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


