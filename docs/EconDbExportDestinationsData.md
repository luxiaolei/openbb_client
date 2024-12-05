# EconDbExportDestinationsData

EconDB Export Destinations Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_country** | **str** | The country of origin. | 
**destination_country** | **str** | The destination country. | 
**value** | [**Value1**](Value1.md) |  | 
**units** | **str** | The units of measurement for the value. | 
**title** | **str** | The title of the data. | 
**footnote** | **str** |  | 

## Example

```python
from openbb_client.models.econ_db_export_destinations_data import EconDbExportDestinationsData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbExportDestinationsData from a JSON string
econ_db_export_destinations_data_instance = EconDbExportDestinationsData.from_json(json)
# print the JSON string representation of the object
print(EconDbExportDestinationsData.to_json())

# convert the object into a dict
econ_db_export_destinations_data_dict = econ_db_export_destinations_data_instance.to_dict()
# create an instance of EconDbExportDestinationsData from a dict
econ_db_export_destinations_data_from_dict = EconDbExportDestinationsData.from_dict(econ_db_export_destinations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


