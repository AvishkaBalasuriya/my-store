from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class TrackingException(BaseDomainError):
    """Exception raised for tracking-related errors."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_TRACKING_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_TRACKING_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_TRACKING_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class TrackingStatusInvalidException(TrackingException):
    """Exception raised when the tracking status is invalid."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.TRACKING_STATUS_INVALID_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.TRACKING_STATUS_INVALID_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.TRACKING_STATUS_INVALID_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
