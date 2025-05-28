import json
import sys


def unpack(data: dict) -> dict:
    result = {}
    for key, value in data.items():
        parts = key.split("__")
        current = result
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return result


def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "flat_en.json"
        output_file = "unpacked_en.json"

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    unpacked = unpack(data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(unpacked, f, indent=4)


if __name__ == "__main__":
    main()
