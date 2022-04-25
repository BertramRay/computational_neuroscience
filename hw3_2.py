import numpy as np
from scipy.io import loadmat

import matplotlib.pyplot as plt

if __name__ == '__main__':
    m1 = loadmat("data/hw3/c1p8.mat")
    rho = m1["rho"]
    rho = rho.squeeze()
    stim = m1["stim"]
    max_list = []
    spike_cnt = 0
    x_data = []
    # single_spike_triggered_average
    for i in range(0, 150):
        x_data.append(i * 2 - 300)
    avg = []
    for i in range(0, 150):
        avg.append(0)
    for i in range(151, 600000):
        if rho[i] == 1:
            spike_cnt += 1
            for j in range(0, 150):
                avg[j] += stim[i - (150 - j)]
    for i in range(0, 150):
        avg[i] /= spike_cnt
    f, ax = plt.subplots(figsize=(9, 6))
    ax.set_title('single_spike_triggered_average')
    ax.set_xlabel('time(ms)')
    ax.set_ylabel('velocity(degs/s)')
    plt.plot(x_data, avg)
    plt.savefig("result/hw3/single_spike_triggered_average.png")
    # multi_spike_triggered_average
    for j in range(0, 50):
        for i in range(0, 150):
            avg[i] = 0
        spike_cnt = 0
        print("now round " + str(j) + "!")
        conv_mat = [1]
        for k in range(0, j):
            conv_mat.append(0)
        conv_mat.append(1)
        tmp = np.argwhere(np.convolve(rho, conv_mat) == 2).squeeze()
        for i in range(0, tmp.shape[0]):
            idx = tmp[i]
            if idx > 150:
                spike_cnt += 1
                for k in range(0, 150):
                    avg[k] += stim[idx - (150 - k)]
        for i in range(0, 150):
            avg[i] /= spike_cnt
        maxx = max(avg)
        max_list.append(maxx[0])
        if j % 10 == 0:
            f, ax = plt.subplots(figsize=(9, 6))
            ax.set_title('multi_spike_triggered_average')
            ax.set_xlabel('time(ms)')
            ax.set_ylabel('velocity(degs/s)')
            plt.plot(x_data, avg)
            plt.savefig("result/hw3/double_spike_triggered_average(interval" + str(j * 2 + 2) + "ms).png")
    f, ax = plt.subplots(figsize=(9, 6))
    ax.set_title('interval_max curve')
    ax.set_xlabel('interval time(ms)')
    ax.set_ylabel('max velocity(degs/s)')
    x_data2 = []
    for i in range(0, 50):
        x_data2.append(2 + i * 2)
    plt.plot(x_data2, max_list)
    plt.savefig("result/hw3/interval_max_curve.png")
    print(max_list)
    print(max(max_list))
    print("hello, world")
