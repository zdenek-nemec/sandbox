import unittest

from parameterized import parameterized

from json_to_csv_converter import JsonToCsv


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
        ["[{\"key\": 0}, {\"key\": 1}]", 2]])
    def test_load_content(self, content, expected_length):
        json_to_csv = JsonToCsv()
        json_to_csv.load_content(content)
        actual_length = len(json_to_csv._json_data)
        self.assertEqual(expected_length, actual_length, "Failed for the JSON content %s" % content)


if __name__ == "__main__":
    unittest.main()
