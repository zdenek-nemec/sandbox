import argparse
import configparser
import logging
import sys

DEFAULT_NAME = "Test Configuration"
DEFAULT_PATH = "."
DEFAULT_MASK = "*.json"
DEFAULT_CSV_COLUMNS = [
    ("RECORD_ID", ["record_id"]),
    ("CALLING_IMSI", ["calling", "imsi"]),
    ("CALLED_IMSI", ["called", "imsi"])
]


class Config(object):
    def __init__(self):
        self._config_filename = None
        self._name = None
        self._path = None
        self._mask = None
        self._csv_columns = None

    def get_config_filename(self):
        return self._config_filename

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_mask(self):
        return self._mask

    def get_csv_columns(self):
        return self._csv_columns

    def generate(self, filename):
        self._config_filename = filename
        self._name = DEFAULT_NAME
        self._path = DEFAULT_PATH
        self._mask = DEFAULT_MASK
        self._csv_columns = DEFAULT_CSV_COLUMNS

    def print(self):
        print("Current configuration:")
        print("\tconfig_filename: %s" % self._config_filename)
        print("\tname: %s" % self._name)
        print("\tpath: %s" % self._path)
        print("\tmask: %s" % self._mask)
        print("\tcsv_columns: %s" % self._csv_columns)

    def write(self, filename=None):
        if filename is not None:
            self._config_filename = filename

        if type(self._config_filename) != str:
            raise TypeError

        parser = configparser.ConfigParser()
        parser.optionxform = str

        parser.add_section("settings")
        parser.set("settings", "name", self._name)
        parser.set("settings", "path", self._path)
        parser.set("settings", "mask", self._mask)

        parser.add_section("csv_columns")
        for column in self._csv_columns:
            parser.set("csv_columns", column[0], ".".join(column[1]))

        try:
            with open(self._config_filename, "w") as config_file:
                parser.write(config_file)
        except FileNotFoundError:
            raise
        except:
            raise

    def read(self, filename):
        if type(filename) != str:
            raise TypeError

        self._config_filename = filename
        parser = configparser.ConfigParser()
        parser.optionxform = str

        try:
            parser.read(filename)
        except configparser.ParsingError:
            raise
        except:
            raise

        try:
            self._name = parser.get("settings", "name")
            self._path = parser.get("settings", "path")
            self._mask = parser.get("settings", "mask")
        except configparser.NoSectionError:
            raise
        except:
            raise

        items = parser.items("csv_columns")
        self._csv_columns = []
        for item in items:
            column_name = item[0]
            column_path = item[1].split(".")
            self._csv_columns.append((column_name, column_path))


def main():
    argument_parser = argparse.ArgumentParser(prog="config")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument(
        "--log_level",
        default="DEBUG",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    argument_group = argument_parser.add_mutually_exclusive_group()
    argument_group.add_argument("--read", "-r")
    argument_group.add_argument("--write", "-w")

    log_file = argument_parser.parse_args().log_file
    log_level = getattr(logging, argument_parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    if log_file == None:
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
    else:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)
    read_config_file = argument_parser.parse_args().read
    write_config_file = argument_parser.parse_args().write

    logging.info("Application started")
    logging.debug("Argument --log_file = %s" % log_file)
    logging.debug("Argument --log_level = %s" % log_level)
    logging.debug("Argument --read_config_file = %s" % read_config_file)
    logging.debug("Argument --write_config_file = %s" % write_config_file)

    if read_config_file is not None:
        logging.info("Reading configuration file %s" % read_config_file)
        config = Config()
        config.read(read_config_file)
        config.print()
    elif write_config_file is not None:
        logging.info("Writing configuration file %s" % write_config_file)
        config = Config()
        config.generate(write_config_file)
        config.write()
        config.print()
    else:
        logging.info("No action requested")

    logging.info("Application finished")


if __name__ == "__main__":
    main()
