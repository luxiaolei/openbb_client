# FederalReserveFederalFundsRateData

FederalReserve FED Data.

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
**intraday_low** | **float** |  | [optional] 
**intraday_high** | **float** |  | [optional] 
**standard_deviation** | **float** |  | [optional] 
**revision_indicator** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.federal_reserve_federal_funds_rate_data import FederalReserveFederalFundsRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalReserveFederalFundsRateData from a JSON string
federal_reserve_federal_funds_rate_data_instance = FederalReserveFederalFundsRateData.from_json(json)
# print the JSON string representation of the object
print(FederalReserveFederalFundsRateData.to_json())

# convert the object into a dict
federal_reserve_federal_funds_rate_data_dict = federal_reserve_federal_funds_rate_data_instance.to_dict()
# create an instance of FederalReserveFederalFundsRateData from a dict
federal_reserve_federal_funds_rate_data_from_dict = FederalReserveFederalFundsRateData.from_dict(federal_reserve_federal_funds_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


