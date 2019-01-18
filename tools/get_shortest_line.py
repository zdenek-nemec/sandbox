#!/usr/bin/env python3


import argparse


DEFAULT_FILENAME = "get_shortest_line.py"


def main():
    parser = argparse.ArgumentParser(prog="get_shortest_line")
    parser.add_argument('--filename', '-f', default=DEFAULT_FILENAME)
    filename = parser.parse_args().filename

    with open(filename, "r") as input_file:
        shortest_length = None
        shortest_line = None
        for line in input_file:
            current_length = len(line) - 1
            if shortest_length == None:
                shortest_length = current_length
                shortest_line = line[:-1]
            elif current_length < shortest_length:
                shortest_length = current_length
                shortest_line = line[:-1]
        input_file.close()

    print("Length %d, line \"%s\"" % (shortest_length, shortest_line))


if __name__ == "__main__":
    main()
