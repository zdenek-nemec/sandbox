# https://www.codewars.com/kata/586c1cf4b98de0399300001d

from unittest import TestCase


def combat(health: int, damage: int) -> int:
    if damage >= health:
        return 0
    else:
        return health - damage


def main():
    print(f"{combat(100, 5)=}")
    print(f"{combat(100, 105)=}")

    TestCase().assertEqual(combat(100, 5), 95)
    TestCase().assertEqual(combat(83, 16), 67)
    TestCase().assertEqual(combat(20, 30), 0)


if __name__ == "__main__":
    main()
