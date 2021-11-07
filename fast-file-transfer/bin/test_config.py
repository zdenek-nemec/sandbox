#!/usr/bin/env python3


import datetime
import logging
import unittest

from parameterized import parameterized
from config import Config


class ConfigTest(unittest.TestCase):
    @parameterized.expand([
        ["U1", "ICAMA", ".zip"],
        ["U1", "ICIAR", ".zip"],
        ["U1", "ICINA", ".zip"],
        ["U2", "ICAMA", ".zip"],
        ["U2", "ICIAR", ".zip"],
        ["U2", "ICINA", ".zip"],
        ["U3", "ICAMA", ".zip"],
        ["U3", "ICIAR", ".zip"],
        ["U3", "ICINA", ".zip"]])
    def test_generate_new_filename(self, switch_id, file_type, file_extension):
        timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
        uta_label = "#M." + switch_id + "." + timestamp + "#"
        expected_filename = (
            "IA." + file_type + "." + uta_label + file_extension)
        config = Config()
        config._switch_id = switch_id
        config._file_type = file_type
        config._file_extension = file_extension
        actual_filename = config.generate_new_filename()
        self.assertEqual(
            expected_filename,
            actual_filename,
            "Failed for %s."
            % expected_filename)


if __name__ == "__main__":
    logging.getLogger().disabled = True
    unittest.main()
