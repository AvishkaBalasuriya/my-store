from dataclasses import dataclass

from app.src.domain.shared.exceptions.error_codes import ErrorCodes
from app.src.domain.shared.exceptions.price_exception import PriceValidationException


@dataclass(kw_only=True, frozen=True, eq=False)
class Price:
    amount: float
    currency: str

    @property
    def formatted(self) -> str:
        return f"{self.amount:.2f} {self.currency}"

    def __post_init__(self) -> None:
        _amount = self.amount
        _currency = self.currency.strip().upper()

        if not _amount or _amount < 0:
            raise PriceValidationException(
                message=ErrorCodes.PRICE_NEGATIVE_ERROR.message,
                short_desc=ErrorCodes.PRICE_NEGATIVE_ERROR.short_desc,
                code=ErrorCodes.PRICE_NEGATIVE_ERROR.status_code,
            )

        if not _currency:
            raise PriceValidationException(
                message=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.message,
                short_desc=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.short_desc,
                code=ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.status_code,
            )

        object.__setattr__(self, "currency", _currency)

    def __eq__(self, other):
        if not isinstance(other, Price):
            return NotImplemented

        # Only compare the e164_formatted, ignore the individual attributes
        return self.formatted == other.formatted

    def __hash__(self):
        # Hash based on the e164_formatted representation
        return hash(self.formatted)

    @classmethod
    def update(cls, amount: float, currency: str) -> "Price":
        return cls(amount=amount, currency=currency)
