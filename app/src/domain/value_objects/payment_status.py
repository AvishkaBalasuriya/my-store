from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.payment_exception import PaymentStatusInvalidException


class PaymentStatusCode(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    CANCELLED = "CANCELLED"


@dataclass(kw_only=True, frozen=True)
class PaymentStatus:
    code: PaymentStatusCode

    def __post_init__(self):
        if not isinstance(self.code, PaymentStatusCode):
            raise PaymentStatusInvalidException(
                message=ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.message,
                short_desc=ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.short_desc,
                code=ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.status_code,
            )

    @property
    def is_pending(self) -> bool:
        return self.code == PaymentStatusCode.PENDING

    @property
    def is_completed(self) -> bool:
        return self.code == PaymentStatusCode.COMPLETED

    @property
    def is_failed(self) -> bool:
        return self.code == PaymentStatusCode.FAILED

    @property
    def is_refunded(self) -> bool:
        return self.code == PaymentStatusCode.REFUNDED

    @property
    def is_cancelled(self) -> bool:
        return self.code == PaymentStatusCode.CANCELLED

    @classmethod
    def create(
        cls, code: Optional[PaymentStatusCode] = PaymentStatusCode.PENDING
    ) -> "PaymentStatus":
        return cls(code=code)
