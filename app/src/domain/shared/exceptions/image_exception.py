from app.src.domain.shared.exceptions.base_exception import BaseException
from app.src.domain.shared.exceptions.error_codes import ErrorCodes


class ImageURLValidationException(BaseException):
    """Exception raised when an invalid image URL is provided."""

    def __init__(
        self,
        message: str = ErrorCodes.GENERIC_IMAGE_ERROR.message,
        short_desc: str = ErrorCodes.GENERIC_IMAGE_ERROR.short_desc,
        code: int = ErrorCodes.GENERIC_IMAGE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
