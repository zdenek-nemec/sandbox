from unittest import TestCase


def round_to_next5(n: int) -> int:
    print(n%5)
    return n + 5 - rem if (rem := n % 5) else n


def main():
    print("Round up to the next multiple of 5")

    print(f"{round_to_next5(12)=}")
    print(f"{round_to_next5(15)=}")
    print(f"{round_to_next5(-7)=}")
    print(f"{round_to_next5(-1)=}")

    TestCase().assertEqual(round_to_next5(0), 0)
    TestCase().assertEqual(round_to_next5(2), 5)
    TestCase().assertEqual(round_to_next5(3), 5)
    TestCase().assertEqual(round_to_next5(12), 15)
    TestCase().assertEqual(round_to_next5(21), 25)
    TestCase().assertEqual(round_to_next5(30), 30)
    TestCase().assertEqual(round_to_next5(-2), 0)
    TestCase().assertEqual(round_to_next5(-5), -5)


if __name__ == "__main__":
    main()
