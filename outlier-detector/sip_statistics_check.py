import csv
import datetime
import os


DEBUG = False
DATA_PATH = "./data"
HARD_LIMIT_OUTLIERS = 10


class StatisticsData(object):
    def __init__(self):
        self._data = {}

    def load(self, file_path):
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                if len(row) != 5:
                    print("Invalid row %s in file %s" % (str(row), file_path))
                elif row[0][0] == "#":
                    continue
                else:
                    timestamp_string = "-".join([row[4], row[2], row[3], row[1]])
                    timestamp = datetime.datetime.strptime(timestamp_string, "%Y-%b-%d-%H")
                    records = int(row[0])
                    if timestamp not in self._data:
                        self._data[timestamp] = records
                    else:
                        self._data[timestamp] = self._data[timestamp] + records

    def get_data(self):
        return [(key, self._data[key]) for key in self._data]


class HardLimit(object):
    def __init__(self, minimum):
        self._minimum = minimum

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum:
                outliers.append(entry)
        return outliers


def main():
    print("Hello, SIP Statistics Check!")

    if DEBUG:
        data_file_list = [("sip_20210714_%02d.csv" % x) for x in range(0, 24)]
    else:
        data_file_list = os.listdir(DATA_PATH)
    print("Files: %d" % len(data_file_list))
    # print(data_file_list)

    train = StatisticsData()
    for data_file in data_file_list:
        train.load(DATA_PATH + "/" + data_file)
    print("Entries: %d" % len(train._data))
    # [print(key, train._data[key]) for key in train._data]

    hard_limit_outliers = HardLimit(HARD_LIMIT_OUTLIERS).get_outliers(train.get_data())
    print("Hard Limit Outliers: %d" % len(hard_limit_outliers))
    [print(entry[0], entry[1]) for entry in hard_limit_outliers]


if __name__ == "__main__":
    main()
