import random


DEFAULT_LUCKY_NUMBERS = [3, 7, 42]


class LuckyNumbers(object):
    """Storage of lucky numbers"""

    def __init__(self, lucky_numbers):
        self.lucky_numbers = lucky_numbers

    def get_lucky_number(self):
        return random.choice(self.lucky_numbers)


def main():
    print("Hello, World!")
    lucky_numbers = LuckyNumbers(DEFAULT_LUCKY_NUMBERS)
    print("Trending lucky number is %d" % lucky_numbers.get_lucky_number())


if __name__ == "__main__":
    main()
