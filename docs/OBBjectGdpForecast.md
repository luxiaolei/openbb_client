# OBBjectGdpForecast

OBBject with results of type GdpForecast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[OECDGdpForecastData]**](OECDGdpForecastData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_gdp_forecast import OBBjectGdpForecast

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectGdpForecast from a JSON string
ob_bject_gdp_forecast_instance = OBBjectGdpForecast.from_json(json)
# print the JSON string representation of the object
print(OBBjectGdpForecast.to_json())

# convert the object into a dict
ob_bject_gdp_forecast_dict = ob_bject_gdp_forecast_instance.to_dict()
# create an instance of OBBjectGdpForecast from a dict
ob_bject_gdp_forecast_from_dict = OBBjectGdpForecast.from_dict(ob_bject_gdp_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


