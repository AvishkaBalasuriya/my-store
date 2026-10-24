import logging
from urllib.parse import urlparse

from src.domain.interfaces.url_validator import URLValidator
from src.domain.shared.enums import Protocol

logger = logging.getLogger(__name__)


class UrlValidatorService(URLValidator):

    @classmethod
    def validate(cls, url: str) -> bool:
        logger.info(f"URL:VALIDATOR:: validating URL: {url}")
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError as e:
            return False

    @classmethod
    def get_protocol(cls, url: str) -> Protocol:
        result = urlparse(url)
        return Protocol(result.scheme)

    @classmethod
    def get_domain(cls, url: str) -> str:
        result = urlparse(url)
        return result.netloc

    @classmethod
    def get_path(cls, url: str) -> str:
        result = urlparse(url)
        return result.path

    @classmethod
    def get_query(cls, url: str) -> str:
        result = urlparse(url)
        return result.query

    @classmethod
    def get_fragment(cls, url: str) -> str:
        result = urlparse(url)
        return result.fragment
