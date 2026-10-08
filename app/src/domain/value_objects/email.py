from dataclasses import dataclass

from app.src.domain.shared.exceptions.email_exception import EmailValidationException
from app.src.domain.shared.exceptions.error_codes import ErrorCodes


@dataclass(kw_only=True, frozen=True)
class Email:
    address: str

    def __post_init__(self) -> None:
        _address = self.address.strip().lower()

        if not _address:
            raise EmailValidationException(
                message=ErrorCodes.EMAIL_EMPTY_ERROR.message,
                short_desc=ErrorCodes.EMAIL_EMPTY_ERROR.short_desc,
                code=ErrorCodes.EMAIL_EMPTY_ERROR.status_code,
            )

        object.__setattr__(self, "address", _address)

    @classmethod
    def update(cls, address: str) -> "Email":
        return cls(address=address)
