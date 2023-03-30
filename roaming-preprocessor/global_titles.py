import csv


class GlobalTitles(object):
    def __init__(self, path):
        self._path = path
        self._data = self._load(path)

    def _load(self, path):
        data = {}
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            for row in reader:
                tadig, entry_type, value = row
                if value not in data.keys():
                    data[value] = tadig
        return data

    def get_tadig(self, phone_number, default_value=None):
        for length in range(len(phone_number), 1, -1):
            if (prefix := phone_number[0:length]) in self._data.keys():
                return prefix, self._data[prefix]
        else:
            return phone_number[0:6], default_value


if __name__ == "__main__":
    pass
