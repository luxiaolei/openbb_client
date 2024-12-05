# FMPInsiderTradingData

FMP Insider Trading Data.

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
**form_type** | **str** | Form type of the insider trading. | 

## Example

```python
from openbb_client.models.fmp_insider_trading_data import FMPInsiderTradingData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPInsiderTradingData from a JSON string
fmp_insider_trading_data_instance = FMPInsiderTradingData.from_json(json)
# print the JSON string representation of the object
print(FMPInsiderTradingData.to_json())

# convert the object into a dict
fmp_insider_trading_data_dict = fmp_insider_trading_data_instance.to_dict()
# create an instance of FMPInsiderTradingData from a dict
fmp_insider_trading_data_from_dict = FMPInsiderTradingData.from_dict(fmp_insider_trading_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


