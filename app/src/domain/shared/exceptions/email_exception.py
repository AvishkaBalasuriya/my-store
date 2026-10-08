from app.src.domain.shared.exceptions.base_exception import BaseException
from app.src.domain.shared.exceptions.error_codes import ErrorCodes


class EmailValidationException(BaseException):
    """Exception raised when an invalid email address is provided."""

    def __init__(
        self,
        message: str = ErrorCodes.GENERIC_EMAIL_ERROR.message,
        short_desc: str = ErrorCodes.GENERIC_EMAIL_ERROR.short_desc,
        code: int = ErrorCodes.GENERIC_EMAIL_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
