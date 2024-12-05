# OBBjectTreasuryRatesResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**week_4** | **float** |  | [optional] 
**month_1** | **float** |  | [optional] 
**month_2** | **float** |  | [optional] 
**month_3** | **float** |  | [optional] 
**month_6** | **float** |  | [optional] 
**year_1** | **float** |  | [optional] 
**year_2** | **float** |  | [optional] 
**year_3** | **float** |  | [optional] 
**year_5** | **float** |  | [optional] 
**year_7** | **float** |  | [optional] 
**year_10** | **float** |  | [optional] 
**year_20** | **float** |  | [optional] 
**year_30** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_treasury_rates_results_inner import OBBjectTreasuryRatesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectTreasuryRatesResultsInner from a JSON string
ob_bject_treasury_rates_results_inner_instance = OBBjectTreasuryRatesResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectTreasuryRatesResultsInner.to_json())

# convert the object into a dict
ob_bject_treasury_rates_results_inner_dict = ob_bject_treasury_rates_results_inner_instance.to_dict()
# create an instance of OBBjectTreasuryRatesResultsInner from a dict
ob_bject_treasury_rates_results_inner_from_dict = OBBjectTreasuryRatesResultsInner.from_dict(ob_bject_treasury_rates_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


