import csv
import datetime
import statistics


# DATA_FILENAME_1 = "random_data.csv"
# DATA_FILENAME_1 = "sip_2021-04.csv"
# DATA_FILENAME_2 = "sip_2021-05.csv"
DATA_FILENAME_1 = "sip_2021-04_train.csv"
DATA_FILENAME_2 = "sip_2021-04_data.csv"

WEEKEND_DAYS = [
    "2021-04-03",
    "2021-04-04",
    "2021-04-10",
    "2021-04-11",
    "2021-04-17",
    "2021-04-18",
    "2021-04-24",
    "2021-04-25",
    "2021-05-01",
    "2021-05-02",
    "2021-05-08",
    "2021-05-09",
    "2021-05-15",
    "2021-05-16",
    "2021-05-22",
    "2021-05-23",
    "2021-05-29",
    "2021-05-30",
]


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


class MinMaxHour(object):
    def __init__(self):
        self._hours = {}

    def learn(self, data):
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                self._hours[hour] = (entry[1], entry[1])
            else:
                minimum, maximum = self._hours[hour]
                self._hours[hour] = (min(minimum, entry[1]), max(maximum, entry[1]))

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                continue
            else:
                if entry[1] < self._hours[hour][0] or entry[1] > self._hours[hour][1]:
                    outliers.append(entry)
        return outliers


class Deviance(object):
    def __init__(self):
        self._hours = {}

    def learn(self, data):
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                self._hours[hour] = [entry[1]]
            else:
                self._hours[hour].append(entry[1])

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                continue
            else:
                hour_list = self._hours[hour]
                if statistics.pstdev(hour_list + [entry[1]]) > statistics.pstdev(hour_list):
                    outliers.append(entry)
        return outliers


class LearningDeviance(object):
    def __init__(self):
        self._hours = {}

    def learn(self, data):
        for entry in data:
            if is_weekend(entry):
                continue
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                self._hours[hour] = [entry[1]]
            else:
                self._hours[hour].append(entry[1])

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if is_weekend(entry):
                continue
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                self._hours[hour] = [entry[1]]
            else:
                hour_list = self._hours[hour]
                current_deviance = statistics.pstdev(hour_list)
                new_deviance = statistics.pstdev(hour_list + [entry[1]])
                if new_deviance > current_deviance and abs(new_deviance - current_deviance) > 1000:
                    outliers.append(entry)
                    # print(hour)
                    # print(sorted(hour_list))
                    # print(entry[1])
                    # print(abs(new_deviance - current_deviance))
                self._hours[hour].append(entry[1])
                # else:
                #     print(abs(new_deviance - current_deviance))
        return outliers


class WeekdayMinimum(object):
    def __init__(self):
        self._trained = {}

    def learn(self, data):
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                self._trained[key] = [entry]
            else:
                entries = sorted(self._trained[key] + [entry])
                self._trained[key] = entries[-2:]

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                self._trained[key] = [entry]
                continue
            else:
                trained_values = [x[1] for x in self._trained[key]]
                if entry[1] < min(trained_values):
                    outliers.append(entry)
                    print(key)
                    print(trained_values)
                    print(entry)
        return outliers


def save_report(report_name, data, outliers):
    output_filename = DATA_FILENAME_2[:-4] + "_" + report_name + ".txt"
    with open(output_filename, "w") as text_file:
        for entry in data:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")


def is_weekend(data_entry):
    day = hour = data_entry[0].strftime("%Y-%m-%d")
    if day in WEEKEND_DAYS:
        return True
    else:
        return False


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

    min_max_hour = MinMaxHour()
    min_max_hour.learn(data1)
    outliers = min_max_hour.get_outliers(data2)
    print("MinMaxHour 2:", len(outliers))
    output_filename = DATA_FILENAME_2[:-4] + "_min_max_hour.txt"
    with open(output_filename, "w") as text_file:
        for entry in data2:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    deviance = Deviance()
    deviance.learn(data1)
    outliers = deviance.get_outliers(data2)
    print("Deviance 2:", len(outliers))
    output_filename = DATA_FILENAME_2[:-4] + "_deviance.txt"
    with open(output_filename, "w") as text_file:
        for entry in data2:
            if entry in outliers:
                text_file.write("Alarm " + str(entry[0]) + ", " + str(entry[1]) + "\n")
            else:
                text_file.write("      " + str(entry[0]) + ", " + str(entry[1]) + "\n")

    learning_deviance = LearningDeviance()
    learning_deviance.learn(data1)
    outliers = learning_deviance.get_outliers(data2)
    print("LearningDeviance 2:", len(outliers))
    save_report("learning_deviance", data2, outliers)

    weekday_minimum = WeekdayMinimum()
    weekday_minimum.learn(data1)
    outliers = weekday_minimum.get_outliers(data2)
    print("WeekdayMinimum 2:", len(outliers))
    save_report("weekday_minimum", data2, outliers)


if __name__ == "__main__":
    main()
