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

from openbb_client.models.econ_db_country_profile_data import EconDbCountryProfileData

class TestEconDbCountryProfileData(unittest.TestCase):
    """EconDbCountryProfileData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EconDbCountryProfileData:
        """Test EconDbCountryProfileData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EconDbCountryProfileData`
        """
        model = EconDbCountryProfileData()
        if include_optional:
            return EconDbCountryProfileData(
                country = '',
                population = 56,
                gdp_usd = 1.337,
                gdp_qoq = 1.337,
                gdp_yoy = 1.337,
                cpi_yoy = 1.337,
                core_yoy = 1.337,
                retail_sales_yoy = 1.337,
                industrial_production_yoy = 1.337,
                policy_rate = 1.337,
                yield_10y = 1.337,
                govt_debt_gdp = 1.337,
                current_account_gdp = 1.337,
                jobless_rate = 1.337
            )
        else:
            return EconDbCountryProfileData(
                country = '',
        )
        """

    def testEconDbCountryProfileData(self):
        """Test EconDbCountryProfileData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
