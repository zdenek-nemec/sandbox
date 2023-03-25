import logging
import os
import socket
import sys
from datetime import datetime

from application_controller import ApplicationController
from application_lock import ApplicationLock
from roaming_data import RoamingData

if socket.gethostname() in ["N007510"]:
    # DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing/big"
    DEFAULT_INPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing/small"
    DEFAULT_OUTPUT_PATH = "c:/Zdenek/_tmp/Cetin/roaming-preprocessor/testing"
else:
    DEFAULT_INPUT_PATH = "/dcs/data01/WORKDATA/W_RR/LOAD"
    DEFAULT_OUTPUT_PATH = "/dcs/data01/WORKDATA/W_RR/LOAD"


def set_logging(log_level, log_format):
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)


def main():
    print("Roaming Preprocessor")
    application_controller = ApplicationController()
    logging.info("Application started")

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

    logging.info("Application finished")
    logging.debug(f"Finished in {application_controller.get_runtime():,.1f}s")


if __name__ == "__main__":
    main()
