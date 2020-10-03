import configparser

DEFAULT_NAME = "Test Configuration"


class Config(object):
    def __init__(self):
        self._config_filename = None
        self._name = None

    def get_config_filename(self):
        return self._config_filename

    def get_name(self):
        return self._name

    def generate(self, filename):
        self._config_filename = filename
        self._name = DEFAULT_NAME

    def print(self):
        print("Current configuration:")
        print("\tconfig_filename: %s" % self._config_filename)
        print("\tname: %s" % self._name)

    def save(self, filename=None):
        if filename is not None:
            self._config_filename = filename

        if type(self._config_filename) != str:
            raise TypeError

        parser = configparser.ConfigParser()
        parser.optionxform = str

        parser.add_section("Settings")
        parser.set("Settings", "name", self._name)

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
        except configparser.NoSectionError:
            raise
        except:
            raise


if __name__ == "__main__":
    pass
