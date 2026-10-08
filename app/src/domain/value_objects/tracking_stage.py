from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TrackingStageCode(str, Enum):
    ORDER_CONFIRMED = "order_confirmed"
    PREPARE_FOR_SHIPMENT = "prepare_for_shipment"
    PICKED_UP = "picked_up"
    ARRIVED_AT_ORIGIN_FACILITY = "arrived_at_origin_facility"
    DEPARTED_FROM_ORIGIN_FACILITY = "departed_from_origin_facility"
    ARRIVED_AT_DESTINATION_FACILITY = "arrived_at_destination_facility"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"


@dataclass(kw_only=True, frozen=True)
class TrackingStage:
    code: Optional[TrackingStageCode] = field(
        default_factory=lambda: TrackingStageCode.ORDER_CONFIRMED, doc="Tracking stage"
    )

    @classmethod
    def update(cls, code: TrackingStageCode) -> "TrackingStage":
        return cls(code=code)
