# Sec

Lookup filings by Central Index Key (CIK) instead of by symbol. (provider: sec)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.sec import Sec

# TODO update the JSON string below
json = "{}"
# create an instance of Sec from a JSON string
sec_instance = Sec.from_json(json)
# print the JSON string representation of the object
print(Sec.to_json())

# convert the object into a dict
sec_dict = sec_instance.to_dict()
# create an instance of Sec from a dict
sec_from_dict = Sec.from_dict(sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


