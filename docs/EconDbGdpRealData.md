# EconDbGdpRealData

EconDB GDP Real Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date of the data. | 
**country** | **str** | The country represented by the GDP value. | [optional] 
**value** | [**Value3**](Value3.md) |  | 
**real_growth_qoq** | **float** | Real GDP growth rate quarter over quarter. | 
**real_growth_yoy** | **float** | Real GDP growth rate year over year. | 

## Example

```python
from openbb_client.models.econ_db_gdp_real_data import EconDbGdpRealData

# TODO update the JSON string below
json = "{}"
# create an instance of EconDbGdpRealData from a JSON string
econ_db_gdp_real_data_instance = EconDbGdpRealData.from_json(json)
# print the JSON string representation of the object
print(EconDbGdpRealData.to_json())

# convert the object into a dict
econ_db_gdp_real_data_dict = econ_db_gdp_real_data_instance.to_dict()
# create an instance of EconDbGdpRealData from a dict
econ_db_gdp_real_data_from_dict = EconDbGdpRealData.from_dict(econ_db_gdp_real_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


