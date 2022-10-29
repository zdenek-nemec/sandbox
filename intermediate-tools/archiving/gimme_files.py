import argparse
import logging
import os
import sys

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget


def get_datetime(timestamp):
    if timestamp is None or not str(timestamp).isdigit():
        raise ValueError("Timestamp {0} is invalid".format(timestamp))
    return None


def main():
    print("Intermediate Tools - Archiving: Gimme Files")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")

    logging.info("Parsing the arguments")
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--stream")
    argument_parser.add_argument("--data_from")
    argument_parser.add_argument("--data_to")
    argument_parser.add_argument("--save_to")
    stream = argument_parser.parse_args().stream
    data_from = argument_parser.parse_args().data_from
    data_to = argument_parser.parse_args().data_to
    save_to = argument_parser.parse_args().save_to
    logging.debug("stream = {0}".format(stream))
    logging.debug("data_from = {0}".format(data_from))
    logging.debug("data_to = {0}".format(data_to))
    logging.debug("save_to = {0}".format(save_to))
    logging.debug("save_to = {0}".format(save_to))

    archive_paths = ArchivePaths()
    logging.debug("archive_paths.is_test() = {0}".format(archive_paths.is_test()))
    logging.info("{0} run".format("Live" if not archive_paths.is_test() else "Test"))

    logging.info("Validating TAR path")
    tar_path = archive_paths.get_path(ArchiveTarget.PATH_TAR)
    logging.debug("tar_path = {0}".format(tar_path))
    archive_paths.validate(tar_path)

    logging.info("Validating times from and to")

    data_from_datetime = get_datetime(data_from)
    data_to_datetime = get_datetime(data_to)

    logging.info("Validating save-to path")
    save_to_path = save_to if save_to is not None else os.getcwd()
    logging.debug("save_to_path = {0}".format(save_to_path))
    archive_paths.validate(save_to_path)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
