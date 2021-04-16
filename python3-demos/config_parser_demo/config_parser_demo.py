import configparser


def main():
    config_parser = configparser.ConfigParser()
    config_parser.optionxform = str
    config_parser.add_section("section_a")
    config_parser.set("section_a", "a1", "1")
    config_parser.set("section_a", "a2", "2")
    config_parser.add_section("section_b")
    config_parser.set("section_b", "b1", "1")
    config_parser.set("section_b", "b2", "2")
    try:
        with open("config_output.cfg", "w") as config_file:
            config_parser.write(config_file)
    except FileNotFoundError:
        raise


if __name__ == "__main__":
    main()
