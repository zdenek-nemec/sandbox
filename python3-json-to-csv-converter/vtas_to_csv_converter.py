import argparse
import csv
import glob
import json
import logging
import os
import sys
from config import Config


def print_list_head(data, lines=10):
    i = 0
    for line in data:
        i += 1
        print(line)
        if i == lines:
            break


def print_json_record(record, indentation=""):
    for key in record.keys():
        if isinstance(record[key], dict):
            print("%s%s:" % (indentation, key))
            print_json_record(record[key], indentation + "\t")
        else:
            print("%s%s: %s" % (indentation, key, record[key]))


def load_vtas_file(path):
    vtas_data = []
    with open(path, "r") as vtas_file:
        for line in vtas_file:
            vtas_data.append(line)
    return vtas_data


def load_json_content(vtas_data):
    json_data = []
    for record in vtas_data:
        json_data.append(json.loads(record))
    return json_data


def extract_csv_data(csv_columns, json_data):
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
                    # logging.debug("Value for %s not found" % column[0])
                    row.append("")
                    break
            else:
                row.append(focus)
        csv_data.append(row)
    return csv_data


def save_csv_file(path, data):
    with open(path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        for record in data:
            csv_writer.writerow(record)


def main():
    argument_parser = argparse.ArgumentParser(prog="vtas_to_csv_converter")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument(
        "--log_level",
        default="DEBUG",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    # argument_parser.add_argument("--config", "-c", required=True)
    argument_parser.add_argument("--config", "-c", required=False)  # Debug

    log_file = argument_parser.parse_args().log_file
    log_level = getattr(logging, argument_parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    if log_file == None:
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
    else:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)
    config_file = argument_parser.parse_args().config

    logging.info("Application started")
    logging.debug("Argument --log_file = %s" % log_file)
    logging.debug("Argument --log_level = %s" % log_level)
    logging.debug("Argument --config = %s" % config_file)

    config = Config()
    # config.read(config_file)
    config.read("vtas_to_csv.cfg")  # Debug

    os.chdir(config.get_path())
    input_files = glob.glob(config.get_mask())

    if config.get_action().lower() == "delete":
        delete_source_files = True
    else:
        delete_source_files = False

    for input_file in input_files:
        logging.debug("Loading input file %s" % input_file)
        vtas_data = load_vtas_file(input_file)
        logging.debug("VTAS records: %d" % len(vtas_data))
        json_data = load_json_content(vtas_data)
        logging.debug("JSON records: %d" % len(json_data))
        if config.get_filter():
            extracted_csv_data = extract_csv_data(config._table_columns, json_data)
            csv_data = []
            for record in extracted_csv_data:
                if any(record):
                    csv_data.append(record)
        else:
            csv_data = extract_csv_data(config._table_columns, json_data)
        logging.debug("CSV records: %d" % len(csv_data))
        output_file = os.path.splitext(input_file)[0] + ".csv"
        logging.debug("Creating output file %s" % output_file)
        save_csv_file(output_file, csv_data)

        if delete_source_files:
            logging.debug("Removing input file %s" % input_file)
            os.remove(input_file)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
