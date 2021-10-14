import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# J = 1/2m * sum((h_x - y).^2)
def cost(x, y, thetas) -> float:
    h_x = thetas[0] + thetas[1] * x + thetas[2] * x**2
    J = (1/(2*len(x))) * sum((h_x - y)**2)
    
    return J

# thetas = (X^T * X)^-1 * X^T * y
def normal_equation(x, y):
    x_new = np.array([np.ones(len(x)), x.array, x.array ** 2, x.array ** 3]).T
    thetas = np.linalg.inv(x_new.T.dot(x_new)).dot(x_new.T).dot(y)

    return thetas

data = pd.read_csv('ex1data1.txt', names=['X', 'Y'])
x = data.iloc[:,0]
y = data.iloc[:,1]

thetas = [0, 0, 0]

print(cost(x, y, thetas))
thetas = normal_equation(x, y)
print(thetas)

x_curve = np.linspace(0,25,100)
y_curve = [np.polyval(np.flip(thetas), i) for i in x_curve]

plt.plot(x_curve, y_curve)
plt.scatter(x, y)
plt.show()