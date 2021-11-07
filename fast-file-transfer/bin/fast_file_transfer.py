#!/usr/bin/env python3

import argparse
import logging
import multiprocessing
import shutil
import sys
import time

from collector import Collector
from config import Config
from exceptions import CannotBuildDataConnectionError
from exceptions import CorruptedFileError
from exceptions import SourceFileNotFoundError
from validator import Validator

DEFAULT_CONFIG_FILE = "default.cfg"
DEFAULT_COLLECTION_TIMEOUT = 900

collector = Collector()


def generate_new_config(filename):
    logging.debug("Initiated generate_new_config()")
    config = Config()
    config.generate(filename=filename)
    config.save()
    logging.debug("Finished generate_new_config()")


def collect_file(filename, path, config, ewsd_check):
    logging.debug("Initiated collect_file()")

    logging.debug("Parameter filename = %s" % filename)
    logging.debug("Parameter path = %s" % path)
    logging.debug("Parameter config = %s" % config)
    logging.debug("Parameter collector = %s" % collector)
    logging.debug("Parameter ewsd_check = %s" % ewsd_check)

    config.add_transfer(filename)
    config.save()
    download_path = config.get_download_path()

    logging.debug("Try Collector.download()")
    try:
        collector.download(
            filename=filename,
            source_path=path,
            destination_path=download_path)
    except SourceFileNotFoundError:
        logging.debug("Exception SourceFileNotFoundError")
        logging.warning("File %s not collected" % filename)
        config.remove_transfer(filename)
        config.save()
        logging.debug("Finished collect_file() - No file collected")
        return
    except CannotBuildDataConnectionError:
        logging.debug("Exception CannotBuildDataConnectionError")
        logging.error(
            "File %s not collected, aborting, download and release manually"
            % filename)
        raise
    except:
        logging.critical(
            "Unknown error - Collector.download() failed when downloading %s "
            "from %s to %s, aborting" % (filename, path, download_path))
        raise
    else:
        logging.debug("Success Collector.download()")

    validator = Validator(filename=filename, path=download_path)
    if validator.test(check_file=True, check_zip=True, check_ewsd=ewsd_check):
        logging.info("Collected file %s is valid" % filename)
        collector.delete(filename=filename, path=path)

        logging.debug("Try shutil.move()")
        try:
            result = shutil.move(
                download_path + "/" + filename,
                config.get_mediation_path() + "/" + filename)
            logging.debug("Result of shutil.move() = %s" % result)
        except:
            logging.critical(
                "Unknown error - shutil.move() failed for file %s, aborting, "
                "investigate and move file manually" % filename)
            raise
        else:
            logging.debug("Success shutil.move()")

        config.remove_transfer(filename)
        config.save()
    else:
        logging.error(
            "Collected file %s is corrupted, aborting, download and release "
            "manually" % filename)
        raise CorruptedFileError

    logging.debug("Finished collect_file()")


def main():
    parser = argparse.ArgumentParser(prog="Fast File Transfer")
    parser.add_argument("--config", "-c", default=DEFAULT_CONFIG_FILE)
    parser.add_argument("--generate", "-g", action="store_true")
    parser.add_argument("--log_file", "-f")
    parser.add_argument("--log_level", "-l", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.add_argument("--skip_site_commands", "-s", action="store_true")
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

    logging.info("Fast File Transfer application started")

    logging.debug("Argument --config = %s" % parser.parse_args().config)
    logging.debug("Argument --generate = %s" % parser.parse_args().generate)
    logging.debug("Argument --log_file = %s" % parser.parse_args().log_file)
    logging.debug("Argument --log_level = %s" % parser.parse_args().log_level)
    logging.debug("Argument --skip_site_commands = %s"
                  % parser.parse_args().skip_site_commands)
    logging.debug("Argument --skip_ewsd_check = %s"
                  % parser.parse_args().skip_ewsd_check)

    logging.info("Configuration: %s" % parser.parse_args().config)

    if parser.parse_args().generate:
        logging.info("Requested new configuration file")
        generate_new_config(filename=parser.parse_args().config)
        logging.info(
            "Fast File Transfer application finished - New configuration file "
            "generated")
        return

    logging.info("Loading configuration")
    config = Config()
    config.load(filename=parser.parse_args().config)

    logging.info("Establishing connection")
    use_site_commands = not parser.parse_args().skip_site_commands
    collector.connect(
        host=config.get_host(),
        username=config.get_username(),
        password=config.get_password(),
        use_site_commands=use_site_commands)

    ewsd_check = not parser.parse_args().skip_ewsd_check
    transfers = config.get_transfers()
    if transfers is None or transfers == []:
        logging.info("No active transfers")
    elif type(transfers) == list:
        logging.error(
            "Unfinished file transfers, aborting, download and release "
            "manually, review the configuration file %s"
            % config.get_config_filename())
        exit(-1)
    else:
        logging.error(
            "List of transfers corrupted, aborting, review the configuration "
            "file %s" % config.get_config_filename())
        exit(-1)

    logging.info("Collecting new file")
    new_filename = config.generate_new_filename()

    process = multiprocessing.Process(target=collect_file,
                                      args=(new_filename, config.get_ewsd_path(), config, ewsd_check))
    process.start()
    process.join(DEFAULT_COLLECTION_TIMEOUT)
    if process.is_alive():
        logging.error(
            "File %s not collected due to timeout, aborting, download and release manually"
            % new_filename)
        process.terminate()
        process.join()

    logging.info("Disconnecting")
    collector.disconnect()

    logging.info("Fast File Transfer application finished")


if __name__ == "__main__":
    main()
