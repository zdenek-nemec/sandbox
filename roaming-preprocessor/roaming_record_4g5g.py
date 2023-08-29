from datetime import datetime


class RoamingRecord4g5g(object):
    def __init__(self, data, columns: int):
        self._validate_input_data_type(data)
        self._validate_input_data_length(data, columns)

        try:
            self._timestamp = datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            self._timestamp = datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S:%f")
        self._direction = data[1]
        self._peername = data[2]
        self._hostname = data[3]
        self._original_realm = data[9]
        self._destination_realm = data[11]
        self._release_cause = data[20]

    @staticmethod
    def _validate_input_data_type(data):
        if type(data) is not list:
            raise TypeError(f"Expected input data to be a list, got {type(data)} instead")

    @staticmethod
    def _validate_input_data_length(data, columns: int):
        if len(data) != columns:
            raise ValueError(f"Expected CSV record with {columns} fields, got {len(data)} instead")

    @staticmethod
    def is_header():
        return False

    @staticmethod
    def is_filtered():
        return False
