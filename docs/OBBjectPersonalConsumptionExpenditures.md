# OBBjectPersonalConsumptionExpenditures

OBBject with results of type PersonalConsumptionExpenditures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredPersonalConsumptionExpendituresData]**](FredPersonalConsumptionExpendituresData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_personal_consumption_expenditures import OBBjectPersonalConsumptionExpenditures

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPersonalConsumptionExpenditures from a JSON string
ob_bject_personal_consumption_expenditures_instance = OBBjectPersonalConsumptionExpenditures.from_json(json)
# print the JSON string representation of the object
print(OBBjectPersonalConsumptionExpenditures.to_json())

# convert the object into a dict
ob_bject_personal_consumption_expenditures_dict = ob_bject_personal_consumption_expenditures_instance.to_dict()
# create an instance of OBBjectPersonalConsumptionExpenditures from a dict
ob_bject_personal_consumption_expenditures_from_dict = OBBjectPersonalConsumptionExpenditures.from_dict(ob_bject_personal_consumption_expenditures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


