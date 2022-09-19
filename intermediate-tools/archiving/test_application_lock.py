import logging
import time
import unittest

from application_lock import ApplicationLock

LOCK_PORT_1 = 23456
LOCK_PORT_2 = 23457


class TestApplicationLock(unittest.TestCase):
    def test_single_instance(self):
        application_lock = ApplicationLock()
        application_lock.disable()
        self.assertTrue(True)

    def test_single_instance_with_port(self):
        application_lock = ApplicationLock(LOCK_PORT_1)
        application_lock.disable()
        self.assertTrue(True)

    def test_two_consecutive_instances(self):
        first_application_lock = ApplicationLock()
        first_application_lock.disable()
        time.sleep(0.1)
        second_application_lock = ApplicationLock()
        second_application_lock.disable()
        self.assertTrue(True)

    def test_two_parallel_instances(self):
        logging.disable()
        first_application_lock = ApplicationLock()
        with self.assertRaises(OSError):
            ApplicationLock()
        first_application_lock.disable()

    def test_two_parallel_instances_with_different_ports(self):
        logging.disable()
        first_application_lock = ApplicationLock(LOCK_PORT_1)
        second_application_lock = ApplicationLock(LOCK_PORT_2)
        first_application_lock.disable()
        second_application_lock.disable()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
