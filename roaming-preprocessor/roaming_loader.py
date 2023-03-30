import csv
import logging

from roaming_record import RoamingRecord


class RoamingLoader(object):
    def __init__(self):
        self._records = []

    def get(self):
        return self._records

    def load(self, path):
        logging.info(f"Processing {path}")
        records = []
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="|")
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
                        records.append(roaming_record)
        logging.debug(f"Lines {row_count}, loaded {len(records)}, invalid {invalid_count}, filtered {filter_count}")
        self._records = records


if __name__ == "__main__":
    pass
