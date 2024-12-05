# OECDCompositeLeadingIndicatorData

OECD Composite Leading Indicator Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**value** | **float** | CLI value | [optional] 
**country** | **str** | Country for the CLI value. | 

## Example

```python
from openbb_client.models.oecd_composite_leading_indicator_data import OECDCompositeLeadingIndicatorData

# TODO update the JSON string below
json = "{}"
# create an instance of OECDCompositeLeadingIndicatorData from a JSON string
oecd_composite_leading_indicator_data_instance = OECDCompositeLeadingIndicatorData.from_json(json)
# print the JSON string representation of the object
print(OECDCompositeLeadingIndicatorData.to_json())

# convert the object into a dict
oecd_composite_leading_indicator_data_dict = oecd_composite_leading_indicator_data_instance.to_dict()
# create an instance of OECDCompositeLeadingIndicatorData from a dict
oecd_composite_leading_indicator_data_from_dict = OECDCompositeLeadingIndicatorData.from_dict(oecd_composite_leading_indicator_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


