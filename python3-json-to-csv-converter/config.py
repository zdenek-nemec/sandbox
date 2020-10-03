import configparser

DEFAULT_NAME = "Test Configuration"
DEFAULT_PATH = "."
DEFAULT_MASK = "*.json"


class Config(object):
    def __init__(self):
        self._config_filename = None
        self._name = None
        self._path = None
        self._mask = None

    def get_config_filename(self):
        return self._config_filename

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_mask(self):
        return self._mask

    def generate(self, filename):
        self._config_filename = filename
        self._name = DEFAULT_NAME
        self._path = DEFAULT_PATH
        self._mask = DEFAULT_MASK

    def print(self):
        print("Current configuration:")
        print("\tconfig_filename: %s" % self._config_filename)
        print("\tname: %s" % self._name)
        print("\tpath: %s" % self._path)
        print("\tmask: %s" % self._mask)

    def save(self, filename=None):
        if filename is not None:
            self._config_filename = filename

        if type(self._config_filename) != str:
            raise TypeError

        parser = configparser.ConfigParser()
        parser.optionxform = str

        parser.add_section("Settings")
        parser.set("Settings", "name", self._name)
        parser.set("Settings", "path", self._path)
        parser.set("Settings", "mask", self._mask)

        try:
            with open(self._config_filename, "w") as config_file:
                parser.write(config_file)
        except FileNotFoundError:
            raise
        except:
            raise

    def load(self, filename):
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
            self._name = parser.get("Settings", "name")
            self._name = parser.get("Settings", "path")
            self._name = parser.get("Settings", "mask")
        except configparser.NoSectionError:
            raise
        except:
            raise


if __name__ == "__main__":
    pass
