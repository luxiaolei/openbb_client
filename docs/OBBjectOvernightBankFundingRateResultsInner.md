# OBBjectOvernightBankFundingRateResultsInner


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
**revision_indicator** | **str** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_overnight_bank_funding_rate_results_inner import OBBjectOvernightBankFundingRateResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectOvernightBankFundingRateResultsInner from a JSON string
ob_bject_overnight_bank_funding_rate_results_inner_instance = OBBjectOvernightBankFundingRateResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectOvernightBankFundingRateResultsInner.to_json())

# convert the object into a dict
ob_bject_overnight_bank_funding_rate_results_inner_dict = ob_bject_overnight_bank_funding_rate_results_inner_instance.to_dict()
# create an instance of OBBjectOvernightBankFundingRateResultsInner from a dict
ob_bject_overnight_bank_funding_rate_results_inner_from_dict = OBBjectOvernightBankFundingRateResultsInner.from_dict(ob_bject_overnight_bank_funding_rate_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


