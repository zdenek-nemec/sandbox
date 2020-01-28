import unittest

from math import pi

from circles import get_circle_area


class TestGetCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(get_circle_area(1), pi)
        self.assertAlmostEqual(get_circle_area(0), 0)
        self.assertAlmostEqual(get_circle_area(4.2), pi * 4.2**2)

    def test_values(self):
        self.assertRaises(ValueError, get_circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, get_circle_area, 3+5j)
        self.assertRaises(TypeError, get_circle_area, True)
        self.assertRaises(TypeError, get_circle_area, "radius")


if __name__ == "__main__":
    unittest.main()
