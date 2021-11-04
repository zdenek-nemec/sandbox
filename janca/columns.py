import csv

DEFAULT_INPUT_FILE = "input_file.csv"
DEFAULT_OUTPUT_FILE = "output_file.csv"


def read_csv_data(input_file, input_delimiter):
    data = []
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=input_delimiter)
        for row in reader:
            data.append(row)
    return data


def remove_header(data):
    data.pop(0)


def alter_data(data):
    for row in data:
        row[2] += ")"


def remove_column(data, column):
    for i in range(len(data)):
        data[i].pop(column)


def write_data(data, output_file, output_delimiter):
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=output_delimiter, quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)


def main():
    print("Columns")
    data = read_csv_data(DEFAULT_INPUT_FILE, ";")
    print(data)
    remove_header(data)
    print(data)
    alter_data(data)
    print(data)
    remove_column(data, 1)
    print(data)
    write_data(data, DEFAULT_OUTPUT_FILE, ",")


if __name__ == "__main__":
    main()
