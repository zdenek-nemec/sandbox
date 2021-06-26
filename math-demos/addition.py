from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import csv
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


MINIMUM = -5
MAXIMUM = 5
OUTPUT_FILENAME = "addition.csv"
HEADER = ["x", "y", "x+y"]


def main():
    print("Hello, Addition!")

    data = []
    for x in range(MINIMUM, MAXIMUM+1):
        for y in range(MINIMUM, MAXIMUM+1):
            data.append((x, y, x+y))

    print("Entries:", len(data))
    # [print(entry) for entry in data]

    # with open(OUTPUT_FILENAME, "w", newline="") as csv_file:
    #     writer = csv.writer(csv_file, delimiter=",")
    #     writer.writerow(HEADER)
    #     for entry in data:
    #         writer.writerow(entry)

    x = [entry[0] for entry in data]
    y = [entry[1] for entry in data]
    z = [entry[2] for entry in data]

    # data = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
    #         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
    #        }

    # df = pd.DataFrame(data,columns=['Unemployment_Rate','Stock_Index_Price'])
    df = pd.DataFrame({"x": x, "y": y, "z": z})
    print(df)

    # df.plot(x ='Unemployment_Rate', y='Stock_Index_Price', kind = 'scatter')

    # fig = plt.figure()
    # ax = Axes3D(fig)
    # surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # ax.plot_trisurf(df.x, df.y, df.z, cmap=cm.jet, linewidth=0.2)
    # plt.show()

    # X = np.arange(-5, 5, 0.25)
    X = x
    # Y = np.arange(-5, 5, 0.25)
    Y = y
    X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    Z = np.add(X, Y)
    # Z = np.subtract(X, Y)
    # Z = np.multiply(X, Y)
    fig = plt.figure()
    ax = Axes3D(fig)
    # surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, antialiased=False, rstride=5, cstride=5)
    # ax.set_zlim(-25, 25)

    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title('Original Code')
    plt.show()




if __name__ == "__main__":
    main()
