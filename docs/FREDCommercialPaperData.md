# FREDCommercialPaperData

FRED Commercial Paper Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**symbol** | **str** |  | [optional] 
**maturity** | **str** | Maturity length of the item. | 
**rate** | **float** | Interest rate. | 
**title** | **str** |  | [optional] 
**asset_type** | **str** | The category of asset. | 

## Example

```python
from openbb_client.models.fred_commercial_paper_data import FREDCommercialPaperData

# TODO update the JSON string below
json = "{}"
# create an instance of FREDCommercialPaperData from a JSON string
fred_commercial_paper_data_instance = FREDCommercialPaperData.from_json(json)
# print the JSON string representation of the object
print(FREDCommercialPaperData.to_json())

# convert the object into a dict
fred_commercial_paper_data_dict = fred_commercial_paper_data_instance.to_dict()
# create an instance of FREDCommercialPaperData from a dict
fred_commercial_paper_data_from_dict = FREDCommercialPaperData.from_dict(fred_commercial_paper_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


