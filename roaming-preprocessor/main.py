import argparse
import csv
import logging
import sys
import timeit

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_INPUT_FILENAME = "c:/Zdenek/_tmp/roaming-preprocessor/2023012600_01782806.dat"
DEFAULT_OUTPUT_FILENAME = "c:/Zdenek/_tmp/roaming-preprocessor/2023012600_01782806.csv"


def main():
    print("Roaming Preprocessor")

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )

    log_level = argument_parser.parse_args().log_level
    log_format = DEFAULT_LOG_FORMAT
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")
    application_start_time = timeit.default_timer()

    logging.debug("Arguments: log_level = {0}".format(
        argument_parser.parse_args().log_level
    ))

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

    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
