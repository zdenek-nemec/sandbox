import argparse
import json
import logging
import os
import sys


def load_json_data(path):
    with open(path) as json_file:
        return json.load(json_file)


def print_records(records):
    for record in records:
        print(record)


def main():
    argument_parser = argparse.ArgumentParser(prog="JSON to CSV Converter")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument(
        "--log_level",
        default="DEBUG",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    argument_parser.add_argument("--input_file", "-i")

    log_file = argument_parser.parse_args().log_file
    log_level = getattr(logging, argument_parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    if log_file == None:
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
    else:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)
    input_file = argument_parser.parse_args().input_file

    logging.debug("Application started")
    logging.debug("Argument --log_file = %s" % log_file)
    logging.debug("Argument --log_level = %s" % log_level)
    logging.debug("Argument --input_file = %s" % input_file)

    input_file = "test_data.json"

    logging.debug("Loading input file %s" % input_file)
    records = load_json_data(input_file)
    logging.debug("Loaded %d records" % len(records))
    output_file = os.path.splitext(input_file)[0] + ".csv"

    # print_records(records)

    csv_columns = [
        ("CALLING_IMSI", ["calling", "imsi"]),
        ("CALLED_IMSI", ["called", "imsi"]),
    ]

    for record in records:
        for csv_column in csv_columns:
            focus = record
            for level in csv_column[1]:
                if level in focus.keys():
                    focus = focus[level]
                else:
                    print("%s = <empty>" % csv_column[0])
                    break
            else:
                print("%s = %s" % (csv_column[0], focus))

    logging.debug("Created output file %s" % output_file)

    logging.debug("Application finished")


if __name__ == "__main__":
    main()
