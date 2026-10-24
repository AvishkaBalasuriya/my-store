import logging

from email_validator import EmailNotValidError, validate_email

from app.src.domain.interfaces.email_validator import EmailValidator

logger = logging.getLogger(__name__)


class EmailValidatorService(EmailValidator):

    @classmethod
    def validate(cls, email_address: str) -> bool:
        logger.info(f"EMAIL:VALIDATOR:: validating EMAIL: {email_address}")

        try:
            validate_email(email_address)
            return True
        except EmailNotValidError:
            return False
