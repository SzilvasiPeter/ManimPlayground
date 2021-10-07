import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import collections

def plot_mesh(x, y):
    Point = collections.namedtuple('Point', ['x', 'y'])

    points = [Point(x, y) for x, y in zip(x, y)]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ms = np.linspace(1.1664-1, 1.1664+1, 10)
    bs = np.linspace(-3.6303-1, -3.6303+1, 10)

    M, B = np.meshgrid(ms, bs)
    zs = np.array([error(mp, bp, points) 
                for mp, bp in zip(np.ravel(M), np.ravel(B))])
    Z = zs.reshape(M.shape)

    ax.plot_surface(M, B, Z, rstride=1, cstride=1, color='b', alpha=0.5)

    ax.set_xlabel('m')
    ax.set_ylabel('b')
    ax.set_zlabel('error')

    plt.show()

def error(m, b, points):
    totalError = 0
    for i in range(0, len(points)):
        totalError += ((m * points[i].x + b) - points[i].y) ** 2
    return totalError / float(len(points))

data = pd.read_csv('ex1data1.txt', names=['X', 'Y'])
x = data.iloc[:,0]
y = data.iloc[:,1]

plot_mesh(x, y)
# linspace = np.linspace(0, 30, 100)
# m = 1.164
# b = -20
# lineX = m*linspace + b

# totalError = (1/len(x)) * sum(((m * x + b) - y) ** 2)
# print(totalError)

# plt.scatter(x, y)
# plt.plot(linspace, lineX)
# plt.show()

