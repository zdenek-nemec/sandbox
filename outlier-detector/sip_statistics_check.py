import csv
import datetime


INPUT_DATA_FILENAME_1 = "sip_2021-06-01_00.csv"


def main():
    print("Hello, SIP Statistics Check!")

    data = {}
    with open(INPUT_DATA_FILENAME_1, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            if len(row) != 5:
                print("Invalid row %s in file %s" % (str(row), INPUT_DATA_FILENAME_1))
            elif row[0][0] == "#":
                continue
            else:
                timestamp_string = "-".join([row[4], row[2], row[3], row[1]])
                timestamp = datetime.datetime.strptime(timestamp_string, "%Y-%b-%d-%H")
                records = int(row[0])
                if timestamp not in data:
                    data[timestamp] = records
                else:
                    data[timestamp] = data[timestamp] + records
    [print(key, data[key]) for key in data]


if __name__ == "__main__":
    main()
