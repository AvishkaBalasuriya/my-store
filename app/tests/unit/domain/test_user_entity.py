import unittest
from copy import deepcopy

from app.src.domain.entities.user import User
from app.src.domain.shared.exceptions.error_codes import ErrorCodes
from app.src.domain.shared.exceptions.mobile_exception import \
    MobileValidationException
from app.src.domain.shared.exceptions.user_exceptions import \
    UserMustHaveMobileOrEmailException
from app.src.domain.value_objects.email import EmailValidationException


class TestUserInitialization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_user_data = {
            "name": "testuser",
            "profile_image": "/default_profile.png",
            "cover_image": "/default_cover.png",
            "email": "testuser@example.com",
            "mobile_number": "778293626",
            "country_code": "+94",
            "order_ids": [],
        }

        cls.user_with_dirty_email = deepcopy(cls.valid_user_data)
        cls.user_with_dirty_email["email"] = "TESTUSER@EXAMPLE.COM "

        cls.user_without_either_mobile_or_email = deepcopy(cls.valid_user_data)
        cls.user_without_either_mobile_or_email["email"] = ""
        cls.user_without_either_mobile_or_email["mobile_number"] = ""

        cls.user_with_invalid_image_url = deepcopy(cls.valid_user_data)
        cls.user_with_invalid_image_url["profile_image"] = "invalid_url"
        cls.user_with_invalid_image_url["cover_image"] = "invalid_url"

        cls.user_with_invalid_mobile_number = deepcopy(cls.valid_user_data)
        cls.user_with_invalid_mobile_number["mobile_number"] = "invalid_mobile_number"

        cls.user_with_invalid_email = deepcopy(cls.valid_user_data)
        cls.user_with_invalid_email["email"] = "invalid_email"

        cls.user_without_mandotory_fields = deepcopy(cls.valid_user_data)
        del cls.user_without_mandotory_fields["name"]

        cls.user_without_optional_fields = deepcopy(cls.valid_user_data)
        del cls.user_without_optional_fields["profile_image"]
        del cls.user_without_optional_fields["cover_image"]

    def test_valid_user_initialization(self):
        user = User.create(**self.valid_user_data)

        self.assertEqual(user.name, self.valid_user_data["name"])
        self.assertEqual(user.email, self.valid_user_data["email"])
        self.assertEqual(user.profile_image, self.valid_user_data["profile_image"])
        self.assertEqual(user.cover_image, self.valid_user_data["cover_image"])
        self.assertEqual(user.mobile_number, self.valid_user_data["mobile_number"])
        self.assertEqual(user.order_ids, self.valid_user_data["order_ids"])

    def test_user_without_mandotory_fields(self):
        with self.assertRaises(TypeError):
            User.create(**self.user_without_mandotory_fields)

    def test_user_without_optional_fields(self):
        user = User.create(**self.user_without_optional_fields)
        self.assertEqual(user.name, self.user_without_optional_fields["name"])
        self.assertIsNone(user.profile_image)
        self.assertIsNone(user.cover_image)

    def test_user_with_invalid_mobile_number(self):
        with self.assertRaises(
            MobileValidationException,
            msg=ErrorCodes.MOBILE_INVALID_FORMAT_ERROR.message,
        ):
            User.create(**self.user_with_invalid_mobile_number)

    def test_user_with_invalid_email(self):
        with self.assertRaises(EmailValidationException):
            User.create(**self.user_with_invalid_email)

    def test_user_without_either_mobile_or_email(self):
        with self.assertRaises(UserMustHaveMobileOrEmailException):
            User.create(**self.user_without_either_mobile_or_email)

    def test_user_email_normalization(self):
        user = User.create(**self.user_with_dirty_email)
        self.assertEqual(
            user.email.address, self.user_with_dirty_email["email"].strip().lower()
        )
