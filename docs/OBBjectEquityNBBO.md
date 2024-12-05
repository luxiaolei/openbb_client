# OBBjectEquityNBBO

OBBject with results of type EquityNBBO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[PolygonEquityNBBOData]**](PolygonEquityNBBOData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_equity_nbbo import OBBjectEquityNBBO

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEquityNBBO from a JSON string
ob_bject_equity_nbbo_instance = OBBjectEquityNBBO.from_json(json)
# print the JSON string representation of the object
print(OBBjectEquityNBBO.to_json())

# convert the object into a dict
ob_bject_equity_nbbo_dict = ob_bject_equity_nbbo_instance.to_dict()
# create an instance of OBBjectEquityNBBO from a dict
ob_bject_equity_nbbo_from_dict = OBBjectEquityNBBO.from_dict(ob_bject_equity_nbbo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


