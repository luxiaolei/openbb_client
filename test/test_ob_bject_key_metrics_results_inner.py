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

from openbb_client.models.ob_bject_key_metrics_results_inner import OBBjectKeyMetricsResultsInner

class TestOBBjectKeyMetricsResultsInner(unittest.TestCase):
    """OBBjectKeyMetricsResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectKeyMetricsResultsInner:
        """Test OBBjectKeyMetricsResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectKeyMetricsResultsInner`
        """
        model = OBBjectKeyMetricsResultsInner()
        if include_optional:
            return OBBjectKeyMetricsResultsInner(
                symbol = '',
                market_cap = 1.337,
                pe_ratio = 1.337,
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                calendar_year = 56,
                revenue_per_share = 1.337,
                capex_per_share = 1.337,
                net_income_per_share = 1.337,
                operating_cash_flow_per_share = 1.337,
                free_cash_flow_per_share = 1.337,
                cash_per_share = 1.337,
                book_value_per_share = 1.337,
                tangible_book_value_per_share = 1.337,
                shareholders_equity_per_share = 1.337,
                interest_debt_per_share = 1.337,
                price_to_sales = 1.337,
                price_to_operating_cash_flow = 1.337,
                price_to_free_cash_flow = 1.337,
                price_to_book = 1.337,
                price_to_tangible_book = 1.337,
                ev_to_sales = 1.337,
                ev_to_ebitda = 1.337,
                ev_to_operating_cash_flow = 1.337,
                ev_to_free_cash_flow = 1.337,
                earnings_yield = 1.337,
                free_cash_flow_yield = 1.337,
                debt_to_market_cap = 1.337,
                debt_to_equity = 1.337,
                debt_to_assets = 1.337,
                net_debt_to_ebitda = 1.337,
                current_ratio = 1.337,
                interest_coverage = 1.337,
                income_quality = 1.337,
                payout_ratio = 1.337,
                sales_general_and_administrative_to_revenue = 1.337,
                research_and_developement_to_revenue = 1.337,
                intangibles_to_total_assets = 1.337,
                capex_to_operating_cash_flow = 1.337,
                capex_to_revenue = 1.337,
                capex_to_depreciation = 1.337,
                stock_based_compensation_to_revenue = 1.337,
                working_capital = 1.337,
                tangible_asset_value = 1.337,
                net_current_asset_value = 1.337,
                enterprise_value = 56,
                invested_capital = 1.337,
                average_receivables = 1.337,
                average_payables = 1.337,
                average_inventory = 1.337,
                days_sales_outstanding = 1.337,
                days_payables_outstanding = 1.337,
                days_of_inventory_on_hand = 1.337,
                receivables_turnover = 1.337,
                payables_turnover = 1.337,
                inventory_turnover = 1.337,
                return_on_equity = 1.337,
                return_on_invested_capital = 1.337,
                return_on_tangible_assets = 1.337,
                dividend_yield = 1.337,
                graham_number = 1.337,
                graham_net_net = 1.337,
                forward_pe = 1.337,
                peg_ratio = 1.337,
                peg_ratio_ttm = 1.337,
                eps_ttm = 1.337,
                eps_forward = 1.337,
                enterprise_to_ebitda = 1.337,
                earnings_growth = 1.337,
                earnings_growth_quarterly = 1.337,
                revenue_growth = 1.337,
                enterprise_to_revenue = 1.337,
                quick_ratio = 1.337,
                gross_margin = 1.337,
                operating_margin = 1.337,
                ebitda_margin = 1.337,
                profit_margin = 1.337,
                return_on_assets = 1.337,
                dividend_yield = 1.337,
                dividend_yield_5y_avg = 1.337,
                book_value = 1.337,
                overall_risk = 1.337,
                audit_risk = 1.337,
                board_risk = 1.337,
                compensation_risk = 1.337,
                shareholder_rights_risk = 1.337,
                beta = 1.337,
                price_return_1y = 1.337,
                currency = '',
                price_to_revenue = 1.337,
                ebit_margin = 1.337,
                eps = 1.337,
                eps_growth = 1.337,
                ebitda_growth = 1.337,
                ebit_growth = 1.337,
                net_income_growth = 1.337,
                free_cash_flow_to_firm_growth = 1.337,
                invested_capital_growth = 1.337,
                ebitda = 56,
                ebit = 56,
                long_term_debt = 56,
                total_debt = 56,
                total_capital = 56,
                free_cash_flow_to_firm = 56,
                altman_z_score = 1.337,
                last_price = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                volume_avg = 56,
                short_interest = 56,
                shares_outstanding = 56,
                days_to_cover = 1.337
            )
        else:
            return OBBjectKeyMetricsResultsInner(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
        )
        """

    def testOBBjectKeyMetricsResultsInner(self):
        """Test OBBjectKeyMetricsResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
