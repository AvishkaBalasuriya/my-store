from dataclasses import dataclass

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.price_exception import (
    PriceInvalidCurrencyCodeException,
    PriceCurrencyCodeEmptyException,
    PriceAmountEmptyOrNegativeException,
    PriceInvalidAmountException,
)
from src.domain.interfaces.currency_validator import CurrencyValidator
from typing import ClassVar, Optional


@dataclass(kw_only=True, frozen=True, eq=False)
class Price:
    amount: float
    currency: str

    __validator: ClassVar[CurrencyValidator] = None

    def __post_init__(self) -> None:
        _currency = self.currency.strip().upper()
        object.__setattr__(self, "currency", _currency)

        if not isinstance(self.amount, (float)):
            raise PriceInvalidAmountException(
                message=ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.message,
                short_desc=ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.short_desc,
                code=ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.status_code,
            )

        if not self.amount or self.amount < 0:
            raise PriceAmountEmptyOrNegativeException(
                message=ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.message,
                short_desc=ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.short_desc,
                code=ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.status_code,
            )

        if not self.currency:
            raise PriceCurrencyCodeEmptyException(
                message=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.message,
                short_desc=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.short_desc,
                code=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.status_code,
            )

        if self.__validator and not self.__validator.validate(
            currency_code=self.currency
        ):
            raise PriceInvalidCurrencyCodeException(
                message=ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.message,
                short_desc=ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.short_desc,
                code=ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.status_code,
            )

    def __eq__(self, other):
        if not isinstance(other, Price):
            return NotImplemented

        # Only compare the e164_formatted, ignore the individual attributes
        return self.formatted == other.formatted

    def __hash__(self):
        # Hash based on the e164_formatted representation
        return hash(self.formatted)

    @property
    def formatted(self) -> str:
        return f"{self.amount:.2f} {self.currency}"

    @classmethod
    def create(
        cls, amount: float, currency: str, validator: Optional[CurrencyValidator] = None
    ) -> "Price":
        cls.__validator = validator

        return cls(amount=amount, currency=currency)
