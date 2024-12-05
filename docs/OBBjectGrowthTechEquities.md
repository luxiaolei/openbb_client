# OBBjectGrowthTechEquities

OBBject with results of type GrowthTechEquities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[YFGrowthTechEquitiesData]**](YFGrowthTechEquitiesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_growth_tech_equities import OBBjectGrowthTechEquities

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectGrowthTechEquities from a JSON string
ob_bject_growth_tech_equities_instance = OBBjectGrowthTechEquities.from_json(json)
# print the JSON string representation of the object
print(OBBjectGrowthTechEquities.to_json())

# convert the object into a dict
ob_bject_growth_tech_equities_dict = ob_bject_growth_tech_equities_instance.to_dict()
# create an instance of OBBjectGrowthTechEquities from a dict
ob_bject_growth_tech_equities_from_dict = OBBjectGrowthTechEquities.from_dict(ob_bject_growth_tech_equities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


