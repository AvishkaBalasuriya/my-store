from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class PriceValidationException(BaseDomainError):
    """Exception raised when an invalid price is provided."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_PRICE_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_PRICE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_PRICE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
