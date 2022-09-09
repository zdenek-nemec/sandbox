import logging
import os.path
import pathlib
import sys

SCRIPTS_PATH = "./tests"


def main():
    print("Intermediate Tools - Compiler")

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Validating the scripts path")
    if not os.path.isdir(SCRIPTS_PATH):
        logging.error("Scripts path {0} does not exist or is not a directory".format(SCRIPTS_PATH))
        raise ValueError("Scripts path {0} does not exist or is not a directory".format(SCRIPTS_PATH))
    scripts_path = os.path.normpath(SCRIPTS_PATH)

    logging.info("Listing relevant files")
    scripts = []
    for item in os.listdir(scripts_path):
        file_path = os.path.normpath(scripts_path + "/" + item)
        if not os.path.isfile(file_path):
            logging.debug("Skipping {0}, not a file".format(file_path))
            continue
        elif pathlib.Path(file_path).suffix != ".scr":
            logging.debug("Skipping {0}, not Intermediate script".format(file_path))
            continue
        scripts.append(item)
    [logging.debug("Relevant script {0}".format(item)) for item in scripts]

    dependencies = {}
    for item in scripts:
        dependencies[item] = []
        with open(scripts_path + "/" + item, "r") as text_file:
            for line in text_file:
                if line[0:6] == "import":
                    dependency = line[:-1].split("\"")[1]
                    dependencies[item].append(dependency + ".scr")
    [print(key, dependencies[key]) for key in dependencies.keys()]

    libraries = {None: []}
    for key in dependencies.keys():
        if len(dependencies[key]) == 0:
            libraries[None].append(key)
        else:
            for library in dependencies[key]:
                if library not in libraries:
                    libraries[library] = [key]
                else:
                    libraries[library].append(key)
    [print(key, libraries[key]) for key in libraries.keys()]

    print("Finished")


if __name__ == "__main__":
    main()
