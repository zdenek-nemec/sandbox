import unittest

from parameterized import parameterized

import army_size


class TestArmySize(unittest.TestCase):
    @parameterized.expand([
        [-1, "Unknown"],
        [0, "Unknown"],
        [1, "Few"],
        [4, "Few"],
        [1001, "Legion"]])
    def test_get_army_description(self, size, expected_description):
        actual_description = army_size.Heroes3().get_army_description(size)
        self.assertEqual(expected_description, actual_description, "Failed for the size %d." % size)


if __name__ == "__main__":
    unittest.main()
