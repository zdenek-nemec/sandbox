import argparse
import datetime
import os
import re

DEFAULT_OFFSET = 0.0
SUBTITLES_FILE_EXTENSIONS = [".srt"]
TIMESTAMP = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]"


def load_subtitles(file):
    with open(file, "r") as text_file:
        data = list(text_file)
    return data


def update_offset(data, offset):
    for index, entry in enumerate(data):
        if re.findall("^" + TIMESTAMP + " --> " + TIMESTAMP + "$", entry):
            start_time = datetime.datetime.strptime(entry[:12], "%H:%M:%S,%f")
            end_time = datetime.datetime.strptime(entry[17:-1], "%H:%M:%S,%f")
            start_time += datetime.timedelta(seconds=offset)
            end_time += datetime.timedelta(seconds=offset)
            data[index] = (
                    start_time.strftime("%H:%M:%S,%f")[:-3]
                    + " --> "
                    + end_time.strftime("%H:%M:%S,%f")[:-3]
                    + "\n"
            )


def save_updated(file, data):
    with open(file, "w") as text_file:
        for line in data:
            text_file.write(line)


def main():
    print("Subtitles Offset")

    argument_parser = argparse.ArgumentParser(prog="Subtitles Offset")
    argument_parser.add_argument("--offset", "-o", type=float, default=DEFAULT_OFFSET)
    offset = argument_parser.parse_args().offset
    print(f"Argument --offset = {offset}")

    file_list = list(filter(lambda filename: filename[-4:] in SUBTITLES_FILE_EXTENSIONS, os.listdir("original")))
    for file in file_list:
        data = load_subtitles("original/" + file)
        update_offset(data, offset)
        save_updated("updated/" + file, data)


if __name__ == "__main__":
    main()
