# openbb_client.IndexApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_available**](IndexApi.md#index_available) | **GET** /api/v1/index/available | Available
[**index_constituents**](IndexApi.md#index_constituents) | **GET** /api/v1/index/constituents | Constituents
[**index_price_historical**](IndexApi.md#index_price_historical) | **GET** /api/v1/index/price/historical | Historical


# **index_available**
> OBBjectAvailableIndices index_available(provider)

Available

All indices available from a given provider.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_available_indices import OBBjectAvailableIndices
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
    api_instance = openbb_client.IndexApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Available
        api_response = api_instance.index_available(provider)
        print("The response of IndexApi->index_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_available: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

[**OBBjectAvailableIndices**](OBBjectAvailableIndices.md)

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

# **index_constituents**
> OBBjectIndexConstituents index_constituents(symbol, provider=provider)

Constituents

Get Index Constituents.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_index_constituents import OBBjectIndexConstituents
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
    api_instance = openbb_client.IndexApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for.
    provider = fmp # str |  (optional) (default to fmp)

    try:
        # Constituents
        api_response = api_instance.index_constituents(symbol, provider=provider)
        print("The response of IndexApi->index_constituents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_constituents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. | 
 **provider** | **str**|  | [optional] [default to fmp]

### Return type

[**OBBjectIndexConstituents**](OBBjectIndexConstituents.md)

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

# **index_price_historical**
> OBBjectIndexHistorical index_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, limit=limit, sort=sort)

Historical

Historical Index Levels.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_index_historical import OBBjectIndexHistorical
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
    api_instance = openbb_client.IndexApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, intrinio, polygon, yfinance.
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    interval = openbb_client.FmpPolygonYfinance() # FmpPolygonYfinance | Time interval of the data to return. (provider: fmp, polygon, yfinance) (optional)
    limit = 56 # int | The number of data entries to return. (provider: intrinio, polygon) (optional)
    sort = asc # str | Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date. (provider: polygon) (optional) (default to asc)

    try:
        # Historical
        api_response = api_instance.index_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, limit=limit, sort=sort)
        print("The response of IndexApi->index_price_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_price_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): fmp, intrinio, polygon, yfinance. | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **interval** | [**FmpPolygonYfinance**](.md)| Time interval of the data to return. (provider: fmp, polygon, yfinance) | [optional] 
 **limit** | **int**| The number of data entries to return. (provider: intrinio, polygon) | [optional] 
 **sort** | **str**| Sort order of the data. This impacts the results in combination with the &#39;limit&#39; parameter. The results are always returned in ascending order by date. (provider: polygon) | [optional] [default to asc]

### Return type

[**OBBjectIndexHistorical**](OBBjectIndexHistorical.md)

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

