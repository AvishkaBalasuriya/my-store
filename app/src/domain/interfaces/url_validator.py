from abc import ABC, abstractmethod

from src.domain.shared.enums import Protocol


class URLValidator(ABC):

    @classmethod
    @abstractmethod
    def validate(cls, url: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def get_protocol(cls, url: str) -> Protocol:
        pass

    @classmethod
    @abstractmethod
    def get_domain(cls, url: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_path(cls, url: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_query(cls, url: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_fragment(cls, url: str) -> str:
        pass
