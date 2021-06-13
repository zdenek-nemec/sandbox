# Print all numbers between 1 to N without using any loop


N = 10


def print_number(n):
    print(n)
    if n < N:
        print_number(n + 1)


def main():
    print_number(1)


if __name__ == '__main__':
    main()
