import random

from multipledispatch import dispatch


class RandomNumbers(object):
    def __init__(self):
        super(RandomNumbers, self).__init__()

    @dispatch()
    def get_integer(self):
        return self.get_integer(0, 10)

    @dispatch(int)
    def get_integer(self, maximum):
        return self.get_integer(0, maximum)

    @dispatch(int, int)
    def get_integer(self, minimum, maximum):
        return random.randint(minimum, maximum)


class Squares(object):
    def __init__(self):
        super(Squares, self).__init__()

    def get_square(self, side):
        return side ** 2

    def get_random_square(self):
        return RandomNumbers().get_integer() ** 2


def main():
    print("Application")
    print(RandomNumbers().get_integer(10, 99))
    print(RandomNumbers().get_integer(10))
    print(Squares().get_square(2))
    print(Squares().get_random_square())


if __name__ == "__main__":
    main()
