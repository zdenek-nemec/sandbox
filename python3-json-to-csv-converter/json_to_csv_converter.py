import argparse
import csv
import json
import logging
import os
import sys


def load_json_file(path):
    with open(path) as json_file:
        return json.load(json_file)


def save_csv_file(path, data):
    with open(path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for record in data:
            csv_writer.writerow(record)


def print_records(records):
    for record in records:
        print(record)


def extract_json_records(csv_columns, json_data):
    csv_data = []
    row = []
    for column in csv_columns:
        row.append(column[0])
    csv_data.append(row)

    for record in json_data:
        row = []
        for column in csv_columns:
            focus = record
            for level in column[1]:
                if level in focus.keys():
                    focus = focus[level]
                else:
                    logging.debug("Value for %s not found" % column[0])
                    row.append("")
                    break
            else:
                row.append(focus)
        csv_data.append(row)
    return csv_data


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
    json_data = load_json_file(input_file)
    logging.debug("Loaded %d records" % len(json_data))
    output_file = os.path.splitext(input_file)[0] + ".csv"
    # print_records(json_data)

    csv_columns = [
        ("RECORD_ID", ["record_id"]),
        ("CALLING_IMSI", ["calling", "imsi"]),
        ("CALLED_IMSI", ["called", "imsi"]),
    ]

    csv_data = extract_json_records(csv_columns, json_data)
    # print(csv_data)

    save_csv_file(output_file, csv_data)

    logging.debug("Created output file %s" % output_file)

    logging.debug("Application finished")


if __name__ == "__main__":
    main()
