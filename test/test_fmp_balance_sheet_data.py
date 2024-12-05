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

from openbb_client.models.fmp_balance_sheet_data import FMPBalanceSheetData

class TestFMPBalanceSheetData(unittest.TestCase):
    """FMPBalanceSheetData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPBalanceSheetData:
        """Test FMPBalanceSheetData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPBalanceSheetData`
        """
        model = FMPBalanceSheetData()
        if include_optional:
            return FMPBalanceSheetData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                fiscal_year = 56,
                filing_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                accepted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reported_currency = '',
                cash_and_cash_equivalents = 1.337,
                short_term_investments = 1.337,
                cash_and_short_term_investments = 1.337,
                net_receivables = 1.337,
                inventory = 1.337,
                other_current_assets = 1.337,
                total_current_assets = 1.337,
                plant_property_equipment_net = 1.337,
                goodwill = 1.337,
                intangible_assets = 1.337,
                goodwill_and_intangible_assets = 1.337,
                long_term_investments = 1.337,
                tax_assets = 1.337,
                other_non_current_assets = 1.337,
                non_current_assets = 1.337,
                other_assets = 1.337,
                total_assets = 1.337,
                accounts_payable = 1.337,
                short_term_debt = 1.337,
                tax_payables = 1.337,
                current_deferred_revenue = 1.337,
                other_current_liabilities = 1.337,
                total_current_liabilities = 1.337,
                long_term_debt = 1.337,
                deferred_revenue_non_current = 1.337,
                deferred_tax_liabilities_non_current = 1.337,
                other_non_current_liabilities = 1.337,
                total_non_current_liabilities = 1.337,
                other_liabilities = 1.337,
                capital_lease_obligations = 1.337,
                total_liabilities = 1.337,
                preferred_stock = 1.337,
                common_stock = 1.337,
                retained_earnings = 1.337,
                accumulated_other_comprehensive_income = 1.337,
                other_shareholders_equity = 1.337,
                other_total_shareholders_equity = 1.337,
                total_common_equity = 1.337,
                total_equity_non_controlling_interests = 1.337,
                total_liabilities_and_shareholders_equity = 1.337,
                minority_interest = 1.337,
                total_liabilities_and_total_equity = 1.337,
                total_investments = 1.337,
                total_debt = 1.337,
                net_debt = 1.337,
                link = '',
                final_link = ''
            )
        else:
            return FMPBalanceSheetData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testFMPBalanceSheetData(self):
        """Test FMPBalanceSheetData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
