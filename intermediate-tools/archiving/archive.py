import argparse
import logging
import os
import shutil
import sys
import tarfile
from datetime import datetime
from pathlib import Path

from archive_paths import ArchivePaths
from archive_target import ArchiveTarget

EXCLUDE = ["ARCHIVE_STORAGE", "Ignored", "lost+found", "202111", "202203", "202204", "202207"]

def main():
    print("Intermediate Tools - Archiving: Archive")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Parsing the arguments")
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--live", action="store_true")

    archive_paths = ArchivePaths(argument_parser.parse_args().live)
    logging.debug("archive_paths.is_live() = {0}".format(archive_paths.is_live()))
    logging.info("{0} run".format("Live" if archive_paths.is_live() else "Test"))

    logging.info("Validating the host")
    if archive_paths.is_host_valid():
        logging.info("Host {0} is valid".format(archive_paths.get_host()))
    else:
        raise ValueError("Unknown host {0}".format(archive_paths.get_host()))

    med_archive_path = archive_paths.get_path(ArchiveTarget.MED_PATH)
    tar_archive_path = archive_paths.get_path(ArchiveTarget.TAR_PATH)
    nas_archive_path = archive_paths.get_path(ArchiveTarget.NAS_PATH)
    ops_archive_path = archive_paths.get_path(ArchiveTarget.OPS_PATH)
    log_archive_path = archive_paths.get_path(ArchiveTarget.LOG_PATH)

    logging.info("Scanning Mediation archive {0}".format(med_archive_path))
    logging.debug("os.listdir({1}) = {0}".format(os.listdir(med_archive_path), med_archive_path))
    content = [os.path.normpath(med_archive_path + "/" + item) for item in filter(
        lambda x: x not in EXCLUDE, os.listdir(med_archive_path)
    )]

    logging.debug("content first item = {0}".format(content[0]))
    logging.debug("content length = {0}".format(len(content)))
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
    logging.debug("directories first item = {0}".format(directories[0]))
    logging.debug("directories length = {0}".format(len(directories)))
    logging.debug("directories basenames = {0}".format([os.path.basename(item) for item in directories]))
    logging.debug("files first item = {0}".format(files[0]))
    logging.debug("files second item = {0}".format(files[1]))
    logging.debug("files length = {0}".format(len(files)))
    logging.debug("files first 10 basenames = {0}".format([os.path.basename(item) for item in files[0:10]]))

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
        stream = stream_key[len(med_archive_path) + 1:].replace("\\", "-").replace("/", "-")
        logging.debug(stream)
        for hour_key in files_to_archive[stream_key]:
            tar_file_path = os.path.normpath(tar_archive_path + "/" + stream + "-" + str(hour_key) + ".tar")
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
            ops_stream_archive_path = os.path.normpath(ops_archive_path + "/" + stream_key[len(med_archive_path) + 1:])
            log_stream_archive_path = os.path.normpath(log_archive_path + "/" + stream_key[len(med_archive_path) + 1:])
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
    os.chdir(tar_archive_path)
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    logging.debug("os.listdir() first 10 = {0}".format(os.listdir()[0:10]))
    tar_directory_content = os.listdir()
    nas_directories = list(filter(
        lambda item: os.path.isdir(nas_archive_path + "/" + item),
        [item for item in os.listdir(nas_archive_path)]
    ))
    for tar_file in tar_directory_content:
        main_directory = tar_file.split("-")[0]
        if main_directory not in nas_directories:
            os.mkdir(nas_archive_path + "/" + main_directory)
            nas_directories.append(main_directory)
        shutil.move(tar_file, nas_archive_path + "/" + main_directory)
    print("Finished")


if __name__ == "__main__":
    main()
