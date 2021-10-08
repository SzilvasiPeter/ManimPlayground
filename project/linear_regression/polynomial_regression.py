from numpy.linalg import norm
import pandas as pd
import numpy as np

# J = 1/2m * sum((h_x - y).^2)
def cost(x, y, thetas) -> float:
    h_x = thetas[0] * x + thetas[1] * x**2 + thetas[2]
    J = (1/(2*len(x))) * sum((h_x - y)**2)
    
    return J

# thetas = (X^T * X)^-1 * X^T * y
def normal_equation(x, y):
    x_new = np.array([np.ones(len(x)),x.values.flatten()]).T
    thetas = np.linalg.inv(x_new.T.dot(x_new)).dot(x_new.T).dot(y)

    return thetas

data = pd.read_csv('ex1data1.txt', names=['X', 'Y'])
x = data.iloc[:,0]
y = data.iloc[:,1]

thetas = [0, 0, 0]

print(cost(x, y, thetas))
print(normal_equation(x, y))