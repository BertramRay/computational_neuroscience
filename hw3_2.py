import numpy as np
from scipy.io import loadmat

import matplotlib.pyplot as plt

if __name__ == '__main__':
    m1 = loadmat("data/hw3/c1p8.mat")
    rho = m1["rho"]
    stim = m1["stim"]
    # list = []
    # spike_cnt = 0
    # for i in range(0, 150):
    #     list.append(0)
    # for i in range(151, 600000):
    #     if rho[i] == 1:
    #         spike_cnt += 1
    #         for j in range(0, 150):
    #             list[j] += stim[i-(150-j)]
    # for i in range(0, 150):
    #     list[i] /= spike_cnt
    #
    # x_data = []
    # for i in range(0, 150):
    #     x_data.append(i*2)
    # plt.plot(x_data, list)
    # plt.show()
    for i in range(0, 150):
        list[i] = 0
    spike_cnt = 0
    rho = rho.squeeze()
    tmp = np.argwhere(np.convolve(rho, [1, 0, 1]) == 2).squeeze()
    for i in range(0, tmp.shape[0]):
        idx = tmp[i]
        if idx >150:
            spike_cnt += 1
            for j in range(0, 150):
                list[j] += stim[idx-(150-j)]
    for i in range(0, 150):
        list[i] /= spike_cnt
    print("hello, world")
