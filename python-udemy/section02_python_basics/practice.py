#!/usr/bin/env python3


def exercise_1():
    """Variables"""
    name = "John Snow"
    age = 29


def exercise_2():
    """Get Variable Value"""
    price = 10
    print(price)


def exercise_3():
    """Math Operators"""
    x = 1
    y = 2
    z = 3
    print(((x * y) ** z) / 8)


def exercise_4():
    """Simple Sum"""
    a = 1.0
    b = 2
    print(int(a + b))


def exercise_5():
    """Lists"""
    mylist = [1, 2, 3]


def exercise_6():
    """Indexing"""
    name = "John"
    print(name[2])


def exercise_7():
    """Slicing"""
    name = "John Smith"
    print(name[2:4])


def exercise_8():
    """More on Indexing"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(letters[-2])


def exercise_9():
    """More on Slicing"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(letters[-3:-1])


def exercise_10():
    """List Indexing"""
    mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(mylist[17])


def exercise_11():
    """Append to List"""
    mylist = ["Marry", "Jack"]
    mylist.append("John")


def exercise_12():
    """Remove from List"""
    mylist = ["Marry", "Jack", "John"]
    mylist.remove("John")


def exercise_13():
    """Append from List to List"""
    list1 = [1.2323442655, 1.4534345567, 1.023458894]
    list2 = [1.9934332091]
    list2.append(list1[-1])


def exercise_14():
    """Concatenating List Items"""
    mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    c = mylist[-1] + mylist[0]


def exercise_15():
    """Create Dictionary"""
    mydict = {"a": 1, "b": 2}


def hello_world():
    """Create Function"""
    return "Hello World"


def power(a):
    return a ** 2


def calculate_length(text):
    if type(text) is int:
        print("Sorry, integers don't have length")
    elif type(text) is float:
        print("Sorry, floats don't have length")
    else:
        return len(text)


def mysum(a, b):
    """Sum up Function"""
    return a + b


def converter(kg, coef=2.20462):
    """Function with Default Parameters"""
    return kg * coef


def celsius_to_fahrenheit(celsius):
    """Weather Function"""
    return celsius * 9 / 5 + 32


def reading_files():
    """Reading Files"""
    with open("fruits.txt", "r") as input_file:
        content = input_file.read()
        print(content)


def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    # exercise_11()
    # exercise_12()
    # exercise_13()
    # exercise_14()
    # exercise_15()
    # print(calculate_length("Hello"))
    # print(mysum(3, 2))
    # print(mysum(10, 20))
    # print(converter(10))
    # print(celsius_to_fahrenheit(20))
    # print(calculate_length("Bye"))
    # calculate_length(10)
    # calculate_length(10.0)
    reading_files()


if __name__ == "__main__":
    main()
