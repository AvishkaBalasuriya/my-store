from dataclasses import dataclass
from typing import ClassVar, Optional

from src.domain.interfaces.email_validator import EmailValidator
from src.domain.shared.exceptions.email_exception import \
    EmailValidationException
from src.domain.shared.exceptions.error_codes import ErrorCodes


@dataclass(kw_only=True, frozen=True)
class Email:
    address: str

    __validator: ClassVar[EmailValidator] = None

    def __post_init__(self) -> None:
        _address = self.address.strip().lower()
        object.__setattr__(self, "address", _address)

        if not self.address:
            raise EmailValidationException(
                message=ErrorCodes.EMAIL_EMPTY_ERROR.message,
                short_desc=ErrorCodes.EMAIL_EMPTY_ERROR.short_desc,
                code=ErrorCodes.EMAIL_EMPTY_ERROR.status_code,
            )

        if self.__validator and not self.__validator.validate(email_address=self.address):
            raise EmailValidationException(
                message=ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.message,
                short_desc=ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.short_desc,
                code=ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.status_code,
            )

    @classmethod
    def create(cls, address: str, validator: Optional[EmailValidator] = None) -> "Email":
        cls.__validator = validator

        return cls(address=address)
