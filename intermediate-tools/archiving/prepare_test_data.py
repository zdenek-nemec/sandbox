import logging
import os
import shutil
import sys

directory_structure = [
    "I_MSC",
    "I_MSC/INPUT_1",
    "I_MSC/INPUT_2",
    "I_MSC/INPUT_3",
    "I_ICS",
    "I_ICS/INPUT_1",
    "I_ICS/INPUT_2",
    "I_ICS/INPUT_3",
    "BM_stream1",
    "BM_stream2"
]


def get_random_filename():
    return "bla.txt"


def write_file(path):
    with open(path, "w") as text_file:
        text_file.write("Ahoj\n")


def main():
    print("Hello")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Checking working directory")
    logging.debug("os.getcwd() = {0}".format(os.getcwd()))
    assert os.getcwd() == "C:\\Zdenek\\Git\\GitHub\\sandbox\\intermediate-tools\\archiving"

    logging.info("Cleaning up \"tests\" directory")
    logging.debug("os.listdir() = {0}".format(os.listdir()))
    if "tests" in os.listdir():
        shutil.rmtree("./tests")
    logging.debug("os.listdir() = {0}".format(os.listdir()))

    logging.info("Creating \"tests\" directory structure")
    current_path = os.getcwd()
    os.mkdir(current_path + "/tests")
    for path in directory_structure:
        os.mkdir(current_path + "/tests/" + path)

    logging.info("Creating test data")
    write_file(current_path + "/tests/" + get_random_filename())
    for path in directory_structure:
        write_file(current_path + "/tests/" + path + "/" + get_random_filename());


if __name__ == "__main__":
    main()
