from abc import ABC, abstractmethod


class EmailValidator(ABC):

    @classmethod
    @abstractmethod
    def validate(cls, email_address: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def get_local_part(cls, email_address: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_domain(cls, email_address: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_tld(cls, email_address: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_subdomain(cls, email_address: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_username(cls, email_address: str) -> str:
        pass
