# EconDbGdpNominalData

EconDB GDP Nominal Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the GDP value. | [optional] 
**value** | [**Value2**](Value2.md) |  | 
**nominal_growth_qoq** | **float** | Nominal GDP growth rate quarter over quarter. | 
**nominal_growth_yoy** | **float** | Nominal GDP growth rate year over year. | 

## Example

```python
from openbb_client.models.econ_db_gdp_nominal_data import EconDbGdpNominalData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbGdpNominalData from a JSON string
econ_db_gdp_nominal_data_instance = EconDbGdpNominalData.from_json(json)
# print the JSON string representation of the object
print(EconDbGdpNominalData.to_json())

# convert the object into a dict
econ_db_gdp_nominal_data_dict = econ_db_gdp_nominal_data_instance.to_dict()
# create an instance of EconDbGdpNominalData from a dict
econ_db_gdp_nominal_data_from_dict = EconDbGdpNominalData.from_dict(econ_db_gdp_nominal_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


