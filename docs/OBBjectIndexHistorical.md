# OBBjectIndexHistorical

OBBject with results of type IndexHistorical

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectIndexHistoricalResultsInner]**](OBBjectIndexHistoricalResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_index_historical import OBBjectIndexHistorical

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectIndexHistorical from a JSON string
ob_bject_index_historical_instance = OBBjectIndexHistorical.from_json(json)
# print the JSON string representation of the object
print(OBBjectIndexHistorical.to_json())

# convert the object into a dict
ob_bject_index_historical_dict = ob_bject_index_historical_instance.to_dict()
# create an instance of OBBjectIndexHistorical from a dict
ob_bject_index_historical_from_dict = OBBjectIndexHistorical.from_dict(ob_bject_index_historical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


