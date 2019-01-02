import matplotlib.pyplot as plt
# import numpy as np

def plot_data(x, y):
    # ===================== Your Code Here =====================
    # Instructions : Plot the training data into a figure using the matplotlib.pyplot
    #                using the "plt.scatter" function. Set the axis labels using
    #                "plt.xlabel" and "plt.ylabel". Assume the population and revenue data
    #                have been passed in as the x and y.

    # Hint : You can use the 'marker' parameter in the "plt.scatter" function to change the marker type (e.g. "x", "o").
    #        Furthermore, you can change the color of markers with 'c' parameter.


    # ===========================================================
    plt.scatter(x, y, color='blue')
    plt.show()


# print('Plotting Data...')
# data = np.loadtxt('ex1data1.txt', delimiter=',', usecols=(0, 1))
# X = data[:, 0]
# y = data[:, 1]
# m = y.size

# plt.ion()
# plt.figure(0)
# plot_data(X, y)