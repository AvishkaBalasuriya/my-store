from src.domain.interfaces.currency_validator import CurrencyValidator
from pydantic_extra_types.currency_code import ISO4217


class PydanticCurrencyValidatorService(CurrencyValidator):

    @classmethod
    def validate(cls, currency_code: str) -> bool:

        return True if currency_code in ISO4217.allowed_currencies else False
