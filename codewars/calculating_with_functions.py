from unittest import TestCase as tc
from typing import Callable


ZDENEK, LARS = True, False


if ZDENEK:
    def plus(value: int) -> int:
        return lambda x: x + value


    def minus(value: int) -> int:
        return lambda x: x - value


    def times(value: int) -> int:
        return lambda x: x * value


    def divided_by(value: int) -> int:
        return lambda x: x // value


    def _digit(value: int, operator: Callable[[int], int]) -> int:
        if operator is None:
            return value
        else:
            return operator(value)

    for value, digit_name in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        exec(f"""def {digit_name}(operator: Callable[[int], int] = None) -> int:
                     return _digit({value}, operator)
              """)


if LARS:
    def identity(a): return a

    def zero(f=identity): return f(0)
    def one(f=identity): return f(1)
    def two(f=identity): return f(2)
    def three(f=identity): return f(3)
    def four(f=identity): return f(4)
    def five(f=identity): return f(5)
    def six(f=identity): return f(6)
    def seven(f=identity): return f(7)
    def eight(f=identity): return f(8)
    def nine(f=identity): return f(9)

    def plus(b): return lambda a: a + b
    def minus(b): return lambda a: a - b
    def times(b): return lambda a: a * b
    def divided_by(b): return lambda a: a // b


class CalculatingWithFunctions:
    """https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python"""
    def demo(self):
        print(two(plus(three())))
        print(two(minus(three())))
        print(two(times(three())))
        print(two(divided_by(three())))

    def test(self):
        tc().assertEqual(seven(times(five())), 35)
        tc().assertEqual(four(plus(nine())), 13)
        tc().assertEqual(eight(minus(three())), 5)
        tc().assertEqual(six(divided_by(two())), 3)


def main():
    print("Calculating with Functions")

    CalculatingWithFunctions().demo()
    CalculatingWithFunctions().test()


if __name__ == "__main__":
    main()
