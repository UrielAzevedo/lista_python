import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def asc():

    data_raw = np.loadtxt('../dados_rj.txt', dtype=float)
    data = [list(a) for a in zip(data_raw[0], data_raw[1], data_raw[2])]

    indices = np.argsort(data[:, 0])
    print(data[indices])

    reshaped_data = data.reshape(3, 12)
    print(reshaped_data)

    transposed_data = data.transpose()
    print(transposed_data)

    concatenated_data = np.concatenate((data, data), axis=0)
    print(concatenated_data)

    split_data = np.split(data, 3)
    for chunk in split_data:
        print(chunk)

    flipped_data = np.flip(data, axis=0)
    print(flipped_data)

    row_to_insert = np.zeros(data.shape[1])
    inserted_data = np.insert(data, 2, row_to_insert, axis=0)
    print(inserted_data)

    row_to_append = np.ones(data.shape[1])
    appended_data = np.append(data, [row_to_append], axis=0)
    print(appended_data)

    deleted_data = np.delete(data, 4, axis=0)
    print(deleted_data)
