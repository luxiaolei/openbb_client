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

from openbb_client.models.fred_search_data import FredSearchData

class TestFredSearchData(unittest.TestCase):
    """FredSearchData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FredSearchData:
        """Test FredSearchData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FredSearchData`
        """
        model = FredSearchData()
        if include_optional:
            return FredSearchData(
                release_id = '',
                series_id = '',
                series_group = '',
                region_type = '',
                name = '',
                title = '',
                observation_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                observation_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                frequency = '',
                frequency_short = '',
                units = '',
                units_short = '',
                seasonal_adjustment = '',
                seasonal_adjustment_short = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                popularity = 56,
                group_popularity = 56,
                realtime_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                realtime_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                notes = '',
                press_release = True,
                url = ''
            )
        else:
            return FredSearchData(
        )
        """

    def testFredSearchData(self):
        """Test FredSearchData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
