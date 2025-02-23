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

from openbb_client.models.fmp_equity_valuation_multiples_data import FMPEquityValuationMultiplesData

class TestFMPEquityValuationMultiplesData(unittest.TestCase):
    """FMPEquityValuationMultiplesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPEquityValuationMultiplesData:
        """Test FMPEquityValuationMultiplesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPEquityValuationMultiplesData`
        """
        model = FMPEquityValuationMultiplesData()
        if include_optional:
            return FMPEquityValuationMultiplesData(
                symbol = '',
                revenue_per_share_ttm = 1.337,
                net_income_per_share_ttm = 1.337,
                operating_cash_flow_per_share_ttm = 1.337,
                free_cash_flow_per_share_ttm = 1.337,
                cash_per_share_ttm = 1.337,
                book_value_per_share_ttm = 1.337,
                tangible_book_value_per_share_ttm = 1.337,
                shareholders_equity_per_share_ttm = 1.337,
                interest_debt_per_share_ttm = 1.337,
                market_cap_ttm = 1.337,
                enterprise_value_ttm = 1.337,
                pe_ratio_ttm = 1.337,
                price_to_sales_ratio_ttm = 1.337,
                pocf_ratio_ttm = 1.337,
                pfcf_ratio_ttm = 1.337,
                pb_ratio_ttm = 1.337,
                ptb_ratio_ttm = 1.337,
                ev_to_sales_ttm = 1.337,
                enterprise_value_over_ebitda_ttm = 1.337,
                ev_to_operating_cash_flow_ttm = 1.337,
                ev_to_free_cash_flow_ttm = 1.337,
                earnings_yield_ttm = 1.337,
                free_cash_flow_yield_ttm = 1.337,
                debt_to_equity_ttm = 1.337,
                debt_to_assets_ttm = 1.337,
                net_debt_to_ebitda_ttm = 1.337,
                current_ratio_ttm = 1.337,
                interest_coverage_ttm = 1.337,
                income_quality_ttm = 1.337,
                dividend_yield_ttm = 1.337,
                dividend_yield_percentage_ttm = 1.337,
                dividend_to_market_cap_ttm = 1.337,
                dividend_per_share_ttm = 1.337,
                payout_ratio_ttm = 1.337,
                sales_general_and_administrative_to_revenue_ttm = 1.337,
                research_and_development_to_revenue_ttm = 1.337,
                intangibles_to_total_assets_ttm = 1.337,
                capex_to_operating_cash_flow_ttm = 1.337,
                capex_to_revenue_ttm = 1.337,
                capex_to_depreciation_ttm = 1.337,
                stock_based_compensation_to_revenue_ttm = 1.337,
                graham_number_ttm = 1.337,
                roic_ttm = 1.337,
                return_on_tangible_assets_ttm = 1.337,
                graham_net_net_ttm = 1.337,
                working_capital_ttm = 1.337,
                tangible_asset_value_ttm = 1.337,
                net_current_asset_value_ttm = 1.337,
                invested_capital_ttm = 1.337,
                average_receivables_ttm = 1.337,
                average_payables_ttm = 1.337,
                average_inventory_ttm = 1.337,
                days_sales_outstanding_ttm = 1.337,
                days_payables_outstanding_ttm = 1.337,
                days_of_inventory_on_hand_ttm = 1.337,
                receivables_turnover_ttm = 1.337,
                payables_turnover_ttm = 1.337,
                inventory_turnover_ttm = 1.337,
                roe_ttm = 1.337,
                capex_per_share_ttm = 1.337
            )
        else:
            return FMPEquityValuationMultiplesData(
                symbol = '',
        )
        """

    def testFMPEquityValuationMultiplesData(self):
        """Test FMPEquityValuationMultiplesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
