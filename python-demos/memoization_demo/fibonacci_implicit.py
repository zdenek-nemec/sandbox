from functools import lru_cache


@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    for n in range(1, 10):
        print(n, ":", fibonacci(n))


if __name__ == "__main__":
    main()
