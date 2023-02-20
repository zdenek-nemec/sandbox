import csv
import logging


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
        logging.info("Processing {0}".format(path))
        data = self._work_data
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="|")
            for row in reader:
                data.append(row)
        logging.debug("Records {0}, columns {1}".format(len(data), len(data[0])))
        # logging.debug("Sample (first record): {0}".format(data[0]))
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
        logging.debug("Started merging, work data entries: {0}".format(len(self._work_data)))
        sessions = {}
        complete = {}
        for entry in self._work_data:
            key = entry[4]
            if key not in sessions:
                sessions[key] = entry
            else:
                complete[key] = sessions[key]
        self._complete_data = list(complete.values())
        self._work_data = [sessions[key] for key in sessions.keys() if key not in complete]
        logging.debug("Finished merging, complete {0}, work {1}".format(len(self._complete_data), len(self._work_data)))

    @staticmethod
    def write_data(data, path):
        logging.debug("Saving {0} records to {1}".format(len(data), path))
        with open(path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)


if __name__ == "__main__":
    pass
