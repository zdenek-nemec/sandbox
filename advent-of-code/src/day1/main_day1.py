from unittest import TestCase


class Day1Part1:
    @staticmethod
    def _get_value(line: str) -> int:
        digits = [c for c in line if c.isdigit()]
        return int("".join([digits[0], digits[-1]]))

    def _sum_values(self, data: list[str]) -> int:
        return sum(map(self._get_value, data))

    def demo(self):
        print("_sum_values:")
        for entries in [
            ["1abc2"],
            ['treb7uchet'],
            ['1abc2', 'treb7uchet']
        ]:
            print(f"\t{entries} = {self._sum_values(entries)}")

    def test(self):
        data = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]
        TestCase().assertEqual(142, self._sum_values(data))

    def solve(self, file_path: str) -> int:
        data = []
        with open(file_path, "r") as input_file:
            for line in input_file:
                data.append(line)
        return self._sum_values(data)


class Day1Part2:
    def __init__(self):
        self.digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def _get_first(self, line: str) -> str | None:
        for i in range(len(line)):
            if line[i].isdigit():
                return line[i]
            for j, digit in enumerate(self.digits, start=1):
                if line[i:i + len(digit)] == digit:
                    return str(j)
        print("first", line)
        return None

    def _get_last(self, line: str) -> str | None:
        for i in range(len(line) + 1):
            if i:
                if line[-i].isdigit():
                    return line[-i]
            for j, digit in enumerate(self.digits, start=1):
                if line[-i - len(digit):][:len(digit)] == digit:
                    return str(j)
        print("last", line)
        return None

    def _sum_values(self, data: list[str]) -> int:
        total = 0
        for line in data:
            total += int(self._get_first(line) + self._get_last(line))
        return total

    def demo(self):
        data = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]
        print("_get_first:")
        for entry in data:
            print(f"\t{entry} {self._get_first(entry)}")
        print("_get_last:")
        for entry in data:
            print(f"\t{entry} {self._get_last(entry)}")

    def test(self):
        data = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]
        TestCase().assertEqual(281, self._sum_values(data))

    def solve(self, file_path: str) -> int:
        data = []
        with open(file_path, "r") as input_file:
            for line in input_file:
                data.append(line)
        return self._sum_values(data)


def main():
    print("Advent of Code 2023 - Day 1: Trebuchet?!")

    # Day1Part1().demo()
    Day1Part1().test()
    print(Day1Part1().solve("input.txt"))

    # Day1Part2().demo()
    Day1Part2().test()
    print(Day1Part2().solve("input.txt"))


if __name__ == "__main__":
    main()
