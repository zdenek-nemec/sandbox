import logging
import os
from datetime import datetime

from application_controller import ApplicationController
from application_lock import ApplicationLock
from configuration import Configuration
from roaming_data import RoamingData


def generate_new_configuration(filename):
    logging.info("New configuration requested")
    configuration = Configuration()
    configuration.generate(filename)
    configuration.save()


def main():
    print("Roaming Preprocessor")
    application_controller = ApplicationController()
    logging.info("Application started")

    if application_controller.is_new_configuration_requested():
        generate_new_configuration(application_controller.get_configuration_file())
    else:
        configuration = Configuration()
        configuration.load(application_controller.get_configuration_file())

        application_lock = ApplicationLock()

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
            roaming_data.aggregate()
            aggregated = roaming_data.get("aggregated")

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
