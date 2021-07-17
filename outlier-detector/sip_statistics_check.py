import csv
import datetime


INPUT_DATA_FILENAME_1 = "sip_2021-06-01_00.csv"


def main():
    print("Hello, SIP Statistics Check!")

    data = []
    with open(INPUT_DATA_FILENAME_1, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            if len(row) != 5:
                print("Invalid row %s in file %s" % (str(row), INPUT_DATA_FILENAME_1))
            elif row[0][0] == "#":
                continue
            else:
                timestamp = "-".join([row[4], row[2], row[3], row[1]])
                records = int(row[0])
                data.append((datetime.datetime.strptime(timestamp, "%Y-%b-%d-%H"), records))
    [print(entry) for entry in data]


if __name__ == "__main__":
    main()
