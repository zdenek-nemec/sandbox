import unittest

from unittest.mock import *
from parameterized import parameterized

import application


class TestApplication(unittest.TestCase):
    @parameterized.expand([
        [0, 0],
        [1, 1],
        [2, 4],
        [3, 9],
        [10, 100]])
    def test_get_square(self, side, expected_square):
        actual_square = application.Squares().get_square(side)
        self.assertEqual(expected_square, actual_square, "Failed for the side %d." % side)

    @patch('application.Squares.get_random_square', return_value=16)
    def test_get_random_square_mocked(self, mocked_method):
        actual_square = application.Squares().get_random_square()
        self.assertEqual(16, actual_square, "Failed for the case when the whole method is mocked.")

    @patch('application.RandomNumbers.get_integer', return_value=4)
    def test_get_random_square_mocked_random_number(self, mocked_method):
        actual_square = application.Squares().get_random_square()
        self.assertEqual(16, actual_square, "Failed for the case when the random number is mocked.")


if __name__ == "__main__":
    unittest.main()
