import argparse
import logging
import sys

from lucky_numbers import LuckyNumbers

DEFAULT_NUMBER_LIST = [-3, 0, 3, 3.14159, 4 + 2j, 7, "Seven", 13, 21, 42]


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    log_level = argument_parser.parse_args().log_level
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")

    lucky_numbers = LuckyNumbers(DEFAULT_NUMBER_LIST)
    print("Trending lucky number is " + str(lucky_numbers.get_lucky_number()))

    logging.info("Application finished")


if __name__ == "__main__":
    main()
