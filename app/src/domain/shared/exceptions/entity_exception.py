from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class EntityCannotBeRetainedError(BaseDomainError):
    """Exception raised when an entity cannot be retained."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.ENTITY_CANNOT_BE_RETAINED_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class EntityAlreadyDiscardedError(BaseDomainError):
    """Exception raised when an entity is already discarded."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.ENTITY_ALREADY_DISCARDED_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class EntityNotDiscardedError(BaseDomainError):
    """Exception raised when an entity has not been discarded."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.ENTITY_NOT_DISCARDED_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
