import unittest

import parameterized

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
        self.assertEqual("%Y-%m-%d %H:%M:%S", data_generator._time_format)

    def test_init_default(self):
        data_generator = DataGenerator()
        self.assertEqual(0, data_generator._minimum)
        self.assertEqual(99, data_generator._maximum)
        self.assertEqual("%Y-%m-%d %H:%M:%S", data_generator._time_format)

    def test_init_invalid(self):
        self.assertRaises(ValueError, DataGenerator, 0, -10)

    @parameterized.parameterized.expand([
        [5],
        [10]])
    def test_get_timestamps(self, entries):
        data_generator = DataGenerator()
        timestamps = data_generator.get_timestamps("2000-01-01 0:00:00", entries)
        self.assertEqual(entries, len(timestamps))

    @parameterized.parameterized.expand([
        [0],
        [10],
        [3.14159]])
    def test_get_timestamps_invalid_start_time_type(self, start_time):
        data_generator = DataGenerator()
        self.assertRaises(TypeError, data_generator.get_timestamps, start_time, 10)

    @parameterized.parameterized.expand([
        [""],
        [3.14159]])
    def test_get_timestamps_invalid_entries_type(self, entries):
        data_generator = DataGenerator()
        self.assertRaises(TypeError, data_generator.get_timestamps, "2000-01-01 0:00:00", entries)

    @parameterized.parameterized.expand([
        [0],
        [-10]])
    def test_get_timestamps_invalid_entries_value(self, entries):
        data_generator = DataGenerator()
        self.assertRaises(ValueError, data_generator.get_timestamps, "2000-01-01 0:00:00", entries)

    @parameterized.parameterized.expand([
        [0, 9, 0],
        [0, 9, 5],
        [0, 5, 5],
        [0, 2, 5]])
    def test_get_random_values(self, minimum, maximum, entries):
        data_generator = DataGenerator()
        values = data_generator.get_random_values(minimum, maximum, entries)
        self.assertEqual(entries, len(values))

    @parameterized.parameterized.expand([
        [0, -2, 1],
        [0, 2, -1]])
    def test_get_random_values_invalid(self, minimum, maximum, entries):
        data_generator = DataGenerator()
        self.assertRaises(ValueError, data_generator.get_random_values, minimum, maximum, entries)

    def test_get_random_data_single(self):
        data_generator = DataGenerator(1, 1)
        data = data_generator.get_random_data(days=1)
        self.assertEqual(list, type(data))
        self.assertEqual(24, len(data))
        values = [x[1] for x in data]
        self.assertEqual(True, all(value == 1 for value in values))

    def test_get_random_data_range(self):
        data_generator = DataGenerator(0, 99)
        data = data_generator.get_random_data(days=31, anomaly_count=0)
        self.assertEqual(list, type(data))
        self.assertEqual(31 * 24, len(data))
        values = [x[1] for x in data]
        self.assertEqual(True, all(value in range(0, 100) for value in values), "Encountered unexpected anomaly")

    def test_get_random_data_outliers(self):
        data_generator = DataGenerator(0, 99)
        data = data_generator.get_random_data(days=31, anomaly_count=5)
        self.assertEqual(list, type(data))
        self.assertEqual(31 * 24, len(data))
        values = [x[1] for x in data]
        anomalies = list(filter(lambda x: x < 0 or x > 99, values))
        self.assertEqual(5, len(anomalies), "Encountered unexpected number of anomalies")


if __name__ == "__main__":
    unittest.main()
