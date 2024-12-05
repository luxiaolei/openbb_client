# FMPEtfSectorsData

FMP ETF Sectors Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sector** | **str** | Sector of exposure. | 
**weight** | **float** |  | 

## Example

```python
from openbb_client.models.fmp_etf_sectors_data import FMPEtfSectorsData

# TODO update the JSON string below
json = "{}"
# create an instance of FMPEtfSectorsData from a JSON string
fmp_etf_sectors_data_instance = FMPEtfSectorsData.from_json(json)
# print the JSON string representation of the object
print(FMPEtfSectorsData.to_json())

# convert the object into a dict
fmp_etf_sectors_data_dict = fmp_etf_sectors_data_instance.to_dict()
# create an instance of FMPEtfSectorsData from a dict
fmp_etf_sectors_data_from_dict = FMPEtfSectorsData.from_dict(fmp_etf_sectors_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


