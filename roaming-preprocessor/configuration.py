from configparser import ConfigParser

DEFAULT_NAME = "N007510 2G/3G"
DEFAULT_PORT_LOCK = 54321
DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing/small"
DEFAULT_OUTPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing"
DEFAULT_GLOBAL_TITLES_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/global_titles.csv"


class Configuration(object):
    def __init__(self):
        self._filename = None
        self._name = None
        self._port_lock = None
        self._input_path = None
        self._output_path = None
        self._global_titles_path = None

    def generate(self, filename):
        self._filename = filename
        self._name = DEFAULT_NAME
        self._port_lock = DEFAULT_PORT_LOCK
        self._input_path = DEFAULT_INPUT_PATH
        self._output_path = DEFAULT_OUTPUT_PATH
        self._global_titles_path = DEFAULT_GLOBAL_TITLES_PATH

    def print(self):
        print(
            "Current configuration:\n"
            f"* filename = {self._filename}\n"
            f"* name = {self._name}\n"
            f"* port_lock = {self._port_lock}\n"
            f"* input_path = {self._input_path}\n"
            f"* output_path = {self._output_path}"
            f"* global_titles_path = {self._global_titles_path}"
        )

    def save(self, filename=None):
        if filename is not None:
            self._filename = filename
        config = ConfigParser()
        config["settings"] = {
            "name": self._name,
            "port_lock": self._port_lock,
            "input_path": self._input_path,
            "output_path": self._output_path,
            "global_titles_path": self._global_titles_path
        }
        with open(self._filename, "w") as configuration_file:
            config.write(configuration_file)

    def load(self, filename):
        config = ConfigParser()
        config.read(filename)
        self._filename = filename
        self._name = config.get("settings", "name")
        self._port_lock = config.get("settings", "port_lock")
        self._input_path = config.get("settings", "input_path")
        self._output_path = config.get("settings", "output_path")
        self._global_titles_path = config.get("settings", "global_titles_path")

    def get_port_lock(self):
        return int(self._port_lock)

    def get_input_path(self):
        return self._input_path

    def get_output_path(self):
        return self._output_path

    def get_global_titles_path(self):
        return self._global_titles_path
