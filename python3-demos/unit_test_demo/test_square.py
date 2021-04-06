import unittest

from parameterized import parameterized

from square import Square


class SquareTest(unittest.TestCase):
    @parameterized.expand([
        [0, 0],
        [1, 1],
        [2, 4],
        [3, 9],
        [10, 100]
    ])
    def test_solve(self, side, expected_square):
        actual_square = Square().get_square(side)
        self.assertEqual(expected_square, actual_square, "Failed for the number %d." % expected_square)


if __name__ == "__main__":
    unittest.main()
