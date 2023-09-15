import openpyxl
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dados_clima():

    meses             = []
    temperatura_max   = []
    temperatura_min   = []
    temperatura_media = []
    cells             = np.array([])

    book  = openpyxl.load_workbook('../Dados_climaticos_historicos.xlsx')
    sheet = book['Historico_Clima_Rio_de_Janeiro']

    for row in range(4, 8):
        for col in range(1, 14):
            char = get_column_letter(col)
            cells = np.append(cells, sheet[char + str(row)].value)

    dados = np.split(cells, 4)

    meses             = np.delete(dados[0], 0)
    temperatura_media = np.delete(dados[1], 0).astype(float)
    temperatura_min   = np.delete(dados[2], 0).astype(float)
    temperatura_max   = np.delete(dados[3], 0).astype(float)

    dicionario = {key: [value1, value2, value3] for key, value1, value2, value3 in zip(meses, temperatura_media, temperatura_min, temperatura_max)}

    plt.plot(meses, temperatura_media)
    plt.plot(meses, temperatura_min)
    plt.plot(meses, temperatura_max)

    print(temperatura_media, temperatura_min, temperatura_max)

    plt.savefig('my_plot.png')
