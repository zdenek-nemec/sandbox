# Multiply two numbers without using multiplication operator or loops


def add(number, count):
    if count == 0:
        return 0
    return number + add(number, count - 1)


def main():
    a = 3
    b = 5

    if b < 0:
        result = add(a, abs(b))
        result = -result
    else:
        result = add(a, b)
    print(result)


if __name__ == '__main__':
    main()
