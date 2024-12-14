# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

from unittest import TestCase

def nb_dig(n: int, d: int) -> int:
    return "".join([str(i**2) for i in range(0, n+1)]).count(str(d))


def main():
    print(nb_dig(10, 1))
    TestCase().assertEqual(nb_dig(5750, 0), 4700)
    TestCase().assertEqual(nb_dig(11011, 2), 9481)
    TestCase().assertEqual(nb_dig(12224, 8), 7733)
    TestCase().assertEqual(nb_dig(11549, 1), 11905)
    TestCase().assertEqual(nb_dig(14550, 7), 8014)
    TestCase().assertEqual(nb_dig(8304, 7), 3927)
    TestCase().assertEqual(nb_dig(10576, 9), 7860)
    TestCase().assertEqual(nb_dig(12526, 1), 13558)
    TestCase().assertEqual(nb_dig(7856, 4), 7132)
    TestCase().assertEqual(nb_dig(14956, 1), 17267)


if __name__ == "__main__":
    main()
