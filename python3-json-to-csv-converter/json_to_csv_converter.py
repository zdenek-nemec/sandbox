import argparse
import csv
import glob
import json
import logging
import os
import sys
from config import Config


class JsonToTable(object):
    """JsonToTable"""

    def __init__(self):
        super(JsonToTable, self).__init__()
        self._json_data = None
        self._table_columns = None
        self._table_data = None

    def load_content(self, content):
        self._json_data = json.loads(content)

    def load_file(self, path):
        with open(path) as json_file:
            self._json_data = json.load(json_file)

    def set_table_columns(self, table_columns):
        self._table_columns = table_columns

    def get_table_header(self):
        header = []
        for column in self._table_columns:
            header.append(column[0])
        return header

    def extract_table_data(self):
        self._table_data = []
        for record in self._json_data:
            row = []
            for column in self._table_columns:
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
            self._table_data.append(row)

    def get_table_data(self):
        return self._table_data

    def get_json_data_length(self):
        return len(self._json_data)

    def get_table_data_length(self):
        return len(self._table_data)


def save_csv_file(path, header, data):
    with open(path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
        for record in data:
            csv_writer.writerow(record)


def main():
    argument_parser = argparse.ArgumentParser(prog="json_to_csv_converter")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument(
        "--log_level",
        default="DEBUG",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
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
    config.read("json_to_csv.cfg")  # Debug

    os.chdir(config.get_path())
    input_files = glob.glob(config.get_mask())
    json_to_table = JsonToTable()
    json_to_table.set_table_columns(config.get_table_columns())

    for input_file in input_files:
        logging.info("Loading input file %s" % input_file)
        json_to_table.load_file(input_file)
        logging.debug("JSON records: %d" % json_to_table.get_json_data_length())
        json_to_table.extract_table_data()
        logging.debug("Table records: %d" % json_to_table.get_table_data_length())
        output_file = os.path.splitext(input_file)[0] + ".csv"
        save_csv_file(output_file, json_to_table.get_table_header(), json_to_table.get_table_data())
        logging.info("Created output file %s" % output_file)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
