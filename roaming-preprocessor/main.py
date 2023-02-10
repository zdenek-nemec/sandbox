import argparse
import logging
import os
import sys
import timeit

from application_lock import ApplicationLock
from roaming_data import RoamingData

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_WORK_DATA_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/work.dat"
DEFAULT_WORK_DATA_OUTPUT_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/work_out.dat"  # Only for development purposes
DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing"
DEFAULT_OUTPUT_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing"


def main():
    print("Roaming Preprocessor")

    # Parse arguments and set up logging
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )

    log_level = argument_parser.parse_args().log_level
    log_format = DEFAULT_LOG_FORMAT
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Application started")
    application_start_time = timeit.default_timer()

    logging.debug("Arguments: log_level = {0}".format(
        argument_parser.parse_args().log_level
    ))

    # Load configuration

    application_lock = ApplicationLock()

    # Check eligible files
    os.chdir(DEFAULT_INPUT_PATH)
    files = [filename for filename in os.listdir() if filename[0:4] == "2023" and filename[-4:] == ".dat"]

    # Load work file
    roaming_data = RoamingData()
    roaming_data.load_data(DEFAULT_WORK_DATA_PATH)

    # Iterate over eligible files
    for filename in files:
        # Load input file
        roaming_data.load_data(DEFAULT_INPUT_PATH + "/" + filename)
        roaming_data.validate()

        # Assemble data
        roaming_data.merge_sessions()

        # Save complete data
        roaming_data.write_data(roaming_data.get_data("complete", ""), DEFAULT_OUTPUT_PATH + "/" + filename[0:len(filename)-4] + ".csv")

        # Save work file
        roaming_data.write_data(roaming_data.get_data("work"), DEFAULT_WORK_DATA_OUTPUT_PATH)

    application_lock.disable()
    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
