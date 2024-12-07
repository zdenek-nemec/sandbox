def maps(a: list) -> list:
    return [i * 2 for i in a]


def main():
    print(f"{maps([1, 2])=}")

    from unittest import TestCase
    TestCase().assertEqual(maps([1, 2, 3]), [2, 4, 6])
    TestCase().assertEqual(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    TestCase().assertEqual(maps([]), [])


if __name__ == "__main__":
    main()

