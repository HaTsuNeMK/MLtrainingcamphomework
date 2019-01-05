import numpy as np
from sigmoid import *


def cost_function_reg(theta, X, y, lmd):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #


    # ===========================================================
    cost = (1 / m) * np.sum(-y * np.log(sigmoid(X.dot(theta))) - (1 - y) * np.log(1 - sigmoid(X.dot(theta)))) + (lmd / (2 * m)) * np.sum(theta ** 2)
    for i in range(m):
        grad[0] += (sigmoid(X[i, :].dot(theta)) - y[i]) * 1
    # grad[0] = grad[0] * (1 / m)
    for j in range(1, theta.shape[0]):
        for i in range(m):
            grad[j] = grad[j] + (sigmoid(X[i, :].dot(theta)) - y[i]) * X[i, j]
        grad[j] = grad[j] + lmd * theta[j]
    grad = grad * (1 / m)   
    return cost, grad
