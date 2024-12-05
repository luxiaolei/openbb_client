# openbb_client.CurrencyApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_price_historical**](CurrencyApi.md#currency_price_historical) | **GET** /api/v1/currency/price/historical | Historical
[**currency_search**](CurrencyApi.md#currency_search) | **GET** /api/v1/currency/search | Search
[**currency_snapshots**](CurrencyApi.md#currency_snapshots) | **GET** /api/v1/currency/snapshots | Snapshots


# **currency_price_historical**
> OBBjectCurrencyHistorical currency_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, sort=sort, limit=limit)

Historical

Currency Historical Price. Currency historical data.  Currency historical prices refer to the past exchange rates of one currency against another over a specific period. This data provides insight into the fluctuations and trends in the foreign exchange market, helping analysts, traders, and economists understand currency performance, evaluate economic health, and make predictions about future movements.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_currency_historical import OBBjectCurrencyHistorical
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
    api_instance = openbb_client.CurrencyApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Can use CURR1-CURR2 or CURR1CURR2 format. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance.
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    interval = openbb_client.FmpPolygonTiingoYfinance1() # FmpPolygonTiingoYfinance1 | Time interval of the data to return. (provider: fmp, polygon, tiingo, yfinance) (optional)
    sort = asc # str | Sort order of the data. This impacts the results in combination with the 'limit' parameter. The results are always returned in ascending order by date. (provider: polygon) (optional) (default to asc)
    limit = 49999 # int | The number of data entries to return. (provider: polygon) (optional) (default to 49999)

    try:
        # Historical
        api_response = api_instance.currency_price_historical(provider, symbol, start_date=start_date, end_date=end_date, interval=interval, sort=sort, limit=limit)
        print("The response of CurrencyApi->currency_price_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_price_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Can use CURR1-CURR2 or CURR1CURR2 format. Multiple comma separated items allowed for provider(s): fmp, polygon, tiingo, yfinance. | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **interval** | [**FmpPolygonTiingoYfinance1**](.md)| Time interval of the data to return. (provider: fmp, polygon, tiingo, yfinance) | [optional] 
 **sort** | **str**| Sort order of the data. This impacts the results in combination with the &#39;limit&#39; parameter. The results are always returned in ascending order by date. (provider: polygon) | [optional] [default to asc]
 **limit** | **int**| The number of data entries to return. (provider: polygon) | [optional] [default to 49999]

### Return type

[**OBBjectCurrencyHistorical**](OBBjectCurrencyHistorical.md)

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

# **currency_search**
> OBBjectCurrencyPairs currency_search(provider, query=query)

Search

Currency Search.  Search available currency pairs. Currency pairs are the national currencies from two countries coupled for trading on the foreign exchange (FX) marketplace. Both currencies will have exchange rates on which the trade will have its position basis. All trading within the forex market, whether selling, buying, or trading, will take place through currency pairs. (ref: Investopedia) Major currency pairs include pairs such as EUR/USD, USD/JPY, GBP/USD, etc.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_currency_pairs import OBBjectCurrencyPairs
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
    api_instance = openbb_client.CurrencyApi(api_client)
    provider = 'provider_example' # str | 
    query = 'query_example' # str | Query to search for currency pairs. (optional)

    try:
        # Search
        api_response = api_instance.currency_search(provider, query=query)
        print("The response of CurrencyApi->currency_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **query** | **str**| Query to search for currency pairs. | [optional] 

### Return type

[**OBBjectCurrencyPairs**](OBBjectCurrencyPairs.md)

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

# **currency_snapshots**
> OBBjectCurrencySnapshots currency_snapshots(provider, base=base, quote_type=quote_type, counter_currencies=counter_currencies)

Snapshots

Snapshots of currency exchange rates from an indirect or direct perspective of a base currency.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_currency_snapshots import OBBjectCurrencySnapshots
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
    api_instance = openbb_client.CurrencyApi(api_client)
    provider = 'provider_example' # str | 
    base = 'usd' # str | The base currency symbol. Multiple comma separated items allowed for provider(s): fmp, polygon. (optional) (default to 'usd')
    quote_type = indirect # str | Whether the quote is direct or indirect. Selecting 'direct' will return the exchange rate as the amount of domestic currency required to buy one unit of the foreign currency. Selecting 'indirect' (default) will return the exchange rate as the amount of foreign currency required to buy one unit of the domestic currency. (optional) (default to indirect)
    counter_currencies = openbb_client.CounterCurrencies() # CounterCurrencies | An optional list of counter currency symbols to filter for. None returns all. (optional)

    try:
        # Snapshots
        api_response = api_instance.currency_snapshots(provider, base=base, quote_type=quote_type, counter_currencies=counter_currencies)
        print("The response of CurrencyApi->currency_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **base** | **str**| The base currency symbol. Multiple comma separated items allowed for provider(s): fmp, polygon. | [optional] [default to &#39;usd&#39;]
 **quote_type** | **str**| Whether the quote is direct or indirect. Selecting &#39;direct&#39; will return the exchange rate as the amount of domestic currency required to buy one unit of the foreign currency. Selecting &#39;indirect&#39; (default) will return the exchange rate as the amount of foreign currency required to buy one unit of the domestic currency. | [optional] [default to indirect]
 **counter_currencies** | [**CounterCurrencies**](.md)| An optional list of counter currency symbols to filter for. None returns all. | [optional] 

### Return type

[**OBBjectCurrencySnapshots**](OBBjectCurrencySnapshots.md)

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

