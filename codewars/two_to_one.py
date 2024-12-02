# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/python

from unittest import TestCase


def longest(a1: str, a2: str) -> str:
    return "".join(sorted(set(a1 + a2)))


def main():
    print(longest("hello", "ahoj"))
    print(longest("aretheyhere", "yestheyarehere"))

    TestCase().assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
    TestCase().assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
    TestCase().assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


if __name__ == "__main__":
    main()
