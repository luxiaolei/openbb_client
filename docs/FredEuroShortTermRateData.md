# FredEuroShortTermRateData

FRED Euro Short Term Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Volume-weighted trimmed mean rate. | 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 
**transactions** | **int** |  | [optional] 
**number_of_banks** | **int** |  | [optional] 
**large_bank_share_of_volume** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_euro_short_term_rate_data import FredEuroShortTermRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FredEuroShortTermRateData from a JSON string
fred_euro_short_term_rate_data_instance = FredEuroShortTermRateData.from_json(json)
# print the JSON string representation of the object
print(FredEuroShortTermRateData.to_json())

# convert the object into a dict
fred_euro_short_term_rate_data_dict = fred_euro_short_term_rate_data_instance.to_dict()
# create an instance of FredEuroShortTermRateData from a dict
fred_euro_short_term_rate_data_from_dict = FredEuroShortTermRateData.from_dict(fred_euro_short_term_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


