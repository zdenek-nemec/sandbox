# Find square of a number without using multiplication and division operator


def main():
    a = -10
    if a < 0:
        a = abs(a)
    square = 0
    for i in range(0, a):
        square += a
    print(square)


if __name__ == '__main__':
    main()
