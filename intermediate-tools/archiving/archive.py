import logging
import os
import sys
from datetime import datetime

archive_path = os.path.normpath("c:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests")


def main():
    print("Hello")

    log_level = "DEBUG"
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
            print("Skipping", item)
            continue
        if directory not in to_archive:
            to_archive[directory] = {filename[0:11]: [filename]}
        else:
            if filename[0:11] not in to_archive[directory]:
                to_archive[directory][filename[0:11]] = [filename]
            else:
                to_archive[directory][filename[0:11]].append(filename)

    for key in to_archive.keys():
        print(key, to_archive[key])



if __name__ == "__main__":
    main()
