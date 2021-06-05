import json


DEFAULT_FILENAME = "input_test_file_json_lines.txt"


def main():
    filename = DEFAULT_FILENAME
    with open(filename, "r") as text_file:
        for line in text_file:
            print(json.loads(line))


if __name__ == "__main__":
    main()
