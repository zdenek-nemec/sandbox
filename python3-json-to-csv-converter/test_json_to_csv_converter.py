import unittest

from json_to_csv_converter import JsonToCsv


class TestJsonToCsv(unittest.TestCase):
    def test_init(self):
        json_to_csv = JsonToCsv()
        self.assertEqual(json_to_csv._json_data, None)
        self.assertEqual(json_to_csv._csv_columns, None)
        self.assertEqual(json_to_csv._csv_data, None)


if __name__ == "__main__":
    unittest.main()
