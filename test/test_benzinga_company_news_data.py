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

from openbb_client.models.benzinga_company_news_data import BenzingaCompanyNewsData

class TestBenzingaCompanyNewsData(unittest.TestCase):
    """BenzingaCompanyNewsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BenzingaCompanyNewsData:
        """Test BenzingaCompanyNewsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BenzingaCompanyNewsData`
        """
        model = BenzingaCompanyNewsData()
        if include_optional:
            return BenzingaCompanyNewsData(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                title = '',
                text = '',
                images = [
                    {
                        'key' : ''
                        }
                    ],
                url = '',
                symbols = '',
                id = '',
                author = '',
                teaser = '',
                channels = '',
                stocks = '',
                tags = '',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BenzingaCompanyNewsData(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                title = '',
                url = '',
                id = '',
        )
        """

    def testBenzingaCompanyNewsData(self):
        """Test BenzingaCompanyNewsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
