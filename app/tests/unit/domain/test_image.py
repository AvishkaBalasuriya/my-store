import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.image_exception import \
    ImageURLValidationException
from src.domain.value_objects.image import Image
from src.infrastructure.services.url_validator import UrlValidatorService


class TestImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_image_url = {"url": "https://picsum.photos/id/1/200/300"}

        cls.invalid_image_url = {
            "url": "invalid_image_url",
        }

        cls.empty_image_url = {
            "url": "",
        }

        cls.valid_image_url_with_spaces = {
            "url": " https://picsum.photos/id/1/200/300 ",
        }

    def test_valid_image_url(self):
        image = Image.create(**self.valid_image_url, url_validator=UrlValidatorService)
        self.assertEqual(image.url, self.valid_image_url["url"])

    def test_image_url_with_spaces(self):
        image = Image.create(
            **self.valid_image_url_with_spaces, url_validator=UrlValidatorService
        )
        self.assertEqual(image.url, self.valid_image_url_with_spaces["url"].strip())

    def test_invalid_image_url(self):
        with self.assertRaises(ImageURLValidationException) as cx:
            Image.create(**self.invalid_image_url, url_validator=UrlValidatorService)

        self.assertEqual(
            cx.exception.code,
            ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.status_code,
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.message
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.IMAGE_URL_INVALID_FORMAT_ERROR.short_desc
        )

    def test_empty_image_url(self):
        with self.assertRaises(ImageURLValidationException) as cx:
            Image.create(**self.empty_image_url, url_validator=UrlValidatorService)

        self.assertEqual(cx.exception.code, ErrorCodes.IMAGE_URL_EMPTY_ERROR.status_code)
        self.assertEqual(cx.exception.message, ErrorCodes.IMAGE_URL_EMPTY_ERROR.message)
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.IMAGE_URL_EMPTY_ERROR.short_desc
        )
