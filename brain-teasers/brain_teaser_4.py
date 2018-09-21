# Swap two numbers without using third variable


def main():
    a = 2
    b = 3

    a = a + b
    b = a - b
    a = a - b
    print(a, b)


if __name__ == '__main__':
    main()
