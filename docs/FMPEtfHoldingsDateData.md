# FMPEtfHoldingsDateData

FMP ETF Holdings Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 

## Example

```python
from openbb_client.models.fmp_etf_holdings_date_data import FMPEtfHoldingsDateData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfHoldingsDateData from a JSON string
fmp_etf_holdings_date_data_instance = FMPEtfHoldingsDateData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfHoldingsDateData.to_json())

# convert the object into a dict
fmp_etf_holdings_date_data_dict = fmp_etf_holdings_date_data_instance.to_dict()
# create an instance of FMPEtfHoldingsDateData from a dict
fmp_etf_holdings_date_data_from_dict = FMPEtfHoldingsDateData.from_dict(fmp_etf_holdings_date_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


