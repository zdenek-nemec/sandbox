import numpy as np


def main():
    """https://numpy.org/devdocs/user/quickstart.html"""
    print("NumPy Demos")

    a = np.arange(15)
    print(a)
    print("---")

    # Do not change the shape permanently
    print(a.reshape(3, 5))
    print(a.shape)
    print("---")

    # Change the shape permanently
    a.resize(3, 5)
    print(a)
    print(a.shape)
    print("---")

    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))
    print("---")

    # Iterate over all elements
    for element in a.flat:
        print(element)
    print("---")

    print(a.flat)  # Iterator
    print(a.ravel())  # Get flattened array
    print(a.shape)  # Shape unchanged
    print(a.T)  # Transpose
    print(a.T.shape)
    print(a.shape)
    print("---")

    b = np.array([6, 7, 8])
    print(b)
    print(type(b))
    print("---")

    # Random integers 0-4
    rg = np.random.default_rng()
    print(rg.integers(5, size=(2, 4)))


if __name__ == "__main__":
    main()
