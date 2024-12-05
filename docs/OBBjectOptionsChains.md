# OBBjectOptionsChains

OBBject with results of type OptionsChains

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**OBBjectOptionsChainsResults**](OBBjectOptionsChainsResults.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_options_chains import OBBjectOptionsChains

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOptionsChains from a JSON string
ob_bject_options_chains_instance = OBBjectOptionsChains.from_json(json)
# print the JSON string representation of the object
print(OBBjectOptionsChains.to_json())

# convert the object into a dict
ob_bject_options_chains_dict = ob_bject_options_chains_instance.to_dict()
# create an instance of OBBjectOptionsChains from a dict
ob_bject_options_chains_from_dict = OBBjectOptionsChains.from_dict(ob_bject_options_chains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


