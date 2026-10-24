from abc import ABC, abstractmethod


class EmailValidator(ABC):

    @abstractmethod
    def validate(self, email_address: str) -> bool:
        pass
