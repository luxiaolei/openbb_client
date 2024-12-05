# OECDImmediateInterestRateData

OECD Immediate Interest Rate Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**country** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openbb_client.models.oecd_immediate_interest_rate_data import OECDImmediateInterestRateData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDImmediateInterestRateData from a JSON string
oecd_immediate_interest_rate_data_instance = OECDImmediateInterestRateData.from_json(json)
# print the JSON string representation of the object
print(OECDImmediateInterestRateData.to_json())

# convert the object into a dict
oecd_immediate_interest_rate_data_dict = oecd_immediate_interest_rate_data_instance.to_dict()
# create an instance of OECDImmediateInterestRateData from a dict
oecd_immediate_interest_rate_data_from_dict = OECDImmediateInterestRateData.from_dict(oecd_immediate_interest_rate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


