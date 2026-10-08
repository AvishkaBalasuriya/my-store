from typing import Optional

from app.src.domain.shared.exceptions.error_codes import ErrorCodes


class BaseDomainError(Exception):
    """Base class for all domain exceptions in the application."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_ERROR.status_code,
    ):
        self.message = message
        self.short_desc = short_desc
        self.code = code
        super().__init__(self.message)
