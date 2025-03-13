from unittest import TestCase

class FindTheCapitals(object):
    """https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def capitals(word: str) -> list:
        return [i for i, c in enumerate(word) if "A" <= c <= "Z"]

    def test(self):
        TestCase().assertEqual(self.capitals('CodEWaRs'), [0,3,4,6])

    def demo(self):
        print("Find the capitals")
        print(f"{self.capitals('Ahoj')=}")


def main():
    FindTheCapitals().demo()
    FindTheCapitals().test()


if __name__ == "__main__":
    main()
