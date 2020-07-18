import csv
import json


def load_json_data(path):
    with open(path) as json_file:
        return json.load(json_file)


def print_records(records):
    for record in records:
        print(record)


def get_header(records):
    header = []
    for record in records:
        for key in record.keys():
            if not key in header:
                header.append(key)
        break
    return header


if __name__ == "__main__":
    records = load_json_data("./test_data.json")
    header = get_header(records)
    with open("output.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(header)
        for record in records:
            row = []
            for column in header:
                if column in record.keys():
                    row.append(record[column])
                else:
                    row.append("")
            csv_writer.writerow(row)
