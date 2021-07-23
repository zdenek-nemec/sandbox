#!/usr/bin/env python3

class FixThreshold(object):
    """Fix Threshold"""

    def __init__(self, minimum):
        self._minimum = minimum

    def get_outliers(self, data):
        outliers = []
        for entry in data:
            if entry[1] < self._minimum:
                outliers.append(entry)
        return outliers


if __name__ == "__main__":
    pass
