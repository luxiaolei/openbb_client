# OBBjectEquityUndervaluedGrowth

OBBject with results of type EquityUndervaluedGrowth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFUndervaluedGrowthEquitiesData]**](YFUndervaluedGrowthEquitiesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_undervalued_growth import OBBjectEquityUndervaluedGrowth

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityUndervaluedGrowth from a JSON string
ob_bject_equity_undervalued_growth_instance = OBBjectEquityUndervaluedGrowth.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityUndervaluedGrowth.to_json())

# convert the object into a dict
ob_bject_equity_undervalued_growth_dict = ob_bject_equity_undervalued_growth_instance.to_dict()
# create an instance of OBBjectEquityUndervaluedGrowth from a dict
ob_bject_equity_undervalued_growth_from_dict = OBBjectEquityUndervaluedGrowth.from_dict(ob_bject_equity_undervalued_growth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


