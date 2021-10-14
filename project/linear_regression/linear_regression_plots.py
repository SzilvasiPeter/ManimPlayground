import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

def plot_2dcost_m(x, y):
    m = np.linspace(0.85, 1.35, 10)
    b = -3.6303

    cost_m = []
    for i in range(len(m)):
        cost_m.append((1/len(x)) * sum(((m[i] * x + b) - y) ** 2))

    print(cost_m)
    plt.plot(m, cost_m)
    plt.show()

def plot_2dcost_b(x, y):
    m = 1.1664
    b = np.linspace(-5, -2, 10)

    cost_m = []
    for i in range(len(m)):
        cost_m.append((1/len(x)) * sum(((m[i] * x + b) - y) ** 2))

    print(cost_m)
    plt.plot(m, cost_m)
    plt.show()

def plot_3dcost(x, y):
    M, B, Z = calculate_3dcost(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(M, B, Z, rstride=1, cstride=1, color='b', alpha=0.5)
    ax.set_xlabel('m')
    ax.set_ylabel('b')
    ax.set_zlabel('error')

    plt.show()

def plot_cost_contour(x, y):
    M, B, Z = calculate_3dcost(x, y)

    fig,ax=plt.subplots(1,1)
    cp = ax.contourf(M, B, Z, 40)
    fig.colorbar(cp)

    plt.show()

def calculate_3dcost(x, y):
    Point = collections.namedtuple('Point', ['x', 'y'])

    points = [Point(x, y) for x, y in zip(x, y)]

    ms = np.linspace(1.1664-0.5, 1.1664+0.5, 10)
    bs = np.linspace(-3.6303-2, -3.6303+2, 10)

    M, B = np.meshgrid(ms, bs)
    zs = np.array([error(mp, bp, points) 
                for mp, bp in zip(np.ravel(M), np.ravel(B))])
    Z = zs.reshape(M.shape)
    return M,B,Z

def error(m, b, points):
    totalError = 0
    for i in range(0, len(points)):
        totalError += ((m * points[i].x + b) - points[i].y) ** 2
    return totalError / float(len(points))

data = pd.read_csv('ex1data1.txt', names=['X', 'Y'])
x = data.iloc[:,0]
y = data.iloc[:,1]

# plot_2dcost_m(x, y)
# plot_2dcost_b(x, y)
# plot_3dcost(x, y)
# plot_cost_contour(x, y)
