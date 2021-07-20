import csv
import datetime
import os


DATA_PATH = "./data"

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

    def print_data(self):
        [print(key, self._data[key]) for key in self._data]


def main():
    print("Hello, SIP Statistics Check!")

    data_file_list = os.listdir(DATA_PATH)
    data_file_list = [("sip_20210720_%02d.csv" % x) for x in range(1, 19)]
    print(data_file_list)

    train = StatisticsData()
    for data_file in data_file_list:
        train.load(DATA_PATH + "/" + data_file)
    train.print_data()


if __name__ == "__main__":
    main()
