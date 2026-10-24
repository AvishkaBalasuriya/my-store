from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.payment_exception import \
    PaymentMethodInvalidMethodException


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

    def __post_init__(self):
        if not isinstance(self.code, PaymentMethodCode):
            raise PaymentMethodInvalidMethodException(
                message=ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.message,
                short_desc=ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.short_desc,
                code=ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.status_code,
            )

    @property
    def is_card(self) -> bool:
        return self.code == PaymentMethodCode.CARD

    @property
    def is_paypal(self) -> bool:
        return self.code == PaymentMethodCode.PAYPAL

    @property
    def is_qr(self) -> bool:
        return self.code == PaymentMethodCode.QR

    @property
    def is_cash(self) -> bool:
        return self.code == PaymentMethodCode.CASH

    @classmethod
    def create(cls, code: PaymentMethodCode) -> "PaymentMethod":
        return cls(code=code)
