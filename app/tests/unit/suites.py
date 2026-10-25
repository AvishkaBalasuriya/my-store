import unittest

from tests.unit.domain.test_user_entity import TestUserInitialization
from tests.unit.domain.test_email_address import TestEmailAddress
from tests.unit.domain.test_mobile_number import TestMobileNumber
from tests.unit.domain.test_price import TestPrice
from tests.unit.domain.test_image import TestImage
from tests.unit.domain.test_entity import TestEntityInitialization
from tests.unit.domain.test_order_status import TestOrderStatus
from tests.unit.domain.test_payment_method import TestPaymentMethod
from tests.unit.domain.test_payment_status import TestPaymentStatus
from tests.unit.domain.test_tracking_status import TestTrackingStatus


def test_entity_suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestUserInitialization))
    suite.addTest(unittest.makeSuite(TestEmailAddress))
    suite.addTest(unittest.makeSuite(TestMobileNumber))
    suite.addTest(unittest.makeSuite(TestPrice))
    suite.addTest(unittest.makeSuite(TestImage))
    suite.addTest(unittest.makeSuite(TestEntityInitialization))
    suite.addTest(unittest.makeSuite(TestOrderStatus))
    suite.addTest(unittest.makeSuite(TestPaymentMethod))
    suite.addTest(unittest.makeSuite(TestPaymentStatus))
    suite.addTest(unittest.makeSuite(TestTrackingStatus))

    return suite


if __name__ == "__main__":
    # Use TextTestRunner to execute the specific suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_entity_suite())
