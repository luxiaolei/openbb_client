# FredFederalFundsRateData

FRED Federal Funds Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Effective federal funds rate. | 
**target_range_upper** | **float** |  | [optional] 
**target_range_lower** | **float** |  | [optional] 
**percentile_1** | **float** |  | [optional] 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 
**percentile_99** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_federal_funds_rate_data import FredFederalFundsRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FredFederalFundsRateData from a JSON string
fred_federal_funds_rate_data_instance = FredFederalFundsRateData.from_json(json)
# print the JSON string representation of the object
print(FredFederalFundsRateData.to_json())

# convert the object into a dict
fred_federal_funds_rate_data_dict = fred_federal_funds_rate_data_instance.to_dict()
# create an instance of FredFederalFundsRateData from a dict
fred_federal_funds_rate_data_from_dict = FredFederalFundsRateData.from_dict(fred_federal_funds_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


