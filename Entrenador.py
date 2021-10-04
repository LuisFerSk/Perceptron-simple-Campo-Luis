import numpy as np
import pandas as pd


class Entrenador:
    def __init__(self, data='Data/prueba.csv'):
        self.dataSet = pd.read_csv(data)

    def GetEntradas(self):
        df = pd.DataFrame()
        for index in self.dataSet.columns:
            if ('x' in index) or ('X' in index):
                df[index] = self.dataSet[index]
        return df.to_numpy()

    def GetSalidas(self):
        df = pd.DataFrame()
        for index in self.dataSet.columns:
            if ('y' in index) or ('Y' in index):
                df[index] = self.dataSet[index]
        return df.to_numpy()

    def GenerarPesos(self, salidas, entradas):

        return np.random.uniform(-1, 1, [len(salidas[0]), len(entradas[0])])

    def GenerarUmbrales(self, salidas):
        return np.random.uniform(-1, 1, [1, len(salidas[0])])
