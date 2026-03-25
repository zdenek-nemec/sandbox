import unittest
from number import Number

class TestNumber(unittest.TestCase):
    def test_number_decadic_default(self):
        my_number = Number("42")
        self.assertEqual(str(my_number), "42 base 10 value 42")
        self.assertEqual(my_number.get(), "42")

    def test_number_decadic_specified(self):
        my_number = Number("42", 10)
        self.assertEqual(str(my_number), "42 base 10 value 42")
        self.assertEqual(my_number.get(), "42")

    def test_number_binary(self):
        my_number = Number("1001", 2)
        self.assertEqual(str(my_number), "1001 base 2 value 9")
        self.assertEqual(my_number.get(), "9")

    def test_exception_invalid_base(self):
        self.assertRaises(ValueError, Number, "0000", 1)
        self.assertRaises(ValueError, Number, "0000", 17)

    def test_exception_invalid_number_for_base(self):
        self.assertRaises(ValueError, Number, "0123", 2)
        self.assertRaises(ValueError, Number, "10A", 10)
        self.assertRaises(ValueError, Number, "EF", 8)
