# FmpIntrinio2

The exchange code the ETF trades on. (provider: fmp);     Target a specific exchange by providing the MIC code. (provider: intrinio)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.fmp_intrinio2 import FmpIntrinio2

# TODO update the JSON string below
json = "{}"
# create an instance of FmpIntrinio2 from a JSON string
fmp_intrinio2_instance = FmpIntrinio2.from_json(json)
# print the JSON string representation of the object
print(FmpIntrinio2.to_json())

# convert the object into a dict
fmp_intrinio2_dict = fmp_intrinio2_instance.to_dict()
# create an instance of FmpIntrinio2 from a dict
fmp_intrinio2_from_dict = FmpIntrinio2.from_dict(fmp_intrinio2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


