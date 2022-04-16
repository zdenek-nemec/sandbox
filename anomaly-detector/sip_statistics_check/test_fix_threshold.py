#!/usr/bin/env python3

import datetime
import parameterized
import random
import unittest

from fix_threshold import FixThreshold


class TestFixThreshold(unittest.TestCase):
    @parameterized.parameterized.expand([[0], [1], [-1], [1000], [-1000]])
    def test_constructor(self, minimum):
        fix_threshold = FixThreshold(minimum)
        self.assertEqual(minimum, fix_threshold._minimum, "Failed to set the minimum")

    @parameterized.parameterized.expand([[0.1], [3+5j], [True], ["Six"]])
    def test_constructor_exception(self, minimum):
        self.assertRaises(TypeError, FixThreshold, minimum)

    def test_get_outliers(self):
        entries = 10
        base_timestamp = datetime.datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        timestamps = [(base_timestamp + datetime.timedelta(hours=x)) for x in range(entries)]
        values = [random.randint(10, 20) for x in range(entries)]
        data = [(timestamps[i], values[i]) for i in range(entries)]
        data[0] = (data[0][0], 0)
        expected_outliers = [(base_timestamp, 0)]
        fix_threshold = FixThreshold(10)
        outliers = fix_threshold.get_outliers(data)
        self.assertEqual(1, len(outliers), "Failed for one outlier, number of outliers")
        self.assertEqual(expected_outliers, outliers, "Failed for one outlier, value")

    def test_get_outliers_none(self):
        entries = 10
        base_timestamp = datetime.datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        timestamps = [(base_timestamp + datetime.timedelta(hours=x)) for x in range(entries)]
        values = [random.randint(10, 20) for x in range(entries)]
        data = [(timestamps[i], values[i]) for i in range(entries)]
        fix_threshold = FixThreshold(10)
        outliers = fix_threshold.get_outliers(data)
        self.assertEqual([], outliers, "Failed for no outliers")

    def test_get_outliers_exception(self):
        fix_threshold = FixThreshold(10)
        self.assertRaises(TypeError, fix_threshold.get_outliers, 0)


if __name__ == "__main__":
    unittest.main()
