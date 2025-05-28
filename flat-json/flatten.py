import json
import sys


def flatten_json(nested_json, separator="__"):
    flattened_json = {}

    def flatten(x, name=""):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f"{name}{a}{separator}")
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f"{name}{i}{separator}")
        else:
            flattened_json[name[:-2]] = x

    flatten(nested_json)
    return flattened_json


def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "en.json"
        output_file = "flat_en.json"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    flattened = flatten_json(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(flattened, f, indent=4)


if __name__ == "__main__":
    main()
