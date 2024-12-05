# openbb_client.CryptoApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_price_historical**](CryptoApi.md#crypto_price_historical) | **GET** /api/v1/crypto/price/historical | Historical
[**crypto_search**](CryptoApi.md#crypto_search) | **GET** /api/v1/crypto/search | Search


# **crypto_price_historical**
> OBBjectCryptoHistorical crypto_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, sort=sort, limit=limit, exchanges=exchanges)

Historical

Get historical price data for cryptocurrency pair(s) within a provider.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_crypto_historical import OBBjectCryptoHistorical
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
    api_instance = openbb_client.CryptoApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Can use CURR1-CURR2 or CURR1CURR2 format. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance.
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    interval = openbb_client.FmpPolygonTiingoYfinance() # FmpPolygonTiingoYfinance | Time interval of the data to return. (provider: fmp, polygon, tiingo, yfinance) (optional)
    sort = asc # str | Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date. (provider: polygon) (optional) (default to asc)
    limit = 49999 # int | The number of data entries to return. (provider: polygon) (optional) (default to 49999)
    exchanges = openbb_client.Tiingo() # Tiingo | To limit the query to a subset of exchanges e.g. ['POLONIEX', 'GDAX'] Multiple comma separated items allowed. (provider: tiingo) (optional)

    try:
        # Historical
        api_response = api_instance.crypto_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, sort=sort, limit=limit, exchanges=exchanges)
        print("The response of CryptoApi->crypto_price_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_price_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Can use CURR1-CURR2 or CURR1CURR2 format. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance. | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **interval** | [**FmpPolygonTiingoYfinance**](.md)| Time interval of the data to return. (provider: fmp, polygon, tiingo, yfinance) | [optional] 
 **sort** | **str**| Sort order of the data. This impacts the results in combination with the &#39;limit&#39; parameter. The results are always returned in ascending order by date. (provider: polygon) | [optional] [default to asc]
 **limit** | **int**| The number of data entries to return. (provider: polygon) | [optional] [default to 49999]
 **exchanges** | [**Tiingo**](.md)| To limit the query to a subset of exchanges e.g. [&#39;POLONIEX&#39;, &#39;GDAX&#39;] Multiple comma separated items allowed. (provider: tiingo) | [optional] 

### Return type

[**OBBjectCryptoHistorical**](OBBjectCryptoHistorical.md)

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

# **crypto_search**
> OBBjectCryptoSearch crypto_search(provider=provider, query=query)

Search

Search available cryptocurrency pairs within a provider.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_crypto_search import OBBjectCryptoSearch
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
    api_instance = openbb_client.CryptoApi(api_client)
    provider = fmp # str |  (optional) (default to fmp)
    query = 'query_example' # str | Search query. (optional)

    try:
        # Search
        api_response = api_instance.crypto_search(provider=provider, query=query)
        print("The response of CryptoApi->crypto_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fmp]
 **query** | **str**| Search query. | [optional] 

### Return type

[**OBBjectCryptoSearch**](OBBjectCryptoSearch.md)

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

