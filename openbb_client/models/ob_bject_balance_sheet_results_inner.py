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
from openbb_client.models.fmp_balance_sheet_data import FMPBalanceSheetData
from openbb_client.models.intrinio_balance_sheet_data import IntrinioBalanceSheetData
from openbb_client.models.polygon_balance_sheet_data import PolygonBalanceSheetData
from openbb_client.models.y_finance_balance_sheet_data import YFinanceBalanceSheetData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

OBBJECTBALANCESHEETRESULTSINNER_ONE_OF_SCHEMAS = ["FMPBalanceSheetData", "IntrinioBalanceSheetData", "PolygonBalanceSheetData", "YFinanceBalanceSheetData"]

class OBBjectBalanceSheetResultsInner(BaseModel):
    """
    OBBjectBalanceSheetResultsInner
    """
    # data type: PolygonBalanceSheetData
    oneof_schema_1_validator: Optional[PolygonBalanceSheetData] = None
    # data type: YFinanceBalanceSheetData
    oneof_schema_2_validator: Optional[YFinanceBalanceSheetData] = None
    # data type: IntrinioBalanceSheetData
    oneof_schema_3_validator: Optional[IntrinioBalanceSheetData] = None
    # data type: FMPBalanceSheetData
    oneof_schema_4_validator: Optional[FMPBalanceSheetData] = None
    actual_instance: Optional[Union[FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData]] = None
    one_of_schemas: Set[str] = { "FMPBalanceSheetData", "IntrinioBalanceSheetData", "PolygonBalanceSheetData", "YFinanceBalanceSheetData" }

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
        instance = OBBjectBalanceSheetResultsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: PolygonBalanceSheetData
        if not isinstance(v, PolygonBalanceSheetData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PolygonBalanceSheetData`")
        else:
            match += 1
        # validate data type: YFinanceBalanceSheetData
        if not isinstance(v, YFinanceBalanceSheetData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `YFinanceBalanceSheetData`")
        else:
            match += 1
        # validate data type: IntrinioBalanceSheetData
        if not isinstance(v, IntrinioBalanceSheetData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IntrinioBalanceSheetData`")
        else:
            match += 1
        # validate data type: FMPBalanceSheetData
        if not isinstance(v, FMPBalanceSheetData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FMPBalanceSheetData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in OBBjectBalanceSheetResultsInner with oneOf schemas: FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in OBBjectBalanceSheetResultsInner with oneOf schemas: FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData. Details: " + ", ".join(error_messages))
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

        # deserialize data into PolygonBalanceSheetData
        try:
            instance.actual_instance = PolygonBalanceSheetData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into YFinanceBalanceSheetData
        try:
            instance.actual_instance = YFinanceBalanceSheetData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IntrinioBalanceSheetData
        try:
            instance.actual_instance = IntrinioBalanceSheetData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FMPBalanceSheetData
        try:
            instance.actual_instance = FMPBalanceSheetData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into OBBjectBalanceSheetResultsInner with oneOf schemas: FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OBBjectBalanceSheetResultsInner with oneOf schemas: FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], FMPBalanceSheetData, IntrinioBalanceSheetData, PolygonBalanceSheetData, YFinanceBalanceSheetData]]:
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


