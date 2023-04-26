from enum import Enum


class DataTypeEnum(Enum):
    DATA_2G_3G = 23
    DATA_4G_5G = 45


class DataType(object):
    def __init__(self, data_type: str):
        self._data_type = self._get_data_type(data_type)

    @staticmethod
    def _get_data_type(data_type: str) -> DataTypeEnum:
        if data_type == "2G/3G":
            return DataTypeEnum.DATA_2G_3G
        elif data_type == "4G/5G":
            return DataTypeEnum.DATA_4G_5G
        else:
            raise ValueError("Unexpected data type")

    def is_2g3g(self) -> bool:
        if self._data_type == DataTypeEnum.DATA_2G_3G:
            return True
        else:
            return False

    def is_4g5g(self) -> bool:
        if self._data_type == DataTypeEnum.DATA_4G_5G:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
