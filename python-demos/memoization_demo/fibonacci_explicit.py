fibonacci_cache = {}


def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


def main():
    for n in range(1, 10):
        print(n, ":", fibonacci(n))


if __name__ == "__main__":
    main()
