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

from openbb_client.models.intrinio_cash_flow_statement_data import IntrinioCashFlowStatementData

class TestIntrinioCashFlowStatementData(unittest.TestCase):
    """IntrinioCashFlowStatementData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioCashFlowStatementData:
        """Test IntrinioCashFlowStatementData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioCashFlowStatementData`
        """
        model = IntrinioCashFlowStatementData()
        if include_optional:
            return IntrinioCashFlowStatementData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                fiscal_year = 56,
                reported_currency = '',
                net_income_continuing_operations = 1.337,
                net_income_discontinued_operations = 1.337,
                net_income = 1.337,
                provision_for_loan_losses = 1.337,
                provision_for_credit_losses = 1.337,
                depreciation_expense = 1.337,
                amortization_expense = 1.337,
                share_based_compensation = 1.337,
                non_cash_adjustments_to_reconcile_net_income = 1.337,
                changes_in_operating_assets_and_liabilities = 1.337,
                net_cash_from_continuing_operating_activities = 1.337,
                net_cash_from_discontinued_operating_activities = 1.337,
                net_cash_from_operating_activities = 1.337,
                divestitures = 1.337,
                sale_of_property_plant_and_equipment = 1.337,
                acquisitions = 1.337,
                purchase_of_investments = 1.337,
                purchase_of_investment_securities = 1.337,
                sale_and_maturity_of_investments = 1.337,
                loans_held_for_sale = 1.337,
                purchase_of_property_plant_and_equipment = 1.337,
                other_investing_activities = 1.337,
                net_cash_from_continuing_investing_activities = 1.337,
                net_cash_from_discontinued_investing_activities = 1.337,
                net_cash_from_investing_activities = 1.337,
                payment_of_dividends = 1.337,
                repurchase_of_common_equity = 1.337,
                repurchase_of_preferred_equity = 1.337,
                issuance_of_common_equity = 1.337,
                issuance_of_preferred_equity = 1.337,
                issuance_of_debt = 1.337,
                repayment_of_debt = 1.337,
                other_financing_activities = 1.337,
                cash_interest_received = 1.337,
                net_change_in_deposits = 1.337,
                net_increase_in_fed_funds_sold = 1.337,
                net_cash_from_continuing_financing_activities = 1.337,
                net_cash_from_discontinued_financing_activities = 1.337,
                net_cash_from_financing_activities = 1.337,
                effect_of_exchange_rate_changes = 1.337,
                other_net_changes_in_cash = 1.337,
                net_change_in_cash_and_equivalents = 1.337,
                cash_income_taxes_paid = 1.337,
                cash_interest_paid = 1.337
            )
        else:
            return IntrinioCashFlowStatementData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testIntrinioCashFlowStatementData(self):
        """Test IntrinioCashFlowStatementData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
