import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.payment_exception import \
    PaymentStatusInvalidException
from src.domain.value_objects import PaymentStatus, PaymentStatusCode


class TestPaymentStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_payment_status = PaymentStatusCode.COMPLETED
        cls.non_payment_status_code = "NON_PAYMENT_STATUS_CODE"

    def test_create_payment_status_with_valid_code(self):
        payment_status = PaymentStatus.create(code=self.valid_payment_status)
        self.assertEqual(payment_status.code, self.valid_payment_status)

    def test_create_payment_status_with_invalid_code(self):
        with self.assertRaises(PaymentStatusInvalidException) as cx:
            PaymentStatus.create(code=self.non_payment_status_code)

        self.assertEqual(
            cx.exception.code, ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.short_desc
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PAYMENT_STATUS_INVALID_ERROR.message
        )

    def test_is_pending_property(self):
        payment_status = PaymentStatus.create(code=PaymentStatusCode.PENDING)
        self.assertTrue(payment_status.is_pending)

    def test_is_completed_property(self):
        payment_status = PaymentStatus.create(code=PaymentStatusCode.COMPLETED)
        self.assertTrue(payment_status.is_completed)

    def test_is_failed_property(self):
        payment_status = PaymentStatus.create(code=PaymentStatusCode.FAILED)
        self.assertTrue(payment_status.is_failed)

    def test_is_refunded_property(self):
        payment_status = PaymentStatus.create(code=PaymentStatusCode.REFUNDED)
        self.assertTrue(payment_status.is_refunded)

    def test_is_canceled_property(self):
        payment_status = PaymentStatus.create(code=PaymentStatusCode.CANCELLED)
        self.assertTrue(payment_status.is_cancelled)
