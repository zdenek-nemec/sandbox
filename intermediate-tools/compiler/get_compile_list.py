import argparse
import logging
import os.path
import pathlib
import socket
import sys

INTERMEDIATE = ["avl4658t", "avl4688t", "avl4713p", "avl4715p"]
SCRIPTS_PATH = {
    "Intermediate": "/dcs/appl01/var_dcs_9.0_db/cgdc/src",
    "Unknown": "./tests"
    # "Unknown": "C:/Zdenek/_tmp/IntermediateScripts"
}


def get_scripts_path():
    hostname = socket.gethostname()
    if hostname in INTERMEDIATE:
        return SCRIPTS_PATH["Intermediate"]
    else:
        return SCRIPTS_PATH["Unknown"]


def get_dependencies(scripts, scripts_path):
    dependencies = {}
    for item in scripts:
        dependencies[item] = []
        with open(scripts_path + "/" + item + ".scr", "r") as text_file:
            for line in text_file:
                if line[0:8] == "#include" and line.find(".pro>") != -1:
                    dependency = line[:-1].split("<")[1].split(".")[0]
                    dependencies[item].append(dependency)
    return dependencies


def get_unique_list(item_list):
    unique_list = []
    for item in item_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


def get_expanded_dependencies(dependencies, key):
    expanded = []
    for dependency in dependencies[key]:
        expanded.append(dependency)
        expanded += get_expanded_dependencies(dependencies, dependency)
    return expanded


def main():
    # print("Intermediate Tools - Compiler")

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--scripts", default="")
    altered = argument_parser.parse_args().scripts
    if altered == "":
        altered = []
        # altered = ["library_b.scr"]

    log_level = "DEBUG"
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)

    logging.info("Validating the scripts path")
    scripts_path = get_scripts_path()
    if not os.path.isdir(scripts_path):
        raise ValueError("Scripts path {0} does not exist or is not a directory".format(scripts_path))
    scripts_path = os.path.normpath(scripts_path)

    logging.info("Listing relevant files")
    relevant = []
    for item in os.listdir(scripts_path):
        file_path = os.path.normpath(scripts_path + "/" + item)
        if not os.path.isfile(file_path):
            logging.debug("Skipping {0}, not a file".format(file_path))
            continue
        elif pathlib.Path(file_path).suffix != ".scr":
            logging.debug("Skipping {0}, not Intermediate script".format(file_path))
            continue
        relevant.append(item[0:-4])
    logging.debug("Identified {0} relevant scripts: {1}".format(len(relevant), relevant))

    logging.info("Identifying dependencies")
    dependencies = get_dependencies(relevant, scripts_path)
    # [print(key, dependencies[key]) for key in dependencies.keys()]
    logging.debug("Identified {0} scripts with no dependencies and {1} with one or more dependencies".format(
        len(list(filter(lambda key: dependencies[key] == [], dependencies.keys()))),
        len(list(filter(lambda key: dependencies[key] != [], dependencies.keys())))
    ))

    logging.info("Identifying expanded dependencies")
    expanded = {}
    for key in dependencies.keys():
        if not dependencies[key]:
            expanded[key] = []
        else:
            expanded[key] = get_unique_list(get_expanded_dependencies(dependencies, key))
    # [print(key, expanded[key]) for key in expanded.keys()]

    logging.info("Targeting compilation list")
    if not altered:
        review = expanded.copy()
        logging.debug("Compile everything, {0} scripts".format(len(review)))
    else:
        review = {}
        for item in altered:
            logging.debug("Checking dependencies on {0}".format(item))
            review[item] = expanded[item]
            for key in expanded.keys():
                if item in expanded[key]:
                    logging.debug("{0} is dependent".format(key))
                    review[key] = expanded[key]
        logging.debug("Compile {0} scripts".format(len(review)))
    # [print(key, review[key]) for key in review.keys()]

    logging.info("Removing unaltered dependencies")
    refined = {}
    for key in review.keys():
        refined[key] = []
        for item in review[key]:
            if item in review.keys():
                refined[key].append(item)
    # [print(key, refined[key]) for key in refined.keys()]

    logging.info("Sorting compilation list")
    ordered = []
    while len(refined) > 0:
        for key in list(refined.keys()):
            if not refined[key]:
                ordered.append(key)
                refined.pop(key)
            else:
                for dependency in refined[key]:
                    if dependency not in ordered:
                        break
                else:
                    ordered.append(key)
                    refined.pop(key)
    # [print(item) for item in ordered]
    print(ordered)

    # print("Finished")


if __name__ == "__main__":
    main()
