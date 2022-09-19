import logging
import time
import unittest

from application_lock import ApplicationLock

APPLICATION_PORT = 12345


class TestApplicationLock(unittest.TestCase):
    def test_single_instance(self):
        application_lock = ApplicationLock(APPLICATION_PORT)
        application_lock.disable()
        self.assertTrue(True)

    def test_two_consecutive_instances(self):
        first_application_lock = ApplicationLock(APPLICATION_PORT)
        first_application_lock.disable()
        time.sleep(0.1)
        second_application_lock = ApplicationLock(APPLICATION_PORT)
        second_application_lock.disable()
        self.assertTrue(True)

    def test_two_parallel_instances(self):
        logging.disable()
        first_application_lock = ApplicationLock(APPLICATION_PORT)
        with self.assertRaises(OSError):
            ApplicationLock(APPLICATION_PORT)
        first_application_lock.disable()


if __name__ == "__main__":
    unittest.main()
