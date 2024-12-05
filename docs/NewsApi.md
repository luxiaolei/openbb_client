# openbb_client.NewsApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**news_company**](NewsApi.md#news_company) | **GET** /api/v1/news/company | Company
[**news_world**](NewsApi.md#news_world) | **GET** /api/v1/news/world | World


# **news_company**
> OBBjectCompanyNews news_company(provider, symbol=symbol, start_date=start_date, end_date=end_date, limit=limit, var_date=var_date, display=display, updated_since=updated_since, published_since=published_since, sort=sort, order=order, isin=isin, cusip=cusip, channels=channels, topics=topics, authors=authors, content_types=content_types, page=page, source=source, sentiment=sentiment, language=language, topic=topic, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, offset=offset)

Company

Company News. Get news for one or more companies.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_company_news import OBBjectCompanyNews
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
    api_instance = openbb_client.NewsApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): benzinga, fmp, intrinio, polygon, tiingo, yfinance. (optional)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    limit = 56 # int | The number of data entries to return. (optional)
    var_date = '2013-10-20' # date | A specific date to get data for. (provider: benzinga) (optional)
    display = full # str | Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga) (optional) (default to full)
    updated_since = 56 # int | Number of seconds since the news was updated. (provider: benzinga) (optional)
    published_since = 56 # int | Number of seconds since the news was published. (provider: benzinga) (optional)
    sort = created # str | Key to sort the news by. (provider: benzinga) (optional) (default to created)
    order = desc # str | Order to sort the news by. (provider: benzinga);     Sort order of the articles. (provider: polygon) (optional) (default to desc)
    isin = 'isin_example' # str | The company's ISIN. (provider: benzinga) (optional)
    cusip = 'cusip_example' # str | The company's CUSIP. (provider: benzinga) (optional)
    channels = 'channels_example' # str | Channels of the news to retrieve. (provider: benzinga) (optional)
    topics = 'topics_example' # str | Topics of the news to retrieve. (provider: benzinga) (optional)
    authors = 'authors_example' # str | Authors of the news to retrieve. (provider: benzinga) (optional)
    content_types = 'content_types_example' # str | Content types of the news to retrieve. (provider: benzinga) (optional)
    page = 56 # int | Page number of the results. Use in combination with limit. (provider: fmp) (optional)
    source = openbb_client.IntrinioTiingo1() # IntrinioTiingo1 | The source of the news article. (provider: intrinio);     A comma-separated list of the domains requested. Multiple comma separated items allowed. (provider: tiingo) (optional)
    sentiment = 'sentiment_example' # str | Return news only from this source. (provider: intrinio) (optional)
    language = 'language_example' # str | Filter by language. Unsupported for yahoo source. (provider: intrinio) (optional)
    topic = 'topic_example' # str | Filter by topic. Unsupported for yahoo source. (provider: intrinio) (optional)
    word_count_greater_than = 56 # int | News stories will have a word count greater than this value. Unsupported for yahoo source. (provider: intrinio) (optional)
    word_count_less_than = 56 # int | News stories will have a word count less than this value. Unsupported for yahoo source. (provider: intrinio) (optional)
    is_spam = True # bool | Filter whether it is marked as spam or not. Unsupported for yahoo source. (provider: intrinio) (optional)
    business_relevance_greater_than = 3.4 # float | News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) (optional)
    business_relevance_less_than = 3.4 # float | News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) (optional)
    offset = 56 # int | Page offset, used in conjunction with limit. (provider: tiingo) (optional)

    try:
        # Company
        api_response = api_instance.news_company(provider, symbol=symbol, start_date=start_date, end_date=end_date, limit=limit, var_date=var_date, display=display, updated_since=updated_since, published_since=published_since, sort=sort, order=order, isin=isin, cusip=cusip, channels=channels, topics=topics, authors=authors, content_types=content_types, page=page, source=source, sentiment=sentiment, language=language, topic=topic, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, offset=offset)
        print("The response of NewsApi->news_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->news_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): benzinga, fmp, intrinio, polygon, tiingo, yfinance. | [optional] 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **limit** | **int**| The number of data entries to return. | [optional] 
 **var_date** | **date**| A specific date to get data for. (provider: benzinga) | [optional] 
 **display** | **str**| Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga) | [optional] [default to full]
 **updated_since** | **int**| Number of seconds since the news was updated. (provider: benzinga) | [optional] 
 **published_since** | **int**| Number of seconds since the news was published. (provider: benzinga) | [optional] 
 **sort** | **str**| Key to sort the news by. (provider: benzinga) | [optional] [default to created]
 **order** | **str**| Order to sort the news by. (provider: benzinga);     Sort order of the articles. (provider: polygon) | [optional] [default to desc]
 **isin** | **str**| The company&#39;s ISIN. (provider: benzinga) | [optional] 
 **cusip** | **str**| The company&#39;s CUSIP. (provider: benzinga) | [optional] 
 **channels** | **str**| Channels of the news to retrieve. (provider: benzinga) | [optional] 
 **topics** | **str**| Topics of the news to retrieve. (provider: benzinga) | [optional] 
 **authors** | **str**| Authors of the news to retrieve. (provider: benzinga) | [optional] 
 **content_types** | **str**| Content types of the news to retrieve. (provider: benzinga) | [optional] 
 **page** | **int**| Page number of the results. Use in combination with limit. (provider: fmp) | [optional] 
 **source** | [**IntrinioTiingo1**](.md)| The source of the news article. (provider: intrinio);     A comma-separated list of the domains requested. Multiple comma separated items allowed. (provider: tiingo) | [optional] 
 **sentiment** | **str**| Return news only from this source. (provider: intrinio) | [optional] 
 **language** | **str**| Filter by language. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **topic** | **str**| Filter by topic. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **word_count_greater_than** | **int**| News stories will have a word count greater than this value. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **word_count_less_than** | **int**| News stories will have a word count less than this value. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **is_spam** | **bool**| Filter whether it is marked as spam or not. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **business_relevance_greater_than** | **float**| News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) | [optional] 
 **business_relevance_less_than** | **float**| News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) | [optional] 
 **offset** | **int**| Page offset, used in conjunction with limit. (provider: tiingo) | [optional] 

### Return type

[**OBBjectCompanyNews**](OBBjectCompanyNews.md)

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

# **news_world**
> OBBjectWorldNews news_world(provider, limit=limit, start_date=start_date, end_date=end_date, var_date=var_date, display=display, updated_since=updated_since, published_since=published_since, sort=sort, order=order, isin=isin, cusip=cusip, channels=channels, topics=topics, authors=authors, content_types=content_types, source=source, sentiment=sentiment, language=language, topic=topic, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, offset=offset)

World

World News. Global news data.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_world_news import OBBjectWorldNews
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
    api_instance = openbb_client.NewsApi(api_client)
    provider = 'provider_example' # str | 
    limit = 2500 # int | The number of data entries to return. The number of articles to return. (optional) (default to 2500)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    var_date = '2013-10-20' # date | A specific date to get data for. (provider: benzinga) (optional)
    display = full # str | Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga) (optional) (default to full)
    updated_since = 56 # int | Number of seconds since the news was updated. (provider: benzinga) (optional)
    published_since = 56 # int | Number of seconds since the news was published. (provider: benzinga) (optional)
    sort = created # str | Key to sort the news by. (provider: benzinga) (optional) (default to created)
    order = desc # str | Order to sort the news by. (provider: benzinga) (optional) (default to desc)
    isin = 'isin_example' # str | The ISIN of the news to retrieve. (provider: benzinga) (optional)
    cusip = 'cusip_example' # str | The CUSIP of the news to retrieve. (provider: benzinga) (optional)
    channels = 'channels_example' # str | Channels of the news to retrieve. (provider: benzinga) (optional)
    topics = 'topics_example' # str | Topics of the news to retrieve. (provider: benzinga) (optional)
    authors = 'authors_example' # str | Authors of the news to retrieve. (provider: benzinga) (optional)
    content_types = 'content_types_example' # str | Content types of the news to retrieve. (provider: benzinga) (optional)
    source = openbb_client.IntrinioTiingo() # IntrinioTiingo | The source of the news article. (provider: intrinio);     A comma-separated list of the domains requested. Multiple comma separated items allowed. (provider: tiingo) (optional)
    sentiment = 'sentiment_example' # str | Return news only from this source. (provider: intrinio) (optional)
    language = 'language_example' # str | Filter by language. Unsupported for yahoo source. (provider: intrinio) (optional)
    topic = 'topic_example' # str | Filter by topic. Unsupported for yahoo source. (provider: intrinio) (optional)
    word_count_greater_than = 56 # int | News stories will have a word count greater than this value. Unsupported for yahoo source. (provider: intrinio) (optional)
    word_count_less_than = 56 # int | News stories will have a word count less than this value. Unsupported for yahoo source. (provider: intrinio) (optional)
    is_spam = True # bool | Filter whether it is marked as spam or not. Unsupported for yahoo source. (provider: intrinio) (optional)
    business_relevance_greater_than = 3.4 # float | News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) (optional)
    business_relevance_less_than = 3.4 # float | News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) (optional)
    offset = 56 # int | Page offset, used in conjunction with limit. (provider: tiingo) (optional)

    try:
        # World
        api_response = api_instance.news_world(provider, limit=limit, start_date=start_date, end_date=end_date, var_date=var_date, display=display, updated_since=updated_since, published_since=published_since, sort=sort, order=order, isin=isin, cusip=cusip, channels=channels, topics=topics, authors=authors, content_types=content_types, source=source, sentiment=sentiment, language=language, topic=topic, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, offset=offset)
        print("The response of NewsApi->news_world:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->news_world: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **limit** | **int**| The number of data entries to return. The number of articles to return. | [optional] [default to 2500]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **var_date** | **date**| A specific date to get data for. (provider: benzinga) | [optional] 
 **display** | **str**| Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga) | [optional] [default to full]
 **updated_since** | **int**| Number of seconds since the news was updated. (provider: benzinga) | [optional] 
 **published_since** | **int**| Number of seconds since the news was published. (provider: benzinga) | [optional] 
 **sort** | **str**| Key to sort the news by. (provider: benzinga) | [optional] [default to created]
 **order** | **str**| Order to sort the news by. (provider: benzinga) | [optional] [default to desc]
 **isin** | **str**| The ISIN of the news to retrieve. (provider: benzinga) | [optional] 
 **cusip** | **str**| The CUSIP of the news to retrieve. (provider: benzinga) | [optional] 
 **channels** | **str**| Channels of the news to retrieve. (provider: benzinga) | [optional] 
 **topics** | **str**| Topics of the news to retrieve. (provider: benzinga) | [optional] 
 **authors** | **str**| Authors of the news to retrieve. (provider: benzinga) | [optional] 
 **content_types** | **str**| Content types of the news to retrieve. (provider: benzinga) | [optional] 
 **source** | [**IntrinioTiingo**](.md)| The source of the news article. (provider: intrinio);     A comma-separated list of the domains requested. Multiple comma separated items allowed. (provider: tiingo) | [optional] 
 **sentiment** | **str**| Return news only from this source. (provider: intrinio) | [optional] 
 **language** | **str**| Filter by language. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **topic** | **str**| Filter by topic. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **word_count_greater_than** | **int**| News stories will have a word count greater than this value. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **word_count_less_than** | **int**| News stories will have a word count less than this value. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **is_spam** | **bool**| Filter whether it is marked as spam or not. Unsupported for yahoo source. (provider: intrinio) | [optional] 
 **business_relevance_greater_than** | **float**| News stories will have a business relevance score more than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) | [optional] 
 **business_relevance_less_than** | **float**| News stories will have a business relevance score less than this value. Unsupported for yahoo source. Value is a decimal between 0 and 1. (provider: intrinio) | [optional] 
 **offset** | **int**| Page offset, used in conjunction with limit. (provider: tiingo) | [optional] 

### Return type

[**OBBjectWorldNews**](OBBjectWorldNews.md)

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

