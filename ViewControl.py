from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import numpy as np

import pandas as pd

from Neurona import *


class ViewControl:
    def ViewUmbrales(self, treevire):
        matriz = []
        for j in range(len(self.neurona.umbrales)):
            matriz.append(self.neurona.umbrales[j])
        self.LlenarTabla(treevire, pd.DataFrame(matriz))

    def LlenarTabla(self, treeview, dataframe):
        treeview.delete(*treeview.get_children())
        treeview["column"] = list(dataframe.columns)
        treeview["show"] = "headings"

        for column in treeview["columns"]:
            treeview.column(column=column, minwidth=0,
                            width=100, anchor="center")
            treeview.heading(column, text=column)

        for row in dataframe.to_numpy().tolist():
            treeview.insert("", "end", values=row)

    def ViewPesos(self, treeview):
        matriz = []
        for j in range(len(self.neurona.pesos)):
            matriz.append(self.neurona.pesos[j])

        self.LlenarTabla(treeview, pd.DataFrame(matriz))

    def reload(self, file_entrada, treeview_umbral, treeview_peso):
        self.ViewPesos(treeview_peso)
        self.ViewUmbrales(treeview_umbral)
        self.neurona = Neurona(file_entrada)

    def LoadData(self, entry, treeview_input_output, treeview_umbral, treeview_peso):
        file_entrada = filedialog.askopenfilename()
        entry.insert(0, file_entrada)

        self.neurona = Neurona(file_entrada)
        self.LlenarTabla(treeview_input_output,
                         self.neurona.entrenador.dataSet)
        self.ViewUmbrales(treeview_umbral)
        self.ViewPesos(treeview_peso)

        return file_entrada

    def CrearGrid(self, treeview, frame):
        treeview.place(relheight=1, relwidth=1)
        treescrolly = Scrollbar(
            frame, orient="vertical", command=treeview.yview)
        treescrollx = Scrollbar(
            frame, orient="horizontal", command=treeview.xview)
        treeview.configure(xscrollcommand=treescrollx.set,
                           yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

    def GraficarDouPoint(self, frame, data_1, data_2):
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(data_1, 'o', data_2, '*')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relwidth=1, relheight=1)

    def Entrenar(self, funcion, treeview_umbral, treeview_peso):
        iterador = 0
        while True:
            error_patron = []
            contador = 0
            self.neurona.Entrenar(funcion)
            iterador += 1
            if ((iterador > self.neurona.numero_iteraciones - 1) or (self.neurona.error_RMS <= self.neurona.error)):
                break

        self.ViewUmbrales(treeview_umbral)
        self.ViewPesos(treeview_peso)

        if (self.neurona.error_RMS <= self.neurona.error):
            np.savetxt('LF/Data/pesos', self.neurona.pesos, delimiter=' ')
            np.savetxt('LF/Data/umbral', self.neurona.umbral, delimiter=' ')
