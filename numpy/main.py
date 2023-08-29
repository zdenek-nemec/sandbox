import numpy as np

def main():
    print("Hello, World!")

    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))

    b = np.array([6, 7, 8])
    print(b)
    print(type(b))


if __name__ == "__main__":
    main()
