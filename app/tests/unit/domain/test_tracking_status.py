import unittest

from src.domain.shared.exceptions.error_codes import ErrorCodes
from src.domain.shared.exceptions.tracking_exception import \
    TrackingStatusInvalidException
from src.domain.value_objects import TrackingStatus, TrackingStatusCode


class TestTrackingStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_tracking_status = TrackingStatusCode.ORDER_CONFIRMED
        cls.non_tracking_status_code = "NON_TRACKING_STATUS_CODE"

    def test_create_tracking_status_with_valid_code(self):
        tracking_status = TrackingStatus.create(code=self.valid_tracking_status)
        self.assertEqual(tracking_status.code, self.valid_tracking_status)

    def test_create_tracking_status_with_invalid_code(self):
        with self.assertRaises(TrackingStatusInvalidException) as cx:
            TrackingStatus.create(code=self.non_tracking_status_code)

        self.assertEqual(
            cx.exception.code, ErrorCodes.TRACKING_STATUS_INVALID_ERROR.status_code
        )
        self.assertEqual(
            cx.exception.short_desc, ErrorCodes.TRACKING_STATUS_INVALID_ERROR.short_desc
        )
        self.assertEqual(
            cx.exception.message, ErrorCodes.TRACKING_STATUS_INVALID_ERROR.message
        )

    def test_create_tracking_status_with_default_code(self):
        tracking_status = TrackingStatus.create()
        self.assertEqual(tracking_status.code, TrackingStatusCode.ORDER_CONFIRMED)

    def test_is_order_confirmed_property(self):
        tracking_status = TrackingStatus.create(code=TrackingStatusCode.ORDER_CONFIRMED)
        self.assertTrue(tracking_status.is_order_confirmed)

    def test_is_prepare_for_shipment_property(self):
        tracking_status = TrackingStatus.create(
            code=TrackingStatusCode.PREPARE_FOR_SHIPMENT
        )
        self.assertTrue(tracking_status.is_prepare_for_shipment)

    def test_is_picked_up_property(self):
        tracking_status = TrackingStatus.create(code=TrackingStatusCode.PICKED_UP)
        self.assertTrue(tracking_status.is_picked_up)

    def test_is_arrived_at_origin_facility_property(self):
        tracking_status = TrackingStatus.create(
            code=TrackingStatusCode.ARRIVED_AT_ORIGIN_FACILITY
        )
        self.assertTrue(tracking_status.is_arrived_at_origin_facility)

    def test_is_departed_from_origin_facility_property(self):
        tracking_status = TrackingStatus.create(
            code=TrackingStatusCode.DEPARTED_FROM_ORIGIN_FACILITY
        )
        self.assertTrue(tracking_status.is_departed_from_origin_facility)

    def test_is_arrived_at_destination_facility_property(self):
        tracking_status = TrackingStatus.create(
            code=TrackingStatusCode.ARRIVED_AT_DESTINATION_FACILITY
        )
        self.assertTrue(tracking_status.is_arrived_at_destination_facility)

    def test_is_out_for_delivery_property(self):
        tracking_status = TrackingStatus.create(code=TrackingStatusCode.OUT_FOR_DELIVERY)
        self.assertTrue(tracking_status.is_out_for_delivery)

    def test_is_delivered_property(self):
        tracking_status = TrackingStatus.create(code=TrackingStatusCode.DELIVERED)
        self.assertTrue(tracking_status.is_delivered)
