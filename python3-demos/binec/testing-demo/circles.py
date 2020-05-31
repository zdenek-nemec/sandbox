from math import pi


def get_circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * radius ** 2


def main():
    print("Hello, World!")
    print(get_circle_area(42))


if __name__ == "__main__":
    main()
