from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.order_exception import \
    OrderInvalidStatusException


class OrderStatusCode(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    RETURNED = "RETURNED"


@dataclass(kw_only=True, frozen=True)
class OrderStatus:
    code: OrderStatusCode

    def __post_init__(self):
        if not isinstance(self.code, OrderStatusCode):
            raise OrderInvalidStatusException(
                message=ErrorCodes.ORDER_INVALID_STATUS_ERROR.message,
                short_desc=ErrorCodes.ORDER_INVALID_STATUS_ERROR.short_desc,
                code=ErrorCodes.ORDER_INVALID_STATUS_ERROR.status_code,
            )

    @property
    def is_pending(self) -> bool:
        return self.code == OrderStatusCode.PENDING

    @property
    def is_processing(self) -> bool:
        return self.code == OrderStatusCode.PROCESSING

    @property
    def is_shipped(self) -> bool:
        return self.code == OrderStatusCode.SHIPPED

    @property
    def is_delivered(self) -> bool:
        return self.code == OrderStatusCode.DELIVERED

    @property
    def is_cancelled(self) -> bool:
        return self.code == OrderStatusCode.CANCELLED

    @property
    def is_returned(self) -> bool:
        return self.code == OrderStatusCode.RETURNED

    @classmethod
    def create(
        cls, code: Optional[OrderStatusCode] = OrderStatusCode.PENDING
    ) -> "OrderStatus":
        return cls(code=code)
