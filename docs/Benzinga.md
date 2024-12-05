# Benzinga

Records last Updated Unix timestamp (UTC). This will force the sort order to be Greater Than or Equal to the timestamp indicated. The date can be a date string or a Unix timestamp. The date string must be in the format of YYYY-MM-DD. (provider: benzinga)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openbb_client.models.benzinga import Benzinga

# TODO update the JSON string below
json = "{}"
# create an instance of Benzinga from a JSON string
benzinga_instance = Benzinga.from_json(json)
# print the JSON string representation of the object
print(Benzinga.to_json())

# convert the object into a dict
benzinga_dict = benzinga_instance.to_dict()
# create an instance of Benzinga from a dict
benzinga_from_dict = Benzinga.from_dict(benzinga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


