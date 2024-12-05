# openbb_client.EconomyApi

All URIs are relative to *http://127.0.0.1:8005*

Method | HTTP request | Description
------------- | ------------- | -------------
[**economy_available_indicators**](EconomyApi.md#economy_available_indicators) | **GET** /api/v1/economy/available_indicators | Available Indicators
[**economy_balance_of_payments**](EconomyApi.md#economy_balance_of_payments) | **GET** /api/v1/economy/balance_of_payments | Balance Of Payments
[**economy_calendar**](EconomyApi.md#economy_calendar) | **GET** /api/v1/economy/calendar | Calendar
[**economy_central_bank_holdings**](EconomyApi.md#economy_central_bank_holdings) | **GET** /api/v1/economy/central_bank_holdings | Central Bank Holdings
[**economy_composite_leading_indicator**](EconomyApi.md#economy_composite_leading_indicator) | **GET** /api/v1/economy/composite_leading_indicator | Composite Leading Indicator
[**economy_country_profile**](EconomyApi.md#economy_country_profile) | **GET** /api/v1/economy/country_profile | Country Profile
[**economy_cpi**](EconomyApi.md#economy_cpi) | **GET** /api/v1/economy/cpi | Cpi
[**economy_direction_of_trade**](EconomyApi.md#economy_direction_of_trade) | **GET** /api/v1/economy/direction_of_trade | Direction Of Trade
[**economy_export_destinations**](EconomyApi.md#economy_export_destinations) | **GET** /api/v1/economy/export_destinations | Export Destinations
[**economy_fred_regional**](EconomyApi.md#economy_fred_regional) | **GET** /api/v1/economy/fred_regional | Fred Regional
[**economy_fred_release_table**](EconomyApi.md#economy_fred_release_table) | **GET** /api/v1/economy/fred_release_table | Fred Release Table
[**economy_fred_search**](EconomyApi.md#economy_fred_search) | **GET** /api/v1/economy/fred_search | Fred Search
[**economy_fred_series**](EconomyApi.md#economy_fred_series) | **GET** /api/v1/economy/fred_series | Fred Series
[**economy_gdp_forecast**](EconomyApi.md#economy_gdp_forecast) | **GET** /api/v1/economy/gdp/forecast | Forecast
[**economy_gdp_nominal**](EconomyApi.md#economy_gdp_nominal) | **GET** /api/v1/economy/gdp/nominal | Nominal
[**economy_gdp_real**](EconomyApi.md#economy_gdp_real) | **GET** /api/v1/economy/gdp/real | Real
[**economy_house_price_index**](EconomyApi.md#economy_house_price_index) | **GET** /api/v1/economy/house_price_index | House Price Index
[**economy_immediate_interest_rate**](EconomyApi.md#economy_immediate_interest_rate) | **GET** /api/v1/economy/immediate_interest_rate | This endpoint will be removed in a future version. Use, &#x60;/economy/interest_rates&#x60;, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
[**economy_indicators**](EconomyApi.md#economy_indicators) | **GET** /api/v1/economy/indicators | Indicators
[**economy_interest_rates**](EconomyApi.md#economy_interest_rates) | **GET** /api/v1/economy/interest_rates | Interest Rates
[**economy_long_term_interest_rate**](EconomyApi.md#economy_long_term_interest_rate) | **GET** /api/v1/economy/long_term_interest_rate | This endpoint will be removed in a future version. Use, &#x60;/economy/interest_rates&#x60;, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
[**economy_money_measures**](EconomyApi.md#economy_money_measures) | **GET** /api/v1/economy/money_measures | Money Measures
[**economy_pce**](EconomyApi.md#economy_pce) | **GET** /api/v1/economy/pce | Pce
[**economy_port_volume**](EconomyApi.md#economy_port_volume) | **GET** /api/v1/economy/port_volume | Port Volume
[**economy_primary_dealer_fails**](EconomyApi.md#economy_primary_dealer_fails) | **GET** /api/v1/economy/primary_dealer_fails | Primary Dealer Fails
[**economy_primary_dealer_positioning**](EconomyApi.md#economy_primary_dealer_positioning) | **GET** /api/v1/economy/primary_dealer_positioning | Primary Dealer Positioning
[**economy_retail_prices**](EconomyApi.md#economy_retail_prices) | **GET** /api/v1/economy/retail_prices | Retail Prices
[**economy_risk_premium**](EconomyApi.md#economy_risk_premium) | **GET** /api/v1/economy/risk_premium | Risk Premium
[**economy_share_price_index**](EconomyApi.md#economy_share_price_index) | **GET** /api/v1/economy/share_price_index | Share Price Index
[**economy_short_term_interest_rate**](EconomyApi.md#economy_short_term_interest_rate) | **GET** /api/v1/economy/short_term_interest_rate | This endpoint will be removed in a future version. Use, &#x60;/economy/interest_rates&#x60;, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
[**economy_survey_bls_search**](EconomyApi.md#economy_survey_bls_search) | **GET** /api/v1/economy/survey/bls_search | Bls Search
[**economy_survey_bls_series**](EconomyApi.md#economy_survey_bls_series) | **GET** /api/v1/economy/survey/bls_series | Bls Series
[**economy_survey_economic_conditions_chicago**](EconomyApi.md#economy_survey_economic_conditions_chicago) | **GET** /api/v1/economy/survey/economic_conditions_chicago | Economic Conditions Chicago
[**economy_survey_manufacturing_outlook_texas**](EconomyApi.md#economy_survey_manufacturing_outlook_texas) | **GET** /api/v1/economy/survey/manufacturing_outlook_texas | Manufacturing Outlook Texas
[**economy_survey_nonfarm_payrolls**](EconomyApi.md#economy_survey_nonfarm_payrolls) | **GET** /api/v1/economy/survey/nonfarm_payrolls | Nonfarm Payrolls
[**economy_survey_sloos**](EconomyApi.md#economy_survey_sloos) | **GET** /api/v1/economy/survey/sloos | Sloos
[**economy_survey_university_of_michigan**](EconomyApi.md#economy_survey_university_of_michigan) | **GET** /api/v1/economy/survey/university_of_michigan | University Of Michigan
[**economy_unemployment**](EconomyApi.md#economy_unemployment) | **GET** /api/v1/economy/unemployment | Unemployment


# **economy_available_indicators**
> OBBjectAvailableIndicators economy_available_indicators(provider, use_cache=use_cache)

Available Indicators

Get the available economic indicators for a provider.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_available_indicators import OBBjectAvailableIndicators
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    use_cache = True # bool | Whether to use cache or not, by default is True The cache of indicator symbols will persist for one week. (provider: econdb) (optional) (default to True)

    try:
        # Available Indicators
        api_response = api_instance.economy_available_indicators(provider, use_cache=use_cache)
        print("The response of EconomyApi->economy_available_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_available_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **use_cache** | **bool**| Whether to use cache or not, by default is True The cache of indicator symbols will persist for one week. (provider: econdb) | [optional] [default to True]

### Return type

[**OBBjectAvailableIndicators**](OBBjectAvailableIndicators.md)

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

# **economy_balance_of_payments**
> OBBjectBalanceOfPayments economy_balance_of_payments(provider=provider, country=country, start_date=start_date, end_date=end_date)

Balance Of Payments

Balance of Payments Reports.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_balance_of_payments import OBBjectBalanceOfPayments
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    country = united_states # str | The country to get data. Enter as a 3-letter ISO country code, default is USA. (provider: fred) (optional) (default to united_states)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (provider: fred) (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (provider: fred) (optional)

    try:
        # Balance Of Payments
        api_response = api_instance.economy_balance_of_payments(provider=provider, country=country, start_date=start_date, end_date=end_date)
        print("The response of EconomyApi->economy_balance_of_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_balance_of_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **country** | **str**| The country to get data. Enter as a 3-letter ISO country code, default is USA. (provider: fred) | [optional] [default to united_states]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. (provider: fred) | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. (provider: fred) | [optional] 

### Return type

[**OBBjectBalanceOfPayments**](OBBjectBalanceOfPayments.md)

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

# **economy_calendar**
> OBBjectEconomicCalendar economy_calendar(provider, start_date=start_date, end_date=end_date, country=country, importance=importance, group=group, calendar_id=calendar_id)

Calendar

Get the upcoming, or historical, economic calendar of global events.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_economic_calendar import OBBjectEconomicCalendar
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = 'country_example' # str | Country of the event. Multiple comma separated items allowed. (provider: tradingeconomics) (optional)
    importance = 'importance_example' # str | Importance of the event. (provider: tradingeconomics) (optional)
    group = 'group_example' # str | Grouping of events. (provider: tradingeconomics) (optional)
    calendar_id = openbb_client.Tradingeconomics() # Tradingeconomics | Get events by TradingEconomics Calendar ID. Multiple comma separated items allowed. (provider: tradingeconomics) (optional)

    try:
        # Calendar
        api_response = api_instance.economy_calendar(provider, start_date=start_date, end_date=end_date, country=country, importance=importance, group=group, calendar_id=calendar_id)
        print("The response of EconomyApi->economy_calendar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_calendar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| Country of the event. Multiple comma separated items allowed. (provider: tradingeconomics) | [optional] 
 **importance** | **str**| Importance of the event. (provider: tradingeconomics) | [optional] 
 **group** | **str**| Grouping of events. (provider: tradingeconomics) | [optional] 
 **calendar_id** | [**Tradingeconomics**](.md)| Get events by TradingEconomics Calendar ID. Multiple comma separated items allowed. (provider: tradingeconomics) | [optional] 

### Return type

[**OBBjectEconomicCalendar**](OBBjectEconomicCalendar.md)

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

# **economy_central_bank_holdings**
> OBBjectCentralBankHoldings economy_central_bank_holdings(provider=provider, var_date=var_date, holding_type=holding_type, summary=summary, cusip=cusip, wam=wam, monthly=monthly)

Central Bank Holdings

Get the balance sheet holdings of a central bank.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_central_bank_holdings import OBBjectCentralBankHoldings
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = federal_reserve # str |  (optional) (default to federal_reserve)
    var_date = '2013-10-20' # date | A specific date to get data for. (optional)
    holding_type = all_treasury # str | Type of holdings to return. (provider: federal_reserve) (optional) (default to all_treasury)
    summary = False # bool | If True, returns historical weekly summary by holding type. This parameter takes priority over other parameters. (provider: federal_reserve) (optional) (default to False)
    cusip = 'cusip_example' # str |  Multiple comma separated items allowed. (optional)
    wam = False # bool | If True, returns weighted average maturity aggregated by agency or treasury securities. This parameter takes priority over `holding_type`, `cusip`, and `monthly`. (provider: federal_reserve) (optional) (default to False)
    monthly = False # bool | If True, returns historical data for all Treasury securities at a monthly interval. This parameter takes priority over other parameters, except `wam`. Only valid when `holding_type` is set to: 'all_treasury', 'bills', 'notesbonds', 'frn', 'tips'. (provider: federal_reserve) (optional) (default to False)

    try:
        # Central Bank Holdings
        api_response = api_instance.economy_central_bank_holdings(provider=provider, var_date=var_date, holding_type=holding_type, summary=summary, cusip=cusip, wam=wam, monthly=monthly)
        print("The response of EconomyApi->economy_central_bank_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_central_bank_holdings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to federal_reserve]
 **var_date** | **date**| A specific date to get data for. | [optional] 
 **holding_type** | **str**| Type of holdings to return. (provider: federal_reserve) | [optional] [default to all_treasury]
 **summary** | **bool**| If True, returns historical weekly summary by holding type. This parameter takes priority over other parameters. (provider: federal_reserve) | [optional] [default to False]
 **cusip** | **str**|  Multiple comma separated items allowed. | [optional] 
 **wam** | **bool**| If True, returns weighted average maturity aggregated by agency or treasury securities. This parameter takes priority over &#x60;holding_type&#x60;, &#x60;cusip&#x60;, and &#x60;monthly&#x60;. (provider: federal_reserve) | [optional] [default to False]
 **monthly** | **bool**| If True, returns historical data for all Treasury securities at a monthly interval. This parameter takes priority over other parameters, except &#x60;wam&#x60;. Only valid when &#x60;holding_type&#x60; is set to: &#39;all_treasury&#39;, &#39;bills&#39;, &#39;notesbonds&#39;, &#39;frn&#39;, &#39;tips&#39;. (provider: federal_reserve) | [optional] [default to False]

### Return type

[**OBBjectCentralBankHoldings**](OBBjectCentralBankHoldings.md)

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

# **economy_composite_leading_indicator**
> OBBjectCompositeLeadingIndicator economy_composite_leading_indicator(provider=provider, start_date=start_date, end_date=end_date, country=country, adjustment=adjustment, growth_rate=growth_rate)

Composite Leading Indicator

Get the composite leading indicator (CLI).  It is designed to provide early signals of turning points in business cycles showing fluctuation of the economic activity around its long term potential level.  CLIs show short-term economic movements in qualitative rather than quantitative terms.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_composite_leading_indicator import OBBjectCompositeLeadingIndicator
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = openbb_client.Oecd() # Oecd | Country to get the CLI for, default is G20. Multiple comma separated items allowed. (provider: oecd) (optional)
    adjustment = amplitude # str | Adjustment of the data, either 'amplitude' or 'normalized'. Default is amplitude. (provider: oecd) (optional) (default to amplitude)
    growth_rate = False # bool | Return the 1-year growth rate (%) of the CLI, default is False. (provider: oecd) (optional) (default to False)

    try:
        # Composite Leading Indicator
        api_response = api_instance.economy_composite_leading_indicator(provider=provider, start_date=start_date, end_date=end_date, country=country, adjustment=adjustment, growth_rate=growth_rate)
        print("The response of EconomyApi->economy_composite_leading_indicator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_composite_leading_indicator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | [**Oecd**](.md)| Country to get the CLI for, default is G20. Multiple comma separated items allowed. (provider: oecd) | [optional] 
 **adjustment** | **str**| Adjustment of the data, either &#39;amplitude&#39; or &#39;normalized&#39;. Default is amplitude. (provider: oecd) | [optional] [default to amplitude]
 **growth_rate** | **bool**| Return the 1-year growth rate (%) of the CLI, default is False. (provider: oecd) | [optional] [default to False]

### Return type

[**OBBjectCompositeLeadingIndicator**](OBBjectCompositeLeadingIndicator.md)

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

# **economy_country_profile**
> OBBjectCountryProfile economy_country_profile(country, provider=provider, latest=latest, use_cache=use_cache)

Country Profile

Get a profile of country statistics and economic indicators.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_country_profile import OBBjectCountryProfile
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
    api_instance = openbb_client.EconomyApi(api_client)
    country = 'country_example' # str | The country to get data. Multiple comma separated items allowed for provider(s): econdb.
    provider = econdb # str |  (optional) (default to econdb)
    latest = True # bool | If True, return only the latest data. If False, return all available data for each indicator. (provider: econdb) (optional) (default to True)
    use_cache = True # bool | If True, the request will be cached for one day.Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) (optional) (default to True)

    try:
        # Country Profile
        api_response = api_instance.economy_country_profile(country, provider=provider, latest=latest, use_cache=use_cache)
        print("The response of EconomyApi->economy_country_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_country_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): econdb. | 
 **provider** | **str**|  | [optional] [default to econdb]
 **latest** | **bool**| If True, return only the latest data. If False, return all available data for each indicator. (provider: econdb) | [optional] [default to True]
 **use_cache** | **bool**| If True, the request will be cached for one day.Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) | [optional] [default to True]

### Return type

[**OBBjectCountryProfile**](OBBjectCountryProfile.md)

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

# **economy_cpi**
> OBBjectConsumerPriceIndex economy_cpi(provider, country=country, transform=transform, frequency=frequency, harmonized=harmonized, start_date=start_date, end_date=end_date, expenditure=expenditure)

Cpi

Get Consumer Price Index (CPI).  Returns either the rescaled index value, or a rate of change (inflation).

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_consumer_price_index import OBBjectConsumerPriceIndex
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): fred, oecd. (optional) (default to 'united_states')
    transform = yoy # str | Transformation of the CPI data. Period represents the change since previous. Defaults to change from one year ago (yoy). (optional) (default to yoy)
    frequency = monthly # str | The frequency of the data. (optional) (default to monthly)
    harmonized = False # bool | If true, returns harmonized data. (optional) (default to False)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    expenditure = total # str | Expenditure component of CPI. (provider: oecd) (optional) (default to total)

    try:
        # Cpi
        api_response = api_instance.economy_cpi(provider, country=country, transform=transform, frequency=frequency, harmonized=harmonized, start_date=start_date, end_date=end_date, expenditure=expenditure)
        print("The response of EconomyApi->economy_cpi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_cpi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): fred, oecd. | [optional] [default to &#39;united_states&#39;]
 **transform** | **str**| Transformation of the CPI data. Period represents the change since previous. Defaults to change from one year ago (yoy). | [optional] [default to yoy]
 **frequency** | **str**| The frequency of the data. | [optional] [default to monthly]
 **harmonized** | **bool**| If true, returns harmonized data. | [optional] [default to False]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **expenditure** | **str**| Expenditure component of CPI. (provider: oecd) | [optional] [default to total]

### Return type

[**OBBjectConsumerPriceIndex**](OBBjectConsumerPriceIndex.md)

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

# **economy_direction_of_trade**
> OBBjectDirectionOfTrade economy_direction_of_trade(provider=provider, country=country, counterpart=counterpart, direction=direction, start_date=start_date, end_date=end_date, frequency=frequency)

Direction Of Trade

Get Direction Of Trade Statistics from the IMF database.  The Direction of Trade Statistics (DOTS) presents the value of merchandise exports and imports disaggregated according to a country's primary trading partners. Area and world aggregates are included in the display of trade flows between major areas of the world. Reported data is supplemented by estimates whenever such data is not available or current. Imports are reported on a cost, insurance and freight (CIF) basis and exports are reported on a free on board (FOB) basis. Time series data includes estimates derived from reports of partner countries for non-reporting and slow-reporting countries.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_direction_of_trade import OBBjectDirectionOfTrade
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = imf # str |  (optional) (default to imf)
    country = 'country_example' # str | The country to get data. None is an equiavlent to 'all'. If 'all' is used, the counterpart field cannot be 'all'. Multiple comma separated items allowed for provider(s): imf. (optional)
    counterpart = 'counterpart_example' # str | Counterpart country to the trade. None is an equiavlent to 'all'. If 'all' is used, the country field cannot be 'all'. Multiple comma separated items allowed for provider(s): imf. (optional)
    direction = balance # str | Trade direction. Use 'all' to get all data for this dimension. (optional) (default to balance)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = month # str | The frequency of the data. (optional) (default to month)

    try:
        # Direction Of Trade
        api_response = api_instance.economy_direction_of_trade(provider=provider, country=country, counterpart=counterpart, direction=direction, start_date=start_date, end_date=end_date, frequency=frequency)
        print("The response of EconomyApi->economy_direction_of_trade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_direction_of_trade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to imf]
 **country** | **str**| The country to get data. None is an equiavlent to &#39;all&#39;. If &#39;all&#39; is used, the counterpart field cannot be &#39;all&#39;. Multiple comma separated items allowed for provider(s): imf. | [optional] 
 **counterpart** | **str**| Counterpart country to the trade. None is an equiavlent to &#39;all&#39;. If &#39;all&#39; is used, the country field cannot be &#39;all&#39;. Multiple comma separated items allowed for provider(s): imf. | [optional] 
 **direction** | **str**| Trade direction. Use &#39;all&#39; to get all data for this dimension. | [optional] [default to balance]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**| The frequency of the data. | [optional] [default to month]

### Return type

[**OBBjectDirectionOfTrade**](OBBjectDirectionOfTrade.md)

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

# **economy_export_destinations**
> OBBjectExportDestinations economy_export_destinations(country, provider=provider)

Export Destinations

Get top export destinations by country from the UN Comtrade International Trade Statistics Database.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_export_destinations import OBBjectExportDestinations
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
    api_instance = openbb_client.EconomyApi(api_client)
    country = 'country_example' # str | The country to get data. Multiple comma separated items allowed for provider(s): econdb.
    provider = econdb # str |  (optional) (default to econdb)

    try:
        # Export Destinations
        api_response = api_instance.economy_export_destinations(country, provider=provider)
        print("The response of EconomyApi->economy_export_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_export_destinations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): econdb. | 
 **provider** | **str**|  | [optional] [default to econdb]

### Return type

[**OBBjectExportDestinations**](OBBjectExportDestinations.md)

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

# **economy_fred_regional**
> OBBjectFredRegional economy_fred_regional(symbol, provider=provider, start_date=start_date, end_date=end_date, limit=limit, is_series_group=is_series_group, region_type=region_type, season=season, units=units, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Fred Regional

Query the Geo Fred API for regional economic data by series group.  The series group ID is found by using `fred_search` and the `series_id` parameter.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_fred_regional import OBBjectFredRegional
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
    api_instance = openbb_client.EconomyApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for.
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    limit = 56 # int | The number of data entries to return. (optional)
    is_series_group = False # bool | When True, the symbol provided is for a series_group, else it is for a series ID. (provider: fred) (optional) (default to False)
    region_type = 'region_type_example' # str | The type of regional data. Parameter is only valid when `is_series_group` is True. (provider: fred) (optional)
    season = nsa # str | The seasonal adjustments to the data. Parameter is only valid when `is_series_group` is True. (provider: fred) (optional) (default to nsa)
    units = 'units_example' # str | The units of the data. This should match the units returned from searching by series ID. An incorrect field will not necessarily return an error. Parameter is only valid when `is_series_group` is True. (provider: fred) (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert high frequency data to lower frequency.              None = No change              a = Annual              q = Quarterly              m = Monthly              w = Weekly              d = Daily              wef = Weekly, Ending Friday              weth = Weekly, Ending Thursday              wew = Weekly, Ending Wednesday              wetu = Weekly, Ending Tuesday              wem = Weekly, Ending Monday              wesu = Weekly, Ending Sunday              wesa = Weekly, Ending Saturday              bwew = Biweekly, Ending Wednesday              bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.              avg = Average              sum = Sum              eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log          (provider: fred) (optional)

    try:
        # Fred Regional
        api_response = api_instance.economy_fred_regional(symbol, provider=provider, start_date=start_date, end_date=end_date, limit=limit, is_series_group=is_series_group, region_type=region_type, season=season, units=units, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of EconomyApi->economy_fred_regional:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_fred_regional: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. | 
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **limit** | **int**| The number of data entries to return. | [optional] 
 **is_series_group** | **bool**| When True, the symbol provided is for a series_group, else it is for a series ID. (provider: fred) | [optional] [default to False]
 **region_type** | **str**| The type of regional data. Parameter is only valid when &#x60;is_series_group&#x60; is True. (provider: fred) | [optional] 
 **season** | **str**| The seasonal adjustments to the data. Parameter is only valid when &#x60;is_series_group&#x60; is True. (provider: fred) | [optional] [default to nsa]
 **units** | **str**| The units of the data. This should match the units returned from searching by series ID. An incorrect field will not necessarily return an error. Parameter is only valid when &#x60;is_series_group&#x60; is True. (provider: fred) | [optional] 
 **frequency** | **str**| Frequency aggregation to convert high frequency data to lower frequency.              None &#x3D; No change              a &#x3D; Annual              q &#x3D; Quarterly              m &#x3D; Monthly              w &#x3D; Weekly              d &#x3D; Daily              wef &#x3D; Weekly, Ending Friday              weth &#x3D; Weekly, Ending Thursday              wew &#x3D; Weekly, Ending Wednesday              wetu &#x3D; Weekly, Ending Tuesday              wem &#x3D; Weekly, Ending Monday              wesu &#x3D; Weekly, Ending Sunday              wesa &#x3D; Weekly, Ending Saturday              bwew &#x3D; Biweekly, Ending Wednesday              bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.              avg &#x3D; Average              sum &#x3D; Sum              eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type              None &#x3D; No transformation              chg &#x3D; Change              ch1 &#x3D; Change from Year Ago              pch &#x3D; Percent Change              pc1 &#x3D; Percent Change from Year Ago              pca &#x3D; Compounded Annual Rate of Change              cch &#x3D; Continuously Compounded Rate of Change              cca &#x3D; Continuously Compounded Annual Rate of Change              log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectFredRegional**](OBBjectFredRegional.md)

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

# **economy_fred_release_table**
> OBBjectFredReleaseTable economy_fred_release_table(release_id, provider=provider, element_id=element_id, var_date=var_date)

Fred Release Table

Get economic release data by ID and/or element from FRED.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_fred_release_table import OBBjectFredReleaseTable
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
    api_instance = openbb_client.EconomyApi(api_client)
    release_id = 'release_id_example' # str | The ID of the release. Use `fred_search` to find releases.
    provider = fred # str |  (optional) (default to fred)
    element_id = 'element_id_example' # str | The element ID of a specific table in the release. (optional)
    var_date = openbb_client.Date2() # Date2 | A specific date to get data for. Multiple comma separated items allowed for provider(s): fred. (optional)

    try:
        # Fred Release Table
        api_response = api_instance.economy_fred_release_table(release_id, provider=provider, element_id=element_id, var_date=var_date)
        print("The response of EconomyApi->economy_fred_release_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_fred_release_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **str**| The ID of the release. Use &#x60;fred_search&#x60; to find releases. | 
 **provider** | **str**|  | [optional] [default to fred]
 **element_id** | **str**| The element ID of a specific table in the release. | [optional] 
 **var_date** | [**Date2**](.md)| A specific date to get data for. Multiple comma separated items allowed for provider(s): fred. | [optional] 

### Return type

[**OBBjectFredReleaseTable**](OBBjectFredReleaseTable.md)

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

# **economy_fred_search**
> OBBjectFredSearch economy_fred_search(provider=provider, query=query, search_type=search_type, release_id=release_id, limit=limit, offset=offset, order_by=order_by, sort_order=sort_order, filter_variable=filter_variable, filter_value=filter_value, tag_names=tag_names, exclude_tag_names=exclude_tag_names, series_id=series_id)

Fred Search

Search for FRED series or economic releases by ID or string.  This does not return the observation values, only the metadata. Use this function to find series IDs for `fred_series()`.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_fred_search import OBBjectFredSearch
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    query = 'query_example' # str | The search word(s). (optional)
    search_type = full_text # str | The type of search to perform. Automatically set to 'release' when a 'release_id' is provided. (provider: fred) (optional) (default to full_text)
    release_id = 56 # int | A specific release ID to target. (provider: fred) (optional)
    limit = 56 # int | The number of data entries to return. (1-1000) (provider: fred) (optional)
    offset = 56 # int | Offset the results in conjunction with limit. This parameter is ignored When search_type is 'release'. (provider: fred) (optional)
    order_by = observation_end # str | Order the results by a specific attribute. The default is 'observation_end'. (provider: fred) (optional) (default to observation_end)
    sort_order = desc # str | Sort the 'order_by' item in ascending or descending order. The default is 'desc'. (provider: fred) (optional) (default to desc)
    filter_variable = 'filter_variable_example' # str | Filter by an attribute. (provider: fred) (optional)
    filter_value = 'filter_value_example' # str | String value to filter the variable by.  Used in conjunction with filter_variable. This parameter is ignored when search_type is 'release'. (provider: fred) (optional)
    tag_names = 'tag_names_example' # str | A semicolon delimited list of tag names that series match all of.  Example: 'japan;imports' This parameter is ignored when search_type is 'release'. Multiple comma separated items allowed. (provider: fred) (optional)
    exclude_tag_names = 'exclude_tag_names_example' # str | A semicolon delimited list of tag names that series match none of.  Example: 'imports;services'. Requires that variable tag_names also be set to limit the number of matching series. This parameter is ignored when search_type is 'release'. Multiple comma separated items allowed. (provider: fred) (optional)
    series_id = 'series_id_example' # str | A FRED Series ID to return series group information for. This returns the required information to query for regional data. Not all series that are in FRED have geographical data. Entering a value for series_id will override all other parameters. Multiple series_ids can be separated by commas. (provider: fred) (optional)

    try:
        # Fred Search
        api_response = api_instance.economy_fred_search(provider=provider, query=query, search_type=search_type, release_id=release_id, limit=limit, offset=offset, order_by=order_by, sort_order=sort_order, filter_variable=filter_variable, filter_value=filter_value, tag_names=tag_names, exclude_tag_names=exclude_tag_names, series_id=series_id)
        print("The response of EconomyApi->economy_fred_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_fred_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **query** | **str**| The search word(s). | [optional] 
 **search_type** | **str**| The type of search to perform. Automatically set to &#39;release&#39; when a &#39;release_id&#39; is provided. (provider: fred) | [optional] [default to full_text]
 **release_id** | **int**| A specific release ID to target. (provider: fred) | [optional] 
 **limit** | **int**| The number of data entries to return. (1-1000) (provider: fred) | [optional] 
 **offset** | **int**| Offset the results in conjunction with limit. This parameter is ignored When search_type is &#39;release&#39;. (provider: fred) | [optional] 
 **order_by** | **str**| Order the results by a specific attribute. The default is &#39;observation_end&#39;. (provider: fred) | [optional] [default to observation_end]
 **sort_order** | **str**| Sort the &#39;order_by&#39; item in ascending or descending order. The default is &#39;desc&#39;. (provider: fred) | [optional] [default to desc]
 **filter_variable** | **str**| Filter by an attribute. (provider: fred) | [optional] 
 **filter_value** | **str**| String value to filter the variable by.  Used in conjunction with filter_variable. This parameter is ignored when search_type is &#39;release&#39;. (provider: fred) | [optional] 
 **tag_names** | **str**| A semicolon delimited list of tag names that series match all of.  Example: &#39;japan;imports&#39; This parameter is ignored when search_type is &#39;release&#39;. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **exclude_tag_names** | **str**| A semicolon delimited list of tag names that series match none of.  Example: &#39;imports;services&#39;. Requires that variable tag_names also be set to limit the number of matching series. This parameter is ignored when search_type is &#39;release&#39;. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **series_id** | **str**| A FRED Series ID to return series group information for. This returns the required information to query for regional data. Not all series that are in FRED have geographical data. Entering a value for series_id will override all other parameters. Multiple series_ids can be separated by commas. (provider: fred) | [optional] 

### Return type

[**OBBjectFredSearch**](OBBjectFredSearch.md)

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

# **economy_fred_series**
> OBBjectFredSeries economy_fred_series(provider, symbol, start_date=start_date, end_date=end_date, limit=limit, frequency=frequency, aggregation_method=aggregation_method, transform=transform, all_pages=all_pages, sleep=sleep)

Fred Series

Get data by series ID from FRED.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_fred_series import OBBjectFredSeries
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): fred.
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    limit = 56 # int | The number of data entries to return. (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert high frequency data to lower frequency.         None = No change         a = Annual         q = Quarterly         m = Monthly         w = Weekly         d = Daily         wef = Weekly, Ending Friday         weth = Weekly, Ending Thursday         wew = Weekly, Ending Wednesday         wetu = Weekly, Ending Tuesday         wem = Weekly, Ending Monday         wesu = Weekly, Ending Sunday         wesa = Weekly, Ending Saturday         bwew = Biweekly, Ending Wednesday         bwem = Biweekly, Ending Monday          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg = Average         sum = Sum         eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type         None = No transformation         chg = Change         ch1 = Change from Year Ago         pch = Percent Change         pc1 = Percent Change from Year Ago         pca = Compounded Annual Rate of Change         cch = Continuously Compounded Rate of Change         cca = Continuously Compounded Annual Rate of Change         log = Natural Log          (provider: fred) (optional)
    all_pages = True # bool | Returns all pages of data from the API call at once. (provider: intrinio) (optional)
    sleep = 3.4 # float | Time to sleep between requests to avoid rate limiting. (provider: intrinio) (optional)

    try:
        # Fred Series
        api_response = api_instance.economy_fred_series(provider, symbol, start_date=start_date, end_date=end_date, limit=limit, frequency=frequency, aggregation_method=aggregation_method, transform=transform, all_pages=all_pages, sleep=sleep)
        print("The response of EconomyApi->economy_fred_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_fred_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): fred. | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **limit** | **int**| The number of data entries to return. | [optional] 
 **frequency** | **str**| Frequency aggregation to convert high frequency data to lower frequency.         None &#x3D; No change         a &#x3D; Annual         q &#x3D; Quarterly         m &#x3D; Monthly         w &#x3D; Weekly         d &#x3D; Daily         wef &#x3D; Weekly, Ending Friday         weth &#x3D; Weekly, Ending Thursday         wew &#x3D; Weekly, Ending Wednesday         wetu &#x3D; Weekly, Ending Tuesday         wem &#x3D; Weekly, Ending Monday         wesu &#x3D; Weekly, Ending Sunday         wesa &#x3D; Weekly, Ending Saturday         bwew &#x3D; Biweekly, Ending Wednesday         bwem &#x3D; Biweekly, Ending Monday          (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.         This parameter has no affect if the frequency parameter is not set.         avg &#x3D; Average         sum &#x3D; Sum         eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type         None &#x3D; No transformation         chg &#x3D; Change         ch1 &#x3D; Change from Year Ago         pch &#x3D; Percent Change         pc1 &#x3D; Percent Change from Year Ago         pca &#x3D; Compounded Annual Rate of Change         cch &#x3D; Continuously Compounded Rate of Change         cca &#x3D; Continuously Compounded Annual Rate of Change         log &#x3D; Natural Log          (provider: fred) | [optional] 
 **all_pages** | **bool**| Returns all pages of data from the API call at once. (provider: intrinio) | [optional] 
 **sleep** | **float**| Time to sleep between requests to avoid rate limiting. (provider: intrinio) | [optional] 

### Return type

[**OBBjectFredSeries**](OBBjectFredSeries.md)

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

# **economy_gdp_forecast**
> OBBjectGdpForecast economy_gdp_forecast(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency, units=units)

Forecast

Get Forecasted GDP Data.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_gdp_forecast import OBBjectGdpForecast
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = 'all' # str | Country, or countries, to get forward GDP projections for. Default is all. Multiple comma separated items allowed. (provider: oecd) (optional) (default to 'all')
    frequency = annual # str | Frequency of the data, default is annual. (provider: oecd) (optional) (default to annual)
    units = volume # str | Units of the data, default is volume (chain linked volume, 2015). 'current_prices', 'volume', and 'capita' are expressed in USD; 'growth' as a percent; 'deflator' as an index. (provider: oecd) (optional) (default to volume)

    try:
        # Forecast
        api_response = api_instance.economy_gdp_forecast(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency, units=units)
        print("The response of EconomyApi->economy_gdp_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_gdp_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| Country, or countries, to get forward GDP projections for. Default is all. Multiple comma separated items allowed. (provider: oecd) | [optional] [default to &#39;all&#39;]
 **frequency** | **str**| Frequency of the data, default is annual. (provider: oecd) | [optional] [default to annual]
 **units** | **str**| Units of the data, default is volume (chain linked volume, 2015). &#39;current_prices&#39;, &#39;volume&#39;, and &#39;capita&#39; are expressed in USD; &#39;growth&#39; as a percent; &#39;deflator&#39; as an index. (provider: oecd) | [optional] [default to volume]

### Return type

[**OBBjectGdpForecast**](OBBjectGdpForecast.md)

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

# **economy_gdp_nominal**
> OBBjectGdpNominal economy_gdp_nominal(provider, start_date=start_date, end_date=end_date, country=country, use_cache=use_cache, frequency=frequency, units=units, price_base=price_base)

Nominal

Get Nominal GDP Data.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_gdp_nominal import OBBjectGdpNominal
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = 'united_states' # str | The country to get data.Use 'all' to get data for all available countries. Multiple comma separated items allowed. (provider: econdb, oecd) (optional) (default to 'united_states')
    use_cache = True # bool | If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) (optional) (default to True)
    frequency = quarter # str | Frequency of the data. (provider: oecd) (optional) (default to quarter)
    units = level # str | The unit of measurement for the data.Both 'level' and 'capita' (per) are measured in USD. (provider: oecd) (optional) (default to level)
    price_base = current_prices # str | Price base for the data, volume is chain linked volume. (provider: oecd) (optional) (default to current_prices)

    try:
        # Nominal
        api_response = api_instance.economy_gdp_nominal(provider, start_date=start_date, end_date=end_date, country=country, use_cache=use_cache, frequency=frequency, units=units, price_base=price_base)
        print("The response of EconomyApi->economy_gdp_nominal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_gdp_nominal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| The country to get data.Use &#39;all&#39; to get data for all available countries. Multiple comma separated items allowed. (provider: econdb, oecd) | [optional] [default to &#39;united_states&#39;]
 **use_cache** | **bool**| If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) | [optional] [default to True]
 **frequency** | **str**| Frequency of the data. (provider: oecd) | [optional] [default to quarter]
 **units** | **str**| The unit of measurement for the data.Both &#39;level&#39; and &#39;capita&#39; (per) are measured in USD. (provider: oecd) | [optional] [default to level]
 **price_base** | **str**| Price base for the data, volume is chain linked volume. (provider: oecd) | [optional] [default to current_prices]

### Return type

[**OBBjectGdpNominal**](OBBjectGdpNominal.md)

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

# **economy_gdp_real**
> OBBjectGdpReal economy_gdp_real(provider, start_date=start_date, end_date=end_date, country=country, use_cache=use_cache, frequency=frequency)

Real

Get Real GDP Data.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_gdp_real import OBBjectGdpReal
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = 'united_states' # str | The country to get data.Use 'all' to get data for all available countries. Multiple comma separated items allowed. (provider: econdb, oecd) (optional) (default to 'united_states')
    use_cache = True # bool | If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) (optional) (default to True)
    frequency = quarter # str | Frequency of the data. (provider: oecd) (optional) (default to quarter)

    try:
        # Real
        api_response = api_instance.economy_gdp_real(provider, start_date=start_date, end_date=end_date, country=country, use_cache=use_cache, frequency=frequency)
        print("The response of EconomyApi->economy_gdp_real:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_gdp_real: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| The country to get data.Use &#39;all&#39; to get data for all available countries. Multiple comma separated items allowed. (provider: econdb, oecd) | [optional] [default to &#39;united_states&#39;]
 **use_cache** | **bool**| If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) | [optional] [default to True]
 **frequency** | **str**| Frequency of the data. (provider: oecd) | [optional] [default to quarter]

### Return type

[**OBBjectGdpReal**](OBBjectGdpReal.md)

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

# **economy_house_price_index**
> OBBjectHousePriceIndex economy_house_price_index(provider=provider, country=country, frequency=frequency, transform=transform, start_date=start_date, end_date=end_date)

House Price Index

Get the House Price Index by country from the OECD Short-Term Economics Statistics.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_house_price_index import OBBjectHousePriceIndex
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): oecd. (optional) (default to 'united_states')
    frequency = quarter # str | The frequency of the data. (optional) (default to quarter)
    transform = index # str | Transformation of the CPI data. Period represents the change since previous. Defaults to change from one year ago (yoy). (optional) (default to index)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)

    try:
        # House Price Index
        api_response = api_instance.economy_house_price_index(provider=provider, country=country, frequency=frequency, transform=transform, start_date=start_date, end_date=end_date)
        print("The response of EconomyApi->economy_house_price_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_house_price_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): oecd. | [optional] [default to &#39;united_states&#39;]
 **frequency** | **str**| The frequency of the data. | [optional] [default to quarter]
 **transform** | **str**| Transformation of the CPI data. Period represents the change since previous. Defaults to change from one year ago (yoy). | [optional] [default to index]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 

### Return type

[**OBBjectHousePriceIndex**](OBBjectHousePriceIndex.md)

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

# **economy_immediate_interest_rate**
> OBBjectImmediateInterestRate economy_immediate_interest_rate(provider=provider, country=country, start_date=start_date, end_date=end_date, frequency=frequency)

This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.

Get immediate interest rates by country.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_immediate_interest_rate import OBBjectImmediateInterestRate
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): oecd. (optional) (default to 'united_states')
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = monthly # str | The frequency of the data. (provider: oecd) (optional) (default to monthly)

    try:
        # This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
        api_response = api_instance.economy_immediate_interest_rate(provider=provider, country=country, start_date=start_date, end_date=end_date, frequency=frequency)
        print("The response of EconomyApi->economy_immediate_interest_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_immediate_interest_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): oecd. | [optional] [default to &#39;united_states&#39;]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**| The frequency of the data. (provider: oecd) | [optional] [default to monthly]

### Return type

[**OBBjectImmediateInterestRate**](OBBjectImmediateInterestRate.md)

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

# **economy_indicators**
> OBBjectEconomicIndicators economy_indicators(provider, country=country, start_date=start_date, end_date=end_date, symbol=symbol, transform=transform, frequency=frequency, use_cache=use_cache)

Indicators

Get economic indicators by country and indicator.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_economic_indicators import OBBjectEconomicIndicators
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = 'provider_example' # str | 
    country = 'country_example' # str | The country to get data. The country represented by the indicator, if available. Multiple comma separated items allowed for provider(s): econdb, imf. (optional)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    symbol = 'symbol_example' # str | Symbol to get data for. The base symbol for the indicator (e.g. GDP, CPI, etc.). Use `available_indicators()` to get a list of available symbols. Multiple comma separated items allowed. (provider: econdb);     Symbol to get data for. Use `available_indicators()` to get the list of available symbols. Use 'IRFCL' to get all the data from the set of indicators. Complete tables are available only by single country, and are keyed as described below. The default is 'irfcl_top_lines'. Available presets not listed in `available_indicators()` are:          'IRFCL': All the data from the set of indicators. Not compatible with multiple countries.         'irfcl_top_lines': The default, top line items from the IRFCL data. Compatible with multiple countries.         'reserve_assets_and_other_fx_assets': Table I of the IRFCL data. Not compatible with multiple countries.         'predetermined_drains_on_fx_assets': Table II of the IRFCL data. Not compatible with multiple countries.         'contingent_drains_fx_assets': Table III of the IRFCL data. Not compatible with multiple countries.         'memorandum_items': The memorandum items table of the IRFCL data. Not compatible with multiple countries.         'gold_reserves': Gold reserves as value in USD and Fine Troy Ounces. Compatible with multiple countries.         'derivative_assets': Net derivative assets as value in USD. Compatible with multipile countries.      Multiple comma separated items allowed. (provider: imf) (optional)
    transform = 'transform_example' # str | The transformation to apply to the data, default is None.      tpop: Change from previous period     toya: Change from one year ago     tusd: Values as US dollars     tpgp: Values as a percent of GDP      Only 'tpop' and 'toya' are applicable to all indicators. Applying transformations across multiple indicators/countries may produce unexpected results.     This is because not all indicators are compatible with all transformations, and the original units and scale differ between entities.     `tusd` should only be used where values are currencies. (provider: econdb) (optional)
    frequency = quarter # str | The frequency of the data, default is 'quarter'. Only valid when 'symbol' is 'main'. (provider: econdb);     Frequency of the data. (provider: imf) (optional) (default to quarter)
    use_cache = True # bool | If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) (optional) (default to True)

    try:
        # Indicators
        api_response = api_instance.economy_indicators(provider, country=country, start_date=start_date, end_date=end_date, symbol=symbol, transform=transform, frequency=frequency, use_cache=use_cache)
        print("The response of EconomyApi->economy_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **country** | **str**| The country to get data. The country represented by the indicator, if available. Multiple comma separated items allowed for provider(s): econdb, imf. | [optional] 
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **symbol** | **str**| Symbol to get data for. The base symbol for the indicator (e.g. GDP, CPI, etc.). Use &#x60;available_indicators()&#x60; to get a list of available symbols. Multiple comma separated items allowed. (provider: econdb);     Symbol to get data for. Use &#x60;available_indicators()&#x60; to get the list of available symbols. Use &#39;IRFCL&#39; to get all the data from the set of indicators. Complete tables are available only by single country, and are keyed as described below. The default is &#39;irfcl_top_lines&#39;. Available presets not listed in &#x60;available_indicators()&#x60; are:          &#39;IRFCL&#39;: All the data from the set of indicators. Not compatible with multiple countries.         &#39;irfcl_top_lines&#39;: The default, top line items from the IRFCL data. Compatible with multiple countries.         &#39;reserve_assets_and_other_fx_assets&#39;: Table I of the IRFCL data. Not compatible with multiple countries.         &#39;predetermined_drains_on_fx_assets&#39;: Table II of the IRFCL data. Not compatible with multiple countries.         &#39;contingent_drains_fx_assets&#39;: Table III of the IRFCL data. Not compatible with multiple countries.         &#39;memorandum_items&#39;: The memorandum items table of the IRFCL data. Not compatible with multiple countries.         &#39;gold_reserves&#39;: Gold reserves as value in USD and Fine Troy Ounces. Compatible with multiple countries.         &#39;derivative_assets&#39;: Net derivative assets as value in USD. Compatible with multipile countries.      Multiple comma separated items allowed. (provider: imf) | [optional] 
 **transform** | **str**| The transformation to apply to the data, default is None.      tpop: Change from previous period     toya: Change from one year ago     tusd: Values as US dollars     tpgp: Values as a percent of GDP      Only &#39;tpop&#39; and &#39;toya&#39; are applicable to all indicators. Applying transformations across multiple indicators/countries may produce unexpected results.     This is because not all indicators are compatible with all transformations, and the original units and scale differ between entities.     &#x60;tusd&#x60; should only be used where values are currencies. (provider: econdb) | [optional] 
 **frequency** | **str**| The frequency of the data, default is &#39;quarter&#39;. Only valid when &#39;symbol&#39; is &#39;main&#39;. (provider: econdb);     Frequency of the data. (provider: imf) | [optional] [default to quarter]
 **use_cache** | **bool**| If True, the request will be cached for one day. Using cache is recommended to avoid needlessly requesting the same data. (provider: econdb) | [optional] [default to True]

### Return type

[**OBBjectEconomicIndicators**](OBBjectEconomicIndicators.md)

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

# **economy_interest_rates**
> OBBjectCountryInterestRates economy_interest_rates(provider=provider, country=country, start_date=start_date, end_date=end_date, duration=duration, frequency=frequency)

Interest Rates

Get interest rates by country(s) and duration. Most OECD countries publish short-term, a long-term, and immediate rates monthly.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_country_interest_rates import OBBjectCountryInterestRates
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): oecd. (optional) (default to 'united_states')
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    duration = short # str | Duration of the interest rate. 'immediate' is the overnight rate, 'short' is the 3-month rate, and 'long' is the 10-year rate. (provider: oecd) (optional) (default to short)
    frequency = monthly # str | Frequency to get interest rate for for. (provider: oecd) (optional) (default to monthly)

    try:
        # Interest Rates
        api_response = api_instance.economy_interest_rates(provider=provider, country=country, start_date=start_date, end_date=end_date, duration=duration, frequency=frequency)
        print("The response of EconomyApi->economy_interest_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_interest_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): oecd. | [optional] [default to &#39;united_states&#39;]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **duration** | **str**| Duration of the interest rate. &#39;immediate&#39; is the overnight rate, &#39;short&#39; is the 3-month rate, and &#39;long&#39; is the 10-year rate. (provider: oecd) | [optional] [default to short]
 **frequency** | **str**| Frequency to get interest rate for for. (provider: oecd) | [optional] [default to monthly]

### Return type

[**OBBjectCountryInterestRates**](OBBjectCountryInterestRates.md)

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

# **economy_long_term_interest_rate**
> OBBjectLTIR economy_long_term_interest_rate(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency)

This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.

Get Long-term interest rates that refer to government bonds maturing in ten years.  Rates are mainly determined by the price charged by the lender, the risk from the borrower and the fall in the capital value. Long-term interest rates are generally averages of daily rates, measured as a percentage. These interest rates are implied by the prices at which the government bonds are traded on financial markets, not the interest rates at which the loans were issued. In all cases, they refer to bonds whose capital repayment is guaranteed by governments. Long-term interest rates are one of the determinants of business investment. Low long-term interest rates encourage investment in new equipment and high interest rates discourage it. Investment is, in turn, a major source of economic growth.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_ltir import OBBjectLTIR
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = united_states # str | Country to get interest rate for. (provider: oecd) (optional) (default to united_states)
    frequency = monthly # str | Frequency to get interest rate for for. (provider: oecd) (optional) (default to monthly)

    try:
        # This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
        api_response = api_instance.economy_long_term_interest_rate(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency)
        print("The response of EconomyApi->economy_long_term_interest_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_long_term_interest_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| Country to get interest rate for. (provider: oecd) | [optional] [default to united_states]
 **frequency** | **str**| Frequency to get interest rate for for. (provider: oecd) | [optional] [default to monthly]

### Return type

[**OBBjectLTIR**](OBBjectLTIR.md)

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

# **economy_money_measures**
> OBBjectMoneyMeasures economy_money_measures(provider=provider, start_date=start_date, end_date=end_date, adjusted=adjusted)

Money Measures

Get Money Measures (M1/M2 and components).  The Federal Reserve publishes as part of the H.6 Release.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_money_measures import OBBjectMoneyMeasures
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = federal_reserve # str |  (optional) (default to federal_reserve)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    adjusted = True # bool | Whether to return seasonally adjusted data. (optional)

    try:
        # Money Measures
        api_response = api_instance.economy_money_measures(provider=provider, start_date=start_date, end_date=end_date, adjusted=adjusted)
        print("The response of EconomyApi->economy_money_measures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_money_measures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to federal_reserve]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **adjusted** | **bool**| Whether to return seasonally adjusted data. | [optional] 

### Return type

[**OBBjectMoneyMeasures**](OBBjectMoneyMeasures.md)

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

# **economy_pce**
> OBBjectPersonalConsumptionExpenditures economy_pce(provider=provider, var_date=var_date, category=category)

Pce

Get Personal Consumption Expenditures (PCE) reports.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_personal_consumption_expenditures import OBBjectPersonalConsumptionExpenditures
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    var_date = openbb_client.Date3() # Date3 | A specific date to get data for. Default is the latest report. Multiple comma separated items allowed for provider(s): fred. (optional)
    category = personal_income # str | The category to query. (provider: fred) (optional) (default to personal_income)

    try:
        # Pce
        api_response = api_instance.economy_pce(provider=provider, var_date=var_date, category=category)
        print("The response of EconomyApi->economy_pce:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_pce: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **var_date** | [**Date3**](.md)| A specific date to get data for. Default is the latest report. Multiple comma separated items allowed for provider(s): fred. | [optional] 
 **category** | **str**| The category to query. (provider: fred) | [optional] [default to personal_income]

### Return type

[**OBBjectPersonalConsumptionExpenditures**](OBBjectPersonalConsumptionExpenditures.md)

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

# **economy_port_volume**
> OBBjectPortVolume economy_port_volume(provider=provider, start_date=start_date, end_date=end_date)

Port Volume

Get average dwelling times and TEU volumes from the top ports.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_port_volume import OBBjectPortVolume
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = econdb # str |  (optional) (default to econdb)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)

    try:
        # Port Volume
        api_response = api_instance.economy_port_volume(provider=provider, start_date=start_date, end_date=end_date)
        print("The response of EconomyApi->economy_port_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_port_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to econdb]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 

### Return type

[**OBBjectPortVolume**](OBBjectPortVolume.md)

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

# **economy_primary_dealer_fails**
> OBBjectPrimaryDealerFails economy_primary_dealer_fails(provider=provider, start_date=start_date, end_date=end_date, asset_class=asset_class, unit=unit)

Primary Dealer Fails

Primary Dealer Statistics for Fails to Deliver and Fails to Receive.  Data from the NY Federal Reserve are updated on Thursdays at approximately 4:15 p.m. with the previous week's statistics.  For research on the topic, see: https://www.federalreserve.gov/econres/notes/feds-notes/the-systemic-nature-of-settlement-fails-20170703.html  \"Large and protracted settlement fails are believed to undermine the liquidity and well-functioning of securities markets.  Near-100 percent pass-through of fails suggests a high degree of collateral re-hypothecation together with the inability or unwillingness to borrow or buy the needed securities.\"

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_primary_dealer_fails import OBBjectPrimaryDealerFails
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = federal_reserve # str |  (optional) (default to federal_reserve)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    asset_class = all # str | Asset class to return, default is 'all'. (provider: federal_reserve) (optional) (default to all)
    unit = value # str | Unit of the data returned to the 'value' field. Default is 'value', which represents millions of USD. 'percent' returns data as the percentage of the total fails-to-receive and fails-to-deliver, by asset class. (provider: federal_reserve) (optional) (default to value)

    try:
        # Primary Dealer Fails
        api_response = api_instance.economy_primary_dealer_fails(provider=provider, start_date=start_date, end_date=end_date, asset_class=asset_class, unit=unit)
        print("The response of EconomyApi->economy_primary_dealer_fails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_primary_dealer_fails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to federal_reserve]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **asset_class** | **str**| Asset class to return, default is &#39;all&#39;. (provider: federal_reserve) | [optional] [default to all]
 **unit** | **str**| Unit of the data returned to the &#39;value&#39; field. Default is &#39;value&#39;, which represents millions of USD. &#39;percent&#39; returns data as the percentage of the total fails-to-receive and fails-to-deliver, by asset class. (provider: federal_reserve) | [optional] [default to value]

### Return type

[**OBBjectPrimaryDealerFails**](OBBjectPrimaryDealerFails.md)

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

# **economy_primary_dealer_positioning**
> OBBjectPrimaryDealerPositioning economy_primary_dealer_positioning(provider=provider, start_date=start_date, end_date=end_date, category=category)

Primary Dealer Positioning

Get Primary dealer positioning statistics.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_primary_dealer_positioning import OBBjectPrimaryDealerPositioning
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = federal_reserve # str |  (optional) (default to federal_reserve)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    category = treasuries # str | The category of asset to return, defaults to 'treasuries'. (provider: federal_reserve) (optional) (default to treasuries)

    try:
        # Primary Dealer Positioning
        api_response = api_instance.economy_primary_dealer_positioning(provider=provider, start_date=start_date, end_date=end_date, category=category)
        print("The response of EconomyApi->economy_primary_dealer_positioning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_primary_dealer_positioning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to federal_reserve]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **category** | **str**| The category of asset to return, defaults to &#39;treasuries&#39;. (provider: federal_reserve) | [optional] [default to treasuries]

### Return type

[**OBBjectPrimaryDealerPositioning**](OBBjectPrimaryDealerPositioning.md)

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

# **economy_retail_prices**
> OBBjectRetailPrices economy_retail_prices(provider=provider, item=item, country=country, start_date=start_date, end_date=end_date, region=region, frequency=frequency, transform=transform)

Retail Prices

Get retail prices for common items.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_retail_prices import OBBjectRetailPrices
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    item = 'item_example' # str | The item or basket of items to query. (optional)
    country = 'united_states' # str | The country to get data. (optional) (default to 'united_states')
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    region = all_city # str | The region to get average price levels for. (provider: fred) (optional) (default to all_city)
    frequency = monthly # str | The frequency of the data. (provider: fred) (optional) (default to monthly)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Retail Prices
        api_response = api_instance.economy_retail_prices(provider=provider, item=item, country=country, start_date=start_date, end_date=end_date, region=region, frequency=frequency, transform=transform)
        print("The response of EconomyApi->economy_retail_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_retail_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **item** | **str**| The item or basket of items to query. | [optional] 
 **country** | **str**| The country to get data. | [optional] [default to &#39;united_states&#39;]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **region** | **str**| The region to get average price levels for. (provider: fred) | [optional] [default to all_city]
 **frequency** | **str**| The frequency of the data. (provider: fred) | [optional] [default to monthly]
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectRetailPrices**](OBBjectRetailPrices.md)

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

# **economy_risk_premium**
> OBBjectRiskPremium economy_risk_premium(provider=provider)

Risk Premium

Get Market Risk Premium by country.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_risk_premium import OBBjectRiskPremium
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fmp # str |  (optional) (default to fmp)

    try:
        # Risk Premium
        api_response = api_instance.economy_risk_premium(provider=provider)
        print("The response of EconomyApi->economy_risk_premium:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_risk_premium: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fmp]

### Return type

[**OBBjectRiskPremium**](OBBjectRiskPremium.md)

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

# **economy_share_price_index**
> OBBjectSharePriceIndex economy_share_price_index(provider=provider, country=country, frequency=frequency, start_date=start_date, end_date=end_date)

Share Price Index

Get the Share Price Index by country from the OECD Short-Term Economics Statistics.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_share_price_index import OBBjectSharePriceIndex
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): oecd. (optional) (default to 'united_states')
    frequency = monthly # str | The frequency of the data. (optional) (default to monthly)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)

    try:
        # Share Price Index
        api_response = api_instance.economy_share_price_index(provider=provider, country=country, frequency=frequency, start_date=start_date, end_date=end_date)
        print("The response of EconomyApi->economy_share_price_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_share_price_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): oecd. | [optional] [default to &#39;united_states&#39;]
 **frequency** | **str**| The frequency of the data. | [optional] [default to monthly]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 

### Return type

[**OBBjectSharePriceIndex**](OBBjectSharePriceIndex.md)

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

# **economy_short_term_interest_rate**
> OBBjectSTIR economy_short_term_interest_rate(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency)

This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.

Get Short-term interest rates.  They are the rates at which short-term borrowings are effected between financial institutions or the rate at which short-term government paper is issued or traded in the market.  Short-term interest rates are generally averages of daily rates, measured as a percentage. Short-term interest rates are based on three-month money market rates where available. Typical standardised names are \"money market rate\" and \"treasury bill rate\".

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_stir import OBBjectSTIR
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    country = united_states # str | Country to get interest rate for. (provider: oecd) (optional) (default to united_states)
    frequency = monthly # str | Frequency to get interest rate for for. (provider: oecd) (optional) (default to monthly)

    try:
        # This endpoint will be removed in a future version. Use, `/economy/interest_rates`, instead. Deprecated in OpenBB Platform V4.3 to be removed in V4.5.
        api_response = api_instance.economy_short_term_interest_rate(provider=provider, start_date=start_date, end_date=end_date, country=country, frequency=frequency)
        print("The response of EconomyApi->economy_short_term_interest_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_short_term_interest_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **country** | **str**| Country to get interest rate for. (provider: oecd) | [optional] [default to united_states]
 **frequency** | **str**| Frequency to get interest rate for for. (provider: oecd) | [optional] [default to monthly]

### Return type

[**OBBjectSTIR**](OBBjectSTIR.md)

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

# **economy_survey_bls_search**
> OBBjectBlsSearch economy_survey_bls_search(provider=provider, query=query, category=category, include_extras=include_extras, include_code_map=include_code_map)

Bls Search

Search BLS surveys by category and keyword or phrase to identify BLS series IDs.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_bls_search import OBBjectBlsSearch
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = bls # str |  (optional) (default to bls)
    query = '' # str | The search word(s). Use semi-colon to separate multiple queries as an & operator. (optional) (default to '')
    category = 'category_example' # str | The category of BLS survey to search within.         An empty search query will return all series within the category. Options are:              cpi - Consumer Price Index              pce - Personal Consumption Expenditure              ppi - Producer Price Index              ip - Industry Productivity              jolts - Job Openings and Labor Turnover Survey              nfp - Nonfarm Payrolls              cps - Current Population Survey              lfs - Labor Force Statistics              wages - Wages              ec - Employer Costs              sla - State and Local Area Employment              bed - Business Employment Dynamics              tu - Time Use          (provider: bls) (optional)
    include_extras = False # bool | Include additional information in the search results. Extra fields returned are metadata and vary by survey. Fields are undefined strings that typically have names ending with '_code'. (provider: bls) (optional) (default to False)
    include_code_map = False # bool | When True, includes the complete code map for eaçh survey in the category, returned separately as a nested JSON to the `extras['results_metadata']` property of the response. Example content is the NAICS industry map for PPI surveys. Each code is a value within the 'symbol' of the time series. (provider: bls) (optional) (default to False)

    try:
        # Bls Search
        api_response = api_instance.economy_survey_bls_search(provider=provider, query=query, category=category, include_extras=include_extras, include_code_map=include_code_map)
        print("The response of EconomyApi->economy_survey_bls_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_bls_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to bls]
 **query** | **str**| The search word(s). Use semi-colon to separate multiple queries as an &amp; operator. | [optional] [default to &#39;&#39;]
 **category** | **str**| The category of BLS survey to search within.         An empty search query will return all series within the category. Options are:              cpi - Consumer Price Index              pce - Personal Consumption Expenditure              ppi - Producer Price Index              ip - Industry Productivity              jolts - Job Openings and Labor Turnover Survey              nfp - Nonfarm Payrolls              cps - Current Population Survey              lfs - Labor Force Statistics              wages - Wages              ec - Employer Costs              sla - State and Local Area Employment              bed - Business Employment Dynamics              tu - Time Use          (provider: bls) | [optional] 
 **include_extras** | **bool**| Include additional information in the search results. Extra fields returned are metadata and vary by survey. Fields are undefined strings that typically have names ending with &#39;_code&#39;. (provider: bls) | [optional] [default to False]
 **include_code_map** | **bool**| When True, includes the complete code map for eaçh survey in the category, returned separately as a nested JSON to the &#x60;extras[&#39;results_metadata&#39;]&#x60; property of the response. Example content is the NAICS industry map for PPI surveys. Each code is a value within the &#39;symbol&#39; of the time series. (provider: bls) | [optional] [default to False]

### Return type

[**OBBjectBlsSearch**](OBBjectBlsSearch.md)

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

# **economy_survey_bls_series**
> OBBjectBlsSeries economy_survey_bls_series(symbol, provider=provider, start_date=start_date, end_date=end_date, calculations=calculations, annual_average=annual_average, aspects=aspects)

Bls Series

Get time series data for one, or more, BLS series IDs.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_bls_series import OBBjectBlsSeries
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
    api_instance = openbb_client.EconomyApi(api_client)
    symbol = 'symbol_example' # str | Symbol to get data for. Multiple comma separated items allowed for provider(s): bls.
    provider = bls # str |  (optional) (default to bls)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    calculations = True # bool | Include calculations in the response, if available. Default is True. (provider: bls) (optional) (default to True)
    annual_average = False # bool | Include annual averages in the response, if available. Default is False. (provider: bls) (optional) (default to False)
    aspects = False # bool | Include all aspects associated with a data point for a given BLS series ID, if available. Returned with the series metadata, under `extras` of the response object. Default is False. (provider: bls) (optional) (default to False)

    try:
        # Bls Series
        api_response = api_instance.economy_survey_bls_series(symbol, provider=provider, start_date=start_date, end_date=end_date, calculations=calculations, annual_average=annual_average, aspects=aspects)
        print("The response of EconomyApi->economy_survey_bls_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_bls_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol to get data for. Multiple comma separated items allowed for provider(s): bls. | 
 **provider** | **str**|  | [optional] [default to bls]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **calculations** | **bool**| Include calculations in the response, if available. Default is True. (provider: bls) | [optional] [default to True]
 **annual_average** | **bool**| Include annual averages in the response, if available. Default is False. (provider: bls) | [optional] [default to False]
 **aspects** | **bool**| Include all aspects associated with a data point for a given BLS series ID, if available. Returned with the series metadata, under &#x60;extras&#x60; of the response object. Default is False. (provider: bls) | [optional] [default to False]

### Return type

[**OBBjectBlsSeries**](OBBjectBlsSeries.md)

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

# **economy_survey_economic_conditions_chicago**
> OBBjectSurveyOfEconomicConditionsChicago economy_survey_economic_conditions_chicago(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Economic Conditions Chicago

Get The Survey Of Economic Conditions For The Chicago Region.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_survey_of_economic_conditions_chicago import OBBjectSurveyOfEconomicConditionsChicago
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert monthly data to lower frequency. None is monthly. (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log          (provider: fred) (optional)

    try:
        # Economic Conditions Chicago
        api_response = api_instance.economy_survey_economic_conditions_chicago(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of EconomyApi->economy_survey_economic_conditions_chicago:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_economic_conditions_chicago: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**| Frequency aggregation to convert monthly data to lower frequency. None is monthly. (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.              avg &#x3D; Average              sum &#x3D; Sum              eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type              None &#x3D; No transformation              chg &#x3D; Change              ch1 &#x3D; Change from Year Ago              pch &#x3D; Percent Change              pc1 &#x3D; Percent Change from Year Ago              pca &#x3D; Compounded Annual Rate of Change              cch &#x3D; Continuously Compounded Rate of Change              cca &#x3D; Continuously Compounded Annual Rate of Change              log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectSurveyOfEconomicConditionsChicago**](OBBjectSurveyOfEconomicConditionsChicago.md)

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

# **economy_survey_manufacturing_outlook_texas**
> OBBjectManufacturingOutlookTexas economy_survey_manufacturing_outlook_texas(provider=provider, start_date=start_date, end_date=end_date, topic=topic, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

Manufacturing Outlook Texas

Get The Manufacturing Outlook Survey For The Texas Region.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_manufacturing_outlook_texas import OBBjectManufacturingOutlookTexas
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    topic = openbb_client.Fred() # Fred | The topic for the survey response. Multiple comma separated items allowed. (provider: fred) (optional)
    frequency = 'frequency_example' # str |          Frequency aggregation to convert monthly data to lower frequency. None is monthly.          (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str |          A key that indicates the aggregation method used for frequency aggregation.             avg = Average             sum = Sum             eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Manufacturing Outlook Texas
        api_response = api_instance.economy_survey_manufacturing_outlook_texas(provider=provider, start_date=start_date, end_date=end_date, topic=topic, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of EconomyApi->economy_survey_manufacturing_outlook_texas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_manufacturing_outlook_texas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **topic** | [**Fred**](.md)| The topic for the survey response. Multiple comma separated items allowed. (provider: fred) | [optional] 
 **frequency** | **str**|          Frequency aggregation to convert monthly data to lower frequency. None is monthly.          (provider: fred) | [optional] 
 **aggregation_method** | **str**|          A key that indicates the aggregation method used for frequency aggregation.             avg &#x3D; Average             sum &#x3D; Sum             eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectManufacturingOutlookTexas**](OBBjectManufacturingOutlookTexas.md)

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

# **economy_survey_nonfarm_payrolls**
> OBBjectNonFarmPayrolls economy_survey_nonfarm_payrolls(provider=provider, var_date=var_date, category=category)

Nonfarm Payrolls

Get Nonfarm Payrolls Survey.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_non_farm_payrolls import OBBjectNonFarmPayrolls
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    var_date = openbb_client.Date1() # Date1 | A specific date to get data for. Default is the latest report. Multiple comma separated items allowed for provider(s): fred. (optional)
    category = employees_nsa # str | The category to query. (provider: fred) (optional) (default to employees_nsa)

    try:
        # Nonfarm Payrolls
        api_response = api_instance.economy_survey_nonfarm_payrolls(provider=provider, var_date=var_date, category=category)
        print("The response of EconomyApi->economy_survey_nonfarm_payrolls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_nonfarm_payrolls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **var_date** | [**Date1**](.md)| A specific date to get data for. Default is the latest report. Multiple comma separated items allowed for provider(s): fred. | [optional] 
 **category** | **str**| The category to query. (provider: fred) | [optional] [default to employees_nsa]

### Return type

[**OBBjectNonFarmPayrolls**](OBBjectNonFarmPayrolls.md)

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

# **economy_survey_sloos**
> OBBjectSeniorLoanOfficerSurvey economy_survey_sloos(provider=provider, start_date=start_date, end_date=end_date, category=category, transform=transform)

Sloos

Get Senior Loan Officers Opinion Survey.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_senior_loan_officer_survey import OBBjectSeniorLoanOfficerSurvey
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    category = spreads # str | Category of survey response. (provider: fred) (optional) (default to spreads)
    transform = 'transform_example' # str |          Transformation type             None = No transformation             chg = Change             ch1 = Change from Year Ago             pch = Percent Change             pc1 = Percent Change from Year Ago             pca = Compounded Annual Rate of Change             cch = Continuously Compounded Rate of Change             cca = Continuously Compounded Annual Rate of Change             log = Natural Log          (provider: fred) (optional)

    try:
        # Sloos
        api_response = api_instance.economy_survey_sloos(provider=provider, start_date=start_date, end_date=end_date, category=category, transform=transform)
        print("The response of EconomyApi->economy_survey_sloos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_sloos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **category** | **str**| Category of survey response. (provider: fred) | [optional] [default to spreads]
 **transform** | **str**|          Transformation type             None &#x3D; No transformation             chg &#x3D; Change             ch1 &#x3D; Change from Year Ago             pch &#x3D; Percent Change             pc1 &#x3D; Percent Change from Year Ago             pca &#x3D; Compounded Annual Rate of Change             cch &#x3D; Continuously Compounded Rate of Change             cca &#x3D; Continuously Compounded Annual Rate of Change             log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectSeniorLoanOfficerSurvey**](OBBjectSeniorLoanOfficerSurvey.md)

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

# **economy_survey_university_of_michigan**
> OBBjectUniversityOfMichigan economy_survey_university_of_michigan(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)

University Of Michigan

Get University of Michigan Consumer Sentiment and Inflation Expectations Surveys.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_university_of_michigan import OBBjectUniversityOfMichigan
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = fred # str |  (optional) (default to fred)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    frequency = 'frequency_example' # str | Frequency aggregation to convert monthly data to lower frequency. None is monthly. (provider: fred) (optional)
    aggregation_method = 'aggregation_method_example' # str | A key that indicates the aggregation method used for frequency aggregation.              avg = Average              sum = Sum              eop = End of Period          (provider: fred) (optional)
    transform = 'transform_example' # str | Transformation type              None = No transformation              chg = Change              ch1 = Change from Year Ago              pch = Percent Change              pc1 = Percent Change from Year Ago              pca = Compounded Annual Rate of Change              cch = Continuously Compounded Rate of Change              cca = Continuously Compounded Annual Rate of Change              log = Natural Log          (provider: fred) (optional)

    try:
        # University Of Michigan
        api_response = api_instance.economy_survey_university_of_michigan(provider=provider, start_date=start_date, end_date=end_date, frequency=frequency, aggregation_method=aggregation_method, transform=transform)
        print("The response of EconomyApi->economy_survey_university_of_michigan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_survey_university_of_michigan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to fred]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **frequency** | **str**| Frequency aggregation to convert monthly data to lower frequency. None is monthly. (provider: fred) | [optional] 
 **aggregation_method** | **str**| A key that indicates the aggregation method used for frequency aggregation.              avg &#x3D; Average              sum &#x3D; Sum              eop &#x3D; End of Period          (provider: fred) | [optional] 
 **transform** | **str**| Transformation type              None &#x3D; No transformation              chg &#x3D; Change              ch1 &#x3D; Change from Year Ago              pch &#x3D; Percent Change              pc1 &#x3D; Percent Change from Year Ago              pca &#x3D; Compounded Annual Rate of Change              cch &#x3D; Continuously Compounded Rate of Change              cca &#x3D; Continuously Compounded Annual Rate of Change              log &#x3D; Natural Log          (provider: fred) | [optional] 

### Return type

[**OBBjectUniversityOfMichigan**](OBBjectUniversityOfMichigan.md)

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

# **economy_unemployment**
> OBBjectUnemployment economy_unemployment(provider=provider, country=country, frequency=frequency, start_date=start_date, end_date=end_date, sex=sex, age=age, seasonal_adjustment=seasonal_adjustment)

Unemployment

Get global unemployment data.

### Example


```python
import openbb_client
from openbb_client.models.ob_bject_unemployment import OBBjectUnemployment
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
    api_instance = openbb_client.EconomyApi(api_client)
    provider = oecd # str |  (optional) (default to oecd)
    country = 'united_states' # str | The country to get data. Multiple comma separated items allowed for provider(s): oecd. (optional) (default to 'united_states')
    frequency = monthly # str | The frequency of the data. (optional) (default to monthly)
    start_date = '2013-10-20' # date | Start date of the data, in YYYY-MM-DD format. (optional)
    end_date = '2013-10-20' # date | End date of the data, in YYYY-MM-DD format. (optional)
    sex = total # str | Sex to get unemployment for. (provider: oecd) (optional) (default to total)
    age = total # str | Age group to get unemployment for. Total indicates 15 years or over (provider: oecd) (optional) (default to total)
    seasonal_adjustment = False # bool | Whether to get seasonally adjusted unemployment. Defaults to False. (provider: oecd) (optional) (default to False)

    try:
        # Unemployment
        api_response = api_instance.economy_unemployment(provider=provider, country=country, frequency=frequency, start_date=start_date, end_date=end_date, sex=sex, age=age, seasonal_adjustment=seasonal_adjustment)
        print("The response of EconomyApi->economy_unemployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomyApi->economy_unemployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] [default to oecd]
 **country** | **str**| The country to get data. Multiple comma separated items allowed for provider(s): oecd. | [optional] [default to &#39;united_states&#39;]
 **frequency** | **str**| The frequency of the data. | [optional] [default to monthly]
 **start_date** | **date**| Start date of the data, in YYYY-MM-DD format. | [optional] 
 **end_date** | **date**| End date of the data, in YYYY-MM-DD format. | [optional] 
 **sex** | **str**| Sex to get unemployment for. (provider: oecd) | [optional] [default to total]
 **age** | **str**| Age group to get unemployment for. Total indicates 15 years or over (provider: oecd) | [optional] [default to total]
 **seasonal_adjustment** | **bool**| Whether to get seasonally adjusted unemployment. Defaults to False. (provider: oecd) | [optional] [default to False]

### Return type

[**OBBjectUnemployment**](OBBjectUnemployment.md)

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

