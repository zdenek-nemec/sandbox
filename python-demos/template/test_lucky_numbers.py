import parameterized
import unittest

from script import LuckyNumbers

class LuckyNumbersTest(unittest.TestCase):
    @parameterized.parameterized.expand([
        [0, 0],
        [1, 1],
        [3, 3],
        [-3, -3]])
    def test_get_lucky_number_single(self, lucky_number, expected_number):
        actual_number = LuckyNumbers([lucky_number]).get_lucky_number()
        self.assertEqual(expected_number, actual_number, "Failed for the single lucky number %d." % lucky_number)

    def test_get_lucky_number_list(self):
        lucky_numbers = [3, 7, 13, 21, 42]
        actual_number = LuckyNumbers(lucky_numbers).get_lucky_number()
        self.assertEqual(True, actual_number in lucky_numbers, "Failed for the lucky number list.")

if __name__ == "__main__":
    unittest.main()
