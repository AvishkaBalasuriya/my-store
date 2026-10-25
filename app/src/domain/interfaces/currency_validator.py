from abc import ABC, abstractmethod


class CurrencyValidator(ABC):

    @classmethod
    @abstractmethod
    def validate(cls, currency_code: str) -> bool:
        pass
