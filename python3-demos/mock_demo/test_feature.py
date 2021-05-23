import unittest

from feature import LuckyNumbers


class LuckyNumbersTest(unittest.TestCase):
    def test_get_lucky_number(self):
        actual_lucky_number = LuckyNumbers([7]).get_lucky_number()
        self.assertEqual(7, actual_lucky_number, "Failed for the single element %d." % 7)


if __name__ == "__main__":
    unittest.main()
