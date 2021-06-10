import csv


DATA_FILE = "sip_2021-05_exported.txt"


def get_month_number(month_name):
    if month_name == "Mar":
        return "03"
    elif month_name == "Apr":
        return "04"
    elif month_name == "May":
        return "05"
    else:
        return month_name


def main():
    print("Hello, Prepare Data!")
    data = {}
    with open(DATA_FILE, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=" ")
        for row in reader:
            if len(row[0]):
                continue
            year = row[-1][:-1]
            month = get_month_number(row[-3])
            day = row[-2]
            hour = row[-4]
            records = int(row[-5])
            timestamp = year + "-" + month + "-" + day + " " + hour + ":00:00"
            if timestamp not in data:
                data[timestamp] = records
            else:
                data[timestamp] += records

    # for key in data:
    #     print(key, ",", data[key], sep="")

    output_filename = DATA_FILE[:11] + ".csv"
    with open(output_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for key in data:
            writer.writerow([key, data[key]])


if __name__ == "__main__":
    main()
