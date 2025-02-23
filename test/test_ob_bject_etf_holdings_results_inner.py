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

from openbb_client.models.ob_bject_etf_holdings_results_inner import OBBjectEtfHoldingsResultsInner

class TestOBBjectEtfHoldingsResultsInner(unittest.TestCase):
    """OBBjectEtfHoldingsResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OBBjectEtfHoldingsResultsInner:
        """Test OBBjectEtfHoldingsResultsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OBBjectEtfHoldingsResultsInner`
        """
        model = OBBjectEtfHoldingsResultsInner()
        if include_optional:
            return OBBjectEtfHoldingsResultsInner(
                symbol = '',
                name = '',
                security_type = '',
                isin = '',
                ric = '',
                sedol = '',
                share_class_figi = '',
                country = '',
                maturity_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                contract_expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                coupon = 1.337,
                balance = 1.337,
                unit = '',
                units_per_share = 1.337,
                face_value = 1.337,
                derivatives_value = 1.337,
                value = 1.337,
                weight = 1.337,
                updated = None,
                lei = '',
                title = '',
                cusip = '',
                units = None,
                currency = '',
                payoff_profile = '',
                asset_category = '',
                issuer_category = '',
                is_restricted = '',
                fair_value_level = 56,
                is_cash_collateral = '',
                is_non_cash_collateral = '',
                is_loan_by_fund = '',
                cik = '',
                acceptance_datetime = '',
                other_id = '',
                loan_value = 1.337,
                issuer_conditional = '',
                asset_conditional = '',
                coupon_kind = '',
                rate_type = '',
                annualized_return = 1.337,
                is_default = '',
                in_arrears = '',
                is_paid_kind = '',
                derivative_category = '',
                counterparty = '',
                underlying_name = '',
                option_type = '',
                derivative_payoff = '',
                expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                exercise_price = 1.337,
                exercise_currency = '',
                shares_per_contract = 1.337,
                delta = None,
                rate_type_rec = '',
                receive_currency = '',
                upfront_receive = 1.337,
                floating_rate_index_rec = '',
                floating_rate_spread_rec = 1.337,
                rate_tenor_rec = '',
                rate_tenor_unit_rec = None,
                reset_date_rec = '',
                reset_date_unit_rec = None,
                rate_type_pmnt = '',
                payment_currency = '',
                upfront_payment = 1.337,
                floating_rate_index_pmnt = '',
                floating_rate_spread_pmnt = 1.337,
                rate_tenor_pmnt = '',
                rate_tenor_unit_pmnt = None,
                reset_date_pmnt = '',
                reset_date_unit_pmnt = None,
                repo_type = '',
                is_cleared = '',
                is_tri_party = '',
                principal_amount = 1.337,
                principal_currency = '',
                collateral_type = '',
                collateral_amount = 1.337,
                collateral_currency = '',
                exchange_currency = '',
                exchange_rate = 1.337,
                currency_sold = '',
                currency_amount_sold = 1.337,
                currency_bought = '',
                currency_amount_bought = 1.337,
                notional_amount = 1.337,
                notional_currency = '',
                unrealized_gain = 1.337
            )
        else:
            return OBBjectEtfHoldingsResultsInner(
        )
        """

    def testOBBjectEtfHoldingsResultsInner(self):
        """Test OBBjectEtfHoldingsResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
