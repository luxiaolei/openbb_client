# FREDSpotRateData

FRED Spot Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fred_spot_rate_data import FREDSpotRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDSpotRateData from a JSON string
fred_spot_rate_data_instance = FREDSpotRateData.from_json(json)
# print the JSON string representation of the object
print(FREDSpotRateData.to_json())

# convert the object into a dict
fred_spot_rate_data_dict = fred_spot_rate_data_instance.to_dict()
# create an instance of FREDSpotRateData from a dict
fred_spot_rate_data_from_dict = FREDSpotRateData.from_dict(fred_spot_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


