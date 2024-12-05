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

from openbb_client.models.fred_series_data import FredSeriesData

class TestFredSeriesData(unittest.TestCase):
    """FredSeriesData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FredSeriesData:
        """Test FredSeriesData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FredSeriesData`
        """
        model = FredSeriesData()
        if include_optional:
            return FredSeriesData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return FredSeriesData(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testFredSeriesData(self):
        """Test FredSeriesData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
