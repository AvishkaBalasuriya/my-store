from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class PaymentStatusCode(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    CANCELLED = "CANCELLED"


@dataclass(kw_only=True, frozen=True)
class PaymentStatus:
    code: Optional[PaymentStatusCode] = field(
        default=PaymentStatusCode.PENDING,
        doc="Payment status",
    )

    @classmethod
    def create(cls, code: PaymentStatusCode) -> "PaymentStatus":
        return cls(code=code)
