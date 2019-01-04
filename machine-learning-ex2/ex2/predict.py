import numpy as np
from sigmoid import *


def predict(theta, X):
    m = X.shape[0]

    # Return the following variable correctly
    p = np.zeros(m)

    # ===================== Your Code Here =====================
    # Instructions : Complete the following code to make predictions using
    #                your learned logistic regression parameters.
    #                You should set p to a 1D-array of 0's and 1's
    #


    # ===========================================================
    '''
    p值用sigmoid全部算出来后遍历所有值，将>=0.5的值赋为1，<0.5的则赋为0
    '''
    p = sigmoid(X.dot(theta))
    for i in range(m):
        if p[i] >= 0.5:
            p[i] = 1
        else:
            p[i] = 0
    return p


# test = np.array([
#     [1],
#     [0.1],
#     [0.2],
#     [0.8]
# ])

# for i in range(test.shape[0]):
#     if test[i] >= 0.5:
#         test[i] = 1
#     else:
#         test[i] = 0

# print(test)
