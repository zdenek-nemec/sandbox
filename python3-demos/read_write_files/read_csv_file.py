import csv


DEFAULT_FILENAME = "input_test_file.csv"


def main():
    filename = DEFAULT_FILENAME
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            print("Row:", row)
            for element in row:
                print("Element:", element)


if __name__ == "__main__":
    main()
