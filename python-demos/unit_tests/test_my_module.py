import unittest

from parameterized import parameterized
from my_module import Square


class TestSquare(unittest.TestCase):
    def test_get_area_zero(self):
        result = Square().get_area(0)
        self.assertEqual(0, result, "Zero side should have zero area")

    @parameterized.expand([
        ["Valid, side 1", 1, 1],
        ["Valid, side 2", 2, 4],
        ["Valid, side 3", 3, 9],
        ["Valid, side 10", 10, 100]])
    def test_get_area_valid(self, test_case, side, expected_result):
        actual_result = Square().get_area(side)
        self.assertEqual(
            expected_result, actual_result, "Testcase: %s" % test_case)

    def test_get_area_invalid_value(self):
        self.assertRaises(ValueError, Square().get_area, -1)

    def test_get_area_invalid_type(self):
        self.assertRaises(TypeError, Square().get_area, "three")


if __name__ == "__main__":
    unittest.main()
