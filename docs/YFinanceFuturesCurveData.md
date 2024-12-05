# YFinanceFuturesCurveData

Yahoo Finance Futures Curve Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**expiration** | **str** | Futures expiration month. | 
**price** | **float** | The price of the futures contract. | [optional] 

## Example

```python
from openbb_client.models.y_finance_futures_curve_data import YFinanceFuturesCurveData

# TODO update the JSON string below
json = "{}"
# create an instance of YFinanceFuturesCurveData from a JSON string
y_finance_futures_curve_data_instance = YFinanceFuturesCurveData.from_json(json)
# print the JSON string representation of the object
print(YFinanceFuturesCurveData.to_json())

# convert the object into a dict
y_finance_futures_curve_data_dict = y_finance_futures_curve_data_instance.to_dict()
# create an instance of YFinanceFuturesCurveData from a dict
y_finance_futures_curve_data_from_dict = YFinanceFuturesCurveData.from_dict(y_finance_futures_curve_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


