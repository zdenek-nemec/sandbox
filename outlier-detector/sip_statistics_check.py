import csv
import datetime
import os
import re
import statistics


DEBUG = False
DATA_PATH = "./data"
TRAIN_FILES_REGEX = r"^sip_20210[6].*\.csv$"
DATA_FILES_REGEX = r"^sip_20210[7].*\.csv$"
TRAIN_DAYS = 40
DATA_DAYS = 1
SKIP = 3
HARD_MINIMUM_OUTLIERS = 4000
REPORT_FILE = "./alarms.log"


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

    def get(self, skip=0):
        return [(key, self._data[key]) for key in sorted(self._data)][skip:]


class HardMinimum(object):
    def __init__(self, minimum):
        self._minimum = minimum

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum:
                outliers.append(entry)
        return outliers


class AllTimeMinimum(object):
    def __init__(self, data):
        self._minimum = data[0][1]
        for entry in data:
            if entry[1] < self._minimum:
                self._minimum = entry[1]

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum:
                outliers.append(entry)
        return outliers


class HourMinimum(object):
    def __init__(self, data):
        self._hours = {}
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                self._hours[hour] = entry[1]
            else:
                self._hours[hour] = min(self._hours[hour], entry[1])

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            hour = entry[0].strftime("%H")
            if hour not in self._hours:
                continue
            else:
                if entry[1] < self._hours[hour]:
                    outliers.append(entry)
        return outliers


class WeekdayHourMinimum(object):
    def __init__(self, data):
        self._trained = {}
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                self._trained[key] = [entry]
            else:
                entries = sorted(self._trained[key] + [entry])
                self._trained[key] = entries

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                continue
            else:
                trained_values = [x[1] for x in self._trained[key]]
                if entry[1] < min(trained_values):
                    outliers.append(entry)
        return outliers


class WeekdayLeftRightHourMinimum(object):
    def __init__(self, data):
        self._trained = {}
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                self._trained[key] = [entry]
            else:
                entries = sorted(self._trained[key] + [entry])
                self._trained[key] = entries

    def get_outliers(self, data):
        candidates = []
        for entry in data:
            weekday = datetime.datetime.weekday(entry[0])
            hour = entry[0].strftime("%H")
            key = str(weekday) + "-" + str(hour)
            if key not in self._trained:
                continue
            else:
                trained_values = [x[1] for x in self._trained[key]]
                if entry[1] < min(trained_values):
                    candidates.append(entry)
        outliers = []
        for i, entry in enumerate(sorted(data)):
            if i in [0, 1] or i in [len(data)-1, len(data)-1]:
                continue
            last_entry = sorted(data)[i-1][1]
            next_entry = sorted(data)[i+1][1]
            if entry in candidates and entry[1] < last_entry and entry[1] < next_entry:
                ADV_CHECK = False
                DEBUG = False
                if not ADV_CHECK:
                    outliers.append(entry)
                    if DEBUG:
                        weekday = datetime.datetime.weekday(entry[0])
                        hour = entry[0].strftime("%H")
                        key = str(weekday) + "-" + str(hour)
                        trained_values = [x[1] for x in self._trained[key]]
                        print(key, trained_values)
                        print(entry[0], entry[1])
                else:
                    last_last_entry = sorted(data)[i-2][1]
                    next_next_entry = sorted(data)[i+2][1]
                    diff = statistics.pstdev([last_last_entry, last_entry, next_entry, next_next_entry])
                    if entry[1] < min(last_last_entry, last_entry, next_entry, next_next_entry) - diff:
                        if (last_last_entry > last_entry and next_entry < next_next_entry
                                and entry[1] > min(last_last_entry, last_entry, next_entry, next_next_entry) - 2*diff):  # If following trend, allow double difference
                            continue
                        outliers.append(entry)
                        if DEBUG:
                            weekday = datetime.datetime.weekday(entry[0])
                            hour = entry[0].strftime("%H")
                            key = str(weekday) + "-" + str(hour)
                            trained_values = [x[1] for x in self._trained[key]]
                            print(key, trained_values)
                            print(last_last_entry, last_entry, next_entry, next_next_entry, diff)
                            print(entry[0], entry[1])
        return outliers

def main():
    print("Hello, SIP Statistics Check!")

    all_files = os.listdir(DATA_PATH)
    print("Files: %d" % len(all_files))
    # print(all_files)

    # train_files = filter(lambda entry: re.match(TRAIN_FILES_REGEX, entry), all_files)
    train_files = all_files[-(TRAIN_DAYS+DATA_DAYS)*24:-DATA_DAYS*24]
    print("Train Files: %d"  % len(train_files))
    # print(train_files)
    # [print(filename) for filename in train_files]
    # data_files = filter(lambda entry: re.match(DATA_FILES_REGEX, entry), all_files)
    data_files = all_files[-DATA_DAYS*24:]
    print("Data Files: %d"  % len(data_files))
    # print(data_files)
    # [print(filename) for filename in data_files]

    train = StatisticsData()
    for filename in train_files:
        train.load(DATA_PATH + "/" + filename)
    print("Train Entries: %d" % len(train._data))
    # [print(key, data._data[key]) for key in data._data]

    data = StatisticsData()
    for filename in data_files:
        data.load(DATA_PATH + "/" + filename)
    print("Data Entries: %d" % len(data._data))
    # [print(key, data._data[key]) for key in data._data]

    hard_minimum_outliers = HardMinimum(HARD_MINIMUM_OUTLIERS).get_outliers(data.get(SKIP))
    print("Hard Minimum Outliers: %d" % len(hard_minimum_outliers))
    [print(entry[0], entry[1]) for entry in hard_minimum_outliers]

    all_time_minimum_outliers = AllTimeMinimum(train.get(SKIP)).get_outliers(data.get(SKIP))
    print("All Time Minimum Outliers: %d" % len(all_time_minimum_outliers))
    [print(entry[0], entry[1]) for entry in all_time_minimum_outliers]

    hour_minimum_outliers = HourMinimum(train.get(SKIP)).get_outliers(data.get(SKIP))
    print("Hour Minimum Outliers: %d" % len(hour_minimum_outliers))
    [print(entry[0], entry[1]) for entry in hour_minimum_outliers]

    weekday_hour_minimum = WeekdayHourMinimum(train.get(SKIP)).get_outliers(data.get(SKIP))
    print("Weekday Hour Minimum Outliers: %d" % len(weekday_hour_minimum))
    [print(entry[0], entry[1]) for entry in weekday_hour_minimum]

    weekday_left_right_hour_minimum = WeekdayLeftRightHourMinimum(train.get(SKIP)).get_outliers(data.get(SKIP))
    print("Weekday Left Right Hour Minimum Outliers: %d" % len(weekday_left_right_hour_minimum))
    [print(entry[0], entry[1]) for entry in weekday_left_right_hour_minimum]

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = []
    for entry in hard_minimum_outliers:
        period = entry[0].strftime("%Y-%m-%d %H:00:00 -- %H:59:59")
        records = entry[1]
        line = timestamp + f" - CRITICAL - Hard minimum {HARD_MINIMUM_OUTLIERS} breached, period {period}, {records} records"
        report_content.append(line)
    for entry in all_time_minimum_outliers:
        period = entry[0].strftime("%Y-%m-%d %H:00:00 -- %H:59:59")
        records = entry[1]
        line = timestamp + f" - MAJOR - New all-time minimum, period {period}, {records} records"
        report_content.append(line)
    for entry in hour_minimum_outliers:
        period = entry[0].strftime("%Y-%m-%d %H:00:00 -- %H:59:59")
        records = entry[1]
        line = timestamp + f" - MINOR - New hour minimum, period {period}, {records} records"
        report_content.append(line)
    for entry in weekday_hour_minimum:
        period = entry[0].strftime("%Y-%m-%d %H:00:00 -- %H:59:59")
        records = entry[1]
        line = timestamp + f" - MINOR - New weekday hour minimum, period {period}, {records} records"
        report_content.append(line)
    for entry in weekday_left_right_hour_minimum:
        period = entry[0].strftime("%Y-%m-%d %H:00:00 -- %H:59:59")
        records = entry[1]
        line = timestamp + f" - MAJOR - New weekday left-right hour minimum, period {period}, {records} records"
        report_content.append(line)

    with open(REPORT_FILE, "a") as text_file:
        for line in report_content:
            text_file.write(line + "\n")


if __name__ == "__main__":
    main()
