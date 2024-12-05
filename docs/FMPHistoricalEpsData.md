# FMPHistoricalEpsData

FMP Historical EPS Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | [optional] 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**announce_time** | **str** |  | [optional] 
**eps_actual** | **float** |  | [optional] 
**eps_estimated** | **float** |  | [optional] 
**revenue_estimated** | **float** |  | [optional] 
**revenue_actual** | **float** |  | [optional] 
**reporting_time** | **str** |  | [optional] 
**updated_at** | **date** |  | [optional] 
**period_ending** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_historical_eps_data import FMPHistoricalEpsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPHistoricalEpsData from a JSON string
fmp_historical_eps_data_instance = FMPHistoricalEpsData.from_json(json)
# print the JSON string representation of the object
print(FMPHistoricalEpsData.to_json())

# convert the object into a dict
fmp_historical_eps_data_dict = fmp_historical_eps_data_instance.to_dict()
# create an instance of FMPHistoricalEpsData from a dict
fmp_historical_eps_data_from_dict = FMPHistoricalEpsData.from_dict(fmp_historical_eps_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


