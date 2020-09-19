import argparse
import logging
import sys


class BusinessLogicsCheck(object):
    """docstring for BusinessLogicsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class BashScriptsCheck(object):
    """docstring for BashScriptsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class GdcScriptsCheck(object):
    """docstring for GdcScriptsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class ReferenceTablesCheck(object):
    """docstring for ReferenceTablesCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


class PortalsCheck(object):
    """docstring for PortalsCheck"""
    def __init__(self):
        pass

    def check(self):
        return "not implemented"


def main():
    argument_parser = argparse.ArgumentParser(prog="Intermediate Synchronisation")
    argument_parser.add_argument("--log_file", "-f")
    argument_parser.add_argument("--log_level", "-l", default="DEBUG", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    log_file = argument_parser.parse_args().log_file
    log_level = getattr(logging, argument_parser.parse_args().log_level, None)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    if log_file is None:
        logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
    else:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)

    logging.debug("main: Started")

    logging.debug("main: argument log_file = %s" % log_file)
    logging.debug("main: argument log_level = %s" % log_level)

    print("Setting up checks")
    business_logics_check = BusinessLogicsCheck()
    bash_scripts_check = BashScriptsCheck()
    gdc_scripts_check = GdcScriptsCheck()
    reference_tables_check = ReferenceTablesCheck()
    portals_check = PortalsCheck()

    print("Business logics check - %s" % business_logics_check.check())
    print("Bash scripts check - %s" % bash_scripts_check.check())
    print("GDC scripts check - %s" % gdc_scripts_check.check())
    print("Reference tables check - %s" % reference_tables_check.check())
    print("Portals check - %s" % portals_check.check())

    logging.debug("main: Finished")


if __name__ == "__main__":
    main()
