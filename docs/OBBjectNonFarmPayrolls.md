# OBBjectNonFarmPayrolls

OBBject with results of type NonFarmPayrolls

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FredNonFarmPayrollsData]**](FredNonFarmPayrollsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_non_farm_payrolls import OBBjectNonFarmPayrolls

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectNonFarmPayrolls from a JSON string
ob_bject_non_farm_payrolls_instance = OBBjectNonFarmPayrolls.from_json(json)
# print the JSON string representation of the object
print(OBBjectNonFarmPayrolls.to_json())

# convert the object into a dict
ob_bject_non_farm_payrolls_dict = ob_bject_non_farm_payrolls_instance.to_dict()
# create an instance of OBBjectNonFarmPayrolls from a dict
ob_bject_non_farm_payrolls_from_dict = OBBjectNonFarmPayrolls.from_dict(ob_bject_non_farm_payrolls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


