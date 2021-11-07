#!/usr/bin/env python3


import argparse
import logging
import os
import sys
import zipfile


class Validator(object):
    def __init__(self, path, filename):
        logging.debug("Validating")
        self._target = self._get_target(path, filename)

    @staticmethod
    def _get_target(path, filename):
        if type(path) != str or type(filename) != str:
            logging.error("Invalid target of validation, aborting")
            exit(-1)
        logging.debug("Path: %s" % path)
        logging.debug("Filename: %s" % filename)
        return path + "/" + filename

    def _is_file(self):
        return os.path.isfile(self._target)

    def _is_zip(self):
        if not(zipfile.is_zipfile(self._target)):
            logging.warning("Target file %s is not ZIP" % self._target)
            return False

        with zipfile.ZipFile(self._target) as zip_file:
            if len(zip_file.infolist()) != 1:
                logging.warning("Zero or multiple files in ZIP file %s" % self._target)
                return False

            if zip_file.testzip() != None:
                logging.error("CRC does not match in ZIP file %s" % self._target)
                return False

            with zip_file.open(zip_file.infolist()[0].filename) as ewsd_file:
                content = ewsd_file.read()
                if len(content) != zip_file.infolist()[0].file_size:
                    logging.warning("File size does not match in ZIP file %s" % self._target)
                    return False
        return True

    def _is_ewsd(self):
        with zipfile.ZipFile(self._target) as zip_file:
            if len(zip_file.infolist()) != 1:
                logging.warning("Zero or multiple files in ZIP file %s" % self._target)
                return False
            if zip_file.testzip() != None:
                logging.error("CRC does not match in ZIP file %s" % self._target)
                return False
            with zip_file.open(zip_file.infolist()[0].filename) as ewsd_file:
                content = ewsd_file.read()
                if len(content) != zip_file.infolist()[0].file_size:
                    logging.warning("File size does not match in ZIP file %s" % self._target)
                    return False
                i = 0
                records = 0
                while True:
                    if i >= len(content):
                        break
                    tag = content[i]
                    if tag == 0x84:  # Data record
                        records += 1
                        length = content[i+1]
                        i += length
                    elif tag == 0x80:  # Filler byte
                        i += 1
                    elif tag == 0x81:  # Filler record
                        length = content[i+1]
                        i += length
                    elif tag == 0x00:
                        i += 32
                    else:
                        return False
        return True

    def test(self, check_file=False, check_zip=False, check_ewsd=False):
        if check_file and not(self._is_file()):
            logging.warning("Target file %s does not exist" % self._target)
            return False

        if check_zip and not(self._is_zip()):
            logging.warning("Target file %s is not a valid ZIP file" % self._target)
            return False

        if check_ewsd and not(self._is_ewsd()):
            logging.warning("Target file %s is not valid" % self._target)
            return False

        return True


def main():
    parser = argparse.ArgumentParser(prog="Fast File Transfer Validator")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--log_file", "-f")
    parser.add_argument("--log_level", "-l", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.add_argument("--skip_ewsd_check", "-e", action="store_true")

    log_level = getattr(logging, parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    if parser.parse_args().log_file is None:
        logging.basicConfig(
            stream=sys.stdout,
            level=log_level,
            format=log_format)
    else:
        logging.basicConfig(
            filename=parser.parse_args().log_file,
            level=log_level,
            format=log_format)

    logging.info("Fast File Transfer Validator started")

    logging.debug("Argument --input = %s" % parser.parse_args().input)
    logging.debug("Argument --log_file = %s" % parser.parse_args().log_file)
    logging.debug("Argument --log_level = %s" % parser.parse_args().log_level)
    logging.debug("Argument --skip_ewsd_check = %s"
        % parser.parse_args().skip_ewsd_check)

    input_file = parser.parse_args().input
    filename = os.path.basename(input_file)
    path = os.path.normcase(os.path.dirname(input_file) + "/")
    ewsd_check = not parser.parse_args().skip_ewsd_check
    validator = Validator(filename=filename, path=path)
    if validator.test(check_file=True, check_zip=True, check_ewsd=ewsd_check):
        logging.info("The file %s is valid" % filename)
    else:
        logging.warning("The file %s is corrupted" % filename)

    logging.info("Fast File Transfer Validator started")


if __name__ == "__main__":
    main()
