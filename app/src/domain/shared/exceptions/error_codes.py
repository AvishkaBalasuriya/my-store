from collections import namedtuple
from enum import Enum

ERROR_OBJECT = namedtuple("ErrorObject", ["status_code", "short_desc", "message"])


class ErrorCodes(ERROR_OBJECT, Enum):
    """Enumeration of error codes for the application."""

    GENERIC_ERROR = ERROR_OBJECT(
        status_code=500,
        short_desc="GENERIC_ERROR",
        message="An unexpected error occurred.",
    )

    # Image-related errors
    GENERIC_IMAGE_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="GENERIC_IMAGE_ERROR",
        message="An error occurred while processing the image.",
    )
    IMAGE_URL_EMPTY_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="IMAGE_URL_EMPTY_ERROR",
        message="The provided image URL is empty.",
    )

    # Email-related errors
    GENERIC_EMAIL_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="GENERIC_EMAIL_ERROR",
        message="An error occurred while processing the email address.",
    )
    EMAIL_EMPTY_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="EMAIL_EMPTY_ERROR",
        message="The provided email address is empty.",
    )

    # Mobile number-related errors
    GENERIC_MOBILE_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="GENERIC_MOBILE_ERROR",
        message="An error occurred while processing the mobile number.",
    )
    MOBILE_INVALID_FORMAT_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="MOBILE_INVALID_FORMAT_ERROR",
        message="The provided mobile number format is invalid.",
    )
    MOBILE_COUNTRY_CODE_EMPTY_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="MOBILE_COUNTRY_CODE_EMPTY_ERROR",
        message="The provided country code is empty.",
    )
    MOBILE_NUMBER_EMPTY_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="MOBILE_NUMBER_EMPTY_ERROR",
        message="The provided mobile number is empty.",
    )

    # Price-related errors
    GENERIC_PRICE_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="GENERIC_PRICE_ERROR",
        message="An error occurred while processing the price.",
    )
    PRICE_NEGATIVE_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="PRICE_NEGATIVE_ERROR",
        message="The provided price cannot be negative.",
    )
    PRICE_CURRENCY_EMPTY_ERROR = ERROR_OBJECT(
        status_code=400,
        short_desc="PRICE_CURRENCY_EMPTY_ERROR",
        message="The provided currency is empty.",
    )
