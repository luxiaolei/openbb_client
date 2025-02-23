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

from openbb_client.models.intrinio_calendar_ipo_data import IntrinioCalendarIpoData

class TestIntrinioCalendarIpoData(unittest.TestCase):
    """IntrinioCalendarIpoData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntrinioCalendarIpoData:
        """Test IntrinioCalendarIpoData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntrinioCalendarIpoData`
        """
        model = IntrinioCalendarIpoData()
        if include_optional:
            return IntrinioCalendarIpoData(
                symbol = '',
                ipo_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                status = 'upcoming',
                exchange = '',
                offer_amount = 1.337,
                share_price = 1.337,
                share_price_lowest = 1.337,
                share_price_highest = 1.337,
                share_count = 56,
                share_count_lowest = 56,
                share_count_highest = 56,
                announcement_url = '',
                sec_report_url = '',
                open_price = 1.337,
                close_price = 1.337,
                volume = 56,
                day_change = 1.337,
                week_change = 1.337,
                month_change = 1.337,
                id = '',
                company = { },
                security = { }
            )
        else:
            return IntrinioCalendarIpoData(
        )
        """

    def testIntrinioCalendarIpoData(self):
        """Test IntrinioCalendarIpoData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
