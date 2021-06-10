import datetime
import csv


DATA_FILE = "random_data.csv"


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

    data = []
    with open(DATA_FILE, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            data.append((datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"), int(row[1])))
    # [print(x) for x in sorted(data)]

    outliers = HardLimit(100, 999).get_outliers(data)
    print("HardLimit:", len(outliers))
    output_filename = DATA_FILE[:-4] + "_hard_limit.txt"
    with open(output_filename, "w") as text_file:
        for entry in data:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    # todd = get_time_of_day_data(data)
    # [print(x) for x in sorted(todd["10"])]


if __name__ == "__main__":
    main()
