# openbb_client.EtfApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**etf_countries**](EtfApi.md#etf_countries) | **GET** /api/v1/etf/countries | Countries
[**etf_equity_exposure**](EtfApi.md#etf_equity_exposure) | **GET** /api/v1/etf/equity_exposure | Equity Exposure
[**etf_historical**](EtfApi.md#etf_historical) | **GET** /api/v1/etf/historical | Historical
[**etf_holdings**](EtfApi.md#etf_holdings) | **GET** /api/v1/etf/holdings | Holdings
[**etf_holdings_date**](EtfApi.md#etf_holdings_date) | **GET** /api/v1/etf/holdings_date | Holdings Date
[**etf_info**](EtfApi.md#etf_info) | **GET** /api/v1/etf/info | Info
[**etf_price_performance**](EtfApi.md#etf_price_performance) | **GET** /api/v1/etf/price_performance | Price Performance
[**etf_search**](EtfApi.md#etf_search) | **GET** /api/v1/etf/search | Search
[**etf_sectors**](EtfApi.md#etf_sectors) | **GET** /api/v1/etf/sectors | Sectors


# **etf_countries**
> OBBjectEtfCountries etf_countries(symbol, provider=provider)

Countries

ETF Country weighting.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_countries import OBBjectEtfCountries
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
    api_instance = openbb_client.EtfApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. (ETF) Multiple comma separated items allowed for provider(s): fmp.
    provider = fmp # str |  (optional) (default to fmp)

    try:
        # Countries
        api_response = api_instance.etf_countries(symbol, provider=provider)
        print("The response of EtfApi->etf_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_countries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. (ETF) Multiple comma separated items allowed for provider(s): fmp. | 
 **provider** | **str**|  | [optional] [default to fmp]

### Return type

[**OBBjectEtfCountries**](OBBjectEtfCountries.md)

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

# **etf_equity_exposure**
> OBBjectEtfEquityExposure etf_equity_exposure(symbol, provider=provider)

Equity Exposure

Get the exposure to ETFs for a specific stock.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_equity_exposure import OBBjectEtfEquityExposure
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
    api_instance = openbb_client.EtfApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. (Stock) Multiple comma separated items allowed for provider(s): fmp.
    provider = fmp # str |  (optional) (default to fmp)

    try:
        # Equity Exposure
        api_response = api_instance.etf_equity_exposure(symbol, provider=provider)
        print("The response of EtfApi->etf_equity_exposure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_equity_exposure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. (Stock) Multiple comma separated items allowed for provider(s): fmp. | 
 **provider** | **str**|  | [optional] [default to fmp]

### Return type

[**OBBjectEtfEquityExposure**](OBBjectEtfEquityExposure.md)

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

# **etf_historical**
> OBBjectEtfHistorical etf_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, start_time=start_time, end_time=end_time, timezone=timezone, source=source, adjustment=adjustment, extended_hours=extended_hours, sort=sort, limit=limit, include_actions=include_actions)

Historical

ETF Historical Market Price.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_historical import OBBjectEtfHistorical
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
    api_instance = openbb_client.EtfApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance.
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    interval = openbb_client.FmpIntrinioPolygonTiingoYfinance1() # FmpIntrinioPolygonTiingoYfinance1 | Time interval of the data to return. (provider: fmp, intrinio, polygon, tiingo, yfinance) (optional)
    start_time = 'start_time_example' # str | Return intervals starting at the specified time on the `start_date` formatted as 'HH:MM:SS'. (provider: intrinio) (optional)
    end_time = 'end_time_example' # str | Return intervals stopping at the specified time on the `end_date` formatted as 'HH:MM:SS'. (provider: intrinio) (optional)
    timezone = 'timezone_example' # str | Timezone of the data, in the IANA format (Continent/City). (provider: intrinio) (optional)
    source = realtime # str | The source of the data. (provider: intrinio) (optional) (default to realtime)
    adjustment = openbb_client.PolygonYfinance() # PolygonYfinance | The adjustment factor to apply. Default is splits only. (provider: polygon, yfinance) (optional)
    extended_hours = False # bool | Include Pre and Post market data. (provider: polygon, yfinance) (optional) (default to False)
    sort = asc # str | Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date. (provider: polygon) (optional) (default to asc)
    limit = 49999 # int | The number of data entries to return. (provider: polygon) (optional) (default to 49999)
    include_actions = True # bool | Include dividends and stock splits in results. (provider: yfinance) (optional) (default to True)

    try:
        # Historical
        api_response = api_instance.etf_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, start_time=start_time, end_time=end_time, timezone=timezone, source=source, adjustment=adjustment, extended_hours=extended_hours, sort=sort, limit=limit, include_actions=include_actions)
        print("The response of EtfApi->etf_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance. | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **interval** | [**FmpIntrinioPolygonTiingoYfinance1**](.md)| Time interval of the data to return. (provider: fmp, intrinio, polygon, tiingo, yfinance) | [optional] 
 **start_time** | **str**| Return intervals starting at the specified time on the &#x60;start_date&#x60; formatted as &#39;HH:MM:SS&#39;. (provider: intrinio) | [optional] 
 **end_time** | **str**| Return intervals stopping at the specified time on the &#x60;end_date&#x60; formatted as &#39;HH:MM:SS&#39;. (provider: intrinio) | [optional] 
 **timezone** | **str**| Timezone of the data, in the IANA format (Continent/City). (provider: intrinio) | [optional] 
 **source** | **str**| The source of the data. (provider: intrinio) | [optional] [default to realtime]
 **adjustment** | [**PolygonYfinance**](.md)| The adjustment factor to apply. Default is splits only. (provider: polygon, yfinance) | [optional] 
 **extended_hours** | **bool**| Include Pre and Post market data. (provider: polygon, yfinance) | [optional] [default to False]
 **sort** | **str**| Sort order of the data. This impacts the results in combination with the &#39;limit&#39; parameter. The results are always returned in ascending order by date. (provider: polygon) | [optional] [default to asc]
 **limit** | **int**| The number of data entries to return. (provider: polygon) | [optional] [default to 49999]
 **include_actions** | **bool**| Include dividends and stock splits in results. (provider: yfinance) | [optional] [default to True]

### Return type

[**OBBjectEtfHistorical**](OBBjectEtfHistorical.md)

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

# **etf_holdings**
> OBBjectEtfHoldings etf_holdings(provider, symbol, var_date=var_date, cik=cik, use_cache=use_cache)

Holdings

Get the holdings for an individual ETF.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_holdings import OBBjectEtfHoldings
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
    api_instance = openbb_client.EtfApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. (ETF)
    var_date = openbb_client.FmpIntrinioSec() # FmpIntrinioSec | A specific date to get data for. Entering a date will attempt to return the NPORT-P filing for the entered date. This needs to be _exactly_ the date of the filing. Use the holdings_date command/endpoint to find available filing dates for the ETF. (provider: fmp);     A specific date to get data for. (provider: intrinio);     A specific date to get data for.  The date represents the period ending. The date entered will return the closest filing. (provider: sec) (optional)
    cik = 'cik_example' # str | The CIK of the filing entity. Overrides symbol. (provider: fmp) (optional)
    use_cache = True # bool | Whether or not to use cache for the request. (provider: sec) (optional) (default to True)

    try:
        # Holdings
        api_response = api_instance.etf_holdings(provider, symbol, var_date=var_date, cik=cik, use_cache=use_cache)
        print("The response of EtfApi->etf_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_holdings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. (ETF) | 
 **var_date** | [**FmpIntrinioSec**](.md)| A specific date to get data for. Entering a date will attempt to return the NPORT-P filing for the entered date. This needs to be _exactly_ the date of the filing. Use the holdings_date command/endpoint to find available filing dates for the ETF. (provider: fmp);     A specific date to get data for. (provider: intrinio);     A specific date to get data for.  The date represents the period ending. The date entered will return the closest filing. (provider: sec) | [optional] 
 **cik** | **str**| The CIK of the filing entity. Overrides symbol. (provider: fmp) | [optional] 
 **use_cache** | **bool**| Whether or not to use cache for the request. (provider: sec) | [optional] [default to True]

### Return type

[**OBBjectEtfHoldings**](OBBjectEtfHoldings.md)

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

# **etf_holdings_date**
> OBBjectEtfHoldingsDate etf_holdings_date(symbol, provider=provider, cik=cik)

Holdings Date

Use this function to get the holdings dates, if available.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_holdings_date import OBBjectEtfHoldingsDate
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
    api_instance = openbb_client.EtfApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. (ETF)
    provider = fmp # str |  (optional) (default to fmp)
    cik = 'cik_example' # str | The CIK of the filing entity. Overrides symbol. (provider: fmp) (optional)

    try:
        # Holdings Date
        api_response = api_instance.etf_holdings_date(symbol, provider=provider, cik=cik)
        print("The response of EtfApi->etf_holdings_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_holdings_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. (ETF) | 
 **provider** | **str**|  | [optional] [default to fmp]
 **cik** | **str**| The CIK of the filing entity. Overrides symbol. (provider: fmp) | [optional] 

### Return type

[**OBBjectEtfHoldingsDate**](OBBjectEtfHoldingsDate.md)

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

# **etf_info**
> OBBjectEtfInfo etf_info(provider, symbol)

Info

ETF Information Overview.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_info import OBBjectEtfInfo
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
    api_instance = openbb_client.EtfApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. (ETF) Multiple comma separated items allowed for provider(s): fmp, intrinio, yfinance.

    try:
        # Info
        api_response = api_instance.etf_info(provider, symbol)
        print("The response of EtfApi->etf_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. (ETF) Multiple comma separated items allowed for provider(s): fmp, intrinio, yfinance. | 

### Return type

[**OBBjectEtfInfo**](OBBjectEtfInfo.md)

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

# **etf_price_performance**
> OBBjectEtfPricePerformance etf_price_performance(provider, symbol, return_type=return_type, adjustment=adjustment)

Price Performance

Price performance as a return, over different periods.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_price_performance import OBBjectEtfPricePerformance
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
    api_instance = openbb_client.EtfApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, intrinio.
    return_type = trailing # str | The type of returns to return, a trailing or calendar window. (provider: intrinio) (optional) (default to trailing)
    adjustment = splits_and_dividends # str | The adjustment factor, 'splits_only' will return pure price performance. (provider: intrinio) (optional) (default to splits_and_dividends)

    try:
        # Price Performance
        api_response = api_instance.etf_price_performance(provider, symbol, return_type=return_type, adjustment=adjustment)
        print("The response of EtfApi->etf_price_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_price_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, intrinio. | 
 **return_type** | **str**| The type of returns to return, a trailing or calendar window. (provider: intrinio) | [optional] [default to trailing]
 **adjustment** | **str**| The adjustment factor, &#39;splits_only&#39; will return pure price performance. (provider: intrinio) | [optional] [default to splits_and_dividends]

### Return type

[**OBBjectEtfPricePerformance**](OBBjectEtfPricePerformance.md)

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

# **etf_search**
> OBBjectEtfSearch etf_search(provider, query=query, exchange=exchange, is_active=is_active)

Search

Search for ETFs.  An empty query returns the full list of ETFs from the provider.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_search import OBBjectEtfSearch
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
    api_instance = openbb_client.EtfApi(api_client)
    provider = 'provider_example' # str | 
    query = 'query_example' # str | Search query. (optional)
    exchange = openbb_client.FmpIntrinio2() # FmpIntrinio2 | The exchange code the ETF trades on. (provider: fmp);     Target a specific exchange by providing the MIC code. (provider: intrinio) (optional)
    is_active = True # bool | Whether the ETF is actively trading. (provider: fmp) (optional)

    try:
        # Search
        api_response = api_instance.etf_search(provider, query=query, exchange=exchange, is_active=is_active)
        print("The response of EtfApi->etf_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **query** | **str**| Search query. | [optional] 
 **exchange** | [**FmpIntrinio2**](.md)| The exchange code the ETF trades on. (provider: fmp);     Target a specific exchange by providing the MIC code. (provider: intrinio) | [optional] 
 **is_active** | **bool**| Whether the ETF is actively trading. (provider: fmp) | [optional] 

### Return type

[**OBBjectEtfSearch**](OBBjectEtfSearch.md)

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

# **etf_sectors**
> OBBjectEtfSectors etf_sectors(symbol, provider=provider)

Sectors

ETF Sector weighting.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_etf_sectors import OBBjectEtfSectors
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
    api_instance = openbb_client.EtfApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. (ETF)
    provider = fmp # str |  (optional) (default to fmp)

    try:
        # Sectors
        api_response = api_instance.etf_sectors(symbol, provider=provider)
        print("The response of EtfApi->etf_sectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtfApi->etf_sectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. (ETF) | 
 **provider** | **str**|  | [optional] [default to fmp]

### Return type

[**OBBjectEtfSectors**](OBBjectEtfSectors.md)

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

