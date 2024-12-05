# coding: utf-8

"""
    OpenBB Platform API

    Investment research for everyone, anywhere.

    The version of the OpenAPI document: 1
    Contact: hello@openbb.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openbb_client.models.fmp_crypto_historical_data import FMPCryptoHistoricalData
from openbb_client.models.polygon_crypto_historical_data import PolygonCryptoHistoricalData
from openbb_client.models.tiingo_crypto_historical_data import TiingoCryptoHistoricalData
from openbb_client.models.y_finance_crypto_historical_data import YFinanceCryptoHistoricalData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

OBBJECTCRYPTOHISTORICALRESULTSINNER_ONE_OF_SCHEMAS = ["FMPCryptoHistoricalData", "PolygonCryptoHistoricalData", "TiingoCryptoHistoricalData", "YFinanceCryptoHistoricalData"]

class OBBjectCryptoHistoricalResultsInner(BaseModel):
    """
    OBBjectCryptoHistoricalResultsInner
    """
    # data type: PolygonCryptoHistoricalData
    oneof_schema_1_validator: Optional[PolygonCryptoHistoricalData] = None
    # data type: YFinanceCryptoHistoricalData
    oneof_schema_2_validator: Optional[YFinanceCryptoHistoricalData] = None
    # data type: FMPCryptoHistoricalData
    oneof_schema_3_validator: Optional[FMPCryptoHistoricalData] = None
    # data type: TiingoCryptoHistoricalData
    oneof_schema_4_validator: Optional[TiingoCryptoHistoricalData] = None
    actual_instance: Optional[Union[FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData]] = None
    one_of_schemas: Set[str] = { "FMPCryptoHistoricalData", "PolygonCryptoHistoricalData", "TiingoCryptoHistoricalData", "YFinanceCryptoHistoricalData" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = OBBjectCryptoHistoricalResultsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: PolygonCryptoHistoricalData
        if not isinstance(v, PolygonCryptoHistoricalData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PolygonCryptoHistoricalData`")
        else:
            match += 1
        # validate data type: YFinanceCryptoHistoricalData
        if not isinstance(v, YFinanceCryptoHistoricalData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `YFinanceCryptoHistoricalData`")
        else:
            match += 1
        # validate data type: FMPCryptoHistoricalData
        if not isinstance(v, FMPCryptoHistoricalData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FMPCryptoHistoricalData`")
        else:
            match += 1
        # validate data type: TiingoCryptoHistoricalData
        if not isinstance(v, TiingoCryptoHistoricalData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TiingoCryptoHistoricalData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OBBjectCryptoHistoricalResultsInner with oneOf schemas: FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OBBjectCryptoHistoricalResultsInner with oneOf schemas: FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into PolygonCryptoHistoricalData
        try:
            instance.actual_instance = PolygonCryptoHistoricalData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into YFinanceCryptoHistoricalData
        try:
            instance.actual_instance = YFinanceCryptoHistoricalData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FMPCryptoHistoricalData
        try:
            instance.actual_instance = FMPCryptoHistoricalData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TiingoCryptoHistoricalData
        try:
            instance.actual_instance = TiingoCryptoHistoricalData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OBBjectCryptoHistoricalResultsInner with oneOf schemas: FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OBBjectCryptoHistoricalResultsInner with oneOf schemas: FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], FMPCryptoHistoricalData, PolygonCryptoHistoricalData, TiingoCryptoHistoricalData, YFinanceCryptoHistoricalData]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


