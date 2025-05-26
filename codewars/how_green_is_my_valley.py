class HowGreenIsMyValley(object):
    """https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python"""
    def __init__(self):
        pass

    @staticmethod
    def make_valley(arr: list) -> list:
        arr_sorted = sorted(arr)
        odd = []
        even = []
        for i, item in enumerate(arr_sorted):
            if i % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
        if len(arr_sorted) % 2 == 0:
            return list(reversed(odd)) + even  # Because of tests
        else:
            return list(reversed(even)) + odd

    def demo(self):
        print("How Green Is My Valley?")
        print(f"{self.make_valley([5, 4, 3, 2, 1])=}")
        print(f"{self.make_valley([20, 7, 6, 2])=}")

    def test(self):
        from unittest import TestCase
        TestCase().assertEqual(self.make_valley([5, 4, 3, 2, 1]), [5, 3, 1, 2, 4])

        TestCase().assertEqual(self.make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]), [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17])
        TestCase().assertEqual(self.make_valley([20, 7, 6, 2]), [20, 6, 2, 7])
        TestCase().assertEqual(self.make_valley([14, 10, 8]), [14, 8, 10])
        TestCase().assertEqual(self.make_valley([20, 18, 17, 13, 12, 12, 10, 9, 4, 2, 2, 1, 1]), [20, 17, 12, 10, 4, 2, 1, 1, 2, 9, 12, 13, 18])
        TestCase().assertEqual(self.make_valley([20, 16, 14, 10, 1]), [20, 14, 1, 10, 16])
        TestCase().assertEqual(self.make_valley([19, 19, 18, 14, 12, 11, 9, 7, 4]), [19, 18, 12, 9, 4, 7, 11, 14, 19])
        TestCase().assertEqual(self.make_valley([20, 18, 16, 15, 14, 14, 13, 13, 10, 9, 4, 4, 4, 1]), [20, 16, 14, 13, 10, 4, 4, 1, 4, 9, 13, 14, 15, 18])
        TestCase().assertEqual(self.make_valley([20, 20, 16, 14, 12, 12, 11, 10, 3, 2]), [20, 16, 12, 11, 3, 2, 10, 12, 14, 20])
        TestCase().assertEqual(self.make_valley([19, 17, 16, 15, 13, 8, 5, 5, 4, 4, 4]), [19, 16, 13, 5, 4, 4, 4, 5, 8, 15, 17])
        TestCase().assertEqual(self.make_valley([19, 8, 6]), [19, 6, 8])


def main():
    HowGreenIsMyValley().demo()
    HowGreenIsMyValley().test()


if __name__ == "__main__":
    main()
