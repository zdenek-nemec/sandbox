#!/usr/bin/env python3


import logging


class MyClass(object):
    def __init__(self):
        logging.info("Initiating MyClass")
        self._lucky_number = None

    def set_lucky_number(self, number):
        logging.debug("Setting MyClass._lucky_number to %d", number)
        self._lucky_number = number


if __name__ == "__main__":
    pass
