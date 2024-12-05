# FMPHistoricalDividendsData

FMP Historical Dividends Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_dividend_date** | **date** | The ex-dividend date - the date on which the stock begins trading without rights to the dividend. | 
**amount** | **float** | The dividend amount per share. | 
**label** | **str** | Label of the historical dividends. | 
**adj_dividend** | **float** | Adjusted dividend of the historical dividends. | 
**record_date** | **date** |  | [optional] 
**payment_date** | **date** |  | [optional] 
**declaration_date** | **date** |  | [optional] 

## Example

```python
from openbb_client.models.fmp_historical_dividends_data import FMPHistoricalDividendsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPHistoricalDividendsData from a JSON string
fmp_historical_dividends_data_instance = FMPHistoricalDividendsData.from_json(json)
# print the JSON string representation of the object
print(FMPHistoricalDividendsData.to_json())

# convert the object into a dict
fmp_historical_dividends_data_dict = fmp_historical_dividends_data_instance.to_dict()
# create an instance of FMPHistoricalDividendsData from a dict
fmp_historical_dividends_data_from_dict = FMPHistoricalDividendsData.from_dict(fmp_historical_dividends_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


