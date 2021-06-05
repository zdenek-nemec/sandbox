#!/usr/bin/env python3

import random

DEFAULT_NUMBER_LIST = [-3, 0, 3, 3.14159, 4+2j, 7, "Seven", 13, 21, 42]


class LuckyNumbers(object):
    """Lucky number generator"""

    def __init__(self, number_list):
        if type(number_list) != list:
            raise TypeError("A list of numbers must be provided")
        elif len(number_list) == 0:
            raise ValueError("The list of numbers cannot be empty")
        else:
            self._number_list = number_list

    def get_lucky_number(self):
        return random.choice(self._number_list)


def main():
    print("Hello, Lucky Numbers!")
    lucky_numbers = LuckyNumbers(DEFAULT_NUMBER_LIST)
    print("Trending lucky number is " + str(lucky_numbers.get_lucky_number()))


if __name__ == "__main__":
    main()
