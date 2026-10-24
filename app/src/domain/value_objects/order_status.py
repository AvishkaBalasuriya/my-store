from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class OrderStatusCode(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    RETURNED = "RETURNED"


@dataclass(kw_only=True, frozen=True)
class OrderStatus:
    code: Optional[OrderStatusCode] = field(
        default=OrderStatusCode.PENDING,
        doc="Order status",
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
    def create(cls, code: OrderStatusCode) -> "OrderStatus":
        return cls(code=code)
