import socket
import unittest

from global_titles import GlobalTitles


class TestGlobalTitles(unittest.TestCase):
    def setUp(self):
        if socket.gethostname()[0:7] == "celimdt":
            self.global_titles = GlobalTitles("/appl/cgi/dcs/data01_loc/TOOLS/roaming-preprocessor/global_titles.csv")
        else:
            self.global_titles = GlobalTitles("c:/Zdenek/_tmp/Cetin/roaming-preprocessor/global_titles.csv")

    def test_exact_match(self):
        actual_output = self.global_titles.get_tadig("8835150")
        expected_output = "AAAWL"
        self.assertEqual(expected_output, actual_output)

    def test_longer(self):
        actual_output = self.global_titles.get_tadig("8835150123")
        expected_output = "AAAWL"
        self.assertEqual(expected_output, actual_output)

    def test_shortest(self):
        actual_output = self.global_titles.get_tadig("56")
        expected_output = "CHLVT"
        self.assertEqual(expected_output, actual_output)

    def test_missing(self):
        actual_output = self.global_titles.get_tadig("123")
        expected_output = None
        self.assertEqual(expected_output, actual_output)

    def test_missing_with_default(self):
        for default_value in ["123", "miss"]:
            actual_output = self.global_titles.get_tadig("123", default_value)
            expected_output = default_value
            self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
