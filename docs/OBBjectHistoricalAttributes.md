# OBBjectHistoricalAttributes

OBBject with results of type HistoricalAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioHistoricalAttributesData]**](IntrinioHistoricalAttributesData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_historical_attributes import OBBjectHistoricalAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalAttributes from a JSON string
ob_bject_historical_attributes_instance = OBBjectHistoricalAttributes.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalAttributes.to_json())

# convert the object into a dict
ob_bject_historical_attributes_dict = ob_bject_historical_attributes_instance.to_dict()
# create an instance of OBBjectHistoricalAttributes from a dict
ob_bject_historical_attributes_from_dict = OBBjectHistoricalAttributes.from_dict(ob_bject_historical_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


