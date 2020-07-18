import argparse
import csv
import json
import logging
import sys


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


def create_csv_file(filename, records):
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


def convert_json_to_csv():
    argument_parser = argparse.ArgumentParser(prog="JSON to CSV Converter")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument(
        "--log_level",
        default="WARNING",
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

    records = load_json_data(input_file)
    create_csv_file("output.csv", records)

    logging.debug("Application finished")


if __name__ == "__main__":
    convert_json_to_csv()
