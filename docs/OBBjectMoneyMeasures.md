# OBBjectMoneyMeasures

OBBject with results of type MoneyMeasures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FederalReserveMoneyMeasuresData]**](FederalReserveMoneyMeasuresData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_money_measures import OBBjectMoneyMeasures

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectMoneyMeasures from a JSON string
ob_bject_money_measures_instance = OBBjectMoneyMeasures.from_json(json)
# print the JSON string representation of the object
print(OBBjectMoneyMeasures.to_json())

# convert the object into a dict
ob_bject_money_measures_dict = ob_bject_money_measures_instance.to_dict()
# create an instance of OBBjectMoneyMeasures from a dict
ob_bject_money_measures_from_dict = OBBjectMoneyMeasures.from_dict(ob_bject_money_measures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


