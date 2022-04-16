import datetime
import random

NORMAL_MINIMUM = 100
NORMAL_MAXIMUM = 999
DAYS_TO_GENERATE = 31
ANOMALIES = 5


class DataGenerator(object):
    def __init__(self, minimum=0, maximum=99):
        super(DataGenerator, self).__init__()
        if minimum > maximum:
            raise ValueError("Minimum cannot be bigger than maximum.")
        self._minimum = minimum
        self._maximum = maximum

    def get_random_data(self, days=1, outliers=0):
        entries = days * 24
        timestamps = [(datetime.datetime.strptime("2021-01-01 0:00:00", "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=x)) for x in range(entries)]
        values = [random.randint(self._minimum, self._maximum) for x in range(entries)]
        difference = self._maximum - self._minimum
        outlier_values = random.sample(
            [random.randint(self._minimum - (difference + 1), self._minimum - 1) for x in range(outliers)]
            + [random.randint(self._maximum + 1, self._maximum + (difference + 1)) for x in range(outliers)],
            outliers)
        for index, outlier_value in zip(random.sample(range(0, entries), outliers), outlier_values):
            values[index] = outlier_value
        return [(timestamps[i], values[i]) for i in range(entries)]


def main():
    print("Hello, Data Generator!")

    data_generator = DataGenerator(NORMAL_MINIMUM, NORMAL_MAXIMUM)
    data = data_generator.get_random_data(DAYS_TO_GENERATE, ANOMALIES)
    for entry in data:
        print(entry[0].strftime("%Y-%m-%d %H:%M:%S"), ",", entry[1], sep="")


if __name__ == "__main__":
    main()
