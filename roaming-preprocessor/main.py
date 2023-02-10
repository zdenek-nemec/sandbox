import argparse
import csv
import logging
import sys
import timeit

from application_lock import ApplicationLock

DEFAULT_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_WORK_DATA_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/work.dat"
DEFAULT_INPUT_DATA_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/2023012600_01782806.dat"
# DEFAULT_INPUT_DATA_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/sample_500m.dat"
DEFAULT_OUTPUT_DATA_PATH = "c:/Zdenek/_tmp/roaming-preprocessor/testing/2023012600_01782806.csv"


class RoamingData(object):
    def __init__(self):
        self._work_data = []
        self._complete_data = []

    def get_data(self, data_type: str, columns: str = "all"):
        if data_type == "work":
            data = self._work_data
        elif data_type == "complete":
            data = self._complete_data
        else:
            raise ValueError("Invalid data type")

        if columns == "all":
            return data
        else:
            return [x[0:5] + x[15:17] for x in data]

    def load_data(self, path):
        data = self._work_data
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="|")
            for row in reader:
                data.append(row)
        logging.debug("Records {0}, columns {1}".format(len(data), len(data[0])))
        logging.debug("Sample (first record): {0}".format(data[0]))
        self._work_data = data

    def validate(self):
        logging.debug("Entries before validation: {0}".format(len(self._work_data)))
        valid = []
        for entry in self._work_data:
            if len(entry) == 32:
                valid.append(entry)
            else:
                logging.error("Removing invalid entry {0}".format(entry))
        self._work_data = valid
        logging.debug("Entries after validation: {0}".format(len(self._work_data)))

    def merge_sessions(self):
        sessions = {}
        for entry in self._work_data.copy():
            key = entry[4]
            if key not in sessions:
                sessions[key] = entry
            else:
                pass
        self._complete_data = list(sessions.values())

    @staticmethod
    def write_data(data, path):
        logging.debug("Records to save {0}".format(len(data)))
        with open(path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)


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

    # Load work file
    roaming_data = RoamingData()
    roaming_data.load_data(DEFAULT_WORK_DATA_PATH)

    # Load input file
    roaming_data.load_data(DEFAULT_INPUT_DATA_PATH)
    roaming_data.validate()

    # Assemble data
    roaming_data.merge_sessions()

    # Save complete data
    roaming_data.write_data(roaming_data.get_data("complete", ""), DEFAULT_OUTPUT_DATA_PATH)

    # Save work file

    application_lock.disable()
    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
