#!/usr/bin/env python3


import configparser
import datetime
import logging

import functions as functions


DEFAULT_NAME = "Ubuntu VM"
DEFAULT_HOST = "ubuntu"
DEFAULT_USERNAME = "fastfile"
DEFAULT_PASSWORD = "superTajne3Heslo"
DEFAULT_SWITCH_ID = "U1"
DEFAULT_FILE_TYPE = "ICAMA"
DEFAULT_FILE_EXTENSION = ".zip"
DEFAULT_EWSD_PATH = "/home/fastfile/ewsd"
DEFAULT_TRANSFER_PATH = "/home/fastfile/transfer"
DEFAULT_DOWNLOAD_PATH = "/home/zdenek/fast-file-transfer/download"
DEFAULT_MEDIATION_PATH = "/home/zdenek/fast-file-transfer/mediation"


class Config(object):
    def __init__(self):
        self._config_filename = None
        self._name = None
        self._host = None
        self._username = None
        self._password = None
        self._switch_id = None
        self._file_type = None
        self._file_extension = None
        self._ewsd_path = None
        self._transfer_path = None
        self._download_path = None
        self._mediation_path = None
        self._transfers = None

    def get_config_filename(self):
        return self._config_filename

    def get_name(self):
        return self._name

    def get_host(self):
        return self._host

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_switch_id(self):
        return self._switch_id

    def get_file_type(self):
        return self._file_type

    def get_file_extension(self):
        return self._file_extension

    def get_ewsd_path(self):
        return self._ewsd_path

    def get_transfer_path(self):
        return self._transfer_path

    def get_download_path(self):
        return self._download_path

    def get_mediation_path(self):
        return self._mediation_path

    def get_transfers(self):
        return self._transfers

    def generate(self, filename):
        logging.debug("Initiated Config.generate()")
        logging.debug("Parameter filename = %s" % filename)
        self._config_filename = filename
        self._name = DEFAULT_NAME
        self._host = DEFAULT_HOST
        self._username = DEFAULT_USERNAME
        self._password = DEFAULT_PASSWORD
        self._switch_id = DEFAULT_SWITCH_ID
        self._file_type = DEFAULT_FILE_TYPE
        self._file_extension = DEFAULT_FILE_EXTENSION
        self._ewsd_path = functions.normalise_path(DEFAULT_EWSD_PATH)
        self._transfer_path = functions.normalise_path(DEFAULT_TRANSFER_PATH)
        self._download_path = functions.normalise_path(DEFAULT_DOWNLOAD_PATH)
        self._mediation_path = functions.normalise_path(DEFAULT_MEDIATION_PATH)
        self._transfers = []
        logging.debug("Finished Config.generate()")

    def print(self):
        print("Current configuration:")
        print("\tconfig_filename:", self._config_filename)
        print("\tname:", self._name)
        print("\thost:", self._host)
        print("\tusername:", self._username)
        print("\tpassword:", self._password)
        print("\tswitch_id:", self._switch_id)
        print("\tfile_type:", self._file_type)
        print("\tfile_extension:", self._file_extension)
        print("\tewsd_path:", self._ewsd_path)
        print("\ttransfer_path:", self._transfer_path)
        print("\tdownload_path:", self._download_path)
        print("\tmediation_path:", self._mediation_path)
        print("\ttransfers:", self._transfers)

    def save(self, filename=None):
        logging.debug("Initiated Config.save()")

        if filename is not None:
            self._config_filename = filename

        if type(self._config_filename) != str:
            logging.critical("Invalid configuration filename")
            raise TypeError

        parser = configparser.ConfigParser()
        parser.optionxform = str

        parser.add_section("Connection")
        parser.set("Connection", "name", self._name)
        parser.set("Connection", "host", self._host)
        parser.set("Connection", "username", self._username)
        parser.set("Connection", "password", self._password)
        parser.set("Connection", "switch_id", self._switch_id)
        parser.set("Connection", "file_type", self._file_type)
        parser.set("Connection", "file_extension", self._file_extension)
        parser.set("Connection", "ewsd_path", self._ewsd_path)
        parser.set("Connection", "transfer_path", self._transfer_path)
        parser.set("Connection", "download_path", self._download_path)
        parser.set("Connection", "mediation_path", self._mediation_path)

        parser.add_section("Transfers")
        for filename in self._transfers:
            parser.set("Transfers", filename, "Active")

        logging.debug("Try open() and ConfigParser.write()")
        try:
            with open(self._config_filename, "w") as config_file:
                parser.write(config_file)
        except FileNotFoundError:
            logging.error(
                "Cannot save the configuration to %s" % self._config_filename)
            raise
        except:
            logging.critical(
                "Unknown error - open() and ConfigParser.write() failed while "
                "saving the configuration to %s" % self._config_filename)
            raise
        else:
            logging.debug("Success open() and ConfigParser.write()")
        logging.debug("Finished Config.save()")

    def load(self, filename):
        logging.debug("Initiated Config.load()")
        logging.debug("Parameter filename = %s" % filename)

        if type(filename) != str:
            logging.critical("Invalid configuration filename")
            raise TypeError

        self._config_filename = filename
        parser = configparser.ConfigParser()
        parser.optionxform = str

        logging.debug("Try ConfigParser.read()")
        try:
            parser.read(filename)
        except configparser.ParsingError:
            logging.error("Configuration file %s is corrupted" % filename)
            raise
        except:
            logging.critical(
                "Unknown error - ConfigParser.read() failed while loading "
                "configuration file %s" % filename)
            raise
        else:
            logging.debug("Success ConfigParser.read()")

        logging.debug("Try ConfigParser.get()")
        try:
            self._name = parser.get("Connection", "name")
            self._host = parser.get("Connection", "host")
            self._username = parser.get("Connection", "username")
            self._password = parser.get("Connection", "password")
            self._switch_id = parser.get("Connection", "switch_id")
            self._file_type = parser.get("Connection", "file_type")
            self._file_extension = parser.get("Connection", "file_extension")
            self._ewsd_path = functions.normalise_path(
                parser.get("Connection", "ewsd_path"))
            self._transfer_path = functions.normalise_path(
                parser.get("Connection", "transfer_path"))
            self._download_path = functions.normalise_path(
                parser.get("Connection", "download_path"))
            self._mediation_path = functions.normalise_path(
                parser.get("Connection", "mediation_path"))
            self._transfers = list(dict(parser.items("Transfers")).keys())
        except configparser.NoSectionError:
            logging.error(
                "Configuration file %s is corrupted or missing" % filename)
            raise
        except:
            logging.critical(
                "Unknown error - ConfigParser.get() failed while loading "
                "configuration file %s" % filename)
            raise
        else:
            logging.debug("Success ConfigParser.get()")
        logging.debug("Finished Config.load()")

    def check_transfers(self):
        if type(self._transfers) != list:
            logging.error(
                "List of transfers in %s is corrupted" % self._config_filename)
            raise TypeError

    def add_transfer(self, filename=""):
        logging.debug("Initiated Config.add_transfer()")
        logging.debug("Parameter filename = %s" % filename)
        self.check_transfers()
        functions.check_filename(filename)
        if filename not in self._transfers:
            self._transfers.append(filename)
            logging.debug(
                "Filename %s successfully added to active transfers"
                % filename)
        else:
            logging.warning(
                "Attempted to add filename %s to active transfers but the "
                "file is there already" % filename)
        logging.debug("Finished Config.add_transfer()")

    def remove_transfer(self, filename=""):
        logging.debug("Initiated Config.remove_transfer()")
        logging.debug("Parameter filename = %s" % filename)
        self.check_transfers()
        functions.check_filename(filename)
        if filename in self._transfers:
            self._transfers.remove(filename)
            logging.debug(
                "Filename %s successfully removed from active transfers"
                % filename)
        else:
            logging.warning(
                "Attempted to remove filename %s from active transfers but "
                "the file is not in the list" % filename)
        logging.debug("Finished Config.remove_transfer()")

    def generate_new_filename(self):
        logging.debug("Initiated Config.generate_new_filename()")
        timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
        uta_label = "#M." + self._switch_id + "." + timestamp + "#"
        filename = ("IA."+ self._file_type + "."
            + uta_label + self._file_extension)
        logging.debug("Generated filename %s" % filename)
        logging.debug("Finished Config.generate_new_filename()")
        return filename


if __name__ == "__main__":
    pass
