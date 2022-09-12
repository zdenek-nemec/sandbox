import argparse
import logging
import os.path
import pathlib
import sys

# SCRIPTS_PATH = "./tests"
SCRIPTS_PATH = "C:/Zdenek/_tmp/IntermediateScripts"
# SCRIPTS_PATH = "/dcs/appl01/var_dcs_9.0_db/cgdc/src"
# TARGET = ["library_a.scr", "library_b.scr"]
# TARGET = []


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
    argument_parser.add_argument("--target", default="")
    # TARGET = [argument_parser.parse_args().target]
    TARGET = []

    log_level = "ERROR"
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
    # [logging.debug("Relevant script {0}".format(item)) for item in scripts]

    dependencies = get_dependencies(scripts, scripts_path)
    # print("Dependencies")
    # [print(key, dependencies[key]) for key in dependencies.keys()]

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
    # [print(key, libraries[key]) for key in libraries.keys()]

    expanded_dependencies = {}
    for key in dependencies.keys():
        if not dependencies[key]:
            expanded_dependencies[key] = []
        else:
            expanded_dependencies[key] = get_unique_list(get_expanded_dependencies(dependencies, key))
    # print("Expanded")
    # [print(key, expanded_dependencies[key]) for key in expanded_dependencies.keys()]

    # print("Full or target")
    if not TARGET:
        to_review = expanded_dependencies.copy()
    else:
        to_review = {}
        for item in TARGET:
            to_review[item] = []
            for key in expanded_dependencies.keys():
                if item in expanded_dependencies[key]:
                    # print("key {0} depends on {1}".format(key, item))
                    to_review[key] = expanded_dependencies[key]

    # print("Removing unaltered")
    for key in to_review.keys():
        # print("* checking key", key)
        for item in to_review[key]:
            # print("  * checking item", item)
            if item not in to_review.keys():
                # print("    * not")
                to_review[key].remove(item)

    # print("To review")
    # [print(key, to_review[key]) for key in to_review.keys()]

    ordered = []
    while len(to_review) > 0:
        for key in list(to_review.keys()):
            if not to_review[key]:
                ordered.append(key)
                to_review.pop(key)
            else:
                for dependency in to_review[key]:
                    if dependency not in ordered:
                        break
                else:
                    ordered.append(key)
                    to_review.pop(key)
    [print(item) for item in ordered]
    # print(ordered)
    # print("Finished")


# Import
def get_dependencies_old(dependencies, scripts, scripts_path):
    for item in scripts:
        dependencies[item] = []
        with open(scripts_path + "/" + item, "r") as text_file:
            for line in text_file:
                if line[0:6] == "import":
                    dependency = line[:-1].split("\"")[1]
                    dependencies[item].append(dependency + ".scr")


def get_dependencies(scripts, scripts_path):
    dependencies = {}
    for item in scripts:
        dependencies[item] = []
        with open(scripts_path + "/" + item, "r") as text_file:
            for line in text_file:
                if line[0:8] == "#include" and line.find(".pro>") != -1:
                    dependency = line[:-1].split("<")[1].split(".")[0]
                    dependencies[item].append(dependency + ".scr")
    return dependencies


if __name__ == "__main__":
    main()
