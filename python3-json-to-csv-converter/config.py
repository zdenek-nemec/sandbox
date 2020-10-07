import argparse
import configparser
import logging
import sys

DEFAULT_NAME = "Test Configuration"
DEFAULT_PATH = "."
DEFAULT_MASK = "*.json"
DEFAULT_FILTER = True
DEFAULT_ACTION = "Keep"
DEFAULT_TABLE_COLUMNS = [
    ("RECORD_ID", ["record_id"]),
    ("CALLING_IMSI", ["calling", "imsi"]),
    ("CALLED_IMSI", ["called", "imsi"])
]
# DEFAULT_TABLE_COLUMNS = [
#         ("csi",   ["body", "charging", "csi"]),
#         ("cri",   ["body", "charging", "cri"]),
#         ("crqt",  ["body", "charging", "crqt"]),
#         ("csct",  ["body", "charging", "csct"]),
#         ("cgn",   ["body", "charging", "cgn"]),
#         ("cdn",   ["body", "charging", "cdn"]),
#         ("cimsi", ["body", "charging", "cimsi"]),
#         ("csc",   ["body", "charging", "csc"]),
#         ("cst",   ["body", "charging", "cst"]),
#         ("crn",   ["body", "charging", "crn"]),
#         ("crt",   ["body", "charging", "crt"]),
#         ("cscid", ["body", "charging", "cscid"]),
#         ("cbc",   ["body", "charging", "cbc"]),
#         ("ctz",   ["body", "charging", "ctz"]),
#         ("cnpri", ["body", "charging", "cnpri"]),
#         ("crpa",  ["body", "charging", "crpa"]),
#         ("cra",   ["body", "charging", "cra"]),
#         ("cul",   ["body", "charging", "cul"]),
#         ("cli",   ["body", "charging", "cli"]),
#         ("cssd",  ["body", "charging", "cssd"]),
#         ("cd",    ["body", "charging", "cd"]),
#         ("cet",   ["body", "charging", "cet"]),
#         ("ccv",   ["body", "charging", "ccv"]),
#         ("cicid", ["body", "charging", "cicid"]),
#         ("cpann", ["body", "charging", "cpann"]),
#         ("ct",    ["body", "charging", "ct"]),
#         ("cres",  ["body", "charging", "cres"]),
#         ("csb",   ["body", "charging", "csb"]),
#         ("cvpn",  ["body", "charging", "cvpn"]),
#         ("cmpbx", ["body", "charging", "cmpbx"]),
#         ("css",   ["body", "charging", "css"]),
#         ("cbar",  ["body", "charging", "cbar"]),
#         ("ciai",  ["body", "charging", "ciai"]),
#         ("cocs",  ["body", "charging", "cocs"]),
#         ("ocsid", ["body", "charging", "ocsid"]),
#         ("crc",   ["body", "charging", "crc"])
# ]


class Config(object):
    def __init__(self):
        self._config_filename = None
        self._name = None
        self._path = None
        self._mask = None
        self._filter = None
        self._action = None
        self._table_columns = None

    def get_config_filename(self):
        return self._config_filename

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_mask(self):
        return self._mask

    def get_filter(self):
        return self._filter

    def get_action(self):
        return self._action

    def get_table_columns(self):
        return self._table_columns

    def generate(self, filename):
        self._config_filename = filename
        self._name = DEFAULT_NAME
        self._path = DEFAULT_PATH
        self._mask = DEFAULT_MASK
        self._filter = DEFAULT_FILTER
        self._action = DEFAULT_ACTION
        self._table_columns = DEFAULT_TABLE_COLUMNS

    def print(self):
        print("Current configuration:")
        print("\tconfig_filename: %s" % self._config_filename)
        print("\tname: %s" % self._name)
        print("\tpath: %s" % self._path)
        print("\tmask: %s" % self._mask)
        print("\tfilter: %s" % self._filter)
        print("\taction: %s" % self._action)
        print("\ttable_columns: %s" % self._table_columns)

    def write(self, filename=None):
        if filename is not None:
            self._config_filename = filename
        if type(self._config_filename) != str:
            raise TypeError
        config_parser = configparser.ConfigParser()
        config_parser.optionxform = str
        config_parser.add_section("settings")
        config_parser.set("settings", "name", self._name)
        config_parser.set("settings", "path", self._path)
        config_parser.set("settings", "mask", self._mask)
        config_parser.set("settings", "filter", str(self._filter))
        config_parser.set("settings", "action", str(self._action))
        config_parser.add_section("table_columns")
        for column in self._table_columns:
            config_parser.set("table_columns", column[0], ".".join(column[1]))
        try:
            with open(self._config_filename, "w") as config_file:
                config_parser.write(config_file)
        except FileNotFoundError:
            raise
        except:
            raise

    def read(self, filename):
        if type(filename) != str:
            raise TypeError
        self._config_filename = filename
        config_parser = configparser.ConfigParser()
        config_parser.optionxform = str
        try:
            config_parser.read(filename)
        except configparser.ParsingError:
            raise
        except:
            raise
        try:
            self._name = config_parser.get("settings", "name")
            self._path = config_parser.get("settings", "path")
            self._mask = config_parser.get("settings", "mask")
            if config_parser.get("settings", "filter").lower() == "true":
                self._filter = True
            else:
                self._filter = False
            self._action = config_parser.get("settings", "action")
        except configparser.NoSectionError:
            raise
        except:
            raise
        items = config_parser.items("table_columns")
        self._table_columns = []
        for item in items:
            column_name = item[0]
            column_path = item[1].split(".")
            self._table_columns.append((column_name, column_path))


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
