import argparse
import logging
import sys
import timeit

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


class ApplicationController(object):
    """Application arguments and logging setup"""

    def __init__(self):
        self._application_start_time = timeit.default_timer()
        self._set_arguments()
        self._set_logging()

    def _set_arguments(self):
        self._argument_parser = argparse.ArgumentParser()
        self._argument_parser.add_argument(
            "--log_level", default="WARNING", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        )
        self._argument_parser.add_argument("--config", required=True)
        self._argument_parser.add_argument("--generate", action="store_true")

    def _set_logging(self):
        log_level = self._argument_parser.parse_args().log_level
        logging.basicConfig(stream=sys.stdout, level=log_level, format=DEFAULT_LOG_FORMAT)

    def get_runtime(self):
        application_stop_time = timeit.default_timer()
        return application_stop_time - self._application_start_time

    def get_configuration_file(self):
        return self._argument_parser.parse_args().config

    def is_new_configuration_requested(self):
        return self._argument_parser.parse_args().generate


if __name__ == "__main__":
    pass
