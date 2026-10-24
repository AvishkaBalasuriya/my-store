import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.payment_exception import \
    PaymentMethodInvalidMethodException
from src.domain.value_objects import PaymentMethod, PaymentMethodCode


class TestPaymentMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.non_payment_method_code = "NON_PAYMENT_METHOD_CODE"
        cls.valid_payment_method_code = PaymentMethodCode.CARD

    def test_create_payment_method_with_valid_code(self):
        payment_method = PaymentMethod.create(code=self.valid_payment_method_code)
        self.assertEqual(payment_method.code, self.valid_payment_method_code)

    def test_create_payment_method_with_invalid_code(self):
        with self.assertRaises(PaymentMethodInvalidMethodException) as cx:
            PaymentMethod.create(code=self.non_payment_method_code)

        self.assertEqual(
            cx.exception.code, ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.short_desc
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.PAYMENT_METHOD_INVALID_ERROR.message
        )

    def test_create_payment_method_with_default_code(self):
        payment_method = PaymentMethod.create()
        self.assertEqual(payment_method.code, PaymentMethodCode.QR)

    def test_is_card_property(self):
        payment_method = PaymentMethod.create(code=PaymentMethodCode.CARD)
        self.assertTrue(payment_method.is_card)

    def test_is_paypal_property(self):
        payment_method = PaymentMethod.create(code=PaymentMethodCode.PAYPAL)
        self.assertTrue(payment_method.is_paypal)

    def test_is_qr_property(self):
        payment_method = PaymentMethod.create(code=PaymentMethodCode.QR)
        self.assertTrue(payment_method.is_qr)

    def test_is_cash_property(self):
        payment_method = PaymentMethod.create(code=PaymentMethodCode.CASH)
        self.assertTrue(payment_method.is_cash)
