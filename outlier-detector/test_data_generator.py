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

    def test_init_default(self):
        data_generator = DataGenerator()
        self.assertEqual(0, data_generator._minimum)
        self.assertEqual(99, data_generator._maximum)

    def test_init_invalid(self):
        self.assertRaises(ValueError, DataGenerator, 0, -10)

    def test_get_random_data_single(self):
        data_generator = DataGenerator(1, 1)
        data = data_generator.get_random_data(1)
        self.assertEqual(list, type(data))
        self.assertEqual(24, len(data))
        values = [x[1] for x in data]
        self.assertEqual(True, all(1 == value for value in values))

    def test_get_random_data_range(self):
        data_generator = DataGenerator(0, 99)
        data = data_generator.get_random_data(days=1, outliers=0)
        self.assertEqual(list, type(data))
        self.assertEqual(24, len(data))
        values = [x[1] for x in data]
        self.assertEqual(True, all((x := value) in range(0, 100) for value in values), "Encountered unexpected outlier %d" % x)

    def test_get_random_data_outliers(self):
        data_generator = DataGenerator(0, 99)
        data = data_generator.get_random_data(days=1, outliers=5)
        self.assertEqual(list, type(data))
        self.assertEqual(24, len(data))
        values = [x[1] for x in data]
        outliers = list(filter(lambda x: x < 0 or x > 99, values))
        self.assertEqual(5, len(outliers), "Encountered unexpected number of outliers")


if __name__ == "__main__":
    unittest.main()
