from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TrackingStageCode(str, Enum):
    ORDER_CONFIRMED = "ORDER_CONFIRMED"
    PREPARE_FOR_SHIPMENT = "PREPARE_FOR_SHIPMENT"
    PICKED_UP = "PICKED_UP"
    ARRIVED_AT_ORIGIN_FACILITY = "ARRIVED_AT_ORIGIN_FACILITY"
    DEPARTED_FROM_ORIGIN_FACILITY = "DEPARTED_FROM_ORIGIN_FACILITY"
    ARRIVED_AT_DESTINATION_FACILITY = "ARRIVED_AT_DESTINATION_FACILITY"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"


@dataclass(kw_only=True, frozen=True)
class TrackingStage:
    code: Optional[TrackingStageCode] = field(
        default=TrackingStageCode.ORDER_CONFIRMED, doc="Tracking stage"
    )

    @classmethod
    def create(cls, code: TrackingStageCode) -> "TrackingStage":
        return cls(code=code)
