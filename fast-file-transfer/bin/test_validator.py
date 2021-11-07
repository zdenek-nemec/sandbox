#!/usr/bin/env python3


import unittest

from parameterized import parameterized
from validator import Validator


class ValidatorTest(unittest.TestCase):
    @parameterized.expand([
        ["Validator - File Exists", "c:/Zdenek/_tmp/", "test.txt", True, False, False, True],
        ["Validator - File does not Exist", "c:/Zdenek/_tmp/", "nonexistant.txt", True, False, False, False],
        ["Validator - File is ZIP", "c:/Zdenek/_tmp/", "test.zip", True, True, False, True],
        ["Validator - File is not ZIP", "c:/Zdenek/_tmp/", "test.txt", True, True, False, False],
        ["Validator - ZIP is Empty", "c:/Zdenek/_tmp/", "empty.zip", True, True, False, False],
        ["Validator - ZIP Contains More than One File", "c:/Zdenek/_tmp/", "multiple_files.zip", True, True, False, False],
        ["Validator - EWSD File is Valid AMA", "c:/Zdenek/_tmp/", "20190604_100502___IA.ICAMA.#M.U3.20190604.08#.zip", True, True, True, True],
        ["Validator - EWSD File is Valid IAR", "c:/Zdenek/_tmp/", "20190604_100502___IA.ICIAR.#M.U3.20190604.08#.zip", True, True, True, True],
        ["Validator - EWSD File is Valid INA", "c:/Zdenek/_tmp/", "20190604_100502___IA.ICINA.#M.U3.20190604.08#.zip", True, True, True, True],
        ["Validator - EWSD File is not Valid", "c:/Zdenek/_tmp/", "corrupted_ewsd.zip", True, True, True, False]])
    def test(self, testcase, path, filename, check_file, check_zip, check_ewsd, expected_result):
        validator = Validator(path, filename)
        actual_result = validator.test(check_file=check_file, check_zip=check_zip, check_ewsd=check_ewsd)
        self.assertEqual(
            expected_result,
            actual_result,
            "Testcase: %s" % testcase)


if __name__ == "__main__":
    unittest.main()
