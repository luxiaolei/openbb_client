# coding: utf-8

"""
    OpenBB Platform API

    Investment research for everyone, anywhere.

    The version of the OpenAPI document: 1
    Contact: hello@openbb.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openbb_client.models.intrinio_key_metrics_data import IntrinioKeyMetricsData

class TestIntrinioKeyMetricsData(unittest.TestCase):
    """IntrinioKeyMetricsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioKeyMetricsData:
        """Test IntrinioKeyMetricsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioKeyMetricsData`
        """
        model = IntrinioKeyMetricsData()
        if include_optional:
            return IntrinioKeyMetricsData(
                symbol = '',
                market_cap = 1.337,
                pe_ratio = 1.337,
                price_to_book = 1.337,
                price_to_tangible_book = 1.337,
                price_to_revenue = 1.337,
                quick_ratio = 1.337,
                gross_margin = 1.337,
                ebit_margin = 1.337,
                profit_margin = 1.337,
                eps = 1.337,
                eps_growth = 1.337,
                revenue_growth = 1.337,
                ebitda_growth = 1.337,
                ebit_growth = 1.337,
                net_income_growth = 1.337,
                free_cash_flow_to_firm_growth = 1.337,
                invested_capital_growth = 1.337,
                return_on_assets = 1.337,
                return_on_equity = 1.337,
                return_on_invested_capital = 1.337,
                ebitda = 56,
                ebit = 56,
                long_term_debt = 56,
                total_debt = 56,
                total_capital = 56,
                enterprise_value = 56,
                free_cash_flow_to_firm = 56,
                altman_z_score = 1.337,
                beta = 1.337,
                dividend_yield = 1.337,
                earnings_yield = 1.337,
                last_price = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                volume_avg = 56,
                short_interest = 56,
                shares_outstanding = 56,
                days_to_cover = 1.337
            )
        else:
            return IntrinioKeyMetricsData(
        )
        """

    def testIntrinioKeyMetricsData(self):
        """Test IntrinioKeyMetricsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
