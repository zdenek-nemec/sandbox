import argparse
import os

DEFAULT_PATH = "./sample"


def get_directory_content(path):
    return [path + "/" + item for item in os.listdir(path)]


def get_file_properties(path):
    return (
        path,
        os.path.getsize(path),
    )


def main():
    print("File Explorer")

    argument_parser = argparse.ArgumentParser(prog="File Explorer")
    argument_parser.add_argument("--path", "-p", default=DEFAULT_PATH)

    path = argument_parser.parse_args().path
    print("Exploring path %s" % path)

    content = get_directory_content(path)
    files = []
    while len(content) > 0:
        item = content.pop(0)
        if os.path.isdir(item):
            content += get_directory_content(item)
        else:
            files.append(get_file_properties(item))
    print(files)


if __name__ == "__main__":
    main()
