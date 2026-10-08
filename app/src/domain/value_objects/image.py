from dataclasses import dataclass
from typing import Optional

from app.src.domain.shared.exceptions.error_codes import ErrorCodes
from app.src.domain.shared.exceptions.image_exception import ImageURLValidationException


@dataclass(kw_only=True, frozen=True)
class Image:
    url: str
    alt_text: Optional[str] = None

    def __post_init__(self):
        _url = self.url.strip().lower()

        if self.alt_text:
            _alt_text = self.alt_text.strip().lower()
            object.__setattr__(self, "alt_text", _alt_text)

        if not _url:
            raise ImageURLValidationException(
                message=ErrorCodes.IMAGE_URL_EMPTY_ERROR.message,
                short_desc=ErrorCodes.IMAGE_URL_EMPTY_ERROR.short_desc,
                code=ErrorCodes.IMAGE_URL_EMPTY_ERROR.status_code,
            )

        object.__setattr__(self, "url", _url)

    @classmethod
    def update(cls, url: str, alt_text: Optional[str] = None) -> "Image":
        return cls(url=url, alt_text=alt_text)
