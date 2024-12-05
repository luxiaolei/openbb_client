# FredOvernightBankFundingRateData

Fred Overnight Bank Funding Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** | Overnight Bank Funding Rate. | 
**percentile_1** | **float** |  | [optional] 
**percentile_25** | **float** |  | [optional] 
**percentile_75** | **float** |  | [optional] 
**percentile_99** | **float** |  | [optional] 
**volume** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.fred_overnight_bank_funding_rate_data import FredOvernightBankFundingRateData

# TODO update the JSON string below
json = "{}"
# create an instance of FredOvernightBankFundingRateData from a JSON string
fred_overnight_bank_funding_rate_data_instance = FredOvernightBankFundingRateData.from_json(json)
# print the JSON string representation of the object
print(FredOvernightBankFundingRateData.to_json())

# convert the object into a dict
fred_overnight_bank_funding_rate_data_dict = fred_overnight_bank_funding_rate_data_instance.to_dict()
# create an instance of FredOvernightBankFundingRateData from a dict
fred_overnight_bank_funding_rate_data_from_dict = FredOvernightBankFundingRateData.from_dict(fred_overnight_bank_funding_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


