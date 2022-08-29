import logging
import os
import sys
import tarfile
from datetime import datetime

archive_path = os.path.normpath("C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation")
archive_output_path = os.path.normpath("C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar")


def main():
    print("Hello")

    log_level = "INFO"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    # logging.debug(os.listdir(archive_path))
    content = [os.path.normpath(archive_path + "/" + item) for item in os.listdir(archive_path)]
    directories = []
    files = []
    for current_path in content:
        if os.path.isdir(current_path):
            directories.append(current_path)
            content += [os.path.normpath(current_path + "/" + item) for item in os.listdir(current_path)]
        elif os.path.isfile(current_path):
            files.append(current_path)
        else:
            print("Error")
    # [print(item) for item in content]
    # [print(item) for item in files]

    current_hour = datetime.now().strftime("%Y%m%d_%H")
    to_archive = {}
    for item in files:
        directory = os.path.dirname(item)
        filename = os.path.basename(item)
        if (filename[0:4] != "2022"
                or filename[8] != "_"
                or filename[15:18] != "___"
                or filename[0:11] == current_hour):
            logging.debug("Skipping", item)
            continue
        if directory not in to_archive:
            to_archive[directory] = {filename[0:11]: [filename]}
        else:
            if filename[0:11] not in to_archive[directory]:
                to_archive[directory][filename[0:11]] = [filename]
            else:
                to_archive[directory][filename[0:11]].append(filename)

    for stream_key in to_archive.keys():
        # print(stream_key, to_archive[stream_key])
        stream = stream_key[len(archive_path) + 1:].replace("\\", "-").replace("/", "-")
        for hour_key in to_archive[stream_key]:
            tar_file_path = os.path.normpath(archive_output_path + "/" + stream + "-" + hour_key + ".tar")
            tar = tarfile.open(tar_file_path, "w")
            # Or w:gz if we want extra compression - Don't
            # TODO: Check if file already exists and handle exception
            os.chdir(stream_key)  # TODO: Or keep absolute path or keep path from main directory? - be flat
            for filename in to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(filename)
                tar.add(path_to_file)
            tar.close()  # TODO: Check exceptions!

            # Delete archived files
            for filename in to_archive[stream_key][hour_key]:
                path_to_file = os.path.normpath(stream_key + "/" + filename)
                os.remove(path_to_file)


# TODO: When all TAR files are created move them to a structure: month/stream (subdirs x 31 x 24)
# TODO: Check if target file already exists and handle
# TODO: When all TAR files are moved, rsync the structure to NAS - Don't rsync, write app

if __name__ == "__main__":
    main()
