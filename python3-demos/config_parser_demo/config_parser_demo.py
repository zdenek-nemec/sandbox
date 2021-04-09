import configparser


def main():
    config_parser = configparser.ConfigParser()
    config_parser.optionxform = str
    config_parser.add_section("settings")
    config_parser.set("settings", "a", "1")
    config_parser.set("settings", "b", "2")
    try:
        with open("config_output.cfg", "w") as config_file:
            config_parser.write(config_file)
    except FileNotFoundError:
        raise


if __name__ == "__main__":
    main()
