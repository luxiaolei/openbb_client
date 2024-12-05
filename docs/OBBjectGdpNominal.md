# OBBjectGdpNominal

OBBject with results of type GdpNominal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OBBjectGdpNominalResultsInner]**](OBBjectGdpNominalResultsInner.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_gdp_nominal import OBBjectGdpNominal

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectGdpNominal from a JSON string
ob_bject_gdp_nominal_instance = OBBjectGdpNominal.from_json(json)
# print the JSON string representation of the object
print(OBBjectGdpNominal.to_json())

# convert the object into a dict
ob_bject_gdp_nominal_dict = ob_bject_gdp_nominal_instance.to_dict()
# create an instance of OBBjectGdpNominal from a dict
ob_bject_gdp_nominal_from_dict = OBBjectGdpNominal.from_dict(ob_bject_gdp_nominal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


