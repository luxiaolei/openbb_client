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

from openbb_client.api.derivatives_api import DerivativesApi


class TestDerivativesApi(unittest.TestCase):
    """DerivativesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DerivativesApi()

    def tearDown(self) -> None:
        pass

    def test_derivatives_futures_curve(self) -> None:
        """Test case for derivatives_futures_curve

        Curve
        """
        pass

    def test_derivatives_futures_historical(self) -> None:
        """Test case for derivatives_futures_historical

        Historical
        """
        pass

    def test_derivatives_options_chains(self) -> None:
        """Test case for derivatives_options_chains

        Chains
        """
        pass

    def test_derivatives_options_snapshots(self) -> None:
        """Test case for derivatives_options_snapshots

        Snapshots
        """
        pass

    def test_derivatives_options_unusual(self) -> None:
        """Test case for derivatives_options_unusual

        Unusual
        """
        pass


if __name__ == '__main__':
    unittest.main()
