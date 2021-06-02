import parameterized
import unittest

from data_generator import DataGenerator


class TestDataGenerator(unittest.TestCase):
    @parameterized.parameterized.expand([
        [0, 0],
        [1, 1],
        [1, 10],
        [-10, -1],
        [-10, 10]])
    def test_init(self, minimum, maximum):
        data_generator = DataGenerator(minimum, maximum)
        self.assertEqual(minimum, data_generator._minimum)
        self.assertEqual(maximum, data_generator._maximum)

    def test_init_invalid(self):
        self.assertRaises(ValueError, DataGenerator, 0, -10)

    def test_get_random_data(self):
        data_generator = DataGenerator(1, 1)
        data = data_generator.get_random_data(1)
        self.assertEqual(list, type(data))
        self.assertEqual(24, len(data))
        values = [x[1] for x in data]
        self.assertEqual(True, all(1 == value for value in values))


if __name__ == "__main__":
    unittest.main()
