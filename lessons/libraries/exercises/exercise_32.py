import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def splitter():
    img = sp.datasets.face()  # Sample image
    img = img.copy()
    # img.setflags(write=1)
    array = np.empty(np.shape(img))
    data = np.asarray(img)
    data[:, :, 1] = 0
    data[:, :, 2] = 0
    np.append(array, data)
    data = np.asarray(img)
    data[:, :, 0] = 0
    data[:, :, 2] = 0
    np.append(array, data)
    data = np.asarray(img)
    data[:, :, 0] = 0
    data[:, :, 1] = 0
    np.append(array, data)
    # temp = np.asarray(data)
    # temp[:, :, 0] *= 0
    # temp[:, :, 2] *= 0
    # np.append(array, temp)
    # temp = np.asarray(data)
    # temp[:, :, 0] *= 0
    # temp[:, :, 1] *= 0
    # np.append(array, temp)
    # print(data)
    # for i in data:
    #    for j in i:
    #        np.append(array[i], [j[0], 0, 0])
    #        np.append(array[i], [0, j[0], 0])
    #        np.append(array[i], [0, 0, j[0]])
    #

    return array


splitter()
