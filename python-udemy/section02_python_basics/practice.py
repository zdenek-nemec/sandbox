#!/usr/bin/env python3


def exercise_1():
    """Variables"""
    name = "John Snow"
    age = 29


def exercice_2():
    """Get Variable Value"""
    price = 10
    print(price)


def exercice_3():
    """Math Operators"""
    x = 1
    y = 2
    z = 3
    print(((x * y) ** z) / 8)


def exercice_4():
    """Simple Sum"""
    a = 1.0
    b = 2
    print(int(a + b))


def exercice_5():
    """Lists"""
    mylist = [1, 2, 3]


def exercice_6():
    """Indexing"""
    name = "John"
    print(name[2])


def exercice_7():
    """Slicing"""
    name = "John Smith"
    print(name[2:4])


def exercice_8():
    """More on Indexing"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(letters[-2])


def exercice_9():
    """More on Slicing"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(letters[-3:-1])


def main():
    exercise_1()
    exercice_2()
    exercice_3()
    exercice_4()
    exercice_5()
    exercice_6()
    exercice_7()
    exercice_8()
    exercice_9()


if __name__ == "__main__":
    main()
