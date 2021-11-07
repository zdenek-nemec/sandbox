#!/usr/bin/env python3


import datetime

from log import Log
from config import Config
from collector import Collector
from validator import Validator


def test_config_default_config_file_is_missing():
    # Tested by deleting the default.cfg
    pass


def test_config_config_file_is_missing():
    config = Config()
    config.load("non-existant.cfg")


def test_config_config_file_is_invalid():
    config = Config()
    config.load("bad.cfg")


def test_config_save_request_is_invalid():
    config = Config()
    config.generate("test.cfg")
    config.save(123)


def test_config_unable_to_save_the_config_file():
    config = Config()
    config.generate("c:/Zdenek/_tmp/nonexistant/new_config.cfg")
    config.save()


def test_config_list_of_active_transfers_is_corrupted():
    config = Config()
    config.load("corrupted_transfers.cfg")


def test_config_generate_filename():
    # Covered by unit tests in test_config.py
    pass


def test_collector_invalid_connection_request():
    collector = Collector()
    collector.connect(host=None, username=None, password=None)


def test_collector_unknown_host():
    collector = Collector()
    collector.connect(host="unknown_host", username="username", password="password")


def test_collector_wrong_credentials():
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="blahblah")


def test_collector_download_success():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path="/home/fastfile/ewsd", filename=filename, destination_path="c:\\Zdenek\\_tmp\\")


def test_collector_download_invalid_request():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path=None, filename=None, destination_path=None)


def test_collector_download_source_path_does_not_exist():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path="/home/fastfile/ewsd/nonexistant", filename=filename, destination_path="c:\\Zdenek\\_tmp\\")


def test_collector_download_destination_path_does_not_exist():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path="/home/fastfile/ewsd", filename=filename, destination_path="c:\\Zdenek\\_tmp\\nonexistant\\")


def test_collector_download_file_does_not_exist():
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path="/home/fastfile/ewsd", filename="nonexistant", destination_path="c:\\Zdenek\\_tmp\\")


def test_collector_download_insufficient_permissions_on_requested_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.download(path="/home/fastfile/ewsd", filename=filename, destination_path="c:\\Zdenek\\_tmp\\")


def test_collector_delete_success():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.delete(path="/home/fastfile/transfer", filename=filename)


def test_collector_delete_invalid_request():
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.delete(path=None, filename=None)


def test_collector_delete_source_path_does_not_exist():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.delete(path="/home/fastfile/nonexistant", filename=filename)


def test_collector_delete_file_does_not_exist():
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.delete(path="/home/fastfile/transfer", filename="nonexistant")


def test_collector_delete_insufficient_permissions_on_requested_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d.%H")
    uta_label = "#" + "M.U1" + "." + timestamp + "#"
    filename = "ia.icama." + uta_label + ".zip"
    collector = Collector()
    collector.connect(host="192.168.179.130", username="fastfile", password="XPB8YHuBihsR")
    collector.delete(path="/home/fastfile/transfer", filename=filename)


def test_validator_file_exists():
    # Covered by unit tests in test_config.py
    pass


def test_validator_file_does_not_exist():
    # Covered by unit tests in test_config.py
    pass


def test_validator_file_is_zip():
    # Covered by unit tests in test_config.py
    pass


def test_validator_file_is_not_zip():
    # Covered by unit tests in test_config.py
    pass


def test_validator_zip_is_empty():
    # Covered by unit tests in test_config.py
    pass


def test_validator_zip_contains_more_than_one_file():
    # Covered by unit tests in test_config.py
    pass


def test_validator_ewsd_file_is_valid():
    # Covered by unit tests in test_config.py
    pass


def test_validator_ewsd_file_is_not_valid():
    # Covered by unit tests in test_config.py
    pass


def main():
    pass
    # test_config_default_config_file_is_missing()
    # test_config_config_file_is_missing()
    # test_config_config_file_is_missing()
    # test_config_save_request_is_invalid()
    # test_config_unable_to_save_the_config_file()
    test_config_list_of_active_transfers_is_corrupted()
    # test_config_generate_filename()
    # test_collector_invalid_connection_request()
    # test_collector_unknown_host()
    # test_collector_wrong_credentials()
    # test_collector_download_success()
    # test_collector_download_invalid_request()
    # test_collector_download_source_path_does_not_exist()
    # test_collector_download_destination_path_does_not_exist()
    # test_collector_download_file_does_not_exist()
    # test_collector_download_insufficient_permissions_on_requested_file()
    # test_collector_delete_success()
    # test_collector_delete_invalid_request()
    # test_collector_delete_source_path_does_not_exist()
    # test_collector_delete_file_does_not_exist()
    # test_collector_delete_insufficient_permissions_on_requested_file()
    # test_validator_file_exists()
    # test_validator_file_does_not_exist()
    # test_validator_file_is_zip()
    # test_validator_file_is_not_zip()
    # test_validator_zip_is_empty()
    # test_validator_zip_contains_more_than_one_file()
    # test_validator_ewsd_file_is_valid()
    # test_validator_ewsd_file_is_not_valid()


if __name__ == "__main__":
    main()
