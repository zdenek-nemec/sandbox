import random


DEFAULT_ITEMS = [3, 7, 42]


def main():
    items = DEFAULT_ITEMS
    print(random.choice(items))


if __name__ == "__main__":
    main()
