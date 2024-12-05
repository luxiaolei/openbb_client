# FMPInstitutionalOwnershipData

FMP Institutional Ownership Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**cik** | **str** |  | [optional] 
**var_date** | **date** | The date of the data. | 
**investors_holding** | **int** | Number of investors holding the stock. | 
**last_investors_holding** | **int** | Number of investors holding the stock in the last quarter. | 
**investors_holding_change** | **int** | Change in the number of investors holding the stock. | 
**number_of_13f_shares** | **int** | Number of 13F shares. | [optional] 
**last_number_of_13f_shares** | **int** | Number of 13F shares in the last quarter. | [optional] 
**number_of_13f_shares_change** | **int** | Change in the number of 13F shares. | [optional] 
**total_invested** | **float** | Total amount invested. | 
**last_total_invested** | **float** | Total amount invested in the last quarter. | 
**total_invested_change** | **float** | Change in the total amount invested. | 
**ownership_percent** | **float** | Ownership percent. | 
**last_ownership_percent** | **float** | Ownership percent in the last quarter. | 
**ownership_percent_change** | **float** | Change in the ownership percent. | 
**new_positions** | **int** | Number of new positions. | 
**last_new_positions** | **int** | Number of new positions in the last quarter. | 
**new_positions_change** | **int** | Change in the number of new positions. | 
**increased_positions** | **int** | Number of increased positions. | 
**last_increased_positions** | **int** | Number of increased positions in the last quarter. | 
**increased_positions_change** | **int** | Change in the number of increased positions. | 
**closed_positions** | **int** | Number of closed positions. | 
**last_closed_positions** | **int** | Number of closed positions in the last quarter. | 
**closed_positions_change** | **int** | Change in the number of closed positions. | 
**reduced_positions** | **int** | Number of reduced positions. | 
**last_reduced_positions** | **int** | Number of reduced positions in the last quarter. | 
**reduced_positions_change** | **int** | Change in the number of reduced positions. | 
**total_calls** | **int** | Total number of call options contracts traded for Apple Inc. on the specified date. | 
**last_total_calls** | **int** | Total number of call options contracts traded for Apple Inc. on the previous reporting date. | 
**total_calls_change** | **int** | Change in the total number of call options contracts traded between the current and previous reporting dates. | 
**total_puts** | **int** | Total number of put options contracts traded for Apple Inc. on the specified date. | 
**last_total_puts** | **int** | Total number of put options contracts traded for Apple Inc. on the previous reporting date. | 
**total_puts_change** | **int** | Change in the total number of put options contracts traded between the current and previous reporting dates. | 
**put_call_ratio** | **float** | Put-call ratio, which is the ratio of the total number of put options to call options traded on the specified date. | 
**last_put_call_ratio** | **float** | Put-call ratio on the previous reporting date. | 
**put_call_ratio_change** | **float** | Change in the put-call ratio between the current and previous reporting dates. | 

## Example

```python
from openbb_client.models.fmp_institutional_ownership_data import FMPInstitutionalOwnershipData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPInstitutionalOwnershipData from a JSON string
fmp_institutional_ownership_data_instance = FMPInstitutionalOwnershipData.from_json(json)
# print the JSON string representation of the object
print(FMPInstitutionalOwnershipData.to_json())

# convert the object into a dict
fmp_institutional_ownership_data_dict = fmp_institutional_ownership_data_instance.to_dict()
# create an instance of FMPInstitutionalOwnershipData from a dict
fmp_institutional_ownership_data_from_dict = FMPInstitutionalOwnershipData.from_dict(fmp_institutional_ownership_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


