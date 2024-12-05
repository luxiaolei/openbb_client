# OECDGdpForecastData

OECD GDP Forecast Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** |  | 
**value** | [**Value8**](Value8.md) |  | 

## Example

```python
from openbb_client.models.oecd_gdp_forecast_data import OECDGdpForecastData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDGdpForecastData from a JSON string
oecd_gdp_forecast_data_instance = OECDGdpForecastData.from_json(json)
# print the JSON string representation of the object
print(OECDGdpForecastData.to_json())

# convert the object into a dict
oecd_gdp_forecast_data_dict = oecd_gdp_forecast_data_instance.to_dict()
# create an instance of OECDGdpForecastData from a dict
oecd_gdp_forecast_data_from_dict = OECDGdpForecastData.from_dict(oecd_gdp_forecast_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


