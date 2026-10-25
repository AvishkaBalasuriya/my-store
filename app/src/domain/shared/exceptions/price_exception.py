from typing import Optional

from src.domain.shared.exceptions.base_exception import BaseDomainError
from src.domain.shared.exceptions.error_codes import ErrorCodes


class PriceException(BaseDomainError):
    """Exception raised when an invalid price is provided."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.GENERIC_PRICE_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.GENERIC_PRICE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.GENERIC_PRICE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PriceInvalidCurrencyCodeException(BaseDomainError):
    """Exception raised when an invalid currency code is provided for the price."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.message,
        short_desc: Optional[
            str
        ] = ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PriceCurrencyCodeEmptyException(BaseDomainError):
    """Exception raised when the currency for the price is empty."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PriceAmountEmptyOrNegativeException(BaseDomainError):
    """Exception raised when the price is empty or negative."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.message,
        short_desc: Optional[
            str
        ] = ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)


class PriceInvalidAmountException(BaseDomainError):
    """Exception raised when the price amount is invalid."""

    def __init__(
        self,
        message: Optional[str] = ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.message,
        short_desc: Optional[str] = ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.short_desc,
        code: Optional[int] = ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.status_code,
    ):
        super().__init__(message, short_desc, code)
