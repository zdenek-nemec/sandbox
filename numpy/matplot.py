import numpy as np
import matplotlib.pyplot as plt


def plot_array():
    a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    plt.plot(a)
    plt.show()


def plot_with_colours():
    x = np.linspace(0, 5, 20)
    y = np.linspace(0, 10, 20)
    plt.plot(x, y, 'purple') # line
    plt.plot(x, y, 'o')      # dots
    plt.show()


def plot_3d():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    X = np.arange(-5, 5, 0.15)
    Y = np.arange(-5, 5, 0.15)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
    plt.show()


def main():
    """https://numpy.org/devdocs/user/absolute_beginners.html"""
    print("Matplotlib Demos")

    # plot_array()
    # plot_with_colours()
    plot_3d()


if __name__ == "__main__":
    main()
