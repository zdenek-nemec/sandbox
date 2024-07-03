from unittest import TestCase


def fake_bin(x: str) -> str:
    """Fake Binary
    https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
    """
    fx = lambda x: "0" if x < "5" else "1"
    return "".join([fx(c) for c in x])


def main():
    print("Fake Binary")

    print(f"{fake_bin('0123456789')}")

    TestCase().assertEqual("01011110001100111", fake_bin("45385593107843568"))
    TestCase().assertEqual("101000111101101", fake_bin("509321967506747"))
    TestCase().assertEqual("011011110000101010000011011", fake_bin("366058562030849490134388085"))
    TestCase().assertEqual("01111100", fake_bin("15889923"))
    TestCase().assertEqual("100111001111", fake_bin("800857237867"))


if __name__ == "__main__":
    main()
