import argparse
import logging
import os
import socket
import sys
import timeit
from datetime import datetime

from application_lock import ApplicationLock
from roaming_data import RoamingData

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

if socket.gethostname() in ["N007510"]:
    DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing/big"
    # DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing/small"
    DEFAULT_OUTPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing"
else:
    DEFAULT_INPUT_PATH = "/dcs/data01/WORKDATA/W_RR/LOAD"
    DEFAULT_OUTPUT_PATH = "/dcs/data01/WORKDATA/W_RR/LOAD"


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
    files = [filename for filename in os.listdir() if filename[0:4] == "2023"]

    aggregated = {}

    # Iterate over eligible files
    for filename in files:
        # Load input file
        roaming_data = RoamingData(aggregated)
        roaming_data.load(DEFAULT_INPUT_PATH + "/" + filename)
        roaming_data.validate()
        roaming_data.filter()
        roaming_data.aggregate()
        aggregated = roaming_data.get("aggregated")

    # Save aggregated data
    aggregated_output = [list(key) + list(aggregated[key]) for key in aggregated.keys()]
    RoamingData.write(aggregated_output,
                      DEFAULT_OUTPUT_PATH + "/report_" + str(datetime.now())[0:19].replace(" ", "_").replace(":",
                                                                                                             "-") + ".csv")

    application_lock.disable()
    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
