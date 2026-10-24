import unittest

from app.tests.unit.domain.test_user_entity import TestUserInitialization


def test_entity_suite():
    suite = unittest.TestSuite()

    suite.addTest(TestUserInitialization("test_valid_user_initialization"))

    return suite


if __name__ == "__main__":
    # Use TextTestRunner to execute the specific suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_entity_suite())
