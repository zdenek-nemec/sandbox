import argparse
import logging
import os
import re
import shutil
import socket
import sys
import tarfile
from datetime import datetime, timedelta

MEDIATION_SERVERS = ["avl4713p", "avl4715p"]
TAR_ARCHIVE_PATH_MEDIATION = "/appl/mediation/med_backup"
TAR_ARCHIVE_PATH_LOCAL = "./tests/tar_archives"
OLDEST_ARCHIVE = "2022-09-01"


def get_stream(value):
    if value is None:
        raise ValueError("Invalid stream")
    else:
        return value


def get_datetime(timestamp):
    if not type(timestamp) is str:
        raise ValueError("Invalid timestamp {0}".format(timestamp))
    elif len(timestamp) == 8 and str(timestamp).isdigit():
        return datetime.strptime(timestamp, "%Y%m%d")
    elif len(timestamp) == 15 and str(timestamp[0:8]).isdigit() and timestamp[8] == "_" and str(
            timestamp[9:15]).isdigit():
        return datetime.strptime(timestamp, "%Y%m%d_%H%M%S")
    else:
        return None


def get_path(path):
    normalised = os.path.abspath(path)
    if os.path.isdir(normalised):
        return normalised
    else:
        raise ValueError("Invalid path {0}".format(path))


def parse_arguments():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--stream")
    argument_parser.add_argument("--period_from", "--from")
    argument_parser.add_argument("--period_to", "--to")
    argument_parser.add_argument("--save_to", default=os.getcwd())
    argument_parser.add_argument("--no_extract", default=False, action='store_true')
    argument_parser.add_argument("--no_prompt", default=False, action='store_true')
    argument_parser.add_argument("--test_run", default=False, action='store_true')

    stream = get_stream(argument_parser.parse_args().stream)
    period_from = get_datetime(argument_parser.parse_args().period_from)
    period_to = get_datetime(argument_parser.parse_args().period_to)
    save_to = get_path(argument_parser.parse_args().save_to)
    no_extract = argument_parser.parse_args().no_extract
    no_prompt = argument_parser.parse_args().no_prompt
    test_run = argument_parser.parse_args().test_run

    if period_from > period_to:
        raise ValueError("Invalid period from {0} to {1}".format(period_from, period_to))
    if period_from < datetime.strptime(OLDEST_ARCHIVE, "%Y-%m-%d"):
        raise ValueError("Data restoration before {0} is not supported".format(OLDEST_ARCHIVE))

    logging.debug("stream = {0}".format(stream))
    logging.debug("period_from = {0}".format(period_from))
    logging.debug("period_to = {0}".format(period_to))
    logging.debug("save_to = {0}".format(save_to))
    logging.debug("no_extract = {0}".format(no_extract))
    logging.debug("no_prompt = {0}".format(no_prompt))
    logging.debug("test_run = {0}".format(test_run))

    return stream, period_from, period_to, save_to, no_extract, no_prompt, test_run


def get_tar_archive_path(test_run):
    if test_run:
        return get_path(TAR_ARCHIVE_PATH_LOCAL)
    elif socket.gethostname() in MEDIATION_SERVERS:
        return get_path(TAR_ARCHIVE_PATH_MEDIATION)
    else:
        return get_path(TAR_ARCHIVE_PATH_LOCAL)


def get_focus_hours(period_from, period_to):
    selected = []
    hour = period_from
    while True:
        selected.append(hour.strftime("%Y%m%d_%H"))
        hour += timedelta(hours=1)
        if hour >= period_to:
            selected.append(hour.strftime("%Y%m%d_%H"))
            break
    return selected


def get_month_directories(hours):
    month_directories = []
    for hour in hours:
        month = hour[0:6]
        if month not in month_directories:
            month_directories.append(month)
    return month_directories


def get_stream_directory(stream):
    return stream.split("-")[0]


def main():
    print("Intermediate Tools - Archiving: Extract")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")

    logging.info("Parsing the arguments")
    stream, period_from, period_to, save_to, no_extract, no_prompt, test_run = parse_arguments()

    logging.info("Validating TAR archive path")
    tar_archive_path = get_tar_archive_path(test_run)
    logging.debug("tar_archive_path = {0}".format(tar_archive_path))

    logging.info("Identifying the time period and stream to restore")
    focus_hours = get_focus_hours(period_from, period_to)
    month_directories = get_month_directories(focus_hours)
    stream_directory = get_stream_directory(stream)
    logging.debug("focus_hours = {0}".format(focus_hours))
    logging.debug("month_directories = {0}".format(month_directories))
    logging.debug("stream_directory = {0}".format(stream_directory))

    logging.info("Retrieving TAR files from the TAR archive")
    for month_directory in month_directories:
        selected_files = []
        target_directory_path = os.path.normpath(tar_archive_path + "/" + month_directory + "/" + stream_directory)
        logging.info("Scanning {0}".format(target_directory_path))
        content = os.listdir(target_directory_path)
        for item in content:
            for hour in focus_hours:
                if re.search(stream + ".*" + hour + ".*.tar", item):
                    selected_files.append(item)
        logging.info("Found {0} TAR files".format(len(selected_files)))
        [print(item) for item in selected_files]
        if no_prompt:
            pass
        elif input("Do you want to continue? (Y/n) ") != "Y":
            logging.info("Restore aborted")
            return
        for filename in selected_files:
            shutil.copyfile(target_directory_path + "/" + filename, save_to + "/" + filename)

    if no_extract:
        logging.info("Not extracting")
    else:
        logging.info("Extracting")
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
            extracted_path = os.path.abspath(sample_filename[0:search_result])
            os.chdir(extracted_path)
            shutil.move(stream_directory, save_to)
            while True:
                current_path = os.path.abspath(os.getcwd())
                if (current_path.find(save_to) != 0
                        or len(current_path) < len(save_to)
                        or len(os.listdir(current_path)) != 0):
                    break
                os.chdir("..")
                os.rmdir(current_path)
            os.chdir(save_to)

    logging.info("Application finished")


if __name__ == "__main__":
    main()
