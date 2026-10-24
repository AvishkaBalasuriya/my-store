from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class PaymentException(BaseDomainError):
    """Exception raised for order-related errors."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_PAYMENT_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_PAYMENT_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_PAYMENT_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PaymentMethodInvalidMethodException(PaymentException):
    """Exception raised when a payment has an invalid method."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PaymentStatusInvalidException(PaymentException):
    """Exception raised when a payment has an invalid status."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
