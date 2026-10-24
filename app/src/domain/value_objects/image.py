from dataclasses import dataclass
from typing import ClassVar, Optional

from src.domain.interfaces.url_validator import URLValidator
from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.image_exception import \
    ImageURLValidationException


@dataclass(kw_only=True, frozen=True)
class Image:
    url: str
    alt_text: Optional[str] = None

    __url_validator: ClassVar[URLValidator] = None

    def __post_init__(self):
        _url = self.url.strip().lower()
        _alt_text = self.alt_text.strip().lower()

        object.__setattr__(self, "url", _url)
        object.__setattr__(self, "alt_text", _alt_text)

        if not self.url:
            raise ImageURLValidationException(
                message=ErrorCodes.IMAGE_URL_EMPTY_ERROR.message,
                short_desc=ErrorCodes.IMAGE_URL_EMPTY_ERROR.short_desc,
                code=ErrorCodes.IMAGE_URL_EMPTY_ERROR.status_code,
            )

        if self.__url_validator and not self.__url_validator.validate(self.url):
            raise ImageURLValidationException(
                message=ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.message,
                short_desc=ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.short_desc,
                code=ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.status_code,
            )

    @classmethod
    def create(
        cls,
        url: str,
        alt_text: Optional[str] = "",
        url_validator: Optional[URLValidator] = None,
    ) -> "Image":
        cls.__url_validator = url_validator

        return cls(url=url, alt_text=alt_text)
