import argparse
import csv
import logging
import os
import sys

STATS_PATH = "c:\\Zdenek\\_tmp\\U-A4A1-14181_Service_Desk_FMS_RA\\intermediate_stats"


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--log_level", default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    log_level = argument_parser.parse_args().log_level
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.debug("Application started")
    logging.info("Intermediate Tools - Analyse Stats")

    stats_path = STATS_PATH
    if not os.path.isdir(stats_path):
        raise OSError("Path {0} does not exist".format(stats_path))

    items = os.listdir(stats_path)
    logging.debug("items: {0}".format(len(items)))
    files = list(filter(lambda item: os.path.isfile(stats_path + "/" + item) and item[-6:] == ".stats", items))
    logging.debug("stats files: {0}".format(len(files)))

    report = {}
    header = []
    for filename in files:
        with open(stats_path + "/" + filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            file_stats = {}
            for row in reader:
                name = row[0]
                selected = int(row[1])
                filtered = int(row[2])
                generated = int(row[3])
                held = int(row[4])
                if name not in header:
                    header.append(name)
                if name in file_stats:
                    raise ValueError("Key {0} exists already for the file {1}".format(name, filename))
                if name == "085-PGW":
                    if filtered > 0 or generated > 0 or held > 0:
                        raise ValueError("File {0} has some weird stats".format(filename))
                    file_stats[name] = selected
                else:
                    if selected > 0:
                        raise ValueError("File {0} has some weird filter stats".format(filename))
                    file_stats[name] = filtered
        report[filename] = file_stats

    # [print(report[key]) for key in report.keys()]

    print("Filename,{0}".format(",".join(header)))
    for key in report.keys():
        print("{0},".format(key[:-11]), end="")
        for header_item in header:
            try:
                print("{0},".format(report[key][header_item]), end="")
            except KeyError:
                print("0,", end="")
        print("")
        # for header_item in header



if __name__ == "__main__":
    main()
