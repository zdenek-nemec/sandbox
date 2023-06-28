import csv
import gzip
import logging
import os
from io import TextIOWrapper
from zipfile import ZipFile

from data_type import DataType
from roaming_record_2g3g import RoamingRecord2g3g
from roaming_record_4g5g import RoamingRecord4g5g


class RoamingLoader(object):
    def __init__(self, data_type: DataType, columns: int):
        self._records = []
        self._type = data_type
        self._columns = columns

    def get_records(self):
        return self._records

    @staticmethod
    def _get_input_file_extension(file_path):
        filename, extension = os.path.splitext(file_path)
        return extension

    def _is_gz(self, file_path):
        if self._get_input_file_extension(file_path) == ".gz":
            return True
        else:
            return False

    def _is_zip(self, file_path):
        if self._get_input_file_extension(file_path) == ".zip":
            return True
        else:
            return False

    def _load_records(self, input_file):
        reader = csv.reader(input_file, delimiter="|")
        row_count = 0
        header_count = 0
        invalid_count = 0
        filter_count = 0
        for row in reader:
            row_count += 1
            try:
                if self._type.is_2g3g():
                    roaming_record = RoamingRecord2g3g(row, self._columns)
                elif self._type.is_4g5g():
                    roaming_record = RoamingRecord4g5g(row, self._columns)
                else:
                    raise ValueError(f"Unknown datatype {type(self._type)}")
            except (TypeError, ValueError) as e:
                logging.error(f"Removing invalid record {row} due to exception {e}")
                invalid_count += 1
            else:
                if roaming_record.is_header():
                    header_count += 1
                elif roaming_record.is_filtered():
                    filter_count += 1
                else:
                    self._records.append(roaming_record)
        logging.debug(
            f"Lines {row_count}, loaded {len(self._records)}, headers {header_count}, invalid {invalid_count}, filtered {filter_count}")

    def load(self, path):
        logging.info(f"Processing {path}")
        if self._is_gz(path):
            with gzip.open(path, "rt") as input_file:
                self._load_records(input_file)
        elif self._is_zip(path):
            with ZipFile(path) as zip_file:
                filename = os.path.splitext(os.path.basename(path))[0] + ".dat"
                with zip_file.open(filename, "r") as input_file:
                    self._load_records(TextIOWrapper(input_file, "utf-8"))
        else:
            with open(path, "r") as input_file:
                self._load_records(input_file)


if __name__ == "__main__":
    pass
