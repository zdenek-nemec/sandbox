#!/usr/bin/env python3


import argparse
import logging
import sys


from some_module import MyClass


def main():
    """Demo of Python Logging module, see https://docs.python.org/3/howto/logging.html"""

    parser = argparse.ArgumentParser(prog="Python Logging Demo")
    parser.add_argument("--log_file", "-f")
    parser.add_argument("--log_level", "-l", default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    log_file = parser.parse_args().log_file
    log_level = getattr(logging, parser.parse_args().log_level, None)
    if log_file is None:
        logging.basicConfig(stream=sys.stdout, level=log_level)
    else:
        logging.basicConfig(filename=log_file, level=log_level)

    logging.warning("I am about to start")

    print("Hello, World!")

    logging.debug("This is debug-level message")
    logging.info("This is info-level message")
    logging.warning("This is warning-level message")
    logging.error("This is error-level message")
    logging.critical("This is critical-level message")

    print(
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL)

    lucky_number = 7
    logging.debug("Variable lucky_number is %d" % lucky_number)
    my_class = MyClass()
    my_class.set_lucky_number(lucky_number)


if __name__ == "__main__":
    main()
