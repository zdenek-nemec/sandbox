#!/usr/bin/env python3

class FixThreshold(object):
    """Fix Threshold"""

    def __init__(self, minimum):
        if type(minimum) != int:
            raise TypeError("The minimum must be an integer")
        self._minimum = minimum

    def get_outliers(self, data):
        if type(data) != list:
            raise TypeError("Data must be a list")
        outliers = []
        for entry in data:
            if entry[1] < self._minimum:
                outliers.append(entry)
        return outliers


if __name__ == "__main__":
    pass
