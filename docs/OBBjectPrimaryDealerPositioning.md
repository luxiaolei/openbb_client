# OBBjectPrimaryDealerPositioning

OBBject with results of type PrimaryDealerPositioning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FederalReservePrimaryDealerPositioningData]**](FederalReservePrimaryDealerPositioningData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_primary_dealer_positioning import OBBjectPrimaryDealerPositioning

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectPrimaryDealerPositioning from a JSON string
ob_bject_primary_dealer_positioning_instance = OBBjectPrimaryDealerPositioning.from_json(json)
# print the JSON string representation of the object
print(OBBjectPrimaryDealerPositioning.to_json())

# convert the object into a dict
ob_bject_primary_dealer_positioning_dict = ob_bject_primary_dealer_positioning_instance.to_dict()
# create an instance of OBBjectPrimaryDealerPositioning from a dict
ob_bject_primary_dealer_positioning_from_dict = OBBjectPrimaryDealerPositioning.from_dict(ob_bject_primary_dealer_positioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


