import csv
import glob
import logging
import os
from datetime import datetime

from application_controller import ApplicationController
from application_lock import ApplicationLock
from configuration import Configuration
from data_type import DataType
from global_titles import GlobalTitles
from roaming_loader import RoamingLoader
from roaming_record_2g3g import RoamingRecord2g3g
from roaming_record_4g5g import RoamingRecord4g5g


def generate_new_configuration(filename):
    logging.info("New configuration requested")
    configuration = Configuration()
    configuration.generate(filename)
    configuration.save()


def get_selected_files(path: str, mask: str) -> list:
    files = [os.path.abspath(filepath) for filepath in glob.glob(path + "/" + mask)]
    logging.info(f"Selected {len(files)} files to be processed")
    return files


def transform_mtp3(original):
    return f"{original // 2048}-{(original % 2048) // 8}-{original % 8}"


def aggregate_2g3g(data, aggregated, global_titles):
    for entry in data:
        if not type(entry) is RoamingRecord2g3g:
            raise RuntimeError(f"Unexpected data type {type(entry)}")
        else:
            entry: RoamingRecord2g3g

        date = str(entry._timestamp)[0:10]
        observation_domain = entry._observation_domain
        observation_point = entry._observation_point
        direction = entry._direction
        mtp3_opc = transform_mtp3(int(entry._mtp3_opc))
        mtp3_dpc = transform_mtp3(int(entry._mtp3_dpc))
        sccp_message_type = entry._sccp_message_type
        global_title_cgpa, tadig_cgpa = global_titles.get_tadig(entry._sccp_cgpa_gt_digits, "unk")
        global_title_cdpa, tadig_cdpa = global_titles.get_tadig(entry._sccp_cdpa_gt_digits, "unk")

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


def aggregate_4g5g(data, aggregated):
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


def write_aggregated(data, path, data_type: DataType):
    logging.debug(f"Saving {len(data)} records to {path}")
    with open(path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter="|", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        if data_type.is_2g3g():
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
        elif data_type.is_4g5g():
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


def process_files(configuration, files):
    global_titles = GlobalTitles(configuration.get_global_titles_path())
    output_filename_without_extension = os.path.abspath(
        configuration.get_output_path()
        + f"/{configuration.get_output_filename_prefix()}{configuration.get_port_lock()}_"
        + str(datetime.now())[0:19].replace(" ", "_").replace(":", "-")
    )
    aggregated = {}
    for filepath in files:
        roaming_data = RoamingLoader(configuration.get_data_type(), configuration.get_columns())
        try:
            roaming_data.load(filepath)
        except Exception as e:
            logging.warning(f"{type(e)} exception while processing {filepath}, ignoring the file. Full exception: {e}")
            continue
        if configuration.get_data_type().is_2g3g():
            aggregate_2g3g(roaming_data._records, aggregated, global_titles)
        elif configuration.get_data_type().is_4g5g():
            aggregate_4g5g(roaming_data._records, aggregated)
        else:
            raise ValueError(f"Unknown datatype")
        aggregated_output = [list(key) + list(aggregated[key]) for key in aggregated.keys()]
        write_aggregated(
            aggregated_output,
            output_filename_without_extension + ".tmp",
            configuration.get_data_type()
        )
        if configuration.get_delete_input_files():
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except OSError:
                    raise RuntimeError(f"Cannot delete input file {filepath}")
                else:
                    logging.debug(f"Deleted input file {filepath}")
            else:
                logging.warning(f"File {filepath} missing before delete")
        else:
            logging.debug(f"Keeping input file {filepath}")
    os.rename(
        output_filename_without_extension + ".tmp", output_filename_without_extension + ".csv")


def main():
    application_controller = ApplicationController()
    logging.info("Roaming Preprocessor")
    logging.info("Application started")

    if application_controller.is_new_configuration_requested():
        generate_new_configuration(application_controller.get_configuration_file())
    else:
        configuration = Configuration()
        configuration.load(application_controller.get_configuration_file())
        application_lock = ApplicationLock(configuration.get_port_lock())
        selected_files = get_selected_files(configuration.get_input_path(), configuration.get_input_mask())
        if selected_files:
            process_files(configuration, selected_files)
        application_lock.disable()

    logging.info("Application finished")
    logging.debug(f"Finished in {application_controller.get_runtime():,.1f}s")


if __name__ == "__main__":
    main()
