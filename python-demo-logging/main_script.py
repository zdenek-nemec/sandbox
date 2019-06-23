#!/usr/bin/env python3


import argparse
import logging
import sys


def main():
    """Demo of Python Logging module, see https://docs.python.org/3/howto/logging.html"""

    parser = argparse.ArgumentParser(prog="Demo")
    parser.add_argument(
        "--log_level",
        "-l",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    logging.basicConfig(
        stream=sys.stdout,
        level=getattr(logging, parser.parse_args().log_level, None))

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


if __name__ == "__main__":
    main()
