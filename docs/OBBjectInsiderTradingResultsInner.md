# OBBjectInsiderTradingResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**company_cik** | [**CompanyCik**](CompanyCik.md) |  | [optional] 
**filing_date** | [**FilingDate**](FilingDate.md) |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**owner_cik** | [**OwnerCik**](OwnerCik.md) |  | [optional] 
**owner_name** | **str** |  | [optional] 
**owner_title** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**acquisition_or_disposition** | **str** |  | [optional] 
**security_type** | **str** |  | [optional] 
**securities_owned** | **float** |  | [optional] 
**securities_transacted** | **float** |  | [optional] 
**transaction_price** | **float** |  | [optional] 
**filing_url** | **str** |  | [optional] 
**company_name** | **str** |  | 
**conversion_exercise_price** | **float** |  | [optional] 
**deemed_execution_date** | **date** |  | [optional] 
**exercise_date** | **date** |  | [optional] 
**expiration_date** | **date** |  | [optional] 
**underlying_security_title** | **str** |  | [optional] 
**underlying_shares** | [**UnderlyingShares**](UnderlyingShares.md) |  | [optional] 
**nature_of_ownership** | **str** |  | [optional] 
**director** | **bool** |  | [optional] 
**officer** | **bool** |  | [optional] 
**ten_percent_owner** | **bool** |  | [optional] 
**other_relation** | **bool** |  | [optional] 
**derivative_transaction** | **bool** |  | [optional] 
**report_line_number** | **int** |  | [optional] 
**form** | [**Form**](Form.md) |  | [optional] 
**other** | **bool** |  | [optional] 
**other_text** | **str** |  | [optional] 
**transaction_timeliness** | **str** |  | [optional] 
**ownership_type** | **str** |  | [optional] 
**underlying_security_shares** | **float** |  | [optional] 
**underlying_security_value** | **float** |  | [optional] 
**transaction_value** | **float** |  | [optional] 
**value_owned** | **float** |  | [optional] 
**footnote** | **str** |  | [optional] 
**form_type** | **str** | Form type of the insider trading. | 

## Example

```python
from openbb_client.models.ob_bject_insider_trading_results_inner import OBBjectInsiderTradingResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectInsiderTradingResultsInner from a JSON string
ob_bject_insider_trading_results_inner_instance = OBBjectInsiderTradingResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectInsiderTradingResultsInner.to_json())

# convert the object into a dict
ob_bject_insider_trading_results_inner_dict = ob_bject_insider_trading_results_inner_instance.to_dict()
# create an instance of OBBjectInsiderTradingResultsInner from a dict
ob_bject_insider_trading_results_inner_from_dict = OBBjectInsiderTradingResultsInner.from_dict(ob_bject_insider_trading_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


