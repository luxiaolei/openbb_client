# OBBjectPrimaryDealerFails

OBBject with results of type PrimaryDealerFails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FederalReservePrimaryDealerFailsData]**](FederalReservePrimaryDealerFailsData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_primary_dealer_fails import OBBjectPrimaryDealerFails

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPrimaryDealerFails from a JSON string
ob_bject_primary_dealer_fails_instance = OBBjectPrimaryDealerFails.from_json(json)
# print the JSON string representation of the object
print(OBBjectPrimaryDealerFails.to_json())

# convert the object into a dict
ob_bject_primary_dealer_fails_dict = ob_bject_primary_dealer_fails_instance.to_dict()
# create an instance of OBBjectPrimaryDealerFails from a dict
ob_bject_primary_dealer_fails_from_dict = OBBjectPrimaryDealerFails.from_dict(ob_bject_primary_dealer_fails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


