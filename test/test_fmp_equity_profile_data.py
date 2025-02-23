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

from openbb_client.models.fmp_equity_profile_data import FMPEquityProfileData

class TestFMPEquityProfileData(unittest.TestCase):
    """FMPEquityProfileData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FMPEquityProfileData:
        """Test FMPEquityProfileData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FMPEquityProfileData`
        """
        model = FMPEquityProfileData()
        if include_optional:
            return FMPEquityProfileData(
                symbol = '',
                name = '',
                cik = '',
                cusip = '',
                isin = '',
                lei = '',
                legal_name = '',
                stock_exchange = '',
                sic = 56,
                short_description = '',
                long_description = '',
                ceo = '',
                company_url = '',
                business_address = '',
                mailing_address = '',
                business_phone_no = '',
                hq_address_1 = '',
                hq_address_2 = '',
                hq_address_city = '',
                hq_address_postal_code = '',
                hq_state = '',
                hq_country = '',
                inc_state = '',
                inc_country = '',
                employees = 56,
                entity_legal_form = '',
                entity_status = '',
                latest_filing_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                irs_number = '',
                sector = '',
                industry_category = '',
                industry_group = '',
                template = '',
                standardized_active = True,
                first_fundamental_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                last_fundamental_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                first_stock_price_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                last_stock_price_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                is_etf = True,
                is_actively_trading = True,
                is_adr = True,
                is_fund = True,
                image = '',
                currency = '',
                market_cap = 56,
                last_price = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                volume_avg = 56,
                annualized_dividend_amount = 1.337,
                beta = 1.337
            )
        else:
            return FMPEquityProfileData(
                symbol = '',
                is_etf = True,
                is_actively_trading = True,
                is_adr = True,
                is_fund = True,
        )
        """

    def testFMPEquityProfileData(self):
        """Test FMPEquityProfileData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
