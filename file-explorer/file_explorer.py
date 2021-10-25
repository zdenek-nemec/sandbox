import argparse
import json
import os

DEFAULT_PATH = "./sample"
DEFAULT_REPORT_PATH = "./report.json"
EXCEPTIONS = [".ssh"]


def get_directory_content(path):
    return [path + "/" + item for item in os.listdir(path)]


def get_file_properties(path):
    return {
        "path": path,
        "creation time": os.path.getctime(path),
        "modification time": os.path.getmtime(path),
        "size": os.path.getsize(path),
    }


def save_report(files, report, mode):
    with open(report, mode, encoding="utf-8") as json_file:
        json.dump(files, json_file, ensure_ascii=False, indent=4)


def main():
    print("File Explorer")

    argument_parser = argparse.ArgumentParser(prog="File Explorer")
    argument_parser.add_argument("--path", "-p", default=DEFAULT_PATH)
    argument_parser.add_argument("--report", "-r", default=DEFAULT_REPORT_PATH)
    argument_parser.add_argument("--batch", "-b", type=int)

    path = argument_parser.parse_args().path
    report = argument_parser.parse_args().report
    batch = argument_parser.parse_args().batch
    print("Arguments")
    print("* path: %s" % path)
    print("* report: %s" % report)
    print("* batch: %s" % batch)

    content = get_directory_content(path)
    files = []
    while len(content) > 0:
        item = content.pop(0)
        print("Current item:", item)
        if os.path.basename(item) in EXCEPTIONS:
            print("* Skipping exception")
            continue
        if os.path.isdir(item):
            print("* Listing directory")
            content += get_directory_content(item)
        else:
            print("* Reporting file")
            files.append(get_file_properties(item))
        if batch is not None and len(files) > 1 and len(files) % batch == 0:
            print("* Saving batch")
            save_report(files, report, "a")
            files = []

    if batch is not None:
        if len(files) > 1:
            save_report(files, report, "a")
    else:
        save_report(files, report, "w")


if __name__ == "__main__":
    main()
