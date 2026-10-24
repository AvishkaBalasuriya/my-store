from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class PaymentMethodCode(str, Enum):
    QR = "QR"
    CARD = "CARD"
    CASH = "CASH"
    PAYPAL = "PAYPAL"


@dataclass(kw_only=True, frozen=True)
class PaymentMethod:
    code: Optional[PaymentMethodCode] = field(
        default=PaymentMethodCode.QR,
        doc="Payment method",
    )

    @classmethod
    def create(cls, code: PaymentMethodCode) -> "PaymentMethod":
        return cls(code=code)
