# FREDICEBofAData

FRED ICE BofA US Corporate Bond Indices Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**rate** | **float** |  | 

## Example

```python
from openbb_client.models.fredice_bof_a_data import FREDICEBofAData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDICEBofAData from a JSON string
fredice_bof_a_data_instance = FREDICEBofAData.from_json(json)
# print the JSON string representation of the object
print(FREDICEBofAData.to_json())

# convert the object into a dict
fredice_bof_a_data_dict = fredice_bof_a_data_instance.to_dict()
# create an instance of FREDICEBofAData from a dict
fredice_bof_a_data_from_dict = FREDICEBofAData.from_dict(fredice_bof_a_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


