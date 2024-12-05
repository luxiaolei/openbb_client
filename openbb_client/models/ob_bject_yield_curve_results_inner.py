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
from openbb_client.models.econ_db_yield_curve_data import EconDbYieldCurveData
from openbb_client.models.federal_reserve_yield_curve_data import FederalReserveYieldCurveData
from openbb_client.models.fmp_yield_curve_data import FMPYieldCurveData
from openbb_client.models.openbb_fred_models_yield_curve_fred_yield_curve_data import OpenbbFredModelsYieldCurveFREDYieldCurveData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

OBBJECTYIELDCURVERESULTSINNER_ONE_OF_SCHEMAS = ["EconDbYieldCurveData", "FMPYieldCurveData", "FederalReserveYieldCurveData", "OpenbbFredModelsYieldCurveFREDYieldCurveData"]

class OBBjectYieldCurveResultsInner(BaseModel):
    """
    OBBjectYieldCurveResultsInner
    """
    # data type: FederalReserveYieldCurveData
    oneof_schema_1_validator: Optional[FederalReserveYieldCurveData] = None
    # data type: EconDbYieldCurveData
    oneof_schema_2_validator: Optional[EconDbYieldCurveData] = None
    # data type: FMPYieldCurveData
    oneof_schema_3_validator: Optional[FMPYieldCurveData] = None
    # data type: OpenbbFredModelsYieldCurveFREDYieldCurveData
    oneof_schema_4_validator: Optional[OpenbbFredModelsYieldCurveFREDYieldCurveData] = None
    actual_instance: Optional[Union[EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData]] = None
    one_of_schemas: Set[str] = { "EconDbYieldCurveData", "FMPYieldCurveData", "FederalReserveYieldCurveData", "OpenbbFredModelsYieldCurveFREDYieldCurveData" }

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
        instance = OBBjectYieldCurveResultsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: FederalReserveYieldCurveData
        if not isinstance(v, FederalReserveYieldCurveData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FederalReserveYieldCurveData`")
        else:
            match += 1
        # validate data type: EconDbYieldCurveData
        if not isinstance(v, EconDbYieldCurveData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EconDbYieldCurveData`")
        else:
            match += 1
        # validate data type: FMPYieldCurveData
        if not isinstance(v, FMPYieldCurveData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FMPYieldCurveData`")
        else:
            match += 1
        # validate data type: OpenbbFredModelsYieldCurveFREDYieldCurveData
        if not isinstance(v, OpenbbFredModelsYieldCurveFREDYieldCurveData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OpenbbFredModelsYieldCurveFREDYieldCurveData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OBBjectYieldCurveResultsInner with oneOf schemas: EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OBBjectYieldCurveResultsInner with oneOf schemas: EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData. Details: " + ", ".join(error_messages))
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

        # deserialize data into FederalReserveYieldCurveData
        try:
            instance.actual_instance = FederalReserveYieldCurveData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EconDbYieldCurveData
        try:
            instance.actual_instance = EconDbYieldCurveData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FMPYieldCurveData
        try:
            instance.actual_instance = FMPYieldCurveData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OpenbbFredModelsYieldCurveFREDYieldCurveData
        try:
            instance.actual_instance = OpenbbFredModelsYieldCurveFREDYieldCurveData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OBBjectYieldCurveResultsInner with oneOf schemas: EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OBBjectYieldCurveResultsInner with oneOf schemas: EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], EconDbYieldCurveData, FMPYieldCurveData, FederalReserveYieldCurveData, OpenbbFredModelsYieldCurveFREDYieldCurveData]]:
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


