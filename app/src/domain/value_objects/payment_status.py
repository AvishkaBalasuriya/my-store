from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class PaymentStatusCode(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"


@dataclass(kw_only=True, frozen=True)
class PaymentStatus:
    code: Optional[PaymentStatusCode] = field(
        default_factory=lambda: PaymentStatus.update(PaymentStatusCode.PENDING),
        doc="Payment status",
    )

    @classmethod
    def update(cls, code: PaymentStatusCode) -> "PaymentStatus":
        return cls(code=code)
