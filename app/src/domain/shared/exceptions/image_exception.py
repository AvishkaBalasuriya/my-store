from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class ImageURLValidationException(BaseDomainError):
    """Exception raised when an invalid image URL is provided."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_IMAGE_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_IMAGE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_IMAGE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
