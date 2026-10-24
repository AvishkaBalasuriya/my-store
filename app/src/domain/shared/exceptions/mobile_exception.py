from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class MobileValidationException(BaseDomainError):
    """Exception raised when an invalid mobile number is provided."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_MOBILE_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_MOBILE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_MOBILE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
