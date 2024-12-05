# OBBjectOptionsSnapshots

OBBject with results of type OptionsSnapshots

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[IntrinioOptionsSnapshotsData]**](IntrinioOptionsSnapshotsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_options_snapshots import OBBjectOptionsSnapshots

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOptionsSnapshots from a JSON string
ob_bject_options_snapshots_instance = OBBjectOptionsSnapshots.from_json(json)
# print the JSON string representation of the object
print(OBBjectOptionsSnapshots.to_json())

# convert the object into a dict
ob_bject_options_snapshots_dict = ob_bject_options_snapshots_instance.to_dict()
# create an instance of OBBjectOptionsSnapshots from a dict
ob_bject_options_snapshots_from_dict = OBBjectOptionsSnapshots.from_dict(ob_bject_options_snapshots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


