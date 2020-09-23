import configparser


def main():
    configuration_filename = "test_configuration.cfg"
    parser = configparser.RawConfigParser()
    parser.add_section("settings")
    parser.set("settings", "name", "Test")
    parser.set("settings", "configuration_file", configuration_filename)
    parser.set("settings", "input_file", "test_data.json")
    parser.set("settings", "source_path", "some_source_path")
    parser.set("settings", "mask", "some_mask")
    parser.set("settings", "destination_path", "some_destination_path")
    parser.set("settings", "delimiter", ",")
    parser.set("settings", "header_line", "...")
    parser.set("settings", "save_header", "True")
    parser.set("settings", "delete_original", "False")
    with open("test_configuration.cfg", "w") as config_file:
        parser.write(config_file)


if __name__ == "__main__":
    main()
