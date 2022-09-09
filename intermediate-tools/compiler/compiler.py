import os.path
import pathlib

SCRIPTS_PATH = "./tests"


def main():
    print("Intermediate Tools - Compiler")

    if not os.path.isdir(SCRIPTS_PATH):
        # TODO: Throw exception
        print("ERROR: Scripts path does not exist or is not a directory")
    scripts_path = os.path.normpath(SCRIPTS_PATH)

    scripts = []
    for item in os.listdir(scripts_path):
        file_path = os.path.normpath(scripts_path + "/" + item)
        # print("{0}".format(file_path))
        if not os.path.isfile(file_path):
            # print("\tNot a file, skipping")
            continue
        elif pathlib.Path(file_path).suffix != ".scr":
            # print("\tNot Intermediate script, skipping")
            continue
        scripts.append(file_path)

    [print(item) for item in scripts]


if __name__ == "__main__":
    main()
