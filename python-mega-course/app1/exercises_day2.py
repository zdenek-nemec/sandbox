def exercise1():
    user_input = input("Please enter your name: ")
    print(user_input.capitalize())


def exercise2():
    user_input = input("Please enter your name: ")
    i = 0
    while i < 5:
        print(user_input.capitalize())
        i += 1


def exercise3():
    user_input = ""
    while user_input != "stop":
        user_input = input("Please enter your name: ")
        print(user_input.capitalize())


def main():
    print("Hello, World!")
    # exercise1()
    # exercise2()
    exercise3()


if __name__ == "__main__":
    main()
