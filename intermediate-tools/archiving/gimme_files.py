import argparse
import logging
import sys


def main():
    print("Intermediate Tools - Archiving: Gimme Files")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Parsing the arguments")
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--stream")
    argument_parser.add_argument("--data_from")
    argument_parser.add_argument("--data_to")
    argument_parser.add_argument("--save_to")
    argument_parser.add_argument("--keep_tar", action="store_true")
    stream = argument_parser.parse_args().stream
    data_from = argument_parser.parse_args().data_from
    data_to = argument_parser.parse_args().data_to
    save_to = argument_parser.parse_args().save_to
    keep_tar = argument_parser.parse_args().keep_tar
    logging.debug("stream = {0}".format(stream))
    logging.debug("data_from = {0}".format(data_from))
    logging.debug("data_to = {0}".format(data_to))
    logging.debug("save_to = {0}".format(save_to))
    logging.debug("keep_tar = {0}".format(keep_tar))


if __name__ == "__main__":
    main()
