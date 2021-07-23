#!/usr/bin/env python3

import unittest

from fix_threshold import FixThreshold


class TestFixThreshold(unittest.TestCase):
    def test_constructor(self):
        threshold = 0
        fix_threshold = FixThreshold(threshold)
        self.assertEqual(threshold, fix_threshold._minimum, "Failed to set the minimum")


if __name__ == "__main__":
    unittest.main()
