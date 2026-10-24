from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class UserMustHaveMobileOrEmailException(BaseDomainError):
    """Exception raised when a user does not have either a mobile number or an email address."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.USER_MUST_HAVE_MOBILE_OR_EMAIL_ERROR.message,
        short_desc: Optional[
            str
        ] = ErrorCodes.USER_MUST_HAVE_MOBILE_OR_EMAIL_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.USER_MUST_HAVE_MOBILE_OR_EMAIL_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
