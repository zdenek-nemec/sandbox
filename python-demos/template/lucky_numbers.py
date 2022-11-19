import random


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


if __name__ == "__main__":
    pass
