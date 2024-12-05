# EconDbPortVolumeData

EconDB Port Volume Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**port_code** | **str** |  | [optional] 
**port_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**export_dwell_time** | **float** |  | [optional] 
**import_dwell_time** | **float** |  | [optional] 
**import_teu** | **int** |  | [optional] 
**export_teu** | **int** |  | [optional] 

## Example

```python
from openbb_client.models.econ_db_port_volume_data import EconDbPortVolumeData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbPortVolumeData from a JSON string
econ_db_port_volume_data_instance = EconDbPortVolumeData.from_json(json)
# print the JSON string representation of the object
print(EconDbPortVolumeData.to_json())

# convert the object into a dict
econ_db_port_volume_data_dict = econ_db_port_volume_data_instance.to_dict()
# create an instance of EconDbPortVolumeData from a dict
econ_db_port_volume_data_from_dict = EconDbPortVolumeData.from_dict(econ_db_port_volume_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


