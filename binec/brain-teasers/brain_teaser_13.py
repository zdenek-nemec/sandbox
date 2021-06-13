# Find if a number is even or odd without using any conditional statement


def main():
    a = 12

    results = ['even', 'odd']
    print(results[a & 1])


if __name__ == '__main__':
    main()
