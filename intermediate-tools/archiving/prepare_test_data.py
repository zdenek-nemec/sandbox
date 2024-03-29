import logging
import os
import random
import shutil
import string
import sys
from datetime import datetime, timedelta

VALID_WORKING_DIRECTORIES = ["archiving", "Archiving"]
MAIN_DIRECTORY_STRUCTURE = [
    "tests",
    "tests/mediation",
    "tests/temp",
    "tests/archive_logs",
    "tests/originals",
    "tests/tar_archives",
]
DATA_DIRECTORY_STRUCTURE = [
    "BlackMed",
    "BlackMed/PRTG",
    "BlackMed/PRTG/in",
    "BlackMed/PRTG/out",
    "BlackMed/SmartSim",
    "BlackMed/TechSplit",
    "BlackMed_old_Nokia_invoices",
    "BlackMed_old_Nokia_Reports",
    "lost+found",
    "lost+found/Subdirectory",
    "I_ICS",
    "I_ICS/CG01_ECSCF",
    "I_ICS/CG01_IPSM",
    "I_ICS/CG01_MGCF",
    "I_ICS/CG01_SCSCF_UC",
    "I_ICS/CG01_SSS",
    "I_ICS/CG01_SSS_UC",
    "I_ICS/CG02_ECSCF",
    "I_ICS/CG02_IPSM",
    "I_ICS/CG02_MGCF",
    "I_ICS/CG02_SCSCF_UC",
    "I_ICS/CG02_SSS",
    "I_ICS/CG02_SSS_UC",
    "I_MSC4",
    "I_MSC4/FLO_02",
    "I_MSC4/FLO_UC",
    "I_MSC4/VIE_01",
    "I_MSC4/VIE_UC",
    "I_VTAS",
    "I_VTAS/VTAS1_0001",
    "I_VTAS/VTAS1_0002",
    "I_VTAS/VTAS2_0001",
    "I_VTAS/VTAS2_0002"
]
FILENAME_LENGTH = 20
ARCHIVE_PREFIXES = {
    "20220801_000000": 1,
    "20220801_005959": 1,
    "20220801_015900": 1,
    "20220801_021500": 15,
    "20220801_030300": 3,
    "20220802_000000": 2,
    "20220802_005959": 2,
    "20220802_015900": 2,
    "20220901_040300": 5,
    "20220901_050300": 5,
    "20220901_050301": 5,
    "20220901_050302": 5,
    "20220901_060300": 5
}


def get_random_filename():
    random_string = "".join(random.choice(string.ascii_lowercase + string.digits + " ") for _ in range(FILENAME_LENGTH))
    return "Filename_" + random_string + ".txt"


def write_file(path):
    with open(path, "w") as text_file:
        text_file.write("Ahoj\n")


def main():
    print("Intermediate Tools - Archiving: Prepare Test Data")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")

    logging.info("Checking the working directory")
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    assert os.path.basename(os.getcwd()) in VALID_WORKING_DIRECTORIES

    logging.info("Cleaning up \"{0}\" directory".format(MAIN_DIRECTORY_STRUCTURE[0]))
    logging.debug("os.listdir() = {0}".format(os.listdir()))
    if "tests" in os.listdir():
        shutil.rmtree("./tests")
    logging.debug("os.listdir() = {0}".format(os.listdir()))

    logging.info("Creating main \"{0}\" directory structure".format(MAIN_DIRECTORY_STRUCTURE[0]))
    current_path = os.getcwd()
    for directory in MAIN_DIRECTORY_STRUCTURE:
        os.mkdir(current_path + "/" + directory)
    logging.debug("os.listdir() = {0}".format(os.listdir()))
    logging.debug("os.listdir(\"{0}\") = {1}".format(
        MAIN_DIRECTORY_STRUCTURE[0],
        os.listdir(MAIN_DIRECTORY_STRUCTURE[0])
    ))

    logging.info("Creating \"{0}\" data directory structure in {1}".format(
        MAIN_DIRECTORY_STRUCTURE[0],
        MAIN_DIRECTORY_STRUCTURE[1]
    ))
    os.chdir(MAIN_DIRECTORY_STRUCTURE[1])
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    logging.debug("os.listdir() = {0}".format(os.listdir()))
    for directory in DATA_DIRECTORY_STRUCTURE:
        os.mkdir(directory)
    logging.debug("os.listdir() = {0}".format(os.listdir()))

    logging.info("Creating \"{0}\" data in {1}".format(
        MAIN_DIRECTORY_STRUCTURE[0],
        MAIN_DIRECTORY_STRUCTURE[1]
    ))
    current_path = os.getcwd()
    write_file(current_path + "/" + get_random_filename())
    for _ in range(3):
        write_file(current_path + "/" + random.choice(list(ARCHIVE_PREFIXES.keys())) + "___" + get_random_filename())
    archive_prefixes = {**ARCHIVE_PREFIXES, **{
        (datetime.now() - timedelta(hours=2)).strftime("%Y%m%d_%H%M%S"): 3,
        (datetime.now() - timedelta(hours=1)).strftime("%Y%m%d_%H%M%S"): 3,
        datetime.now().strftime("%Y%m%d_%H%M%S"): 3,
        (datetime.now() + timedelta(hours=1)).strftime("%Y%m%d_%H%M%S"): 3
    }}
    for prefix in archive_prefixes.keys():
        for path in DATA_DIRECTORY_STRUCTURE:
            for i in range(archive_prefixes[prefix]):
                write_file(current_path + "/" + path + "/" + prefix + "___" + get_random_filename())

    logging.info("Application finished")


if __name__ == "__main__":
    main()
