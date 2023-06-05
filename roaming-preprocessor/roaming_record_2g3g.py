from datetime import datetime


class RoamingRecord2g3g(object):
    def __init__(self, data, columns: int):
        self._validate_input_data_type(data)
        self._validate_input_data_length(data, columns)

        self._timestamp = datetime.fromtimestamp(int(data[0]) / 1000.0)
        self._observation_domain = data[2]
        self._observation_point = data[3]
        self._direction = data[4]
        self._mtp3_variant = data[6]
        self._mtp3_opc = data[7]
        self._mtp3_dpc = data[8]
        self._mtp3_si = data[10]
        self._sccp_message_type = data[12]
        self._sccp_cgpa_gt_noa = data[20]
        self._sccp_cgpa_gt_digits = data[21]
        self._sccp_cdpa_gt_noa = data[27]
        self._sccp_cdpa_gt_digits = data[28]
        self._msu_length = data[11]

    @staticmethod
    def _validate_input_data_type(data):
        if type(data) is not list:
            raise TypeError(f"Expected input data to be a list, got {type(data)} instead")

    @staticmethod
    def _validate_input_data_length(data, columns: int):
        if len(data) != columns:
            raise ValueError(f"Expected CSV record with {columns} fields, got {len(data)} instead")

    def is_filtered(self):
        if (self._sccp_cgpa_gt_noa == "4"
                and self._sccp_cdpa_gt_noa == "4"
                and self._mtp3_si == "3"
                and self._mtp3_variant == "1"):
            return False
        else:
            return True
