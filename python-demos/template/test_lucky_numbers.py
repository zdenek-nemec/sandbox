#!/usr/bin/env python3

import parameterized
import unittest

from lucky_numbers import LuckyNumbers

DEFAULT_NUMBER_LIST = [-3, 0, 3, 3.14159, 4+2j, 7, "Seven", 13, 21, 42]


class LuckyNumbersTest(unittest.TestCase):
    def test_constructor(self):
        number_list = DEFAULT_NUMBER_LIST
        lucky_numbers = LuckyNumbers(number_list)
        self.assertEqual(number_list, lucky_numbers._number_list)

    @parameterized.parameterized.expand([
        (-3, TypeError),
        (0, TypeError),
        (3, TypeError),
        (3.14159, TypeError),
        (4+2j, TypeError),
        (7, TypeError),
        ("Seven", TypeError),
        (13, TypeError),
        (21, TypeError),
        (42, TypeError),
        ([], ValueError)])
    def test_constructor_exceptions(self, number_list, exception):
        self.assertRaises(exception, LuckyNumbers, number_list)

    @parameterized.parameterized.expand([
        [[0], 0],
        [[1], 1],
        [[3], 3],
        [[-3], -3]])
    def test_get_lucky_number_single(self, number_list, expected_number):
        actual_number = LuckyNumbers(number_list).get_lucky_number()
        self.assertEqual(expected_number, actual_number, "Failed for the single lucky number " + str(number_list))

    def test_get_lucky_number_list(self):
        number_list = DEFAULT_NUMBER_LIST
        actual_number = LuckyNumbers(number_list).get_lucky_number()
        self.assertEqual(True, actual_number in number_list, "Failed for the lucky number list " + str(number_list))


if __name__ == "__main__":
    unittest.main()
