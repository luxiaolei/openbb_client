# openbb_client.CommodityApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commodity_petroleum_status_report**](CommodityApi.md#commodity_petroleum_status_report) | **GET** /api/v1/commodity/petroleum_status_report | Petroleum Status Report
[**commodity_price_spot**](CommodityApi.md#commodity_price_spot) | **GET** /api/v1/commodity/price/spot | Spot
[**commodity_short_term_energy_outlook**](CommodityApi.md#commodity_short_term_energy_outlook) | **GET** /api/v1/commodity/short_term_energy_outlook | Short Term Energy Outlook


# **commodity_petroleum_status_report**
> OBBjectPetroleumStatusReport commodity_petroleum_status_report(provider=provider, start_date=start_date, end_date=end_date, category=category, table=table, use_cache=use_cache)

Petroleum Status Report

EIA Weekly Petroleum Status Report.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_petroleum_status_report import OBBjectPetroleumStatusReport
from openbb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8005
# See configuration.py for a list of all supported configuration parameters.
configuration = openbb_client.Configuration(
    host = "http://127.0.0.1:8005"
)


# Enter a context with an instance of the API client
with openbb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openbb_client.CommodityApi(api_client)
    provider = eia # str |  (optional) (default to eia)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    category = balance_sheet # str | The group of data to be returned. The default is the balance sheet. (provider: eia) (optional) (default to balance_sheet)
    table = 'table_example' # str | The specific table element within the category to be returned, default is 'stocks', if the category is 'weekly_estimates', else 'all'.     Note: Choices represent all available tables from the entire collection and are not all available for every category.     Invalid choices will raise a ValidationError with a message indicating the valid choices for the selected category.     Choices are:         all         conventional_gas         crude         crude_production         crude_production_avg         diesel         ethanol_plant_production         ethanol_plant_production_avg         exports         exports_avg         heating_oil         imports         imports_avg         imports_by_country         imports_by_country_avg         inputs_and_utilization         inputs_and_utilization_avg         jet_fuel         monthly         net_imports_inc_spr_avg         net_imports_incl_spr         net_production         net_production_avg         net_production_by_product         net_production_by_production_avg         product_by_region         product_by_region_avg         product_supplied         product_supplied_avg         propane         rbob         refiner_blender_net_production         refiner_blender_net_production_avg         stocks         supply         supply_avg         ulta_low_sulfur_distillate_reclassification         ulta_low_sulfur_distillate_reclassification_avg         weekly     Multiple comma separated items allowed. (provider: eia) (optional)
    use_cache = True # bool | Subsequent requests for the same source data are cached for the session using ALRU cache. (provider: eia) (optional) (default to True)

    try:
        # Petroleum Status Report
        api_response = api_instance.commodity_petroleum_status_report(provider=provider, start_date=start_date, end_date=end_date, category=category, table=table, use_cache=use_cache)
        print("The response of CommodityApi->commodity_petroleum_status_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommodityApi->commodity_petroleum_status_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to eia]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **category** | **str**| The group of data to be returned. The default is the balance sheet. (provider: eia) | [optional] [default to balance_sheet]
 **table** | **str**| The specific table element within the category to be returned, default is &#39;stocks&#39;, if the category is &#39;weekly_estimates&#39;, else &#39;all&#39;.     Note: Choices represent all available tables from the entire collection and are not all available for every category.     Invalid choices will raise a ValidationError with a message indicating the valid choices for the selected category.     Choices are:         all         conventional_gas         crude         crude_production         crude_production_avg         diesel         ethanol_plant_production         ethanol_plant_production_avg         exports         exports_avg         heating_oil         imports         imports_avg         imports_by_country         imports_by_country_avg         inputs_and_utilization         inputs_and_utilization_avg         jet_fuel         monthly         net_imports_inc_spr_avg         net_imports_incl_spr         net_production         net_production_avg         net_production_by_product         net_production_by_production_avg         product_by_region         product_by_region_avg         product_supplied         product_supplied_avg         propane         rbob         refiner_blender_net_production         refiner_blender_net_production_avg         stocks         supply         supply_avg         ulta_low_sulfur_distillate_reclassification         ulta_low_sulfur_distillate_reclassification_avg         weekly     Multiple comma separated items allowed. (provider: eia) | [optional] 
 **use_cache** | **bool**| Subsequent requests for the same source data are cached for the session using ALRU cache. (provider: eia) | [optional] [default to True]

### Return type

[**OBBjectPetroleumStatusReport**](OBBjectPetroleumStatusReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**204** | Empty response |  -  |
**400** | No Results Found |  -  |
**500** | Internal Error |  -  |
**502** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commodity_price_spot**
> OBBjectCommoditySpotPrices commodity_price_spot(provider=provider, start_date=start_date, end_date=end_date, commodity=commodity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Spot

Commodity Spot Prices.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_commodity_spot_prices import OBBjectCommoditySpotPrices
from openbb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8005
# See configuration.py for a list of all supported configuration parameters.
configuration = openbb_client.Configuration(
    host = "http://127.0.0.1:8005"
)


# Enter a context with an instance of the API client
with openbb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openbb_client.CommodityApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    commodity = all # str | Commodity name associated with the EIA spot price commodity data, default is 'all'. (provider: fred) (optional) (default to all)
    frequency = 'frequency_example' # str | Frequency aggregation to convert high frequency data to lower frequency.         None = No change         a = Annual         q = Quarterly         m = Monthly         w = Weekly         d = Daily         wef = Weekly, Ending Friday         weth = Weekly, Ending Thursday         wew = Weekly, Ending Wednesday         wetu = Weekly, Ending Tuesday         wem = Weekly, Ending Monday         wesu = Weekly, Ending Sunday         wesa = Weekly, Ending Saturday         bwew = Biweekly, Ending Wednesday         bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = eop # str | A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg = Average         sum = Sum         eop = End of Period          (provider: fred) (optional) (default to eop)
    transform = 'transform_example' # str | Transformation type         None = No transformation         chg = Change         ch1 = Change from Year Ago         pch = Percent Change         pc1 = Percent Change from Year Ago         pca = Compounded Annual Rate of Change         cch = Continuously Compounded Rate of Change         cca = Continuously Compounded Annual Rate of Change         log = Natural Log          (provider: fred) (optional)

    try:
        # Spot
        api_response = api_instance.commodity_price_spot(provider=provider, start_date=start_date, end_date=end_date, commodity=commodity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of CommodityApi->commodity_price_spot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommodityApi->commodity_price_spot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **commodity** | **str**| Commodity name associated with the EIA spot price commodity data, default is &#39;all&#39;. (provider: fred) | [optional] [default to all]
 **frequency** | **str**| Frequency aggregation to convert high frequency data to lower frequency.         None &#x3D; No change         a &#x3D; Annual         q &#x3D; Quarterly         m &#x3D; Monthly         w &#x3D; Weekly         d &#x3D; Daily         wef &#x3D; Weekly, Ending Friday         weth &#x3D; Weekly, Ending Thursday         wew &#x3D; Weekly, Ending Wednesday         wetu &#x3D; Weekly, Ending Tuesday         wem &#x3D; Weekly, Ending Monday         wesu &#x3D; Weekly, Ending Sunday         wesa &#x3D; Weekly, Ending Saturday         bwew &#x3D; Biweekly, Ending Wednesday         bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg &#x3D; Average         sum &#x3D; Sum         eop &#x3D; End of Period          (provider: fred) | [optional] [default to eop]
 **transform** | **str**| Transformation type         None &#x3D; No transformation         chg &#x3D; Change         ch1 &#x3D; Change from Year Ago         pch &#x3D; Percent Change         pc1 &#x3D; Percent Change from Year Ago         pca &#x3D; Compounded Annual Rate of Change         cch &#x3D; Continuously Compounded Rate of Change         cca &#x3D; Continuously Compounded Annual Rate of Change         log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectCommoditySpotPrices**](OBBjectCommoditySpotPrices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**204** | Empty response |  -  |
**400** | No Results Found |  -  |
**500** | Internal Error |  -  |
**502** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commodity_short_term_energy_outlook**
> OBBjectShortTermEnergyOutlook commodity_short_term_energy_outlook(provider=provider, start_date=start_date, end_date=end_date, symbol=symbol, table=table, frequency=frequency)

Short Term Energy Outlook

Monthly short term (18 month) projections using EIA's STEO model.  Source: www.eia.gov/steo/

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_short_term_energy_outlook import OBBjectShortTermEnergyOutlook
from openbb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8005
# See configuration.py for a list of all supported configuration parameters.
configuration = openbb_client.Configuration(
    host = "http://127.0.0.1:8005"
)


# Enter a context with an instance of the API client
with openbb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openbb_client.CommodityApi(api_client)
    provider = eia # str |  (optional) (default to eia)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    symbol = 'symbol_example' # str | Symbol to get data for. If provided, overrides the 'table' parameter to return only the specified symbol from the STEO API. Multiple comma separated items allowed. (provider: eia) (optional)
    table = 01 # str | The specific table within the STEO dataset. Default is '01'. When 'symbol' is provided, this parameter is ignored.         01: US Energy Markets Summary         02: Nominal Energy Prices         03a: World Petroleum and Other Liquid Fuels Production, Consumption, and Inventories         03b: Non-OPEC Petroleum and Other Liquid Fuels Production         03c: World Petroleum and Other Liquid Fuels Production         03d: World Crude Oil Production         03e: World Petroleum and Other Liquid Fuels Consumption         04a: US Petroleum and Other Liquid Fuels Supply, Consumption, and Inventories         04b: US Hydrocarbon Gas Liquids (HGL) and Petroleum Refinery Balances         04c: US Regional Motor Gasoline Prices and Inventories         04d: US Biofuel Supply, Consumption, and Inventories         05a: US Natural Gas Supply, Consumption, and Inventories         05b: US Regional Natural Gas Prices         06: US Coal Supply, Consumption, and Inventories         07a: US Electricity Industry Overview         07b: US Regional Electricity Retail Sales         07c: US Regional Electricity Prices         07d1: US Regional Electricity Generation, Electric Power Sector         07d2: US Regional Electricity Generation, Electric Power Sector, continued         07e: US Electricity Generating Capacity         08: US Renewable Energy Consumption         09a: US Macroeconomic Indicators and CO2 Emissions         09b: US Regional Macroeconomic Data         09c: US Regional Weather Data         10a: Drilling Productivity Metrics         10b: Crude Oil and Natural Gas Production from Shale and Tight Formations (provider: eia) (optional) (default to 01)
    frequency = month # str | The frequency of the data. Default is 'month'. (provider: eia) (optional) (default to month)

    try:
        # Short Term Energy Outlook
        api_response = api_instance.commodity_short_term_energy_outlook(provider=provider, start_date=start_date, end_date=end_date, symbol=symbol, table=table, frequency=frequency)
        print("The response of CommodityApi->commodity_short_term_energy_outlook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommodityApi->commodity_short_term_energy_outlook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to eia]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **symbol** | **str**| Symbol to get data for. If provided, overrides the &#39;table&#39; parameter to return only the specified symbol from the STEO API. Multiple comma separated items allowed. (provider: eia) | [optional] 
 **table** | **str**| The specific table within the STEO dataset. Default is &#39;01&#39;. When &#39;symbol&#39; is provided, this parameter is ignored.         01: US Energy Markets Summary         02: Nominal Energy Prices         03a: World Petroleum and Other Liquid Fuels Production, Consumption, and Inventories         03b: Non-OPEC Petroleum and Other Liquid Fuels Production         03c: World Petroleum and Other Liquid Fuels Production         03d: World Crude Oil Production         03e: World Petroleum and Other Liquid Fuels Consumption         04a: US Petroleum and Other Liquid Fuels Supply, Consumption, and Inventories         04b: US Hydrocarbon Gas Liquids (HGL) and Petroleum Refinery Balances         04c: US Regional Motor Gasoline Prices and Inventories         04d: US Biofuel Supply, Consumption, and Inventories         05a: US Natural Gas Supply, Consumption, and Inventories         05b: US Regional Natural Gas Prices         06: US Coal Supply, Consumption, and Inventories         07a: US Electricity Industry Overview         07b: US Regional Electricity Retail Sales         07c: US Regional Electricity Prices         07d1: US Regional Electricity Generation, Electric Power Sector         07d2: US Regional Electricity Generation, Electric Power Sector, continued         07e: US Electricity Generating Capacity         08: US Renewable Energy Consumption         09a: US Macroeconomic Indicators and CO2 Emissions         09b: US Regional Macroeconomic Data         09c: US Regional Weather Data         10a: Drilling Productivity Metrics         10b: Crude Oil and Natural Gas Production from Shale and Tight Formations (provider: eia) | [optional] [default to 01]
 **frequency** | **str**| The frequency of the data. Default is &#39;month&#39;. (provider: eia) | [optional] [default to month]

### Return type

[**OBBjectShortTermEnergyOutlook**](OBBjectShortTermEnergyOutlook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**204** | Empty response |  -  |
**400** | No Results Found |  -  |
**500** | Internal Error |  -  |
**502** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

