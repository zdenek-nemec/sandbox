#!/usr/bin/env python3


import logging


def main():
    """Demo of Python Logging module, see https://docs.python.org/3/howto/logging.html"""
    logging.basicConfig(filename="my_log.log")
    logging.warning("I am about to start")

    print("Hello, World!")


if __name__ == "__main__":
    main()
