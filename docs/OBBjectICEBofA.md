# OBBjectICEBofA

OBBject with results of type ICEBofA

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**results** | [**List[FREDICEBofAData]**](FREDICEBofAData.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**chart** | [**Chart**](Chart.md) |  | [optional] 
**extra** | **object** | Extra info. | [optional] 

## Example

```python
from openbb_client.models.ob_bject_ice_bof_a import OBBjectICEBofA

# TODO update the JSON string below
json = "{}"
# create an instance of OBBjectICEBofA from a JSON string
ob_bject_ice_bof_a_instance = OBBjectICEBofA.from_json(json)
# print the JSON string representation of the object
print(OBBjectICEBofA.to_json())

# convert the object into a dict
ob_bject_ice_bof_a_dict = ob_bject_ice_bof_a_instance.to_dict()
# create an instance of OBBjectICEBofA from a dict
ob_bject_ice_bof_a_from_dict = OBBjectICEBofA.from_dict(ob_bject_ice_bof_a_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


