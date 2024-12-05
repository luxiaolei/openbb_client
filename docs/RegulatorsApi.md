# openbb_client.RegulatorsApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regulators_cftc_cot**](RegulatorsApi.md#regulators_cftc_cot) | **GET** /api/v1/regulators/cftc/cot | Cot
[**regulators_cftc_cot_search**](RegulatorsApi.md#regulators_cftc_cot_search) | **GET** /api/v1/regulators/cftc/cot_search | Cot Search
[**regulators_sec_cik_map**](RegulatorsApi.md#regulators_sec_cik_map) | **GET** /api/v1/regulators/sec/cik_map | Cik Map
[**regulators_sec_institutions_search**](RegulatorsApi.md#regulators_sec_institutions_search) | **GET** /api/v1/regulators/sec/institutions_search | Institutions Search
[**regulators_sec_rss_litigation**](RegulatorsApi.md#regulators_sec_rss_litigation) | **GET** /api/v1/regulators/sec/rss_litigation | Rss Litigation
[**regulators_sec_schema_files**](RegulatorsApi.md#regulators_sec_schema_files) | **GET** /api/v1/regulators/sec/schema_files | Schema Files
[**regulators_sec_sic_search**](RegulatorsApi.md#regulators_sec_sic_search) | **GET** /api/v1/regulators/sec/sic_search | Sic Search
[**regulators_sec_symbol_map**](RegulatorsApi.md#regulators_sec_symbol_map) | **GET** /api/v1/regulators/sec/symbol_map | Symbol Map


# **regulators_cftc_cot**
> OBBjectCOT regulators_cftc_cot(provider=provider, id=id, start_date=start_date, end_date=end_date, report_type=report_type, futures_only=futures_only)

Cot

Get Commitment of Traders Reports.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_cot import OBBjectCOT
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = cftc # str |  (optional) (default to cftc)
    id = '045601' # str | A string with the CFTC market code or other identifying string, such as the contract market name, commodity name, or commodity group - i.e, 'gold' or 'japanese yen'.Default report is Fed Funds Futures. Use the 'cftc_market_code' for an exact match. (optional) (default to '045601')
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. Default is the most recent report. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    report_type = legacy # str | The type of report to retrieve. Set `id` as 'all' to return all items in the report             type (default date range returns the latest report). The Legacy report is broken down by exchange             with reported open interest further broken down into three trader classifications: commercial,             non-commercial and non-reportable. The Disaggregated reports are broken down by Agriculture and             Natural Resource contracts. The Disaggregated reports break down reportable open interest positions             into four classifications: Producer/Merchant, Swap Dealers, Managed Money and Other Reportables.             The Traders in Financial Futures (TFF) report includes financial contracts. The TFF report breaks             down the reported open interest into five classifications: Dealer, Asset Manager, Leveraged Money,             Other Reportables and Non-Reportables. (provider: cftc) (optional) (default to legacy)
    futures_only = False # bool | Returns the futures-only report. Default is False, for the combined report. (provider: cftc) (optional) (default to False)

    try:
        # Cot
        api_response = api_instance.regulators_cftc_cot(provider=provider, id=id, start_date=start_date, end_date=end_date, report_type=report_type, futures_only=futures_only)
        print("The response of RegulatorsApi->regulators_cftc_cot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_cftc_cot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to cftc]
 **id** | **str**| A string with the CFTC market code or other identifying string, such as the contract market name, commodity name, or commodity group - i.e, &#39;gold&#39; or &#39;japanese yen&#39;.Default report is Fed Funds Futures. Use the &#39;cftc_market_code&#39; for an exact match. | [optional] [default to &#39;045601&#39;]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. Default is the most recent report. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **report_type** | **str**| The type of report to retrieve. Set &#x60;id&#x60; as &#39;all&#39; to return all items in the report             type (default date range returns the latest report). The Legacy report is broken down by exchange             with reported open interest further broken down into three trader classifications: commercial,             non-commercial and non-reportable. The Disaggregated reports are broken down by Agriculture and             Natural Resource contracts. The Disaggregated reports break down reportable open interest positions             into four classifications: Producer/Merchant, Swap Dealers, Managed Money and Other Reportables.             The Traders in Financial Futures (TFF) report includes financial contracts. The TFF report breaks             down the reported open interest into five classifications: Dealer, Asset Manager, Leveraged Money,             Other Reportables and Non-Reportables. (provider: cftc) | [optional] [default to legacy]
 **futures_only** | **bool**| Returns the futures-only report. Default is False, for the combined report. (provider: cftc) | [optional] [default to False]

### Return type

[**OBBjectCOT**](OBBjectCOT.md)

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

# **regulators_cftc_cot_search**
> OBBjectCOTSearch regulators_cftc_cot_search(provider=provider, query=query)

Cot Search

Get the current Commitment of Traders Reports.  Search a list of the current Commitment of Traders Reports series information.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_cot_search import OBBjectCOTSearch
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = cftc # str |  (optional) (default to cftc)
    query = '' # str | Search query. (optional) (default to '')

    try:
        # Cot Search
        api_response = api_instance.regulators_cftc_cot_search(provider=provider, query=query)
        print("The response of RegulatorsApi->regulators_cftc_cot_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_cftc_cot_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to cftc]
 **query** | **str**| Search query. | [optional] [default to &#39;&#39;]

### Return type

[**OBBjectCOTSearch**](OBBjectCOTSearch.md)

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

# **regulators_sec_cik_map**
> OBBjectCikMap regulators_sec_cik_map(symbol, provider=provider, use_cache=use_cache)

Cik Map

Map a ticker symbol to a CIK number.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_cik_map import OBBjectCikMap
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for.
    provider = sec # str |  (optional) (default to sec)
    use_cache = True # bool | Whether or not to use cache for the request, default is True. (provider: sec) (optional)

    try:
        # Cik Map
        api_response = api_instance.regulators_sec_cik_map(symbol, provider=provider, use_cache=use_cache)
        print("The response of RegulatorsApi->regulators_sec_cik_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_cik_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. | 
 **provider** | **str**|  | [optional] [default to sec]
 **use_cache** | **bool**| Whether or not to use cache for the request, default is True. (provider: sec) | [optional] 

### Return type

[**OBBjectCikMap**](OBBjectCikMap.md)

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

# **regulators_sec_institutions_search**
> OBBjectInstitutionsSearch regulators_sec_institutions_search(provider=provider, query=query, use_cache=use_cache)

Institutions Search

Search SEC-regulated institutions by name and return a list of results with CIK numbers.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_institutions_search import OBBjectInstitutionsSearch
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = sec # str |  (optional) (default to sec)
    query = '' # str | Search query. (optional) (default to '')
    use_cache = True # bool | Whether or not to use cache. (provider: sec) (optional)

    try:
        # Institutions Search
        api_response = api_instance.regulators_sec_institutions_search(provider=provider, query=query, use_cache=use_cache)
        print("The response of RegulatorsApi->regulators_sec_institutions_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_institutions_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to sec]
 **query** | **str**| Search query. | [optional] [default to &#39;&#39;]
 **use_cache** | **bool**| Whether or not to use cache. (provider: sec) | [optional] 

### Return type

[**OBBjectInstitutionsSearch**](OBBjectInstitutionsSearch.md)

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

# **regulators_sec_rss_litigation**
> OBBjectRssLitigation regulators_sec_rss_litigation(provider=provider)

Rss Litigation

Get the RSS feed that provides links to litigation releases concerning civil lawsuits brought by the Commission in federal court.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_rss_litigation import OBBjectRssLitigation
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = sec # str |  (optional) (default to sec)

    try:
        # Rss Litigation
        api_response = api_instance.regulators_sec_rss_litigation(provider=provider)
        print("The response of RegulatorsApi->regulators_sec_rss_litigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_rss_litigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to sec]

### Return type

[**OBBjectRssLitigation**](OBBjectRssLitigation.md)

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

# **regulators_sec_schema_files**
> OBBjectSchemaFiles regulators_sec_schema_files(provider=provider, query=query, url=url, use_cache=use_cache)

Schema Files

Use tool for navigating the directory of SEC XML schema files by year.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_schema_files import OBBjectSchemaFiles
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = sec # str |  (optional) (default to sec)
    query = '' # str | Search query. (optional) (default to '')
    url = 'url_example' # str | Enter an optional URL path to fetch the next level. (provider: sec) (optional)
    use_cache = True # bool | Whether or not to use cache. (provider: sec) (optional)

    try:
        # Schema Files
        api_response = api_instance.regulators_sec_schema_files(provider=provider, query=query, url=url, use_cache=use_cache)
        print("The response of RegulatorsApi->regulators_sec_schema_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_schema_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to sec]
 **query** | **str**| Search query. | [optional] [default to &#39;&#39;]
 **url** | **str**| Enter an optional URL path to fetch the next level. (provider: sec) | [optional] 
 **use_cache** | **bool**| Whether or not to use cache. (provider: sec) | [optional] 

### Return type

[**OBBjectSchemaFiles**](OBBjectSchemaFiles.md)

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

# **regulators_sec_sic_search**
> OBBjectSicSearch regulators_sec_sic_search(provider=provider, query=query, use_cache=use_cache)

Sic Search

Search for Industry Titles, Reporting Office, and SIC Codes. An empty query string returns all results.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_sic_search import OBBjectSicSearch
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    provider = sec # str |  (optional) (default to sec)
    query = '' # str | Search query. (optional) (default to '')
    use_cache = True # bool | Whether or not to use cache. (provider: sec) (optional)

    try:
        # Sic Search
        api_response = api_instance.regulators_sec_sic_search(provider=provider, query=query, use_cache=use_cache)
        print("The response of RegulatorsApi->regulators_sec_sic_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_sic_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to sec]
 **query** | **str**| Search query. | [optional] [default to &#39;&#39;]
 **use_cache** | **bool**| Whether or not to use cache. (provider: sec) | [optional] 

### Return type

[**OBBjectSicSearch**](OBBjectSicSearch.md)

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

# **regulators_sec_symbol_map**
> OBBjectSymbolMap regulators_sec_symbol_map(query, provider=provider, use_cache=use_cache)

Symbol Map

Map a CIK number to a ticker symbol, leading 0s can be omitted or included.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_symbol_map import OBBjectSymbolMap
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
    api_instance = openbb_client.RegulatorsApi(api_client)
    query = 'query_example' # str | Search query.
    provider = sec # str |  (optional) (default to sec)
    use_cache = True # bool | Whether or not to use cache. If True, cache will store for seven days. (optional)

    try:
        # Symbol Map
        api_response = api_instance.regulators_sec_symbol_map(query, provider=provider, use_cache=use_cache)
        print("The response of RegulatorsApi->regulators_sec_symbol_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegulatorsApi->regulators_sec_symbol_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query. | 
 **provider** | **str**|  | [optional] [default to sec]
 **use_cache** | **bool**| Whether or not to use cache. If True, cache will store for seven days. | [optional] 

### Return type

[**OBBjectSymbolMap**](OBBjectSymbolMap.md)

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

