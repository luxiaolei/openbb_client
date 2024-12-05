# OBBjectHistoricalEps

OBBject with results of type HistoricalEps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FMPHistoricalEpsData]**](FMPHistoricalEpsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_historical_eps import OBBjectHistoricalEps

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalEps from a JSON string
ob_bject_historical_eps_instance = OBBjectHistoricalEps.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalEps.to_json())

# convert the object into a dict
ob_bject_historical_eps_dict = ob_bject_historical_eps_instance.to_dict()
# create an instance of OBBjectHistoricalEps from a dict
ob_bject_historical_eps_from_dict = OBBjectHistoricalEps.from_dict(ob_bject_historical_eps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


