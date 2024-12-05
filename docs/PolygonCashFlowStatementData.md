# PolygonCashFlowStatementData

Polygon Cash Flow Statement Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_ending** | **date** | The end date of the reporting period. | 
**fiscal_period** | **str** |  | [optional] 
**fiscal_year** | **int** |  | [optional] 
**net_cash_flow_from_operating_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_operating_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_operating_activities** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_investing_activities** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities_continuing** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities_discontinued** | **float** |  | [optional] 
**net_cash_flow_from_financing_activities** | **float** |  | [optional] 
**net_cash_flow_continuing** | **float** |  | [optional] 
**net_cash_flow_discontinued** | **float** |  | [optional] 
**exchange_gains_losses** | **float** |  | [optional] 
**net_cash_flow** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.polygon_cash_flow_statement_data import PolygonCashFlowStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonCashFlowStatementData from a JSON string
polygon_cash_flow_statement_data_instance = PolygonCashFlowStatementData.from_json(json)
# print the JSON string representation of the object
print(PolygonCashFlowStatementData.to_json())

# convert the object into a dict
polygon_cash_flow_statement_data_dict = polygon_cash_flow_statement_data_instance.to_dict()
# create an instance of PolygonCashFlowStatementData from a dict
polygon_cash_flow_statement_data_from_dict = PolygonCashFlowStatementData.from_dict(polygon_cash_flow_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


