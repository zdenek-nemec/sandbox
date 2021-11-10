import datetime
import re

DEFAULT_OFFSET = 3.5


def load_subtitles(file):
    with open(file, "r") as text_file:
        data = list(text_file)
    return data


def update_offset(data, offset):
    for index, entry in enumerate(data):
        if re.findall(
                "^[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]$",
                entry):
            start_time = datetime.datetime.strptime(entry[:12], "%H:%M:%S,%f")
            end_time = datetime.datetime.strptime(entry[17:-1], "%H:%M:%S,%f")
            start_time += datetime.timedelta(seconds=offset)
            end_time += datetime.timedelta(seconds=offset)
            data[index] = start_time.strftime("%H:%M:%S,%f")[:-3] + " --> " + end_time.strftime("%H:%M:%S,%f")[:-2]


def main():
    print("Subtitles Offset")

    data = load_subtitles("original/Stargate.SG-1.S06E01.1080p.BluRay.x264-BORDURE Cz dabing.srt")
    print("Loaded:  ", end="")
    [print(entry[:-1]) for entry in data[:2] if entry[:3] == "00:"]
    update_offset(data, DEFAULT_OFFSET)
    print("Updated: ", end="")
    [print(entry[:-1]) for entry in data[:2] if entry[:3] == "00:"]


if __name__ == "__main__":
    main()
