# FMPEquityOwnershipData

FMP Equity Ownership Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**cik** | **int** | Central Index Key (CIK) for the requested entity. | 
**filing_date** | **date** | Filing date of the stock ownership. | 
**investor_name** | **str** | Investor name of the stock ownership. | 
**symbol** | **str** | Symbol representing the entity requested in the data. | 
**security_name** | **str** | Security name of the stock ownership. | 
**type_of_security** | **str** | Type of security of the stock ownership. | 
**security_cusip** | **str** | Security cusip of the stock ownership. | 
**shares_type** | **str** | Shares type of the stock ownership. | 
**put_call_share** | **str** | Put call share of the stock ownership. | 
**investment_discretion** | **str** | Investment discretion of the stock ownership. | 
**industry_title** | **str** | Industry title of the stock ownership. | 
**weight** | **float** | Weight of the stock ownership. | 
**last_weight** | **float** | Last weight of the stock ownership. | 
**change_in_weight** | **float** | Change in weight of the stock ownership. | 
**change_in_weight_percentage** | **float** | Change in weight percentage of the stock ownership. | 
**market_value** | **int** | Market value of the stock ownership. | 
**last_market_value** | **int** | Last market value of the stock ownership. | 
**change_in_market_value** | **int** | Change in market value of the stock ownership. | 
**change_in_market_value_percentage** | **float** | Change in market value percentage of the stock ownership. | 
**shares_number** | **int** | Shares number of the stock ownership. | 
**last_shares_number** | **int** | Last shares number of the stock ownership. | 
**change_in_shares_number** | **float** | Change in shares number of the stock ownership. | 
**change_in_shares_number_percentage** | **float** | Change in shares number percentage of the stock ownership. | 
**quarter_end_price** | **float** | Quarter end price of the stock ownership. | 
**avg_price_paid** | **float** | Average price paid of the stock ownership. | 
**is_new** | **bool** | Is the stock ownership new. | 
**is_sold_out** | **bool** | Is the stock ownership sold out. | 
**ownership** | **float** | How much is the ownership. | 
**last_ownership** | **float** | Last ownership amount. | 
**change_in_ownership** | **float** | Change in ownership amount. | 
**change_in_ownership_percentage** | **float** | Change in ownership percentage. | 
**holding_period** | **int** | Holding period of the stock ownership. | 
**first_added** | **date** | First added date of the stock ownership. | 
**performance** | **float** | Performance of the stock ownership. | 
**performance_percentage** | **float** | Performance percentage of the stock ownership. | 
**last_performance** | **float** | Last performance of the stock ownership. | 
**change_in_performance** | **float** | Change in performance of the stock ownership. | 
**is_counted_for_performance** | **bool** | Is the stock ownership counted for performance. | 

## Example

```python
from openbb_client.models.fmp_equity_ownership_data import FMPEquityOwnershipData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEquityOwnershipData from a JSON string
fmp_equity_ownership_data_instance = FMPEquityOwnershipData.from_json(json)
# print the JSON string representation of the object
print(FMPEquityOwnershipData.to_json())

# convert the object into a dict
fmp_equity_ownership_data_dict = fmp_equity_ownership_data_instance.to_dict()
# create an instance of FMPEquityOwnershipData from a dict
fmp_equity_ownership_data_from_dict = FMPEquityOwnershipData.from_dict(fmp_equity_ownership_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


