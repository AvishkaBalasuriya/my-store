import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.order_exception import \
    OrderInvalidStatusException
from src.domain.value_objects.order_status import OrderStatus, OrderStatusCode


class TestOrderStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.non_order_status_code = "NON_ORDER_STATUS_CODE"
        cls.valid_order_status_code = OrderStatusCode.PENDING

    def test_create_order_status_with_valid_code(self):
        order_status = OrderStatus.create(code=self.valid_order_status_code)
        self.assertEqual(order_status.code, self.valid_order_status_code)

    def test_create_order_status_with_invalid_code(self):
        with self.assertRaises(OrderInvalidStatusException) as cx:
            OrderStatus.create(code=self.non_order_status_code)

        self.assertEqual(
            cx.exception.code, ErrorCodes.ORDER_INVALID_STATUS_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.ORDER_INVALID_STATUS_ERROR.short_desc
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.ORDER_INVALID_STATUS_ERROR.message
        )

    def test_create_order_status_with_default_code(self):
        order_status = OrderStatus.create(code=OrderStatusCode.PENDING)
        self.assertEqual(order_status.code, OrderStatusCode.PENDING)

    def test_is_pending_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.PENDING)
        self.assertTrue(order_status.is_pending)

    def test_is_processing_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.PROCESSING)
        self.assertTrue(order_status.is_processing)

    def test_is_shipped_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.SHIPPED)
        self.assertTrue(order_status.is_shipped)

    def test_is_delivered_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.DELIVERED)
        self.assertTrue(order_status.is_delivered)

    def test_is_cancelled_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.CANCELLED)
        self.assertTrue(order_status.is_cancelled)

    def test_is_returned_property(self):
        order_status = OrderStatus.create(code=OrderStatusCode.RETURNED)
        self.assertTrue(order_status.is_returned)
