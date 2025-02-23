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

from openbb_client.models.ob_bject_income_statement_results_inner import OBBjectIncomeStatementResultsInner

class TestOBBjectIncomeStatementResultsInner(unittest.TestCase):
    """OBBjectIncomeStatementResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectIncomeStatementResultsInner:
        """Test OBBjectIncomeStatementResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectIncomeStatementResultsInner`
        """
        model = OBBjectIncomeStatementResultsInner()
        if include_optional:
            return OBBjectIncomeStatementResultsInner(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fiscal_period = '',
                fiscal_year = 56,
                revenue = 1.337,
                cost_of_revenue_goods = 1.337,
                cost_of_revenue_services = 1.337,
                cost_of_revenue = 1.337,
                gross_profit = 1.337,
                provisions_for_loan_lease_and_other_losses = 1.337,
                depreciation_and_amortization = 1.337,
                income_tax_expense_benefit_current = 1.337,
                deferred_tax_benefit = 1.337,
                benefits_costs_expenses = 1.337,
                selling_general_and_administrative_expense = 1.337,
                research_and_development = 1.337,
                costs_and_expenses = 1.337,
                other_operating_expenses = 1.337,
                operating_expenses = 1.337,
                operating_income = 1.337,
                non_operating_income = 1.337,
                interest_and_dividend_income = 1.337,
                total_interest_expense = 1.337,
                interest_and_debt_expense = 1.337,
                net_interest_income = 1.337,
                interest_income_after_provision_for_losses = 1.337,
                non_interest_expense = 1.337,
                non_interest_income = 1.337,
                income_from_discontinued_operations_net_of_tax_on_disposal = 1.337,
                income_from_discontinued_operations_net_of_tax = 1.337,
                income_before_equity_method_investments = 1.337,
                income_from_equity_method_investments = 1.337,
                total_pre_tax_income = 1.337,
                income_tax_expense = 1.337,
                income_after_tax = 1.337,
                consolidated_net_income = 1.337,
                net_income_attributable_noncontrolling_interest = 1.337,
                net_income_attributable_to_parent = 1.337,
                net_income_attributable_to_common_shareholders = 1.337,
                participating_securities_earnings = 1.337,
                undistributed_earnings_allocated_to_participating_securities = 1.337,
                common_stock_dividends = 1.337,
                preferred_stock_dividends_and_other_adjustments = 1.337,
                basic_earnings_per_share = 1.337,
                diluted_earnings_per_share = 1.337,
                weighted_average_basic_shares_outstanding = 1.337,
                weighted_average_diluted_shares_outstanding = 1.337,
                reported_currency = '',
                operating_revenue = 1.337,
                operating_cost_of_revenue = 1.337,
                gross_profit_margin = 1.337,
                provision_for_credit_losses = 1.337,
                research_and_development_expense = 1.337,
                selling_general_and_admin_expense = 1.337,
                salaries_and_employee_benefits = 1.337,
                marketing_expense = 1.337,
                net_occupancy_and_equipment_expense = 1.337,
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
                other_income = 1.337,
                other_revenue = 1.337,
                extraordinary_income = 1.337,
                total_other_income = 1.337,
                ebitda = 1.337,
                ebitda_margin = 1.337,
                ebit = 1.337,
                pre_tax_income_margin = 1.337,
                impairment_charge = 1.337,
                restructuring_charge = 1.337,
                service_charges_on_deposit_accounts = 1.337,
                other_service_charges = 1.337,
                other_special_charges = 1.337,
                other_cost_of_revenue = 1.337,
                net_income_continuing_operations = 1.337,
                net_income_discontinued_operations = 1.337,
                other_adjustments_to_consolidated_net_income = 1.337,
                other_adjustment_to_net_income_attributable_to_common_shareholders = 1.337,
                net_income_attributable_to_noncontrolling_interest = 1.337,
                basic_and_diluted_earnings_per_share = 1.337,
                cash_dividends_to_common_per_share = 1.337,
                preferred_stock_dividends_declared = 1.337,
                weighted_average_basic_and_diluted_shares_outstanding = 1.337,
                filing_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                accepted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                general_and_admin_expense = 1.337,
                selling_and_marketing_expense = 1.337,
                other_expenses = 1.337,
                cost_and_expenses = 1.337,
                interest_income = 1.337,
                operating_income_margin = 1.337,
                total_other_income_expenses = 1.337,
                net_income_margin = 1.337,
                link = '',
                final_link = ''
            )
        else:
            return OBBjectIncomeStatementResultsInner(
                period_ending = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testOBBjectIncomeStatementResultsInner(self):
        """Test OBBjectIncomeStatementResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
