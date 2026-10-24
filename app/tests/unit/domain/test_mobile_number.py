import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.mobile_exception import \
    MobileValidationException
from src.domain.value_objects import Mobile


class TestMobileNumber(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_mobile_data = {"number": "778293626", "country_code": "+94"}

        cls.invalid_mobile_data = {
            "number": "invalid_mobile_number",
            "country_code": "+94",
        }

        cls.empty_mobile_data = {
            "number": "",
            "country_code": "+94",
        }

        cls.empty_country_code_data = {
            "number": "778293626",
            "country_code": "",
        }

        cls.mobile_number_with_spaces = {
            "number": " 778293626 ",
            "country_code": "+94",
        }

        cls.mobile_number_with_non_numeric_characters = {
            "number": "77829abc26",
            "country_code": "+94",
        }

    def test_valid_mobile_data(self):
        mobile = Mobile(**self.valid_mobile_data)
        self.assertEqual(mobile.number, self.valid_mobile_data["number"])
        self.assertEqual(mobile.country_code, self.valid_mobile_data["country_code"])

    def test_mobile_number_with_spaces(self):
        mobile = Mobile(**self.mobile_number_with_spaces)
        self.assertEqual(mobile.number, self.mobile_number_with_spaces["number"].strip())
        self.assertEqual(
            mobile.country_code, self.mobile_number_with_spaces["country_code"]
        )

    def test_invalid_mobile_data(self):
        with self.assertRaises(MobileValidationException) as cx:
            Mobile(**self.invalid_mobile_data)

        self.assertEqual(
            cx.exception.code, ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.short_desc
        )

    def test_empty_mobile_data(self):
        with self.assertRaises(MobileValidationException) as cx:
            Mobile(**self.empty_mobile_data)

        self.assertEqual(
            cx.exception.code, ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.MOBILE_NUMBER_EMPTY_ERROR.short_desc,
        )

    def test_empty_country_code_data(self):
        with self.assertRaises(MobileValidationException) as cx:
            Mobile(**self.empty_country_code_data)

        self.assertEqual(
            cx.exception.code, ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.MOBILE_COUNTRY_CODE_EMPTY_ERROR.short_desc,
        )

    def test_mobile_number_with_non_numeric_characters(self):
        with self.assertRaises(MobileValidationException) as cx:
            Mobile(**self.mobile_number_with_non_numeric_characters)

        self.assertEqual(
            cx.exception.code,
            ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.status_code,
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.short_desc,
        )
