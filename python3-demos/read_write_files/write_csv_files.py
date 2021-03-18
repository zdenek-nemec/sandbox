import csv


DEFAULT_FILENAME = "output_test_file.csv"
DEFAULT_CONTENT = [
    ["a1", "b1"],
    ["a2", "b2"]
]


def main():
    filename = DEFAULT_FILENAME
    content = DEFAULT_CONTENT;
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for row in content:
            writer.writerow(row)


if __name__ == "__main__":
    main()
