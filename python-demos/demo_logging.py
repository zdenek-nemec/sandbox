#!/usr/bin/env python3


import logging
import sys


def main():
    # logging.basicConfig(filename="test.log", level=logging.DEBUG)
    # logger = logging.getLogger()
    # logger.info("First message")


    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.info("nla")



if __name__ == "__main__":
    main()
