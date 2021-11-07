#!/usr/bin/env python3


import logging
import parameterized
import unittest

import functions as functions


class FunctionsTest(unittest.TestCase):
    @parameterized.parameterized.expand([
        ["IA.ICAMA.#M.U1.20190724.10#.zip"],
        ["IA.ICIAR.#M.U1.20190724.10#.zip"],
        ["IA.ICINA.#M.U1.20190724.10#.zip"],
        ["IA.ICAMA.#M.U2.20190724.10#.zip"],
        ["IA.ICIAR.#M.U2.20190724.10#.zip"],
        ["IA.ICINA.#M.U2.20190724.10#.zip"],
        ["IA.ICAMA.#M.U3.20190724.10#.zip"],
        ["IA.ICIAR.#M.U3.20190724.10#.zip"],
        ["IA.ICINA.#M.U3.20190724.10#.zip"],
        ["Blablabla"]])
    def test_check_filename(self, filename):
        result = functions.check_filename(filename)
        self.assertEqual(None, result, "Failed for %s." % filename)

    @parameterized.parameterized.expand([
        [None]])
    def test_check_filename_type_error(self, filename):
        self.assertRaises(TypeError, functions.check_filename, filename)

    @parameterized.parameterized.expand([
        ["/home/fastfile/ewsd", "/home/fastfile/ewsd"],
        ["/home/fastfile/ewsd/", "/home/fastfile/ewsd"],
        ["~/fastfile/ewsd", "~/fastfile/ewsd"],
        ["~/fastfile/ewsd/", "~/fastfile/ewsd"],
        ["c:/Zdenek/_tmp", "c:/Zdenek/_tmp"],
        ["c:/Zdenek/_tmp/", "c:/Zdenek/_tmp"],
        ["c:\\Zdenek\\_tmp", "c:/Zdenek/_tmp"],
        ["c:\\Zdenek\\_tmp\\", "c:/Zdenek/_tmp"]])
    def test_normalise_path(self, path, expected_result):
        actual_result = functions.normalise_path(path)
        self.assertEqual(
            expected_result, actual_result, "Failed for %s." % path)

    @parameterized.parameterized.expand([
        [None]])
    def test_normalise_path_type_error(self, path):
        self.assertRaises(TypeError, functions.normalise_path, path)


if __name__ == "__main__":
    logging.getLogger().disabled = True
    unittest.main()
