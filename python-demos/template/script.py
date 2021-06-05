#!/usr/bin/env python3

import random

DEFAULT_LUCKY_NUMBERS = [3, 7, 42]

class LuckyNumbers(object):
    """Lucky number generator"""

    def __init__(self, lucky_numbers):
        self.lucky_numbers = lucky_numbers

    def get_lucky_number(self):
        return random.choice(self.lucky_numbers)

def main():
    print("Hello, Script!")
    lucky_numbers = LuckyNumbers(DEFAULT_LUCKY_NUMBERS)
    print("Trending lucky number is %d" % lucky_numbers.get_lucky_number())


if __name__ == "__main__":
    main()
