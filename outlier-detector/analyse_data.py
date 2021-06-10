import datetime
import csv


# DATA_FILENAME_1 = "random_data.csv"
DATA_FILENAME_1 = "sip_2021-04.csv"
DATA_FILENAME_2 = "sip_2021-05.csv"


class HardLimit(object):
    def __init__(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum or entry[1] > self._maximum:
                outliers.append(entry)
        return outliers


class MinMax(object):
    def __init__(self):
        self._minimum = None
        self._maximum = None

    def learn(self, data):
        self._minimum = self._maximum = data[0][1]
        for entry in data:
            if entry[1] < self._minimum:
                self._minimum = entry[1]
            if entry[1] > self._maximum:
                self._maximum = entry[1]

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum or entry[1] > self._maximum:
                outliers.append(entry)
        return outliers


def get_time_of_day_data(data):
    todd = {}
    for entry in data:
        hour = entry[0].strftime("%H")
        if hour in todd:
            todd[hour].append((entry[0].strftime("%Y-%m-%d"), entry[1]))
        else:
            todd[hour] = [(entry[0].strftime("%Y-%m-%d"), entry[1])]
    return todd


def main():
    print("Hello, Analyse Data!")

    data1 = []
    with open(DATA_FILENAME_1, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            data1.append((datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"), int(row[1])))
    # [print(x) for x in sorted(data1)]

    data2 = []
    with open(DATA_FILENAME_2, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            data2.append((datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"), int(row[1])))
    # [print(x) for x in sorted(data2)]

    outliers = HardLimit(100, 999).get_outliers(data1)
    print("HardLimit 1:", len(outliers))
    output_filename = DATA_FILENAME_1[:-4] + "_hard_limit.txt"
    with open(output_filename, "w") as text_file:
        for entry in data1:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    outliers = HardLimit(100, 999).get_outliers(data2)
    print("HardLimit 2:", len(outliers))
    output_filename = DATA_FILENAME_2[:-4] + "_hard_limit.txt"
    with open(output_filename, "w") as text_file:
        for entry in data2:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    min_max = MinMax()
    min_max.learn(data1)
    outliers = min_max.get_outliers(data2)
    print("MinMax 2:", len(outliers))
    output_filename = DATA_FILENAME_2[:-4] + "_min_max.txt"
    with open(output_filename, "w") as text_file:
        for entry in data2:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    # todd = get_time_of_day_data(data)
    # [print(x) for x in sorted(todd["10"])]


if __name__ == "__main__":
    main()
