# OBBjectHistoricalDividendsResultsInner


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
**factor** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**split_ratio** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.ob_bject_historical_dividends_results_inner import OBBjectHistoricalDividendsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectHistoricalDividendsResultsInner from a JSON string
ob_bject_historical_dividends_results_inner_instance = OBBjectHistoricalDividendsResultsInner.from_json(json)
# print the JSON string representation of the object
print(OBBjectHistoricalDividendsResultsInner.to_json())

# convert the object into a dict
ob_bject_historical_dividends_results_inner_dict = ob_bject_historical_dividends_results_inner_instance.to_dict()
# create an instance of OBBjectHistoricalDividendsResultsInner from a dict
ob_bject_historical_dividends_results_inner_from_dict = OBBjectHistoricalDividendsResultsInner.from_dict(ob_bject_historical_dividends_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


