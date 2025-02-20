from unittest import TestCase


def pipe_fix(nums: list) -> list:
    return list(range(min(nums), max(nums) + 1))


def main():
    print("Lario and Muigi Pipe Problem")

    print(f"{pipe_fix([1, 2, 3, 12])}")

    TestCase().assertEqual(pipe_fix([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
    TestCase().assertEqual(pipe_fix([1, 2, 3, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    TestCase().assertEqual(pipe_fix([6, 9]), [6, 7, 8, 9])
    TestCase().assertEqual(pipe_fix([-1, 4]), [-1, 0, 1, 2, 3, 4])
    TestCase().assertEqual(pipe_fix([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    main()
