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

from openbb_client.models.yf_growth_tech_equities_data import YFGrowthTechEquitiesData

class TestYFGrowthTechEquitiesData(unittest.TestCase):
    """YFGrowthTechEquitiesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YFGrowthTechEquitiesData:
        """Test YFGrowthTechEquitiesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YFGrowthTechEquitiesData`
        """
        model = YFGrowthTechEquitiesData()
        if include_optional:
            return YFGrowthTechEquitiesData(
                symbol = '',
                name = '',
                price = 1.337,
                change = 1.337,
                percent_change = 1.337,
                volume = None,
                open = 1.337,
                high = 1.337,
                low = 1.337,
                previous_close = 1.337,
                ma_50 = 1.337,
                ma_200 = 1.337,
                year_high = 1.337,
                year_low = 1.337,
                market_cap = 1.337,
                shares_outstanding = 1.337,
                book_value = 1.337,
                price_to_book = 1.337,
                eps_ttm = 1.337,
                eps_forward = 1.337,
                pe_forward = 1.337,
                dividend_yield = 1.337,
                exchange = '',
                exchange_timezone = '',
                earnings_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                currency = ''
            )
        else:
            return YFGrowthTechEquitiesData(
                symbol = '',
                price = 1.337,
                change = 1.337,
                percent_change = 1.337,
                volume = None,
        )
        """

    def testYFGrowthTechEquitiesData(self):
        """Test YFGrowthTechEquitiesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
