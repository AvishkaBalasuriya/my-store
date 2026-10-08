import re
from dataclasses import dataclass
from typing import ClassVar

from app.src.domain.shared.exceptions.error_codes import ErrorCodes
from app.src.domain.shared.exceptions.mobile_exception import MobileValidationException


@dataclass(kw_only=True, frozen=True, eq=False)
class Mobile:
    number: str
    country_code: str

    __REGEX_FORMAT: ClassVar[re.Pattern[str]] = re.compile(
        r"^(?:7|0|(?:\+94))[0-9]{9,10}$"
    )

    @property
    def e164_formatted(self) -> str:
        return f"{self.country_code}{self.number}"

    def __post_init__(self) -> None:
        _number = self.number.strip()
        _country_code = self.country_code.strip()

        if not _number:
            raise MobileValidationException(
                message=ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.message,
                short_desc=ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.short_desc,
                code=ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.status_code,
            )

        if not _country_code:
            raise MobileValidationException(
                message=ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.message,
                short_desc=ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.short_desc,
                code=ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.status_code,
            )

        object.__setattr__(self, "number", _number)
        object.__setattr__(self, "country_code", _country_code)

        if not self.__REGEX_FORMAT.match(string=self.e164_formatted):
            raise MobileValidationException(
                message=ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.message,
                short_desc=ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.short_desc,
                code=ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.status_code,
            )

    def __eq__(self, other):
        if not isinstance(other, Mobile):
            return NotImplemented

        # Only compare the e164_formatted, ignore the individual attributes
        return self.e164_formatted == other.e164_formatted

    def __hash__(self):
        # Hash based on the e164_formatted representation
        return hash(self.e164_formatted)

    @classmethod
    def update(cls, number: str, country_code: str) -> "Mobile":
        return cls(number=number, country_code=country_code)
