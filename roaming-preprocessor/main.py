import csv

DEFAULT_INPUT_FILENAME = "c:/Zdenek/_tmp/roaming-preprocessor/2023012600_01782806.dat"
DEFAULT_OUTPUT_FILENAME = "c:/Zdenek/_tmp/roaming-preprocessor/2023012600_01782806.csv"


def main():
    print("Roaming Preprocessor")

    # Load configuration

    # Check eligible files

    # Load work file

    # Load input file
    input_data = []
    input_filename = DEFAULT_INPUT_FILENAME
    with open(input_filename, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter="|")
        for row in reader:
            input_data.append(row)
    print("First record:", input_data[0])
    print("Number of columns:", len(input_data[0]))
    print("Number of records:", len(input_data))

    # Assemble data

    # Save complete data
    output_data = [x[0:2] for x in input_data]
    output_filename = DEFAULT_OUTPUT_FILENAME
    with open(output_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for row in output_data:
            writer.writerow(row)

    # Save work file


if __name__ == "__main__":
    main()
