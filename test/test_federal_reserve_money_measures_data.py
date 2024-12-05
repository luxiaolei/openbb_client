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

from openbb_client.models.federal_reserve_money_measures_data import FederalReserveMoneyMeasuresData

class TestFederalReserveMoneyMeasuresData(unittest.TestCase):
    """FederalReserveMoneyMeasuresData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FederalReserveMoneyMeasuresData:
        """Test FederalReserveMoneyMeasuresData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FederalReserveMoneyMeasuresData`
        """
        model = FederalReserveMoneyMeasuresData()
        if include_optional:
            return FederalReserveMoneyMeasuresData(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                m1 = 1.337,
                m2 = 1.337,
                currency = 1.337,
                demand_deposits = 1.337,
                retail_money_market_funds = 1.337,
                other_liquid_deposits = 1.337,
                small_denomination_time_deposits = 1.337
            )
        else:
            return FederalReserveMoneyMeasuresData(
                month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                m1 = 1.337,
                m2 = 1.337,
        )
        """

    def testFederalReserveMoneyMeasuresData(self):
        """Test FederalReserveMoneyMeasuresData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
