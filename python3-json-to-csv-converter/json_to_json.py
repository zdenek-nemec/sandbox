import argparse
import json
import logging
import sys


def main():
    argument_parser = argparse.ArgumentParser(prog="json_to_json")
    argument_parser.add_argument("--log_file")
    argument_parser.add_argument("--log_level", default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    log_file = argument_parser.parse_args().log_file
    log_level = getattr(logging, argument_parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    if log_file == None:
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
    else:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)

    logging.info("Application started")
    logging.debug("Argument --log_file = %s" % log_file)
    logging.debug("Argument --log_level = %s" % log_level)

    with open("Preferences.json", "r") as input_file:
        data = json.load(input_file)
        with open("preferences2.json", "w") as output_file:
            json.dump(data, output_file, indent=4)


    logging.info("Application finished")


if __name__ == "__main__":
    main()
