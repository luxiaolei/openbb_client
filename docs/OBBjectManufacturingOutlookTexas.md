# OBBjectManufacturingOutlookTexas

OBBject with results of type ManufacturingOutlookTexas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredManufacturingOutlookTexasData]**](FredManufacturingOutlookTexasData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_manufacturing_outlook_texas import OBBjectManufacturingOutlookTexas

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectManufacturingOutlookTexas from a JSON string
ob_bject_manufacturing_outlook_texas_instance = OBBjectManufacturingOutlookTexas.from_json(json)
# print the JSON string representation of the object
print(OBBjectManufacturingOutlookTexas.to_json())

# convert the object into a dict
ob_bject_manufacturing_outlook_texas_dict = ob_bject_manufacturing_outlook_texas_instance.to_dict()
# create an instance of OBBjectManufacturingOutlookTexas from a dict
ob_bject_manufacturing_outlook_texas_from_dict = OBBjectManufacturingOutlookTexas.from_dict(ob_bject_manufacturing_outlook_texas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


