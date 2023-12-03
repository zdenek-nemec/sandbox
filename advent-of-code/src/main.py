from src.day1.main_day1 import Day1Part1, Day1Part2
from src.day2.part1 import Day2Part1
from src.day2.part2 import Day2Part2


def main():
    print("Advent of Code 2023")

    for i, dp in enumerate([
        [Day1Part1, Day1Part2],
        [Day2Part1, Day2Part2],
    ], start=1):
        print(f"Day {i}, first {dp[0]().solve()}, second {dp[1]().solve()}")


if __name__ == "__main__":
    main()
