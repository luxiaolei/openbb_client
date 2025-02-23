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

from openbb_client.models.intrinio_income_statement_data import IntrinioIncomeStatementData

class TestIntrinioIncomeStatementData(unittest.TestCase):
    """IntrinioIncomeStatementData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioIncomeStatementData:
        """Test IntrinioIncomeStatementData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioIncomeStatementData`
        """
        model = IntrinioIncomeStatementData()
        if include_optional:
            return IntrinioIncomeStatementData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                fiscal_year = 56,
                reported_currency = '',
                revenue = 1.337,
                operating_revenue = 1.337,
                cost_of_revenue = 1.337,
                operating_cost_of_revenue = 1.337,
                gross_profit = 1.337,
                gross_profit_margin = 1.337,
                provision_for_credit_losses = 1.337,
                research_and_development_expense = 1.337,
                selling_general_and_admin_expense = 1.337,
                salaries_and_employee_benefits = 1.337,
                marketing_expense = 1.337,
                net_occupancy_and_equipment_expense = 1.337,
                other_operating_expenses = 1.337,
                depreciation_expense = 1.337,
                amortization_expense = 1.337,
                amortization_of_deferred_policy_acquisition_costs = 1.337,
                exploration_expense = 1.337,
                depletion_expense = 1.337,
                total_operating_expenses = 1.337,
                total_operating_income = 1.337,
                deposits_and_money_market_investments_interest_income = 1.337,
                federal_funds_sold_and_securities_borrowed_interest_income = 1.337,
                investment_securities_interest_income = 1.337,
                loans_and_leases_interest_income = 1.337,
                trading_account_interest_income = 1.337,
                other_interest_income = 1.337,
                total_non_interest_income = 1.337,
                interest_and_investment_income = 1.337,
                short_term_borrowings_interest_expense = 1.337,
                long_term_debt_interest_expense = 1.337,
                capitalized_lease_obligations_interest_expense = 1.337,
                deposits_interest_expense = 1.337,
                federal_funds_purchased_and_securities_sold_interest_expense = 1.337,
                other_interest_expense = 1.337,
                total_interest_expense = 1.337,
                net_interest_income = 1.337,
                other_non_interest_income = 1.337,
                investment_banking_income = 1.337,
                trust_fees_by_commissions = 1.337,
                premiums_earned = 1.337,
                insurance_policy_acquisition_costs = 1.337,
                current_and_future_benefits = 1.337,
                property_and_liability_insurance_claims = 1.337,
                total_non_interest_expense = 1.337,
                net_realized_and_unrealized_capital_gains_on_investments = 1.337,
                other_gains = 1.337,
                non_operating_income = 1.337,
                other_income = 1.337,
                other_revenue = 1.337,
                extraordinary_income = 1.337,
                total_other_income = 1.337,
                ebitda = 1.337,
                ebitda_margin = 1.337,
                total_pre_tax_income = 1.337,
                ebit = 1.337,
                pre_tax_income_margin = 1.337,
                income_tax_expense = 1.337,
                impairment_charge = 1.337,
                restructuring_charge = 1.337,
                service_charges_on_deposit_accounts = 1.337,
                other_service_charges = 1.337,
                other_special_charges = 1.337,
                other_cost_of_revenue = 1.337,
                net_income_continuing_operations = 1.337,
                net_income_discontinued_operations = 1.337,
                consolidated_net_income = 1.337,
                other_adjustments_to_consolidated_net_income = 1.337,
                other_adjustment_to_net_income_attributable_to_common_shareholders = 1.337,
                net_income_attributable_to_noncontrolling_interest = 1.337,
                net_income_attributable_to_common_shareholders = 1.337,
                basic_earnings_per_share = 1.337,
                diluted_earnings_per_share = 1.337,
                basic_and_diluted_earnings_per_share = 1.337,
                cash_dividends_to_common_per_share = 1.337,
                preferred_stock_dividends_declared = 1.337,
                weighted_average_basic_shares_outstanding = 1.337,
                weighted_average_diluted_shares_outstanding = 1.337,
                weighted_average_basic_and_diluted_shares_outstanding = 1.337
            )
        else:
            return IntrinioIncomeStatementData(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testIntrinioIncomeStatementData(self):
        """Test IntrinioIncomeStatementData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
