import json


DEFAULT_FILENAME = "input_test_file.json"


def main():
    filename = DEFAULT_FILENAME
    with open(filename) as json_file:
        print(json.load(json_file))


if __name__ == "__main__":
    main()
