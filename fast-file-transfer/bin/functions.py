#!/usr/bin/env python3


import logging


def check_filename(filename):
	if type(filename) != str:
		logging.critical("Invalid filename")
		raise TypeError


def normalise_path(path):
    if type(path) != str:
        logging.critical("Invalid path")
        raise TypeError
    normalised = path.replace("\\", "/")
    if normalised[-1] == "/":
        return normalised[:-1]
    else:
        return normalised


if __name__ == "__main__":
    pass
