# openbb_client.FixedincomeApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fixedincome_bond_indices**](FixedincomeApi.md#fixedincome_bond_indices) | **GET** /api/v1/fixedincome/bond_indices | Bond Indices
[**fixedincome_corporate_commercial_paper**](FixedincomeApi.md#fixedincome_corporate_commercial_paper) | **GET** /api/v1/fixedincome/corporate/commercial_paper | Commercial Paper
[**fixedincome_corporate_hqm**](FixedincomeApi.md#fixedincome_corporate_hqm) | **GET** /api/v1/fixedincome/corporate/hqm | Hqm
[**fixedincome_corporate_ice_bofa**](FixedincomeApi.md#fixedincome_corporate_ice_bofa) | **GET** /api/v1/fixedincome/corporate/ice_bofa | This endpoint is deprecated; use &#x60;/fixedincome/bond_indices&#x60; instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
[**fixedincome_corporate_moody**](FixedincomeApi.md#fixedincome_corporate_moody) | **GET** /api/v1/fixedincome/corporate/moody | This endpoint is deprecated; use &#x60;/fixedincome/bond_indices&#x60; instead. Set &#x60;category&#x60; to &#x60;us&#x60; and &#x60;index&#x60; to &#x60;seasoned_corporate&#x60;. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
[**fixedincome_corporate_spot_rates**](FixedincomeApi.md#fixedincome_corporate_spot_rates) | **GET** /api/v1/fixedincome/corporate/spot_rates | Spot Rates
[**fixedincome_government_tips_yields**](FixedincomeApi.md#fixedincome_government_tips_yields) | **GET** /api/v1/fixedincome/government/tips_yields | Tips Yields
[**fixedincome_government_treasury_rates**](FixedincomeApi.md#fixedincome_government_treasury_rates) | **GET** /api/v1/fixedincome/government/treasury_rates | Treasury Rates
[**fixedincome_government_us_yield_curve**](FixedincomeApi.md#fixedincome_government_us_yield_curve) | **GET** /api/v1/fixedincome/government/us_yield_curve | This endpoint will be removed in a future version. Use, &#x60;/fixedincome/government/yield_curve&#x60;, instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.4.
[**fixedincome_government_yield_curve**](FixedincomeApi.md#fixedincome_government_yield_curve) | **GET** /api/v1/fixedincome/government/yield_curve | Yield Curve
[**fixedincome_mortgage_indices**](FixedincomeApi.md#fixedincome_mortgage_indices) | **GET** /api/v1/fixedincome/mortgage_indices | Mortgage Indices
[**fixedincome_rate_ameribor**](FixedincomeApi.md#fixedincome_rate_ameribor) | **GET** /api/v1/fixedincome/rate/ameribor | Ameribor
[**fixedincome_rate_dpcredit**](FixedincomeApi.md#fixedincome_rate_dpcredit) | **GET** /api/v1/fixedincome/rate/dpcredit | Dpcredit
[**fixedincome_rate_ecb**](FixedincomeApi.md#fixedincome_rate_ecb) | **GET** /api/v1/fixedincome/rate/ecb | Ecb
[**fixedincome_rate_effr**](FixedincomeApi.md#fixedincome_rate_effr) | **GET** /api/v1/fixedincome/rate/effr | Effr
[**fixedincome_rate_effr_forecast**](FixedincomeApi.md#fixedincome_rate_effr_forecast) | **GET** /api/v1/fixedincome/rate/effr_forecast | Effr Forecast
[**fixedincome_rate_estr**](FixedincomeApi.md#fixedincome_rate_estr) | **GET** /api/v1/fixedincome/rate/estr | Estr
[**fixedincome_rate_iorb**](FixedincomeApi.md#fixedincome_rate_iorb) | **GET** /api/v1/fixedincome/rate/iorb | Iorb
[**fixedincome_rate_overnight_bank_funding**](FixedincomeApi.md#fixedincome_rate_overnight_bank_funding) | **GET** /api/v1/fixedincome/rate/overnight_bank_funding | Overnight Bank Funding
[**fixedincome_rate_sofr**](FixedincomeApi.md#fixedincome_rate_sofr) | **GET** /api/v1/fixedincome/rate/sofr | Sofr
[**fixedincome_rate_sonia**](FixedincomeApi.md#fixedincome_rate_sonia) | **GET** /api/v1/fixedincome/rate/sonia | Sonia
[**fixedincome_sofr**](FixedincomeApi.md#fixedincome_sofr) | **GET** /api/v1/fixedincome/sofr | This endpoint is deprecated; use &#x60;/fixedincome/rate/sofr&#x60; instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
[**fixedincome_spreads_tcm**](FixedincomeApi.md#fixedincome_spreads_tcm) | **GET** /api/v1/fixedincome/spreads/tcm | Tcm
[**fixedincome_spreads_tcm_effr**](FixedincomeApi.md#fixedincome_spreads_tcm_effr) | **GET** /api/v1/fixedincome/spreads/tcm_effr | Tcm Effr
[**fixedincome_spreads_treasury_effr**](FixedincomeApi.md#fixedincome_spreads_treasury_effr) | **GET** /api/v1/fixedincome/spreads/treasury_effr | Treasury Effr


# **fixedincome_bond_indices**
> OBBjectBondIndices fixedincome_bond_indices(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, category=category, index=index, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Bond Indices

Bond Indices.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_bond_indices import OBBjectBondIndices
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    index_type = yield # str | The type of series. OAS is the option-adjusted spread. Default is yield. (optional) (default to yield)
    category = us # str | The type of index category. Used in conjunction with 'index', default is 'us'. (provider: fred) (optional) (default to us)
    index = 'yield_curve' # str | The specific index to query. Used in conjunction with 'category' and 'index_type', default is 'yield_curve'. Multiple comma separated items allowed. (provider: fred) (optional) (default to 'yield_curve')
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = avg # str |          A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is 'avg'.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional) (default to avg)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Bond Indices
        api_response = api_instance.fixedincome_bond_indices(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, category=category, index=index, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_bond_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_bond_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **index_type** | **str**| The type of series. OAS is the option-adjusted spread. Default is yield. | [optional] [default to yield]
 **category** | **str**| The type of index category. Used in conjunction with &#39;index&#39;, default is &#39;us&#39;. (provider: fred) | [optional] [default to us]
 **index** | **str**| The specific index to query. Used in conjunction with &#39;category&#39; and &#39;index_type&#39;, default is &#39;yield_curve&#39;. Multiple comma separated items allowed. (provider: fred) | [optional] [default to &#39;yield_curve&#39;]
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             None &#x3D; No change             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             d &#x3D; Daily             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is &#39;avg&#39;.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] [default to avg]
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectBondIndices**](OBBjectBondIndices.md)

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

# **fixedincome_corporate_commercial_paper**
> OBBjectCommercialPaper fixedincome_corporate_commercial_paper(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, category=category, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Commercial Paper

Commercial Paper.  Commercial paper (CP) consists of short-term, promissory notes issued primarily by corporations. Maturities range up to 270 days but average about 30 days. Many companies use CP to raise cash needed for current transactions, and many find it to be a lower-cost alternative to bank loans.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_commercial_paper import OBBjectCommercialPaper
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = openbb_client.Fred2() # Fred2 | A target maturity. Multiple comma separated items allowed. (provider: fred) (optional)
    category = openbb_client.Fred3() # Fred3 | The category of asset. Multiple comma separated items allowed. (provider: fred) (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Commercial Paper
        api_response = api_instance.fixedincome_corporate_commercial_paper(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, category=category, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_corporate_commercial_paper:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_corporate_commercial_paper: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | [**Fred2**](.md)| A target maturity. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **category** | [**Fred3**](.md)| The category of asset. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectCommercialPaper**](OBBjectCommercialPaper.md)

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

# **fixedincome_corporate_hqm**
> OBBjectHighQualityMarketCorporateBond fixedincome_corporate_hqm(provider=provider, var_date=var_date, yield_curve=yield_curve)

Hqm

High Quality Market Corporate Bond.  The HQM yield curve represents the high quality corporate bond market, i.e., corporate bonds rated AAA, AA, or A.  The HQM curve contains two regression terms. These terms are adjustment factors that blend AAA, AA, and A bonds into a single HQM yield curve that is the market-weighted average (MWA) quality of high quality bonds.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_high_quality_market_corporate_bond import OBBjectHighQualityMarketCorporateBond
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    var_date = openbb_client.Date5() # Date5 | A specific date to get data for. Multiple comma separated items allowed for provider(s): fred. (optional)
    yield_curve = spot # str | The yield curve type. (provider: fred) (optional) (default to spot)

    try:
        # Hqm
        api_response = api_instance.fixedincome_corporate_hqm(provider=provider, var_date=var_date, yield_curve=yield_curve)
        print("The response of FixedincomeApi->fixedincome_corporate_hqm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_corporate_hqm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **var_date** | [**Date5**](.md)| A specific date to get data for. Multiple comma separated items allowed for provider(s): fred. | [optional] 
 **yield_curve** | **str**| The yield curve type. (provider: fred) | [optional] [default to spot]

### Return type

[**OBBjectHighQualityMarketCorporateBond**](OBBjectHighQualityMarketCorporateBond.md)

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

# **fixedincome_corporate_ice_bofa**
> OBBjectICEBofA fixedincome_corporate_ice_bofa(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, category=category, area=area, grade=grade, options=options)

This endpoint is deprecated; use `/fixedincome/bond_indices` instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.

ICE BofA US Corporate Bond Indices.  The ICE BofA US Corporate Index tracks the performance of US dollar denominated investment grade corporate debt publicly issued in the US domestic market. Qualifying securities must have an investment grade rating (based on an average of Moody’s, S&P and Fitch), at least 18 months to final maturity at the time of issuance, at least one year remaining term to final maturity as of the rebalance date, a fixed coupon schedule and a minimum amount outstanding of $250 million. The ICE BofA US Corporate Index is a component of the US Corporate Master Index.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_ice_bof_a import OBBjectICEBofA
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    index_type = yield # str | The type of series. (optional) (default to yield)
    category = all # str | The type of category. (provider: fred) (optional) (default to all)
    area = us # str | The type of area. (provider: fred) (optional) (default to us)
    grade = non_sovereign # str | The type of grade. (provider: fred) (optional) (default to non_sovereign)
    options = False # bool | Whether to include options in the results. (provider: fred) (optional) (default to False)

    try:
        # This endpoint is deprecated; use `/fixedincome/bond_indices` instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
        api_response = api_instance.fixedincome_corporate_ice_bofa(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, category=category, area=area, grade=grade, options=options)
        print("The response of FixedincomeApi->fixedincome_corporate_ice_bofa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_corporate_ice_bofa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **index_type** | **str**| The type of series. | [optional] [default to yield]
 **category** | **str**| The type of category. (provider: fred) | [optional] [default to all]
 **area** | **str**| The type of area. (provider: fred) | [optional] [default to us]
 **grade** | **str**| The type of grade. (provider: fred) | [optional] [default to non_sovereign]
 **options** | **bool**| Whether to include options in the results. (provider: fred) | [optional] [default to False]

### Return type

[**OBBjectICEBofA**](OBBjectICEBofA.md)

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

# **fixedincome_corporate_moody**
> OBBjectMoodyCorporateBondIndex fixedincome_corporate_moody(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, spread=spread)

This endpoint is deprecated; use `/fixedincome/bond_indices` instead. Set `category` to `us` and `index` to `seasoned_corporate`. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.

Moody Corporate Bond Index.  Moody's Aaa and Baa are investment bonds that acts as an index of the performance of all bonds given an Aaa or Baa rating by Moody's Investors Service respectively. These corporate bonds often are used in macroeconomics as an alternative to the federal ten-year Treasury Bill as an indicator of the interest rate.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_moody_corporate_bond_index import OBBjectMoodyCorporateBondIndex
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    index_type = aaa # str | The type of series. (optional) (default to aaa)
    spread = 'spread_example' # str | The type of spread. (provider: fred) (optional)

    try:
        # This endpoint is deprecated; use `/fixedincome/bond_indices` instead. Set `category` to `us` and `index` to `seasoned_corporate`. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
        api_response = api_instance.fixedincome_corporate_moody(provider=provider, start_date=start_date, end_date=end_date, index_type=index_type, spread=spread)
        print("The response of FixedincomeApi->fixedincome_corporate_moody:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_corporate_moody: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **index_type** | **str**| The type of series. | [optional] [default to aaa]
 **spread** | **str**| The type of spread. (provider: fred) | [optional] 

### Return type

[**OBBjectMoodyCorporateBondIndex**](OBBjectMoodyCorporateBondIndex.md)

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

# **fixedincome_corporate_spot_rates**
> OBBjectSpotRate fixedincome_corporate_spot_rates(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, category=category)

Spot Rates

Spot Rates.  The spot rates for any maturity is the yield on a bond that provides a single payment at that maturity. This is a zero coupon bond. Because each spot rate pertains to a single cashflow, it is the relevant interest rate concept for discounting a pension liability at the same maturity.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_spot_rate import OBBjectSpotRate
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = openbb_client.Maturity() # Maturity | Maturities in years. Multiple comma separated items allowed for provider(s): fred. (optional)
    category = 'spot_rate' # str | Rate category. Options: spot_rate, par_yield. Multiple comma separated items allowed for provider(s): fred. (optional) (default to 'spot_rate')

    try:
        # Spot Rates
        api_response = api_instance.fixedincome_corporate_spot_rates(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, category=category)
        print("The response of FixedincomeApi->fixedincome_corporate_spot_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_corporate_spot_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | [**Maturity**](.md)| Maturities in years. Multiple comma separated items allowed for provider(s): fred. | [optional] 
 **category** | **str**| Rate category. Options: spot_rate, par_yield. Multiple comma separated items allowed for provider(s): fred. | [optional] [default to &#39;spot_rate&#39;]

### Return type

[**OBBjectSpotRate**](OBBjectSpotRate.md)

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

# **fixedincome_government_tips_yields**
> OBBjectTipsYields fixedincome_government_tips_yields(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Tips Yields

Get current Treasury inflation-protected securities yields.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_tips_yields import OBBjectTipsYields
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = 56 # int | The maturity of the security in years - 5, 10, 20, 30 - defaults to all. Note that the maturity is the tenor of the security, not the time to maturity. (provider: fred) (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert high frequency data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change          (provider: fred) (optional)

    try:
        # Tips Yields
        api_response = api_instance.fixedincome_government_tips_yields(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_government_tips_yields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_government_tips_yields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | **int**| The maturity of the security in years - 5, 10, 20, 30 - defaults to all. Note that the maturity is the tenor of the security, not the time to maturity. (provider: fred) | [optional] 
 **frequency** | **str**| Frequency aggregation to convert high frequency data to lower frequency.             None &#x3D; No change             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             d &#x3D; Daily             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change          (provider: fred) | [optional] 

### Return type

[**OBBjectTipsYields**](OBBjectTipsYields.md)

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

# **fixedincome_government_treasury_rates**
> OBBjectTreasuryRates fixedincome_government_treasury_rates(provider, start_date=start_date, end_date=end_date)

Treasury Rates

Government Treasury Rates.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_treasury_rates import OBBjectTreasuryRates
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)

    try:
        # Treasury Rates
        api_response = api_instance.fixedincome_government_treasury_rates(provider, start_date=start_date, end_date=end_date)
        print("The response of FixedincomeApi->fixedincome_government_treasury_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_government_treasury_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 

### Return type

[**OBBjectTreasuryRates**](OBBjectTreasuryRates.md)

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

# **fixedincome_government_us_yield_curve**
> OBBjectUSYieldCurve fixedincome_government_us_yield_curve(provider=provider, var_date=var_date, inflation_adjusted=inflation_adjusted)

This endpoint will be removed in a future version. Use, `/fixedincome/government/yield_curve`, instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.4.

US Yield Curve. Get United States yield curve.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_us_yield_curve import OBBjectUSYieldCurve
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    var_date = '2013-10-20' # date | A specific date to get data for. Defaults to the most recent FRED entry. (optional)
    inflation_adjusted = True # bool | Get inflation adjusted rates. (optional)

    try:
        # This endpoint will be removed in a future version. Use, `/fixedincome/government/yield_curve`, instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.4.
        api_response = api_instance.fixedincome_government_us_yield_curve(provider=provider, var_date=var_date, inflation_adjusted=inflation_adjusted)
        print("The response of FixedincomeApi->fixedincome_government_us_yield_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_government_us_yield_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **var_date** | **date**| A specific date to get data for. Defaults to the most recent FRED entry. | [optional] 
 **inflation_adjusted** | **bool**| Get inflation adjusted rates. | [optional] 

### Return type

[**OBBjectUSYieldCurve**](OBBjectUSYieldCurve.md)

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

# **fixedincome_government_yield_curve**
> OBBjectYieldCurve fixedincome_government_yield_curve(provider, var_date=var_date, country=country, use_cache=use_cache, yield_curve_type=yield_curve_type)

Yield Curve

Get yield curve data by country and date.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_yield_curve import OBBjectYieldCurve
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    var_date = openbb_client.Date4() # Date4 | A specific date to get data for. By default is the current data. Multiple comma separated items allowed for provider(s): econdb, federal_reserve, fmp, fred. (optional)
    country = 'united_states' # str | The country to get data. New Zealand, Mexico, Singapore, and Thailand have only monthly data. The nearest date to the requested one will be used. Multiple comma separated items allowed. (provider: econdb) (optional) (default to 'united_states')
    use_cache = True # bool | If true, cache the request for four hours. (provider: econdb) (optional) (default to True)
    yield_curve_type = nominal # str | Yield curve type. Nominal and Real Rates are available daily, others are monthly. The closest date to the requested date will be returned. (provider: fred) (optional) (default to nominal)

    try:
        # Yield Curve
        api_response = api_instance.fixedincome_government_yield_curve(provider, var_date=var_date, country=country, use_cache=use_cache, yield_curve_type=yield_curve_type)
        print("The response of FixedincomeApi->fixedincome_government_yield_curve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_government_yield_curve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **var_date** | [**Date4**](.md)| A specific date to get data for. By default is the current data. Multiple comma separated items allowed for provider(s): econdb, federal_reserve, fmp, fred. | [optional] 
 **country** | **str**| The country to get data. New Zealand, Mexico, Singapore, and Thailand have only monthly data. The nearest date to the requested one will be used. Multiple comma separated items allowed. (provider: econdb) | [optional] [default to &#39;united_states&#39;]
 **use_cache** | **bool**| If true, cache the request for four hours. (provider: econdb) | [optional] [default to True]
 **yield_curve_type** | **str**| Yield curve type. Nominal and Real Rates are available daily, others are monthly. The closest date to the requested date will be returned. (provider: fred) | [optional] [default to nominal]

### Return type

[**OBBjectYieldCurve**](OBBjectYieldCurve.md)

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

# **fixedincome_mortgage_indices**
> OBBjectMortgageIndices fixedincome_mortgage_indices(provider=provider, start_date=start_date, end_date=end_date, index=index, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Mortgage Indices

Mortgage Indices.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_mortgage_indices import OBBjectMortgageIndices
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    index = openbb_client.Fred4() # Fred4 | The specific index, or index group, to query. Default is the 'primary' group. Multiple comma separated items allowed. (provider: fred) (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             None = No change             a = Annual             q = Quarterly             m = Monthly             w = Weekly             d = Daily             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = avg # str |          A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is 'avg'.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional) (default to avg)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Mortgage Indices
        api_response = api_instance.fixedincome_mortgage_indices(provider=provider, start_date=start_date, end_date=end_date, index=index, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_mortgage_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_mortgage_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **index** | [**Fred4**](.md)| The specific index, or index group, to query. Default is the &#39;primary&#39; group. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             None &#x3D; No change             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             d &#x3D; Daily             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set, default is &#39;avg&#39;.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] [default to avg]
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectMortgageIndices**](OBBjectMortgageIndices.md)

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

# **fixedincome_rate_ameribor**
> OBBjectAmeribor fixedincome_rate_ameribor(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Ameribor

AMERIBOR.  AMERIBOR (short for the American interbank offered rate) is a benchmark interest rate that reflects the true cost of short-term interbank borrowing. This rate is based on transactions in overnight unsecured loans conducted on the American Financial Exchange (AFX).

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_ameribor import OBBjectAmeribor
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = openbb_client.Fred1() # Fred1 | Period of AMERIBOR rate. Multiple comma separated items allowed. (provider: fred) (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Ameribor
        api_response = api_instance.fixedincome_rate_ameribor(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_rate_ameribor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_ameribor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | [**Fred1**](.md)| Period of AMERIBOR rate. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectAmeribor**](OBBjectAmeribor.md)

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

# **fixedincome_rate_dpcredit**
> OBBjectDiscountWindowPrimaryCreditRate fixedincome_rate_dpcredit(provider=provider, start_date=start_date, end_date=end_date, parameter=parameter)

Dpcredit

Discount Window Primary Credit Rate.  A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board of Governors set the bank rate, also known as the discount rate.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_discount_window_primary_credit_rate import OBBjectDiscountWindowPrimaryCreditRate
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    parameter = daily_excl_weekend # str | FRED series ID of DWPCR data. (provider: fred) (optional) (default to daily_excl_weekend)

    try:
        # Dpcredit
        api_response = api_instance.fixedincome_rate_dpcredit(provider=provider, start_date=start_date, end_date=end_date, parameter=parameter)
        print("The response of FixedincomeApi->fixedincome_rate_dpcredit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_dpcredit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **parameter** | **str**| FRED series ID of DWPCR data. (provider: fred) | [optional] [default to daily_excl_weekend]

### Return type

[**OBBjectDiscountWindowPrimaryCreditRate**](OBBjectDiscountWindowPrimaryCreditRate.md)

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

# **fixedincome_rate_ecb**
> OBBjectEuropeanCentralBankInterestRates fixedincome_rate_ecb(provider=provider, start_date=start_date, end_date=end_date, interest_rate_type=interest_rate_type)

Ecb

European Central Bank Interest Rates.  The Governing Council of the ECB sets the key interest rates for the euro area:  - The interest rate on the main refinancing operations (MRO), which provide the bulk of liquidity to the banking system. - The rate on the deposit facility, which banks may use to make overnight deposits with the Eurosystem. - The rate on the marginal lending facility, which offers overnight credit to banks from the Eurosystem.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_european_central_bank_interest_rates import OBBjectEuropeanCentralBankInterestRates
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    interest_rate_type = lending # str | The type of interest rate. (optional) (default to lending)

    try:
        # Ecb
        api_response = api_instance.fixedincome_rate_ecb(provider=provider, start_date=start_date, end_date=end_date, interest_rate_type=interest_rate_type)
        print("The response of FixedincomeApi->fixedincome_rate_ecb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_ecb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **interest_rate_type** | **str**| The type of interest rate. | [optional] [default to lending]

### Return type

[**OBBjectEuropeanCentralBankInterestRates**](OBBjectEuropeanCentralBankInterestRates.md)

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

# **fixedincome_rate_effr**
> OBBjectFederalFundsRate fixedincome_rate_effr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform, effr_only=effr_only)

Effr

Fed Funds Rate.  Get Effective Federal Funds Rate data. A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates central banks charge are set to stabilize the economy.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_federal_funds_rate import OBBjectFederalFundsRate
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)
    effr_only = False # bool | Return data without quantiles, target ranges, and volume. (provider: fred) (optional) (default to False)

    try:
        # Effr
        api_response = api_instance.fixedincome_rate_effr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform, effr_only=effr_only)
        print("The response of FixedincomeApi->fixedincome_rate_effr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_effr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 
 **effr_only** | **bool**| Return data without quantiles, target ranges, and volume. (provider: fred) | [optional] [default to False]

### Return type

[**OBBjectFederalFundsRate**](OBBjectFederalFundsRate.md)

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

# **fixedincome_rate_effr_forecast**
> OBBjectPROJECTIONS fixedincome_rate_effr_forecast(provider=provider, long_run=long_run)

Effr Forecast

Fed Funds Rate Projections.  The projections for the federal funds rate are the value of the midpoint of the projected appropriate target range for the federal funds rate or the projected appropriate target level for the federal funds rate at the end of the specified calendar year or over the longer run.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_projections import OBBjectPROJECTIONS
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    long_run = False # bool | Flag to show long run projections (provider: fred) (optional) (default to False)

    try:
        # Effr Forecast
        api_response = api_instance.fixedincome_rate_effr_forecast(provider=provider, long_run=long_run)
        print("The response of FixedincomeApi->fixedincome_rate_effr_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_effr_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **long_run** | **bool**| Flag to show long run projections (provider: fred) | [optional] [default to False]

### Return type

[**OBBjectPROJECTIONS**](OBBjectPROJECTIONS.md)

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

# **fixedincome_rate_estr**
> OBBjectEuroShortTermRate fixedincome_rate_estr(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Estr

Euro Short-Term Rate.  The euro short-term rate (€STR) reflects the wholesale euro unsecured overnight borrowing costs of banks located in the euro area. The €STR is published on each TARGET2 business day based on transactions conducted and settled on the previous TARGET2 business day (the reporting date “T”) with a maturity date of T+1 which are deemed to have been executed at arm's length and thus reflect market rates in an unbiased way.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_euro_short_term_rate import OBBjectEuroShortTermRate
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert daily data to lower frequency.              a = Annual              q = Quarterly              m = Monthly              w = Weekly              d = Daily              wef = Weekly, Ending Friday              weth = Weekly, Ending Thursday              wew = Weekly, Ending Wednesday              wetu = Weekly, Ending Tuesday              wem = Weekly, Ending Monday              wesu = Weekly, Ending Sunday              wesa = Weekly, Ending Saturday              bwew = Biweekly, Ending Wednesday              bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log          (provider: fred) (optional)

    try:
        # Estr
        api_response = api_instance.fixedincome_rate_estr(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_rate_estr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_estr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**| Frequency aggregation to convert daily data to lower frequency.              a &#x3D; Annual              q &#x3D; Quarterly              m &#x3D; Monthly              w &#x3D; Weekly              d &#x3D; Daily              wef &#x3D; Weekly, Ending Friday              weth &#x3D; Weekly, Ending Thursday              wew &#x3D; Weekly, Ending Wednesday              wetu &#x3D; Weekly, Ending Tuesday              wem &#x3D; Weekly, Ending Monday              wesu &#x3D; Weekly, Ending Sunday              wesa &#x3D; Weekly, Ending Saturday              bwew &#x3D; Biweekly, Ending Wednesday              bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.              avg &#x3D; Average              sum &#x3D; Sum              eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type              None &#x3D; No transformation              chg &#x3D; Change              ch1 &#x3D; Change from Year Ago              pch &#x3D; Percent Change              pc1 &#x3D; Percent Change from Year Ago              pca &#x3D; Compounded Annual Rate of Change              cch &#x3D; Continuously Compounded Rate of Change              cca &#x3D; Continuously Compounded Annual Rate of Change              log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectEuroShortTermRate**](OBBjectEuroShortTermRate.md)

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

# **fixedincome_rate_iorb**
> OBBjectIORB fixedincome_rate_iorb(provider=provider, start_date=start_date, end_date=end_date)

Iorb

Interest on Reserve Balances.  Get Interest Rate on Reserve Balances data A bank rate is the interest rate a nation's central bank charges to its domestic banks to borrow money. The rates central banks charge are set to stabilize the economy. In the United States, the Federal Reserve System's Board of Governors set the bank rate, also known as the discount rate.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_iorb import OBBjectIORB
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)

    try:
        # Iorb
        api_response = api_instance.fixedincome_rate_iorb(provider=provider, start_date=start_date, end_date=end_date)
        print("The response of FixedincomeApi->fixedincome_rate_iorb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_iorb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 

### Return type

[**OBBjectIORB**](OBBjectIORB.md)

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

# **fixedincome_rate_overnight_bank_funding**
> OBBjectOvernightBankFundingRate fixedincome_rate_overnight_bank_funding(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Overnight Bank Funding

Overnight Bank Funding.  For the United States, the overnight bank funding rate (OBFR) is calculated as a volume-weighted median of overnight federal funds transactions and Eurodollar transactions reported in the FR 2420 Report of Selected Money Market Rates.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_overnight_bank_funding_rate import OBBjectOvernightBankFundingRate
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Overnight Bank Funding
        api_response = api_instance.fixedincome_rate_overnight_bank_funding(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_rate_overnight_bank_funding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_overnight_bank_funding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectOvernightBankFundingRate**](OBBjectOvernightBankFundingRate.md)

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

# **fixedincome_rate_sofr**
> OBBjectSOFR fixedincome_rate_sofr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Sofr

Secured Overnight Financing Rate.  The Secured Overnight Financing Rate (SOFR) is a broad measure of the cost of borrowing cash overnight collateralizing by Treasury securities.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_sofr import OBBjectSOFR
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Sofr
        api_response = api_instance.fixedincome_rate_sofr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_rate_sofr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_sofr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectSOFR**](OBBjectSOFR.md)

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

# **fixedincome_rate_sonia**
> OBBjectSONIA fixedincome_rate_sonia(provider=provider, start_date=start_date, end_date=end_date, parameter=parameter)

Sonia

Sterling Overnight Index Average.  SONIA (Sterling Overnight Index Average) is an important interest rate benchmark. SONIA is based on actual transactions and reflects the average of the interest rates that banks pay to borrow sterling overnight from other financial institutions and other institutional investors.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_sonia import OBBjectSONIA
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    parameter = rate # str | Period of SONIA rate. (provider: fred) (optional) (default to rate)

    try:
        # Sonia
        api_response = api_instance.fixedincome_rate_sonia(provider=provider, start_date=start_date, end_date=end_date, parameter=parameter)
        print("The response of FixedincomeApi->fixedincome_rate_sonia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_rate_sonia: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **parameter** | **str**| Period of SONIA rate. (provider: fred) | [optional] [default to rate]

### Return type

[**OBBjectSONIA**](OBBjectSONIA.md)

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

# **fixedincome_sofr**
> OBBjectSOFR fixedincome_sofr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

This endpoint is deprecated; use `/fixedincome/rate/sofr` instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.

Secured Overnight Financing Rate.  The Secured Overnight Financing Rate (SOFR) is a broad measure of the cost of borrowing cash overnight collateralizing by Treasury securities.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_sofr import OBBjectSOFR
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert daily data to lower frequency.             a = Annual             q = Quarterly             m = Monthly             w = Weekly             wef = Weekly, Ending Friday             weth = Weekly, Ending Thursday             wew = Weekly, Ending Wednesday             wetu = Weekly, Ending Tuesday             wem = Weekly, Ending Monday             wesu = Weekly, Ending Sunday             wesa = Weekly, Ending Saturday             bwew = Biweekly, Ending Wednesday             bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # This endpoint is deprecated; use `/fixedincome/rate/sofr` instead. Deprecated in OpenBB Platform V4.2 to be removed in V4.5.
        api_response = api_instance.fixedincome_sofr(provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of FixedincomeApi->fixedincome_sofr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_sofr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert daily data to lower frequency.             a &#x3D; Annual             q &#x3D; Quarterly             m &#x3D; Monthly             w &#x3D; Weekly             wef &#x3D; Weekly, Ending Friday             weth &#x3D; Weekly, Ending Thursday             wew &#x3D; Weekly, Ending Wednesday             wetu &#x3D; Weekly, Ending Tuesday             wem &#x3D; Weekly, Ending Monday             wesu &#x3D; Weekly, Ending Sunday             wesa &#x3D; Weekly, Ending Saturday             bwew &#x3D; Biweekly, Ending Wednesday             bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectSOFR**](OBBjectSOFR.md)

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

# **fixedincome_spreads_tcm**
> OBBjectTreasuryConstantMaturity fixedincome_spreads_tcm(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)

Tcm

Treasury Constant Maturity.  Get data for 10-Year Treasury Constant Maturity Minus Selected Treasury Constant Maturity. Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S. Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_treasury_constant_maturity import OBBjectTreasuryConstantMaturity
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = 'maturity_example' # str | The maturity (optional)

    try:
        # Tcm
        api_response = api_instance.fixedincome_spreads_tcm(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)
        print("The response of FixedincomeApi->fixedincome_spreads_tcm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_spreads_tcm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | **str**| The maturity | [optional] 

### Return type

[**OBBjectTreasuryConstantMaturity**](OBBjectTreasuryConstantMaturity.md)

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

# **fixedincome_spreads_tcm_effr**
> OBBjectSelectedTreasuryConstantMaturity fixedincome_spreads_tcm_effr(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)

Tcm Effr

Select Treasury Constant Maturity.  Get data for Selected Treasury Constant Maturity Minus Federal Funds Rate Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S. Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_selected_treasury_constant_maturity import OBBjectSelectedTreasuryConstantMaturity
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = 'maturity_example' # str | The maturity (optional)

    try:
        # Tcm Effr
        api_response = api_instance.fixedincome_spreads_tcm_effr(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)
        print("The response of FixedincomeApi->fixedincome_spreads_tcm_effr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_spreads_tcm_effr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | **str**| The maturity | [optional] 

### Return type

[**OBBjectSelectedTreasuryConstantMaturity**](OBBjectSelectedTreasuryConstantMaturity.md)

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

# **fixedincome_spreads_treasury_effr**
> OBBjectSelectedTreasuryBill fixedincome_spreads_treasury_effr(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)

Treasury Effr

Select Treasury Bill.  Get Selected Treasury Bill Minus Federal Funds Rate. Constant maturity is the theoretical value of a U.S. Treasury that is based on recent values of auctioned U.S. Treasuries. The value is obtained by the U.S. Treasury on a daily basis through interpolation of the Treasury yield curve which, in turn, is based on closing bid-yields of actively-traded Treasury securities.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_selected_treasury_bill import OBBjectSelectedTreasuryBill
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
    api_instance = openbb_client.FixedincomeApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    maturity = 'maturity_example' # str | The maturity (optional)

    try:
        # Treasury Effr
        api_response = api_instance.fixedincome_spreads_treasury_effr(provider=provider, start_date=start_date, end_date=end_date, maturity=maturity)
        print("The response of FixedincomeApi->fixedincome_spreads_treasury_effr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FixedincomeApi->fixedincome_spreads_treasury_effr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **maturity** | **str**| The maturity | [optional] 

### Return type

[**OBBjectSelectedTreasuryBill**](OBBjectSelectedTreasuryBill.md)

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

