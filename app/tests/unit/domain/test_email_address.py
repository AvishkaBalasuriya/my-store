import unittest

from src.domain.shared.exceptions.email_exception import \
    EmailValidationException
from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.value_objects import Email
from src.infrastructure.services.email_validator import EmailValidatorService


class TestEmailAddress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_email_data = {"address": "test@gmail.com"}
        cls.invalid_email_data = {"address": "invalid_email"}
        cls.empty_email_data = {"address": ""}
        cls.valid_email_with_spaces = {"address": " test@gmail.com "}
        cls.email_with_non_numeric_characters = {"address": "test@exam!ple.com"}

    def test_valid_email_data(self):
        email = Email.create(**self.valid_email_data, validator=EmailValidatorService)
        self.assertEqual(email.address, self.valid_email_data["address"])

    def test_email_with_spaces(self):
        email = Email.create(
            **self.valid_email_with_spaces, validator=EmailValidatorService
        )
        self.assertEqual(
            email.address, self.valid_email_with_spaces["address"].strip().lower()
        )

    def test_invalid_email_data(self):
        with self.assertRaises(EmailValidationException) as cx:
            Email.create(**self.invalid_email_data, validator=EmailValidatorService)

        self.assertEqual(
            cx.exception.code, ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.short_desc
        )

    def test_empty_email_data(self):
        with self.assertRaises(EmailValidationException) as cx:
            Email.create(**self.empty_email_data, validator=EmailValidatorService)

        self.assertEqual(cx.exception.code, ErrorCodes.EMAIL_EMPTY_ERROR.status_code)
        self.assertEqual(cx.exception.message, ErrorCodes.EMAIL_EMPTY_ERROR.message)
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.EMAIL_EMPTY_ERROR.short_desc,
        )

    def test_email_with_non_numeric_characters(self):
        with self.assertRaises(EmailValidationException) as cx:
            Email.create(
                **self.email_with_non_numeric_characters, validator=EmailValidatorService
            )

        self.assertEqual(
            cx.exception.code,
            ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.status_code,
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc,
            ErrorCodes.EMAIL_INVALID_FORMAT_ERROR.short_desc,
        )
