#!/usr/bin/env python3


import argparse


DEFAULT_FILENAME = "get_longest_line.py"


def main():
    parser = argparse.ArgumentParser(prog="get_longest_line")
    parser.add_argument('--filename', '-f', default=DEFAULT_FILENAME)
    filename = parser.parse_args().filename

    with open(filename, "r") as input_file:
        longest_length = 0
        longest_line = ""
        for line in input_file:
            current_length = len(line) - 1
            if current_length > longest_length:
                longest_length = current_length
                longest_line = line[:-1]
        input_file.close()

    print("Length %d, line \"%s\"" % (longest_length, longest_line))


if __name__ == "__main__":
    main()
