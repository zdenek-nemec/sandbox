import csv
import gzip
import logging
import os

from roaming_record import RoamingRecord


class RoamingLoader(object):
    def __init__(self):
        self._records = []

    def get_records(self):
        return self._records

    @staticmethod
    def _get_input_file_extension(file_path):
        filename, extension = os.path.splitext(file_path)
        return extension

    def _is_compressed(self, file_path):
        if self._get_input_file_extension(file_path) == ".gz":
            return True
        else:
            return False

    def _load_records(self, input_file):
        reader = csv.reader(input_file, delimiter="|")
        row_count = 0
        invalid_count = 0
        filter_count = 0
        for row in reader:
            row_count += 1
            try:
                roaming_record = RoamingRecord(row)
            except (TypeError, ValueError):
                logging.error(f"Removing invalid record {row}")
                invalid_count += 1
            else:
                if roaming_record.is_filtered():
                    filter_count += 1
                else:
                    self._records.append(roaming_record)
        logging.debug(
            f"Lines {row_count}, loaded {len(self._records)}, invalid {invalid_count}, filtered {filter_count}")

    def load(self, path):
        logging.info(f"Processing {path}")
        if self._is_compressed(path):
            with gzip.open(path, "rt") as input_file:
                self._load_records(input_file)
        else:
            with open(path, "r") as input_file:
                self._load_records(input_file)


if __name__ == "__main__":
    pass
