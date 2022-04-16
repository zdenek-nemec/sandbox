import datetime
import random

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
ENTRIES_PER_DAY = 24

DEFAULT_MINIMUM = 0
DEFAULT_MAXIMUM = 99
DEFAULT_DAYS = 1
DEFAULT_ANOMALY_COUNT = 0
DEFAULT_START_TIME = "2000-01-01 0:00:00"

ALLOWED_MINIMUM = 100
ALLOWED_MAXIMUM = 999
DAYS_TO_GENERATE = 31
ANOMALIES_TO_GENERATE = 5
START_TIME = "2021-01-01 0:00:00"


class DataGenerator(object):
    def __init__(self, minimum=DEFAULT_MINIMUM, maximum=DEFAULT_MAXIMUM):
        super(DataGenerator, self).__init__()
        if minimum > maximum:
            raise ValueError("Minimum cannot be bigger than maximum.")
        self._minimum = minimum
        self._maximum = maximum
        self._time_format = TIME_FORMAT

    def get_random_data(self, days=DEFAULT_DAYS, anomaly_count=DEFAULT_ANOMALY_COUNT, start_time=DEFAULT_START_TIME):
        entries = days * ENTRIES_PER_DAY
        timestamps = self.get_timestamps(start_time, entries)
        values = self.get_random_values(self._minimum, self._maximum, entries)
        difference = self._maximum - self._minimum
        anomaly_values = random.sample(
            self.get_random_values(self._minimum - (difference + 1), self._minimum - 1, anomaly_count)
            + self.get_random_values(self._maximum + 1, self._maximum + difference + 1, anomaly_count),
            anomaly_count)
        for index, anomaly in zip(random.sample(range(0, entries), anomaly_count), anomaly_values):
            values[index] = anomaly
        return [(timestamps[i], values[i]) for i in range(entries)]

    def get_timestamps(self, start_time, entries):
        if type(start_time) not in [str]:
            raise TypeError("Start time must be a string.")
        if type(entries) not in [int]:
            raise TypeError("Number of entries must be an integer.")
        elif entries <= 0:
            raise ValueError("Number of entries must be a positive number.")
        timestamps = []
        for step in range(entries):
            timestamp = datetime.datetime.strptime(start_time, self._time_format) + datetime.timedelta(hours=step)
            timestamps.append(timestamp)
        return timestamps

    @staticmethod
    def get_random_values(minimum, maximum, entries):
        if minimum > maximum:
            raise ValueError("Minimum cannot be bigger than maximum.")
        elif entries < 0:
            raise ValueError("Number of entries must be a positive number.")
        values = list(range(minimum, maximum + 1))
        values *= int(entries / len(values)) + 1
        return random.sample(values, entries)


def main():
    print("Hello, Data Generator!")

    data_generator = DataGenerator(ALLOWED_MINIMUM, ALLOWED_MAXIMUM)
    data = data_generator.get_random_data(DAYS_TO_GENERATE, ANOMALIES_TO_GENERATE)
    for entry in data:
        print(entry[0].strftime(TIME_FORMAT), ",", entry[1], sep="")


if __name__ == "__main__":
    main()
