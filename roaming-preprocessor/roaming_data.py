import csv
import logging
from datetime import datetime


class RoamingData(object):
    def __init__(self, aggregated):
        self._data = []
        self._aggregated = aggregated

    def get(self, data_type: str):
        if data_type == "data":
            return self._data
        elif data_type == "aggregated":
            return self._aggregated
        else:
            raise ValueError("Invalid data type")

    def load(self, path):
        logging.info(f"Processing {path}")
        data = []
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="|")
            for row in reader:
                data.append(row)
        logging.debug(f"Records {len(data)}, columns {len(data[0])}")
        self._data = []
        self._data = data

    def validate(self):
        data = self._data
        logging.debug(f"Entries before validation: {len(data)}")
        valid = []
        for entry in data:
            if len(entry) == 47:
                valid.append(entry)
            else:
                logging.error(f"Removing invalid entry {entry}")
        logging.debug(f"Entries after validation: {len(valid)}")
        self._data = valid

    def filter(self):
        data = self._data
        logging.debug(f"Entries before filtering: {len(data)}")
        output = []
        for entry in data:
            sccp_cgpa_gt_noa = entry[20]
            sccp_cdpa_gt_noa = entry[27]
            mtp3_si = entry[10]
            mtp3_variant = entry[6]

            if (sccp_cgpa_gt_noa == "4" and sccp_cdpa_gt_noa == "4" and mtp3_si == "3" and mtp3_variant == "1"):
                output.append(entry)
        logging.debug(f"Entries after filtering: {len(output)}")
        self._data = output

    def aggregate(self):
        data = self._data
        aggregated = self._aggregated
        for entry in data:
            timestamp = str(datetime.fromtimestamp(int(entry[0]) / 1000.0))[0:13]
            observation_domain = entry[2]
            observation_point = entry[3]
            direction = entry[4]
            mtp3_variant = entry[6]
            mtp3_opc = entry[7]
            mtp3_dpc = entry[8]
            mtp3_si = entry[10]
            sccp_message_type = entry[12]
            sccp_cgpa_gt_noa = entry[20]
            sccp_cgpa_gt_digits = entry[21][0:6]
            sccp_cdpa_gt_noa = entry[27]
            sccp_cdpa_gt_digits = entry[28][0:6]

            msu_length = int(entry[11])

            key = (
                timestamp,
                observation_domain,
                observation_point,
                direction,
                mtp3_variant,
                mtp3_opc,
                mtp3_dpc,
                mtp3_si,
                sccp_message_type,
                sccp_cgpa_gt_noa,
                sccp_cgpa_gt_digits,
                sccp_cdpa_gt_noa,
                sccp_cdpa_gt_digits
            )

            if key in aggregated:
                aggregated[key][0] += 1
                aggregated[key][1] += msu_length
            else:
                aggregated[key] = [1, msu_length]

    @staticmethod
    def write(data, path):
        logging.debug(f"Saving {len(data)} records to {path}")
        with open(path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)


if __name__ == "__main__":
    pass
