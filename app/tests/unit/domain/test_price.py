import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.price_exception import (
    PriceInvalidCurrencyCodeException,
    PriceCurrencyCodeEmptyException,
    PriceAmountEmptyOrNegativeException,
    PriceInvalidAmountException,
)
from src.domain.value_objects import Price
from src.infrastructure.services.currency_validator import (
    PydanticCurrencyValidatorService,
)


class TestPrice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_price = {"amount": 100.0, "currency": "USD"}
        cls.invalid_currency_price = {"amount": 100.0, "currency": "INVALID"}
        cls.invalid_amount_price = {"amount": -100.0, "currency": "USD"}
        cls.empty_currency_price = {"amount": 100.0, "currency": ""}
        cls.invalid_amount_data_type = {"amount": 100, "currency": "USD"}
        cls.empty_amount_price = {"amount": 0.0, "currency": "USD"}

    def test_valid_price(self):
        price = Price.create(
            **self.valid_price, validator=PydanticCurrencyValidatorService
        )
        self.assertEqual(price.amount, self.valid_price["amount"])
        self.assertEqual(price.currency, self.valid_price["currency"])

    def test_invalid_currency_price(self):
        with self.assertRaises(PriceInvalidCurrencyCodeException) as cx:
            Price.create(
                **self.invalid_currency_price, validator=PydanticCurrencyValidatorService
            )

        self.assertEqual(
            cx.exception.code, ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.PRICE_INVALID_CURRENCY_CODE_ERROR.short_desc,
        )

    def test_invalid_amount_price(self):
        with self.assertRaises(PriceAmountEmptyOrNegativeException) as cx:
            Price.create(
                **self.invalid_amount_price, validator=PydanticCurrencyValidatorService
            )

        self.assertEqual(
            cx.exception.code, ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.short_desc,
        )

    def test_currency_empty(self):
        with self.assertRaises(PriceCurrencyCodeEmptyException) as cx:
            Price.create(
                **self.empty_currency_price, validator=PydanticCurrencyValidatorService
            )

        self.assertEqual(
            cx.exception.code, ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.PRICE_CURRENCY_EMPTY_ERROR.short_desc
        )

    def test_formatted_price(self):
        price = Price.create(
            **self.valid_price, validator=PydanticCurrencyValidatorService
        )

        self.assertEqual(
            price.formatted,
            f"{float(self.valid_price['amount']):.2f} {self.valid_price['currency']}",
        )

    def test_invalid_amount_data_type(self):
        with self.assertRaises(PriceInvalidAmountException) as cx:
            Price.create(
                **self.invalid_amount_data_type,
                validator=PydanticCurrencyValidatorService,
            )

        self.assertEqual(
            cx.exception.code, ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.PRICE_INVALID_AMOUNT_ERROR.short_desc
        )

    def test_empty_amount_price(self):
        with self.assertRaises(PriceAmountEmptyOrNegativeException) as cx:
            Price.create(
                **self.empty_amount_price, validator=PydanticCurrencyValidatorService
            )

        self.assertEqual(
            cx.exception.code, ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.PRICE_AMOUNT_EMPTY_OR_NEGATIVE_ERROR.short_desc,
        )
