# FredManufacturingOutlookTexasData

FRED Manufacturing Outlook - Texas - Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**topic** | **str** |  | [optional] 
**diffusion_index** | **float** |  | [optional] 
**percent_reporting_increase** | **float** |  | [optional] 
**percent_reporting_decrease** | **float** |  | [optional] 
**percent_reporting_no_change** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_manufacturing_outlook_texas_data import FredManufacturingOutlookTexasData

# TODO update the JSON string below
json = "{}"
# create an instance of FredManufacturingOutlookTexasData from a JSON string
fred_manufacturing_outlook_texas_data_instance = FredManufacturingOutlookTexasData.from_json(json)
# print the JSON string representation of the object
print(FredManufacturingOutlookTexasData.to_json())

# convert the object into a dict
fred_manufacturing_outlook_texas_data_dict = fred_manufacturing_outlook_texas_data_instance.to_dict()
# create an instance of FredManufacturingOutlookTexasData from a dict
fred_manufacturing_outlook_texas_data_from_dict = FredManufacturingOutlookTexasData.from_dict(fred_manufacturing_outlook_texas_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


