import argparse
import logging
import os
import re
import shutil
import sys
import tarfile
from datetime import datetime, timedelta

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget


def get_datetime(timestamp):
    if not type(timestamp) is str:
        raise ValueError("Timestamp {0} is invalid".format(timestamp))
    elif len(timestamp) == 8 and str(timestamp).isdigit():
        return datetime.strptime(timestamp, "%Y%m%d")
    elif len(timestamp) == 15 and str(timestamp[0:8]).isdigit() and timestamp[8] == "_" and str(
            timestamp[9:15]).isdigit():
        return datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
    return None


def get_focus_hours(hour_from, hour_to):
    selected = []
    current_hour = hour_from
    while True:
        selected.append(current_hour.strftime("%Y%m%d_%H"))
        current_hour += timedelta(hours=1)
        if current_hour > hour_to:
            selected.append(current_hour.strftime("%Y%m%d_%H"))
            break
    return selected


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
    argument_parser.add_argument("--save_to", default=os.getcwd())
    stream = argument_parser.parse_args().stream
    data_from = argument_parser.parse_args().data_from
    data_to = argument_parser.parse_args().data_to
    save_to = os.path.normpath(argument_parser.parse_args().save_to)
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

    # Get time period
    data_from_datetime = get_datetime(data_from)
    data_to_datetime = get_datetime(data_to)
    print(data_from_datetime)
    print(data_to_datetime)
    if data_from_datetime > data_to_datetime:
        raise ValueError("Value of data-from cannot be bigger than data-to")
    focus_hours = get_focus_hours(data_from_datetime, data_to_datetime)
    print(focus_hours)

    # Get month directory
    month_directories = []
    for focus_hour in focus_hours:
        month = focus_hour[0:6]
        if month not in month_directories:
            month_directories.append(month)
    print(month_directories)

    # Get stream directory
    stream_directory = stream.split("-")[0]
    print(stream_directory)

    # Validate save-to
    archive_paths.validate(save_to)
    print(save_to)

    # TODO: Prevent going before 2022-09 (deployment of archive.py)
    for month_directory in month_directories:
        selected_files = []
        target_directory_path = os.path.normpath(tar_path + "/" + month_directory + "/" + stream_directory)
        content = os.listdir(target_directory_path)
        for item in content:
            for hour in focus_hours:
                if re.search(stream + ".*" + hour + ".*.tar", item):
                    selected_files.append(item)
        for filename in selected_files:
            shutil.copyfile(target_directory_path + "/" + filename, save_to + "/" + filename)

    # Extract
    os.chdir(save_to)
    content = os.listdir()
    sample_filename = None
    for item in content:
        if item[-4:] == ".tar":
            with tarfile.open(item) as tar_file:
                tar_file.extractall(".")
                if sample_filename is None:
                    sample_filename = tar_file.getnames()[0]

    search_result = sample_filename.find(stream_directory)
    if search_result > 0:
        save_to_absolute_path = os.getcwd()
        os.chdir(sample_filename[0:search_result])
        shutil.move(stream_directory, save_to_absolute_path)
        os.chdir(save_to_absolute_path)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
