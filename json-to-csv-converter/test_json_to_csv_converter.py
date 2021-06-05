import create_json_test_file
import unittest

from json_to_csv_converter import JsonToCsv
from parameterized import parameterized


class TestJsonToCsv(unittest.TestCase):
    def test_init(self):
        json_to_csv = JsonToCsv()
        self.assertEqual(json_to_csv._json_data, None)
        self.assertEqual(json_to_csv._csv_columns, None)
        self.assertEqual(json_to_csv._csv_data, None)

    @parameterized.expand([
        ["{}", 0],
        ["[]", 0],
        ["[{}]", 1],
        ["[{}, {}]", 2],
        ["{\"key\": 0}", 1],
        ["[{\"key\": 0}, {\"key\": 1}]", 2]
    ])
    def test_load_content(self, content, expected_length):
        json_to_csv = JsonToCsv()
        json_to_csv.load_content(content)
        actual_length = len(json_to_csv._json_data)
        self.assertEqual(expected_length, actual_length, "Failed for the JSON content %s" % content)

    def test_load_file(self):
        create_json_test_file.main()
        json_to_csv = JsonToCsv()
        json_to_csv.load_file("test_data.json")
        self.assertEqual(len(json_to_csv._json_data), 2)


if __name__ == "__main__":
    unittest.main()
