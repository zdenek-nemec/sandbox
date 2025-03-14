from unittest import TestCase

class MaximumLengthDifference(object):
    """https://www.codewars.com/kata/5663f5305102699bad000056/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def mxdiflg(a1: list, a2: list) -> int:
        if len(a1) == 0 or len(a2) == 0:
            return -1
        a1_len = [len(s) for s in a1]
        a1_min = min(a1_len)
        a1_max = max(a1_len)
        a2_len = [len(s) for s in a2]
        a2_min = min(a2_len)
        a2_max = max(a2_len)
        return max(abs(a2_max - a1_min), abs(a1_max - a2_min))

    def test(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        TestCase().assertEqual(self.mxdiflg(s1, s2), 13)
        s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
        s2 = ["bbbaaayddqbbrrrv"]
        TestCase().assertEqual(self.mxdiflg(s1, s2), 10)
        s2 = []
        s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        TestCase().assertEqual(self.mxdiflg(s1, s2), -1)


    def demo(self):
        print("Maximum Length Difference")
        print(f"{self.mxdiflg(['a', 'aaa'], ['b', 'bbbb'])=}")


def main():
    MaximumLengthDifference().demo()
    MaximumLengthDifference().test()


if __name__ == "__main__":
    main()
