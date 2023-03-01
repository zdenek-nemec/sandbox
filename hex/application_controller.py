import argparse
import logging
import sys


class ApplicationController(object):
    """Application arguments and logging setup"""

    def __init__(self):
        self._set_arguments()
        self._set_logging()

    def _set_arguments(self):
        self._argument_parser = argparse.ArgumentParser()
        self._argument_parser.add_argument(
            "--log_level", default="WARNING", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        )

    def _set_logging(self):
        log_level = self._argument_parser.parse_args().log_level
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)


if __name__ == "__main__":
    pass
