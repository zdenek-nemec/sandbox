import argparse
import json
import os

DEFAULT_PATH = "./sample"
DEFAULT_REPORT_PATH = "./report.json"


def get_directory_content(path):
    return [path + "/" + item for item in os.listdir(path)]


def get_file_properties(path):
    return {
        "path": path,
        "size": os.path.getsize(path),
    }


def main():
    print("File Explorer")

    argument_parser = argparse.ArgumentParser(prog="File Explorer")
    argument_parser.add_argument("--path", "-p", default=DEFAULT_PATH)
    argument_parser.add_argument("--report", "-r", default=DEFAULT_REPORT_PATH)
    argument_parser.add_argument("--batch", "-b", type=int)

    path = argument_parser.parse_args().path
    report = argument_parser.parse_args().report
    batch = argument_parser.parse_args().batch
    print("Exploring path: %s" % path)
    print("Report: %s" % report)
    print("Batch: %s" % batch)

    content = get_directory_content(path)
    files = []
    while len(content) > 0:
        item = content.pop(0)
        if os.path.isdir(item):
            content += get_directory_content(item)
        else:
            files.append(get_file_properties(item))
        if batch is not None and len(files) > 1 and len(files) % batch == 0:
            save_report(files, report, "a")
            files = []

    if batch is not None:
        if len(files) > 1:
            save_report(files, report, "a")
    else:
        save_report(files, report, "w")


def save_report(files, report, mode):
    with open(report, mode, encoding="utf-8") as json_file:
        json.dump(files, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
