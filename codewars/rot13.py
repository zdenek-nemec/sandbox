# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

from unittest import TestCase


def rot13(message: str) -> str:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fl = lambda c: lower[(lower.index(c) + 13) % len(lower)] if c in lower else c
    fu = lambda c: upper[(upper.index(c) + 13) % len(upper)] if c in upper else c
    return "".join([fu(fl(c)) for c in message])


def main():
    print("Rot13")

    print(f"{rot13('Ahoj')=}")


    TestCase().assertEqual(rot13("test"), "grfg")
    TestCase().assertEqual(rot13("Test"), "Grfg")
    TestCase().assertEqual(rot13("aA bB zZ 1234 *!?%"), "nN oO mM 1234 *!?%")


if __name__ == "__main__":
    main()
