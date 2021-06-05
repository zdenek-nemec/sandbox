import unittest

from parameterized import parameterized

from math_demo import MathDemo


class MathDemoTest(unittest.TestCase):
    @parameterized.expand([
        [3, 5, 8],
        [-1, 7, 6]])
    def test_add(self, a, b, expected):
        actual = MathDemo().add(a, b)
        self.assertEqual(
            expected,
            actual,
            "Failed for the numbers %d, %d."
            % (a, b))


if __name__ == "__main__":
    unittest.main()
