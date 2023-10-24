import numpy as np


def create_matrix():
    print("Define")
    a = np.array([[0, 1],
                  [2, 3]])
    print(a)

    print("Ones")
    b = np.ones((2, 3), dtype=int)
    print(b)

    print("Zeros")
    c = np.zeros((2, 3), dtype=int)
    print(c)

    print("Random")
    rg = np.random.default_rng(1)
    d = rg.random((2, 3))
    print(d)


def basic_operations():
    rg = np.random.default_rng()
    a = np.floor(rg.random((2, 3)) * 10).astype(int)
    print(a)

    print("Add to all")
    print(a + 1)

    print("Substract from all")
    print(a - 2)

    print("Multiply all")
    print(a * 3)

    print("Divide all")
    print(a / 4)

    print("Power all")
    print(a ** 2)

    print("Compare all")
    print(a < 5)

    print("Sinus")
    print(np.sin(a))


def matrix_operations():
    a = np.array([[0, 1],
                  [2, 3]])
    b = np.array([[4, 5],
                  [6, 7]])

    print("Elementwise product")
    print(a * b)

    print("Matrix product")
    print(a @ b)
    print(a.dot(b))  # Alternative


def main():
    """https://numpy.org/devdocs/user/quickstart.html"""
    print("NumPy Matrix Demos")

    # create_matrix()
    # basic_operations()
    matrix_operations()


if __name__ == "__main__":
    main()
