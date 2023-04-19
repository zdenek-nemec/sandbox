import csv
import logging
import os
from datetime import datetime

from application_controller import ApplicationController
from application_lock import ApplicationLock
from configuration import Configuration
from global_titles import GlobalTitles
from roaming_loader import RoamingLoader
from roaming_record_2g3g import RoamingRecord2g3g
from roaming_record_4g5g import RoamingRecord4g5g


def generate_new_configuration(filename):
    logging.info("New configuration requested")
    configuration = Configuration()
    configuration.generate(filename)
    configuration.save()


def aggregate(data, aggregated, global_titles):
    for entry in data:
        if not type(entry) is RoamingRecord2g3g:
            raise RuntimeError(f"Unexpected data type {type(entry)}")
        else:
            entry: RoamingRecord2g3g

        date = str(entry._timestamp)[0:10]
        observation_domain = entry._observation_domain
        observation_point = entry._observation_point
        direction = entry._direction
        mtp3_opc = entry._mtp3_opc
        mtp3_dpc = entry._mtp3_dpc
        sccp_message_type = entry._sccp_message_type
        global_title_cgpa, tadig_cgpa = global_titles.get_tadig(entry._sccp_cgpa_gt_digits, "unknown")
        global_title_cdpa, tadig_cdpa = global_titles.get_tadig(entry._sccp_cdpa_gt_digits, "unknown")

        msu_length = int(entry._msu_length)

        key = (
            date,
            observation_domain,
            observation_point,
            direction,
            mtp3_opc,
            mtp3_dpc,
            sccp_message_type,
            global_title_cgpa,
            tadig_cgpa,
            global_title_cdpa,
            tadig_cdpa
        )

        if key in aggregated:
            aggregated[key][0] += 1
            aggregated[key][1] += msu_length
        else:
            aggregated[key] = [1, msu_length]


def aggregate_4g5g(data, aggregated, global_titles):
    for entry in data:
        if not type(entry) is RoamingRecord4g5g:
            raise RuntimeError(f"Unexpected data type {type(entry)}")
        else:
            entry: RoamingRecord4g5g

        date = str(entry._timestamp)[0:10]
        direction = entry._direction
        peername = entry._peername
        hostname = entry._hostname
        original_realm = entry._original_realm
        destination_realm = entry._destination_realm
        release_cause = entry._release_cause

        key = (
            date,
            direction,
            peername,
            hostname,
            original_realm,
            destination_realm,
            release_cause
        )

        if key in aggregated:
            aggregated[key][0] += 1
        else:
            aggregated[key] = [1]


def write_aggregated(data, path, data_type):
    logging.debug(f"Saving {len(data)} records to {path}")
    with open(path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        if data_type == "2G/3G":
            writer.writerow([
                "Date",
                "Observation domain",
                "Observation point",
                "Direction",
                "MTP3 OPC",
                "MTP3 DPC",
                "SCCP message type",
                "Global title CGPA",
                "TADIG CGPA",
                "Global title CDPA",
                "TADIG CDPA",
                "MSU Count",
                "MSU Length"
            ])
        elif data_type == "4G/5G":
            writer.writerow([
                "Date",
                "Direction",
                "Peername",
                "Hostname",
                "Original realm",
                "Destination realm",
                "Release cause",
                "MSU count"
            ])
        else:
            raise ValueError(f"Unknown datatype")
        for row in data:
            writer.writerow(row)


def main():
    print("Roaming Preprocessor")
    application_controller = ApplicationController()
    logging.info("Application started")

    if application_controller.is_new_configuration_requested():
        generate_new_configuration(application_controller.get_configuration_file())
    else:
        configuration = Configuration()
        configuration.load(application_controller.get_configuration_file())
        application_lock = ApplicationLock(configuration.get_port_lock())
        global_titles = GlobalTitles(configuration.get_global_titles_path())

        # Check eligible files
        os.chdir(configuration.get_input_path())
        files = [filename for filename in os.listdir() if filename[0:4] == "2023"]

        aggregated = {}
        # Iterate over eligible files
        for filename in files:
            # Load input file
            roaming_data = RoamingLoader(configuration.get_type())
            roaming_data.load(configuration.get_input_path() + "/" + filename)
            if configuration.get_type() == "2G/3G":
                aggregate(roaming_data._records, aggregated, global_titles)
            elif configuration.get_type() == "4G/5G":
                aggregate_4g5g(roaming_data._records, aggregated, global_titles)
            else:
                raise ValueError(f"Unknown datatype")

        # Save aggregated data
        aggregated_output = [list(key) + list(aggregated[key]) for key in aggregated.keys()]
        write_aggregated(
            aggregated_output,
            configuration.get_output_path()
            + "/report_"
            + str(datetime.now())[0:19].replace(" ", "_").replace(":", "-") + ".csv",
            configuration.get_type()
        )

        application_lock.disable()

    logging.info("Application finished")
    logging.debug(f"Finished in {application_controller.get_runtime():,.1f}s")


if __name__ == "__main__":
    main()
