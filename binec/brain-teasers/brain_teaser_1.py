# Add two numbers without using addition operator


def main():
    a = 2
    b = 3

    print(a - (-b))

    value = 0
    for i in range(0, abs(a)):
        if a > 0:
            value -= -1
        else:
            value -= 1
    for i in range(0, abs(b)):
        if b > 0:
            value -= -1
        else:
            value -= 1
    print(value)


if __name__ == '__main__':
    main()
