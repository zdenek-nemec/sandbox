import argparse
import logging
import os
import shutil
import socket
import sys
import tarfile
from datetime import datetime

MEDIATION_ARCHIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/tests/target1_mediation",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"
}
TAR_ARCHIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/tests/target2_tar",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"
}
NAS_ARCHIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/tests/target3_nas",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"
}
OPS_ARCHIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/tests/target4_ops",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
}
MEDIATION_ARCHIVE_LIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/mediation_archive",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation"
}
TAR_ARCHIVE_LIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/tar_archive",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar"
}
NAS_ARCHIVE_LIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/nas_archive",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas"
}
OPS_ARCHIVE_LIVE = {
    "avl4658t": "/appl/dcs/data01/tmp/OC-12871/ops_archive",
    "JISKRA": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops",
    "N007510": "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
}


def main():
    print("Intermediate Tools - Archiving")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Checking the options")
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--live", action='store_true')
    if argument_parser.parse_args().live:
        logging.info("Running live")
        mediation_archive = MEDIATION_ARCHIVE_LIVE
        tar_archive = TAR_ARCHIVE_LIVE
        nas_archive = NAS_ARCHIVE_LIVE
        ops_archive = OPS_ARCHIVE_LIVE
    else:
        logging.info("Running test")
        mediation_archive = MEDIATION_ARCHIVE
        tar_archive = TAR_ARCHIVE
        nas_archive = NAS_ARCHIVE
        ops_archive = OPS_ARCHIVE

    logging.info("Checking the host")
    logging.debug("socket.gethostname() = {0}".format(socket.gethostname()))
    assert socket.gethostname() in mediation_archive.keys()

    mediation_archive_path = os.path.normpath(mediation_archive[socket.gethostname()])
    logging.info("Scanning Mediation archive {0}".format(mediation_archive_path))
    logging.debug("os.listdir({1}) = {0}".format(os.listdir(mediation_archive_path), mediation_archive_path))
    content = [os.path.normpath(mediation_archive_path + "/" + item) for item in os.listdir(mediation_archive_path)]
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
        # Check filename
        if (len(filename) <= 18  # YYYYmmdd_HHMMSS___
                or filename[8] != "_"
                or filename[15:18] != "___"):
            logging.debug("Skipping invalid filename {0}".format(item))
            continue
        if (file_hour == current_hour):
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
        stream = stream_key[len(mediation_archive_path) + 1:].replace("\\", "-").replace("/", "-")
        logging.debug(stream)
        for hour_key in files_to_archive[stream_key]:
            tar_file_path = os.path.normpath(tar_archive[socket.gethostname()] + "/" + stream + "-" + hour_key + ".tar")
            logging.debug(tar_file_path)
            tar = tarfile.open(tar_file_path, "w")
            os.chdir(stream_key)
            for filename in files_to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(filename)
                tar.add(path_to_file)
            tar.close()

            logging.debug("Deleting archived files")
            for filename in files_to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(stream_key + "/" + filename)
                os.remove(path_to_file)

    logging.info("Distributing TAR files")
    os.chdir(tar_archive[socket.gethostname()])
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    logging.debug("os.listdir() first 10 = {0}".format(os.listdir()[0:10]))
    tar_directory_content = os.listdir()
    nas_directories = list(filter(lambda item: os.path.isdir(nas_archive[socket.gethostname()] + "/" + item),
                                  [item for item in os.listdir(nas_archive[socket.gethostname()])]))
    ops_directories = list(filter(lambda item: os.path.isdir(ops_archive[socket.gethostname()] + "/" + item),
                                  [item for item in os.listdir(ops_archive[socket.gethostname()])]))
    for tar_file in tar_directory_content:
        main_directory = tar_file.split("-")[0]
        if main_directory not in nas_directories:
            os.mkdir(nas_archive[socket.gethostname()] + "/" + main_directory)
            nas_directories.append(main_directory)
        if main_directory not in ops_directories:
            os.mkdir(ops_archive[socket.gethostname()] + "/" + main_directory)
            ops_directories.append(main_directory)
        shutil.copyfile(tar_file, nas_archive[socket.gethostname()] + "/" + main_directory + "/" + tar_file)
        shutil.move(tar_file, ops_archive[socket.gethostname()] + "/" + main_directory)
    print("Finished")


if __name__ == "__main__":
    main()
