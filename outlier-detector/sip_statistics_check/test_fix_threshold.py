#!/usr/bin/env python3

import unittest

from parameterized import parameterized

from fix_threshold import FixThreshold


class TestFixThreshold(unittest.TestCase):
    @parameterized.expand([[0], [1], [-1], [1000], [-1000]])
    def test_constructor(self, minimum):
        fix_threshold = FixThreshold(minimum)
        self.assertEqual(minimum, fix_threshold._minimum, "Failed to set the minimum")

    @parameterized.expand([[0.1], [3+5j], [True], ["Six"]])
    def test_constructor_exceptions(self, minimum):
        self.assertRaises(TypeError, FixThreshold, minimum)


if __name__ == "__main__":
    unittest.main()
