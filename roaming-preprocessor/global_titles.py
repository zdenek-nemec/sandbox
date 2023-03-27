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
                if entry_type == "GT":
                    data[value] = tadig
        return data

    def get_tadig(self, phone_number):
        for length in range(len(phone_number), 1, -1):
            if (prefix := phone_number[0:length]) in self._data.keys():
                return self._data[prefix]
        else:
            return None


if __name__ == "__main__":
    pass