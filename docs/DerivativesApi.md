# openbb_client.DerivativesApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**derivatives_futures_curve**](DerivativesApi.md#derivatives_futures_curve) | **GET** /api/v1/derivatives/futures/curve | Curve
[**derivatives_futures_historical**](DerivativesApi.md#derivatives_futures_historical) | **GET** /api/v1/derivatives/futures/historical | Historical
[**derivatives_options_chains**](DerivativesApi.md#derivatives_options_chains) | **GET** /api/v1/derivatives/options/chains | Chains
[**derivatives_options_snapshots**](DerivativesApi.md#derivatives_options_snapshots) | **GET** /api/v1/derivatives/options/snapshots | Snapshots
[**derivatives_options_unusual**](DerivativesApi.md#derivatives_options_unusual) | **GET** /api/v1/derivatives/options/unusual | Unusual


# **derivatives_futures_curve**
> OBBjectFuturesCurve derivatives_futures_curve(symbol, provider=provider, var_date=var_date)

Curve

Futures Term Structure, current or historical.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_futures_curve import OBBjectFuturesCurve
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
    api_instance = openbb_client.DerivativesApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for.
    provider = yfinance # str |  (optional) (default to yfinance)
    var_date = openbb_client.ModelDate() # ModelDate | A specific date to get data for. Multiple comma separated items allowed for provider(s): yfinance. (optional)

    try:
        # Curve
        api_response = api_instance.derivatives_futures_curve(symbol, provider=provider, var_date=var_date)
        print("The response of DerivativesApi->derivatives_futures_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_futures_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. | 
 **provider** | **str**|  | [optional] [default to yfinance]
 **var_date** | [**ModelDate**](.md)| A specific date to get data for. Multiple comma separated items allowed for provider(s): yfinance. | [optional] 

### Return type

[**OBBjectFuturesCurve**](OBBjectFuturesCurve.md)

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

# **derivatives_futures_historical**
> OBBjectFuturesHistorical derivatives_futures_historical(symbol, provider=provider, start_date=start_date, end_date=end_date, expiration=expiration, interval=interval)

Historical

Historical futures prices.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_futures_historical import OBBjectFuturesHistorical
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
    api_instance = openbb_client.DerivativesApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): yfinance.
    provider = yfinance # str |  (optional) (default to yfinance)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    expiration = 'expiration_example' # str | Future expiry date with format YYYY-MM (optional)
    interval = 1d # str | Time interval of the data to return. (provider: yfinance) (optional) (default to 1d)

    try:
        # Historical
        api_response = api_instance.derivatives_futures_historical(symbol, provider=provider, start_date=start_date, end_date=end_date, expiration=expiration, interval=interval)
        print("The response of DerivativesApi->derivatives_futures_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_futures_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): yfinance. | 
 **provider** | **str**|  | [optional] [default to yfinance]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **expiration** | **str**| Future expiry date with format YYYY-MM | [optional] 
 **interval** | **str**| Time interval of the data to return. (provider: yfinance) | [optional] [default to 1d]

### Return type

[**OBBjectFuturesHistorical**](OBBjectFuturesHistorical.md)

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

# **derivatives_options_chains**
> OBBjectOptionsChains derivatives_options_chains(provider, symbol, delay=delay, var_date=var_date, option_type=option_type, moneyness=moneyness, strike_gt=strike_gt, strike_lt=strike_lt, volume_gt=volume_gt, volume_lt=volume_lt, oi_gt=oi_gt, oi_lt=oi_lt, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)

Chains

Get the complete options chain for a ticker.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_options_chains import OBBjectOptionsChains
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
    api_instance = openbb_client.DerivativesApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for.
    delay = eod # str | Whether to return delayed, realtime, or eod data. (provider: intrinio) (optional) (default to eod)
    var_date = '2013-10-20' # date | The end-of-day date for options chains data. (provider: intrinio) (optional)
    option_type = 'option_type_example' # str | The option type, call or put, 'None' is both (default). (provider: intrinio) (optional)
    moneyness = all # str | Return only contracts that are in or out of the money, default is 'all'. Parameter is ignored when a date is supplied. (provider: intrinio) (optional) (default to all)
    strike_gt = 56 # int | Return options with a strike price greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    strike_lt = 56 # int | Return options with a strike price less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    volume_gt = 56 # int | Return options with a volume greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    volume_lt = 56 # int | Return options with a volume less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    oi_gt = 56 # int | Return options with an open interest greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    oi_lt = 56 # int | Return options with an open interest less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) (optional)
    model = black_scholes # str | The pricing model to use for options chains data, default is 'black_scholes'. Parameter is ignored when a date is supplied. (provider: intrinio) (optional) (default to black_scholes)
    show_extended_price = True # bool | Whether to include OHLC type fields, default is True. Parameter is ignored when a date is supplied. (provider: intrinio) (optional) (default to True)
    include_related_symbols = False # bool | Include related symbols that end in a 1 or 2 because of a corporate action, default is False. (provider: intrinio) (optional) (default to False)

    try:
        # Chains
        api_response = api_instance.derivatives_options_chains(provider, symbol, delay=delay, var_date=var_date, option_type=option_type, moneyness=moneyness, strike_gt=strike_gt, strike_lt=strike_lt, volume_gt=volume_gt, volume_lt=volume_lt, oi_gt=oi_gt, oi_lt=oi_lt, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)
        print("The response of DerivativesApi->derivatives_options_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_options_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. | 
 **delay** | **str**| Whether to return delayed, realtime, or eod data. (provider: intrinio) | [optional] [default to eod]
 **var_date** | **date**| The end-of-day date for options chains data. (provider: intrinio) | [optional] 
 **option_type** | **str**| The option type, call or put, &#39;None&#39; is both (default). (provider: intrinio) | [optional] 
 **moneyness** | **str**| Return only contracts that are in or out of the money, default is &#39;all&#39;. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] [default to all]
 **strike_gt** | **int**| Return options with a strike price greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **strike_lt** | **int**| Return options with a strike price less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **volume_gt** | **int**| Return options with a volume greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **volume_lt** | **int**| Return options with a volume less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **oi_gt** | **int**| Return options with an open interest greater than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **oi_lt** | **int**| Return options with an open interest less than the given value. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] 
 **model** | **str**| The pricing model to use for options chains data, default is &#39;black_scholes&#39;. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] [default to black_scholes]
 **show_extended_price** | **bool**| Whether to include OHLC type fields, default is True. Parameter is ignored when a date is supplied. (provider: intrinio) | [optional] [default to True]
 **include_related_symbols** | **bool**| Include related symbols that end in a 1 or 2 because of a corporate action, default is False. (provider: intrinio) | [optional] [default to False]

### Return type

[**OBBjectOptionsChains**](OBBjectOptionsChains.md)

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

# **derivatives_options_snapshots**
> OBBjectOptionsSnapshots derivatives_options_snapshots(provider=provider, var_date=var_date, only_traded=only_traded)

Snapshots

Get a snapshot of the options market universe.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_options_snapshots import OBBjectOptionsSnapshots
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
    api_instance = openbb_client.DerivativesApi(api_client)
    provider = intrinio # str |  (optional) (default to intrinio)
    var_date = openbb_client.Intrinio2() # Intrinio2 | The date of the data. Can be a datetime or an ISO datetime string. Data appears to go back to around 2022-06-01 Example: '2024-03-08T12:15:00+0400' (provider: intrinio) (optional)
    only_traded = True # bool | Only include options that have been traded during the session, default is True. Setting to false will dramatically increase the size of the response - use with caution. (provider: intrinio) (optional) (default to True)

    try:
        # Snapshots
        api_response = api_instance.derivatives_options_snapshots(provider=provider, var_date=var_date, only_traded=only_traded)
        print("The response of DerivativesApi->derivatives_options_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_options_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to intrinio]
 **var_date** | [**Intrinio2**](.md)| The date of the data. Can be a datetime or an ISO datetime string. Data appears to go back to around 2022-06-01 Example: &#39;2024-03-08T12:15:00+0400&#39; (provider: intrinio) | [optional] 
 **only_traded** | **bool**| Only include options that have been traded during the session, default is True. Setting to false will dramatically increase the size of the response - use with caution. (provider: intrinio) | [optional] [default to True]

### Return type

[**OBBjectOptionsSnapshots**](OBBjectOptionsSnapshots.md)

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

# **derivatives_options_unusual**
> OBBjectOptionsUnusual derivatives_options_unusual(provider=provider, symbol=symbol, start_date=start_date, end_date=end_date, trade_type=trade_type, sentiment=sentiment, min_value=min_value, max_value=max_value, limit=limit, source=source)

Unusual

Get the complete options chain for a ticker.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_options_unusual import OBBjectOptionsUnusual
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
    api_instance = openbb_client.DerivativesApi(api_client)
    provider = intrinio # str |  (optional) (default to intrinio)
    symbol = 'symbol_example' # str | Symbol to get data for. (the underlying symbol) (optional)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. If no symbol is supplied, requests are only allowed for a single date. Use the start_date for the target date. Intrinio appears to have data beginning Feb/2022, but is unclear when it actually began. (provider: intrinio) (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. If a symbol is not supplied, do not include an end date. (provider: intrinio) (optional)
    trade_type = 'trade_type_example' # str | The type of unusual activity to query for. (provider: intrinio) (optional)
    sentiment = 'sentiment_example' # str | The sentiment type to query for. (provider: intrinio) (optional)
    min_value = openbb_client.Intrinio() # Intrinio | The inclusive minimum total value for the unusual activity. (provider: intrinio) (optional)
    max_value = openbb_client.Intrinio1() # Intrinio1 | The inclusive maximum total value for the unusual activity. (provider: intrinio) (optional)
    limit = 100000 # int | The number of data entries to return. A typical day for all symbols will yield 50-80K records. The API will paginate at 1000 records. The high default limit (100K) is to be able to reliably capture the most days. The high absolute limit (1.25M) is to allow for outlier days. Queries at the absolute limit will take a long time, and might be unreliable. Apply filters to improve performance. (provider: intrinio) (optional) (default to 100000)
    source = delayed # str | The source of the data. Either realtime or delayed. (provider: intrinio) (optional) (default to delayed)

    try:
        # Unusual
        api_response = api_instance.derivatives_options_unusual(provider=provider, symbol=symbol, start_date=start_date, end_date=end_date, trade_type=trade_type, sentiment=sentiment, min_value=min_value, max_value=max_value, limit=limit, source=source)
        print("The response of DerivativesApi->derivatives_options_unusual:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DerivativesApi->derivatives_options_unusual: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to intrinio]
 **symbol** | **str**| Symbol to get data for. (the underlying symbol) | [optional] 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. If no symbol is supplied, requests are only allowed for a single date. Use the start_date for the target date. Intrinio appears to have data beginning Feb/2022, but is unclear when it actually began. (provider: intrinio) | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. If a symbol is not supplied, do not include an end date. (provider: intrinio) | [optional] 
 **trade_type** | **str**| The type of unusual activity to query for. (provider: intrinio) | [optional] 
 **sentiment** | **str**| The sentiment type to query for. (provider: intrinio) | [optional] 
 **min_value** | [**Intrinio**](.md)| The inclusive minimum total value for the unusual activity. (provider: intrinio) | [optional] 
 **max_value** | [**Intrinio1**](.md)| The inclusive maximum total value for the unusual activity. (provider: intrinio) | [optional] 
 **limit** | **int**| The number of data entries to return. A typical day for all symbols will yield 50-80K records. The API will paginate at 1000 records. The high default limit (100K) is to be able to reliably capture the most days. The high absolute limit (1.25M) is to allow for outlier days. Queries at the absolute limit will take a long time, and might be unreliable. Apply filters to improve performance. (provider: intrinio) | [optional] [default to 100000]
 **source** | **str**| The source of the data. Either realtime or delayed. (provider: intrinio) | [optional] [default to delayed]

### Return type

[**OBBjectOptionsUnusual**](OBBjectOptionsUnusual.md)

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

