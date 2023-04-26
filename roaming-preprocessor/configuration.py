import os
from configparser import ConfigParser

DEFAULT_NAME = "Local 2G/3G test"
DEFAULT_TYPE = "2G/3G"
DEFAULT_COLUMNS = 47
DEFAULT_PORT_LOCK = 54321
DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-processing/testing"
DEFAULT_INPUT_MASK = "2023*"
DEFAULT_DELETE_INPUT_FILES = False
DEFAULT_OUTPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-processing/testing"
DEFAULT_OUTPUT_FILENAME_PREFIX = "aggregated_2G-3G_"
DEFAULT_GLOBAL_TITLES_PATH = "c:/Zdenek/_tmp/Cetin/roaming-processing/global_titles.csv"


class Configuration(object):
    def __init__(self):
        self._filename = None
        self._name = None
        self._type = None
        self._columns = None
        self._port_lock = None
        self._input_path = None
        self._input_mask = None
        self._delete_input_files = None
        self._output_path = None
        self._output_filename_prefix = None
        self._global_titles_path = None

    def generate(self, filename: str):
        self._filename = filename
        self._name = DEFAULT_NAME
        self._type = DEFAULT_TYPE
        self._columns = DEFAULT_COLUMNS
        self._port_lock = DEFAULT_PORT_LOCK
        self._input_path = DEFAULT_INPUT_PATH
        self._input_mask = DEFAULT_INPUT_MASK
        self._delete_input_files = DEFAULT_DELETE_INPUT_FILES
        self._output_path = DEFAULT_OUTPUT_PATH
        self._output_filename_prefix = DEFAULT_OUTPUT_FILENAME_PREFIX
        self._global_titles_path = DEFAULT_GLOBAL_TITLES_PATH

    def print(self):
        print(
            "Current configuration:\n"
            f"* filename = {self._filename}\n"
            f"* name = {self._name}\n"
            f"* type = {self._type}\n"
            f"* columns = {self._columns}\n"
            f"* port_lock = {self._port_lock}\n"
            f"* input_path = {self._input_path}\n"
            f"* input_mask = {self._input_mask}\n"
            f"* delete_input_files = {self._delete_input_files}\n"
            f"* output_path = {self._output_path}"
            f"* output_filename_prefix = {self._output_filename_prefix}"
            f"* global_titles_path = {self._global_titles_path}"
        )

    def save(self, filename: str = None):
        if filename is not None:
            self._filename = filename
        config = ConfigParser()
        config["settings"] = {
            "name": self._name,
            "type": self._type,
            "columns": self._columns,
            "port_lock": self._port_lock,
            "input_path": self._input_path,
            "input_mask": self._input_mask,
            "delete_input_files": self._delete_input_files,
            "output_path": self._output_path,
            "output_filename_prefix": self._output_filename_prefix,
            "global_titles_path": self._global_titles_path
        }
        with open(self._filename, "w") as configuration_file:
            config.write(configuration_file)

    def load(self, filename: str):
        config = ConfigParser()
        config.read(filename)
        self._filename = filename
        self._name = config.get("settings", "name")
        self._type = config.get("settings", "type")
        self._columns = config.getint("settings", "columns")
        self._port_lock = config.getint("settings", "port_lock")
        self._input_path = os.path.abspath(config.get("settings", "input_path"))
        self._input_mask = config.get("settings", "input_mask")
        self._delete_input_files = config.getboolean("settings", "delete_input_files")
        self._output_path = os.path.abspath(config.get("settings", "output_path"))
        self._output_filename_prefix = config.get("settings", "output_filename_prefix")
        self._global_titles_path = os.path.abspath(config.get("settings", "global_titles_path"))

    def get_type(self) -> str:
        return self._type

    def get_columns(self) -> int:
        return self._columns

    def get_port_lock(self) -> int:
        return self._port_lock

    def get_input_path(self) -> str:
        return self._input_path

    def get_output_path(self) -> str:
        return self._output_path

    def get_global_titles_path(self) -> str:
        return self._global_titles_path
