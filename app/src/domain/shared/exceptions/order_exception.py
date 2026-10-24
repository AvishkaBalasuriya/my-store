from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class OrderException(BaseDomainError):
    """Exception raised for order-related errors."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_ORDER_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_ORDER_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_ORDER_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class OrderInvalidStatusException(OrderException):
    """Exception raised when an order has an invalid status."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.ORDER_INVALID_STATUS_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.ORDER_INVALID_STATUS_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.ORDER_INVALID_STATUS_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
