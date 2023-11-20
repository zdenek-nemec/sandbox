from unittest import TestCase as tc


class AlphabetSymmetry:
    """https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python"""
    def __init__(self):
        pass

    def _solve_a(self, array: list[str]) -> list[int]:
        symmetric = []
        for i, string in enumerate(array):
            symmetric.append(0)
            for j, c in enumerate(string.lower()):
                if j == ord(c) - ord("a"):
                    symmetric[i] += 1
        return symmetric

    def _solve_b(self, array: list[str]) -> list[int]:
        symmetric = []
        for i, string in enumerate(array):
            symmetric.append(len([c for j, c in enumerate(string.lower()) if j == ord(c) - ord("a")]))
        return symmetric

    def _solve_c(self, array: list[str]) -> list[int]:
        return [len([c for i, c in enumerate(string.lower()) if i == ord(c) - ord("a")]) for string in array]

    def solve(self, array: list[str]) -> list[int]:
        return self._solve_c(array)

    def demo(self):
        print(self.solve([]))
        print(self.solve(["abode", "ABc", "xyzD"]))

    def test(self):
        tc().assertEqual(self.solve(["abode", "ABc", "xyzD"]), [4,3,1])
        tc().assertEqual(self.solve(["abide", "ABc", "xyz"]), [4,3,0])
        tc().assertEqual(self.solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"]), [6,5,7])
        tc().assertEqual(self.solve(["encode", "abc", "xyzD", "ABmD"]), [1, 3, 1, 3])


class Testing123:
    """https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def number(lines: list) -> list:
        return [f"{i}: {line}" for i, line in enumerate(lines, 1)]

    def demo(self):
        print(self.number([]))
        print(self.number(["a", "b", "c"]))

    def test(self):
        tc().assertEqual(self.number([]), [])
        tc().assertEqual(self.number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])


def main():
    print("Codewars")

    # AlphabetSymmetry().demo()
    # AlphabetSymmetry().test()

    Testing123().demo()
    Testing123().test()


if __name__ == "__main__":
    main()
