# OBBjectEtfHoldingsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**security_type** | **str** |  | [optional] 
**isin** | **str** |  | [optional] 
**ric** | **str** |  | [optional] 
**sedol** | **str** |  | [optional] 
**share_class_figi** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**maturity_date** | **date** |  | [optional] 
**contract_expiry_date** | **date** |  | [optional] 
**coupon** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**unit** | **str** |  | [optional] 
**units_per_share** | **float** |  | [optional] 
**face_value** | **float** |  | [optional] 
**derivatives_value** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**updated** | [**Updated**](Updated.md) |  | [optional] 
**lei** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**units** | [**Units1**](Units1.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**payoff_profile** | **str** |  | [optional] 
**asset_category** | **str** |  | [optional] 
**issuer_category** | **str** |  | [optional] 
**is_restricted** | **str** |  | [optional] 
**fair_value_level** | **int** |  | [optional] 
**is_cash_collateral** | **str** |  | [optional] 
**is_non_cash_collateral** | **str** |  | [optional] 
**is_loan_by_fund** | **str** |  | [optional] 
**cik** | **str** |  | [optional] 
**acceptance_datetime** | **str** |  | [optional] 
**other_id** | **str** |  | [optional] 
**loan_value** | **float** |  | [optional] 
**issuer_conditional** | **str** |  | [optional] 
**asset_conditional** | **str** |  | [optional] 
**coupon_kind** | **str** |  | [optional] 
**rate_type** | **str** |  | [optional] 
**annualized_return** | **float** |  | [optional] 
**is_default** | **str** |  | [optional] 
**in_arrears** | **str** |  | [optional] 
**is_paid_kind** | **str** |  | [optional] 
**derivative_category** | **str** |  | [optional] 
**counterparty** | **str** |  | [optional] 
**underlying_name** | **str** |  | [optional] 
**option_type** | **str** |  | [optional] 
**derivative_payoff** | **str** |  | [optional] 
**expiry_date** | **date** |  | [optional] 
**exercise_price** | **float** |  | [optional] 
**exercise_currency** | **str** |  | [optional] 
**shares_per_contract** | **float** |  | [optional] 
**delta** | [**Delta**](Delta.md) |  | [optional] 
**rate_type_rec** | **str** |  | [optional] 
**receive_currency** | **str** |  | [optional] 
**upfront_receive** | **float** |  | [optional] 
**floating_rate_index_rec** | **str** |  | [optional] 
**floating_rate_spread_rec** | **float** |  | [optional] 
**rate_tenor_rec** | **str** |  | [optional] 
**rate_tenor_unit_rec** | [**RateTenorUnitRec**](RateTenorUnitRec.md) |  | [optional] 
**reset_date_rec** | **str** |  | [optional] 
**reset_date_unit_rec** | [**ResetDateUnitRec**](ResetDateUnitRec.md) |  | [optional] 
**rate_type_pmnt** | **str** |  | [optional] 
**payment_currency** | **str** |  | [optional] 
**upfront_payment** | **float** |  | [optional] 
**floating_rate_index_pmnt** | **str** |  | [optional] 
**floating_rate_spread_pmnt** | **float** |  | [optional] 
**rate_tenor_pmnt** | **str** |  | [optional] 
**rate_tenor_unit_pmnt** | [**RateTenorUnitPmnt**](RateTenorUnitPmnt.md) |  | [optional] 
**reset_date_pmnt** | **str** |  | [optional] 
**reset_date_unit_pmnt** | [**ResetDateUnitPmnt**](ResetDateUnitPmnt.md) |  | [optional] 
**repo_type** | **str** |  | [optional] 
**is_cleared** | **str** |  | [optional] 
**is_tri_party** | **str** |  | [optional] 
**principal_amount** | **float** |  | [optional] 
**principal_currency** | **str** |  | [optional] 
**collateral_type** | **str** |  | [optional] 
**collateral_amount** | **float** |  | [optional] 
**collateral_currency** | **str** |  | [optional] 
**exchange_currency** | **str** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**currency_sold** | **str** |  | [optional] 
**currency_amount_sold** | **float** |  | [optional] 
**currency_bought** | **str** |  | [optional] 
**currency_amount_bought** | **float** |  | [optional] 
**notional_amount** | **float** |  | [optional] 
**notional_currency** | **str** |  | [optional] 
**unrealized_gain** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_etf_holdings_results_inner import OBBjectEtfHoldingsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectEtfHoldingsResultsInner from a JSON string
ob_bject_etf_holdings_results_inner_instance = OBBjectEtfHoldingsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectEtfHoldingsResultsInner.to_json())

# convert the object into a dict
ob_bject_etf_holdings_results_inner_dict = ob_bject_etf_holdings_results_inner_instance.to_dict()
# create an instance of OBBjectEtfHoldingsResultsInner from a dict
ob_bject_etf_holdings_results_inner_from_dict = OBBjectEtfHoldingsResultsInner.from_dict(ob_bject_etf_holdings_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


