from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.tracking_exception import TrackingStatusInvalidException


class TrackingStatusCode(str, Enum):
    ORDER_CONFIRMED = "ORDER_CONFIRMED"
    PREPARE_FOR_SHIPMENT = "PREPARE_FOR_SHIPMENT"
    PICKED_UP = "PICKED_UP"
    ARRIVED_AT_ORIGIN_FACILITY = "ARRIVED_AT_ORIGIN_FACILITY"
    DEPARTED_FROM_ORIGIN_FACILITY = "DEPARTED_FROM_ORIGIN_FACILITY"
    ARRIVED_AT_DESTINATION_FACILITY = "ARRIVED_AT_DESTINATION_FACILITY"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"


@dataclass(kw_only=True, frozen=True)
class TrackingStatus:
    code: TrackingStatusCode

    def __post_init__(self):
        if not isinstance(self.code, TrackingStatusCode):
            raise TrackingStatusInvalidException(
                message=ErrorCodes.TRACKING_STATUS_INVALID_ERROR.message,
                short_desc=ErrorCodes.TRACKING_STATUS_INVALID_ERROR.short_desc,
                code=ErrorCodes.TRACKING_STATUS_INVALID_ERROR.status_code,
            )

    @property
    def is_order_confirmed(self) -> bool:
        return self.code == TrackingStatusCode.ORDER_CONFIRMED

    @property
    def is_prepare_for_shipment(self) -> bool:
        return self.code == TrackingStatusCode.PREPARE_FOR_SHIPMENT

    @property
    def is_picked_up(self) -> bool:
        return self.code == TrackingStatusCode.PICKED_UP

    @property
    def is_arrived_at_origin_facility(self) -> bool:
        return self.code == TrackingStatusCode.ARRIVED_AT_ORIGIN_FACILITY

    @property
    def is_departed_from_origin_facility(self) -> bool:
        return self.code == TrackingStatusCode.DEPARTED_FROM_ORIGIN_FACILITY

    @property
    def is_arrived_at_destination_facility(self) -> bool:
        return self.code == TrackingStatusCode.ARRIVED_AT_DESTINATION_FACILITY

    @property
    def is_out_for_delivery(self) -> bool:
        return self.code == TrackingStatusCode.OUT_FOR_DELIVERY

    @property
    def is_delivered(self) -> bool:
        return self.code == TrackingStatusCode.DELIVERED

    @classmethod
    def create(
        cls, code: Optional[TrackingStatusCode] = TrackingStatusCode.ORDER_CONFIRMED
    ) -> "TrackingStatus":
        return cls(code=code)
