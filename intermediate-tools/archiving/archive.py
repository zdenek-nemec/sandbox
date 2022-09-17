import argparse
import logging
import os
import shutil
import sys
import tarfile
from datetime import datetime
from pathlib import Path

from application_lock import ApplicationLock
from archive_paths import ArchivePaths
from archive_target import ArchiveTarget

APPLICATION_PORT = 12345
EXCLUDE = [
    "ARCHIVE_STORAGE", "lost+found",
    "202111", "202203", "202204", "202205", "202206", "202207", "202208", "202209"
]


def get_directories(path, exclusions):
    if not os.path.isdir(path):
        raise OSError("Path {0} does not exist".format(path))

    directories = [path]
    content = [os.path.normpath(path + "/" + item) for item in filter(
        lambda x: x not in exclusions, os.listdir(path)
    )]
    for current_path in content:
        if os.path.isdir(current_path):
            directories.append(current_path)
            content += [os.path.normpath(current_path + "/" + item) for item in os.listdir(current_path)]
    return directories


def main():
    print("Intermediate Tools - Archiving: Archive")

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    argument_parser.add_argument("--live", action="store_true")

    log_level = argument_parser.parse_args().log_level
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")

    logging.debug("Arguments: log_level = {0}, live = {1}".format(
        argument_parser.parse_args().log_level,
        argument_parser.parse_args().live
    ))

    logging.info("Locking to a single instance")
    application_lock = ApplicationLock(APPLICATION_PORT)

    archive_paths = ArchivePaths(argument_parser.parse_args().live)
    logging.debug("archive_paths.is_test() = {0}".format(archive_paths.is_test()))
    logging.info("{0} run".format("Live" if not archive_paths.is_test() else "Test"))

    logging.info("Validating paths")
    mediation_path = archive_paths.get_path(ArchiveTarget.PATH_MEDIATION)
    temporary_path = archive_paths.get_path(ArchiveTarget.PATH_TEMPORARY)
    logs_path = archive_paths.get_path(ArchiveTarget.PATH_LOGS)
    originals_path = archive_paths.get_path(ArchiveTarget.PATH_ORIGINALS)
    tar_path = archive_paths.get_path(ArchiveTarget.PATH_TAR)
    for path in [mediation_path, temporary_path, logs_path, originals_path, tar_path]:
        archive_paths.validate(path)

    logging.info("Scanning Mediation archive {0} for directories".format(mediation_path))
    mediation_directories = get_directories(mediation_path, EXCLUDE)

    logging.info("Scanning Mediation archive {0}".format(mediation_path))
    logging.debug("os.listdir({1}) = {0}".format(os.listdir(mediation_path), mediation_path))
    content = [os.path.normpath(mediation_path + "/" + item) for item in filter(
        lambda x: x not in EXCLUDE, os.listdir(mediation_path)
    )]
    logging.debug("content length = {0}".format(len(content)))
    logging.debug("content first items = {0}".format(content[0:3]))
    logging.debug("content basenames = {0}".format([os.path.basename(item) for item in content]))
    directories = []
    files = []
    for current_path in content:
        if os.path.isdir(current_path):
            directories.append(current_path)
            content += [os.path.normpath(current_path + "/" + item) for item in os.listdir(current_path)]
        elif os.path.isfile(current_path):
            files.append(current_path)
        else:
            logging.error("Item is neither a file nor directory")
    logging.debug("directories length = {0}".format(len(directories)))
    logging.debug("directories first items = {0}".format(directories[0:3]))
    logging.debug("directories basenames = {0}".format([os.path.basename(item) for item in directories]))
    logging.debug("files length = {0}".format(len(files)))
    logging.debug("files first items = {0}".format(files[0:3]))
    logging.debug("files first basenames = {0}".format([os.path.basename(item) for item in files[0:3]]))

    logging.info("Getting the list of files to archive")
    current_hour = datetime.now().strftime("%Y%m%d_%H")
    logging.debug("current_hour = {0}".format(current_hour))
    files_to_archive = {}
    for item in files:
        directory_path = os.path.dirname(item)
        filename = os.path.basename(item)
        file_hour = filename[0:11]
        if (len(filename) <= 18  # YYYYmmdd_HHMMSS___
                or filename[8] != "_"
                or filename[15:18] != "___"):
            logging.debug("Skipping invalid filename {0}".format(item))
            continue
        if file_hour == current_hour:
            logging.debug("Skipping current hour {0}".format(item))
            continue
        if directory_path not in files_to_archive:
            files_to_archive[directory_path] = {file_hour: [filename]}
        else:
            if file_hour not in files_to_archive[directory_path]:
                files_to_archive[directory_path][file_hour] = [filename]
            else:
                files_to_archive[directory_path][file_hour].append(filename)
    logging.debug("files_to_archive length (streams/portals) = {0}".format(len(files_to_archive.keys())))

    logging.info("Creating TAR files")
    for stream_key in files_to_archive.keys():
        stream = stream_key[len(mediation_path) + 1:].replace("\\", "-").replace("/", "-")
        logging.debug(stream)
        for hour_key in files_to_archive[stream_key]:
            tar_file_path = os.path.normpath(temporary_path + "/" + stream + "-" + str(hour_key) + ".tar")
            logging.debug(tar_file_path)
            tar = tarfile.open(tar_file_path, "w")
            os.chdir(stream_key)
            tar_files = []
            for filename in files_to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(filename)
                tar.add(path_to_file)
                tar_files.append(filename)
            tar.close()

            logging.debug("Moving originals and creating the log")
            ops_stream_archive_path = os.path.normpath(originals_path + "/" + stream_key[len(mediation_path) + 1:])
            log_stream_archive_path = os.path.normpath(
                logs_path + "/" + str(hour_key[0:6]) + "/" + stream_key[len(mediation_path) + 1:])
            logging.debug("OPS archive = {0}".format(ops_stream_archive_path))
            logging.debug("LOG archive = {0}".format(log_stream_archive_path))
            if not os.path.isdir(ops_stream_archive_path):
                Path(ops_stream_archive_path).mkdir(parents=True, exist_ok=True)
            for filename in files_to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(stream_key + "/" + filename)
                shutil.move(path_to_file, ops_stream_archive_path)
            if not os.path.isdir(log_stream_archive_path):
                Path(log_stream_archive_path).mkdir(parents=True, exist_ok=True)
            log_file_path = os.path.normpath(
                str(log_stream_archive_path) + "/" + (os.path.basename(tar_file_path)).replace(".tar", ".log")
            )
            with open(log_file_path, "w") as text_file:
                for filename in tar_files:
                    text_file.write(filename + "\n")

    logging.info("Distributing TAR files")
    os.chdir(temporary_path)
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    logging.debug("os.listdir() first 10 = {0}".format(os.listdir()[0:10]))
    tar_directory_content = os.listdir()
    for tar_file in tar_directory_content:
        stream_directory = tar_file.split("-")[0]
        month_directory = tar_file.split("-")[-1][0:6]
        tar_file_directory_path = tar_path + "/" + month_directory + "/" + stream_directory
        if not os.path.isdir(tar_file_directory_path):
            Path(tar_file_directory_path).mkdir(parents=True, exist_ok=True)
        shutil.move(tar_file, tar_file_directory_path)

    application_lock.disable()
    print("Finished")


if __name__ == "__main__":
    main()
