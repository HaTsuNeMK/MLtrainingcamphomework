import matplotlib.pyplot as plt
import numpy as np

def plot_data(X, y):
    plt.figure()

    # ===================== Your Code Here =====================
    # Instructions : Plot the positive and negative examples on a
    #                2D plot, using the marker="+" for the positive
    #                examples and marker="o" for the negative examples
    #

    '''
    这里借助4个列表用来储存正样本和负样本的坐标然后用plt.scatter将散点图画出来，
    X[i:, 0].tolist()[0]的意思是将第i的样本的第一列数据拿出来，即横坐标，但是直接取出来是array的格式画图不能用，
    因此这个用tolist()将值变为列表，后面[0]是因为列表中只有一个值。
    X[i:, 1]同理，只不过数据是第二列的即纵坐标
    '''
    px = []
    nx = []
    py = []
    ny = []
    for i in range(X.shape[0]):
        if y[i] == 0:
            nx.append(X[i:, 0].tolist()[0])
            ny.append(X[i:, 1].tolist()[0])
        if y[i] == 1:
            px.append(X[i:, 0].tolist()[0])
            py.append(X[i:, 0].tolist()[0])
    plt.scatter(nx, ny, marker='o')
    plt.scatter(px, py, marker='+')
    plt.show()
