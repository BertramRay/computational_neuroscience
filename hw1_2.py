from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m1 = loadmat("data/Auditory Neuron/R15N111_Spikes.mat")
    m2 = loadmat("data/Auditory Neuron/R15N111_Stimulus.mat")
    unit1 = m1["unit1"]
    unit2 = m1["unit2"]
    freqs = m2["freqs"]
    levels = m2["levels"]
    sti_onset = m2["sti_onset"]
    mat1 = [[0 for col in range(21)] for row in range(9)]
    mat2 = [[0 for col in range(21)] for row in range(9)]
    u1len = unit1.shape[0]
    u2len = unit2.shape[0]
    sti_len = sti_onset.shape[0]

    for i in range(u1len):
        spike_time = unit1[i][0]
        for j in range(sti_len):
            sti_time = sti_onset[j][0]
            if (spike_time - sti_time > 0) and (spike_time - sti_time < 0.1):
                freq = freqs[j][0]
                level = levels[j][0]
                freq_idx = int((freq - 20000) / 2000)
                level_idx = int(level / 5)
                # print(level_idx, freq_idx)
                mat1[level_idx][freq_idx] += 1

    for i in range(u2len):
        spike_time = unit2[i][0]
        for j in range(sti_len):
            sti_time = sti_onset[j][0]
            if (spike_time - sti_time > 0) and (spike_time - sti_time < 0.1):
                freq = freqs[j][0]
                level = levels[j][0]
                freq_idx = int((freq - 20000) / 2000)
                level_idx = int(level / 5)
                # print(level_idx, freq_idx)
                mat2[level_idx][freq_idx] += 1

    f, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("Frequency Response Area(Unit 1)")
    ax.set_xlabel("Freq (kHz)")
    ax.set_ylabel("dB SPL")
    data1 = np.array(mat1)
    data1 = pd.DataFrame(data1, columns=np.arange(20, 62, 2), index=np.arange(0, 45, 5))
    ax = sns.heatmap(data1)
    plt.savefig("result/unit_1_result.png")

    f, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("Frequency Response Area(Unit 2)")
    ax.set_xlabel("Freq (kHz)")
    ax.set_ylabel("dB SPL")
    data2 = np.array(mat2)
    data2 = pd.DataFrame(data2, columns=np.arange(20, 62, 2), index=np.arange(0, 45, 5))
    ax = sns.heatmap(data2)
    plt.savefig("result/unit_2_result.png")