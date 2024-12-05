# IntrinioHistoricalDividendsData

Intrinio Historical Dividends Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_dividend_date** | **date** | The ex-dividend date - the date on which the stock begins trading without rights to the dividend. | 
**amount** | **float** | The dividend amount per share. | 
**factor** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**split_ratio** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.intrinio_historical_dividends_data import IntrinioHistoricalDividendsData

# TODO update the JSON string below
json = "{}"
# create an instance of IntrinioHistoricalDividendsData from a JSON string
intrinio_historical_dividends_data_instance = IntrinioHistoricalDividendsData.from_json(json)
# print the JSON string representation of the object
print(IntrinioHistoricalDividendsData.to_json())

# convert the object into a dict
intrinio_historical_dividends_data_dict = intrinio_historical_dividends_data_instance.to_dict()
# create an instance of IntrinioHistoricalDividendsData from a dict
intrinio_historical_dividends_data_from_dict = IntrinioHistoricalDividendsData.from_dict(intrinio_historical_dividends_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


