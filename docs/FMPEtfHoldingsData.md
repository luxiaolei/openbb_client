# FMPEtfHoldingsData

FMP ETF Holdings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**lei** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**balance** | **int** |  | [optional] 
**units** | [**Units**](Units.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**payoff_profile** | **str** |  | [optional] 
**asset_category** | **str** |  | [optional] 
**issuer_category** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**is_restricted** | **str** |  | [optional] 
**fair_value_level** | **int** |  | [optional] 
**is_cash_collateral** | **str** |  | [optional] 
**is_non_cash_collateral** | **str** |  | [optional] 
**is_loan_by_fund** | **str** |  | [optional] 
**cik** | **str** |  | [optional] 
**acceptance_datetime** | **str** |  | [optional] 
**updated** | [**Updated**](Updated.md) |  | [optional] 

## Example

```python
from openbb_client.models.fmp_etf_holdings_data import FMPEtfHoldingsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfHoldingsData from a JSON string
fmp_etf_holdings_data_instance = FMPEtfHoldingsData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfHoldingsData.to_json())

# convert the object into a dict
fmp_etf_holdings_data_dict = fmp_etf_holdings_data_instance.to_dict()
# create an instance of FMPEtfHoldingsData from a dict
fmp_etf_holdings_data_from_dict = FMPEtfHoldingsData.from_dict(fmp_etf_holdings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


