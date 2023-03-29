import logging
import os
from datetime import datetime

from application_controller import ApplicationController
from application_lock import ApplicationLock
from configuration import Configuration
from global_titles import GlobalTitles
from roaming_data import RoamingData


def generate_new_configuration(filename):
    logging.info("New configuration requested")
    configuration = Configuration()
    configuration.generate(filename)
    configuration.save()


def aggregate(data, aggregated, global_titles):
    for entry in data:
        timestamp = datetime.fromtimestamp(int(entry[0]) / 1000.0)
        timestamp_day = str(timestamp)[0:10]
        timestamp_hour = str(timestamp)[11:13]
        observation_domain = entry[2]
        observation_point = entry[3]
        direction = entry[4]
        mtp3_opc = entry[7]
        mtp3_dpc = entry[8]
        sccp_message_type = entry[12]
        sccp_cgpa_gt_digits_tadig = global_titles.get_tadig(entry[21], "unknown")
        sccp_cdpa_gt_digits_tadig = global_titles.get_tadig(entry[28], "unknown")

        msu_length = int(entry[11])

        key = (
            timestamp_day,
            timestamp_hour,
            observation_domain,
            observation_point,
            direction,
            mtp3_opc,
            mtp3_dpc,
            sccp_message_type,
            sccp_cgpa_gt_digits_tadig,
            sccp_cdpa_gt_digits_tadig
        )

        if key in aggregated:
            aggregated[key][0] += 1
            aggregated[key][1] += msu_length
        else:
            aggregated[key] = [1, msu_length]


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
            roaming_data = RoamingData(aggregated)
            roaming_data.load(configuration.get_input_path() + "/" + filename)
            roaming_data.validate()
            roaming_data.filter()
            aggregate(roaming_data._data, aggregated, global_titles)

        # Save aggregated data
        aggregated_output = [list(key) + list(aggregated[key]) for key in aggregated.keys()]
        RoamingData.write(aggregated_output,
                          configuration.get_output_path() + "/report_" + str(datetime.now())[0:19].replace(" ",
                                                                                                           "_").replace(
                              ":",
                              "-") + ".csv")

        application_lock.disable()

    logging.info("Application finished")
    logging.debug(f"Finished in {application_controller.get_runtime():,.1f}s")


if __name__ == "__main__":
    main()
