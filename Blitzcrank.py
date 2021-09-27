from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import numpy as np

import pandas as pd

from Neurona import *
from ViewControl import *


class View:
    def __init__(self):
        viewControl = ViewControl()

        self.root = Tk()
        self.root.title('Perceptron Simple')
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        ###################################################################

        frame_input_output = Frame(self.root)
        frame_input_output.place(
            relx=.01, rely=.01, relwidth=.33, relheight=.11)

        button_data = Button(frame_input_output, text="Cargar entrada", command=lambda:
                             viewControl.LoadData(entry_data, treeview_input_output, treeview_umbral, treeview_peso))
        button_data.place(relx=.05, rely=.01, relwidth=.25, relheight=.30)

        entry_data = Entry(frame_input_output, width=50)
        entry_data.place(relx=.35, rely=.01, relwidth=.64, relheight=.30)

        combo = Combobox(frame_input_output)
        combo['values'] = ('Funcion Escalon',
                           'Funcion Lineal', 'Funcion Sigma')
        combo.current(0)
        combo.place(relx=.35, rely=.67, relwidth=.64, relheight=.30)

        button_entrenar = Button(frame_input_output, text="Entrenar", command=lambda:
                                 viewControl.Entrenar(combo.get(), treeview_new_umbral, treeview_new_peso))
        button_entrenar.place(relx=.05, rely=.67, relwidth=.25, relheight=.30)

        ###################################################################

        frame_view_input_output = LabelFrame(
            self.root, text="Entradas y salidas")
        frame_view_input_output.place(
            relx=.01, rely=.12, relwidth=.33, relheight=.33)

        treeview_input_output = Treeview(frame_view_input_output)
        viewControl.CrearGrid(treeview_input_output, frame_view_input_output)

        ###################################################################

        frame_view_umbral = LabelFrame(self.root, text="Umbral")
        frame_view_umbral.place(
            relx=.01, rely=.47, relwidth=.16, relheight=.16)

        treeview_umbral = Treeview(frame_view_umbral)
        viewControl.CrearGrid(treeview_umbral, frame_view_umbral)

        ###################################################################

        frame_view_Peso = LabelFrame(self.root, text="Pesos")
        frame_view_Peso.place(relx=.18, rely=.47, relwidth=.16, relheight=.16)

        treeview_peso = Treeview(frame_view_Peso)
        viewControl.CrearGrid(treeview_peso, frame_view_Peso)

        ###################################################################

        frame_view_new_umbral = LabelFrame(self.root, text="Umbral final")
        frame_view_new_umbral.place(
            relx=.01, rely=.65, relwidth=.16, relheight=.16)

        treeview_new_umbral = Treeview(frame_view_new_umbral)
        viewControl.CrearGrid(treeview_new_umbral, frame_view_new_umbral)

        ###################################################################

        frame_view_new_Peso = LabelFrame(self.root, text="Pesos finales")
        frame_view_new_Peso.place(
            relx=.18, rely=.65, relwidth=.16, relheight=.16)

        treeview_new_peso = Treeview(frame_view_new_Peso)
        viewControl.CrearGrid(treeview_new_peso, frame_view_new_Peso)

        ###################################################################

        frame_grafica_simulacion = LabelFrame(
            self.root, text="Grafica")
        frame_grafica_simulacion.place(
            relx=.36, rely=.01, relwidth=.60, relheight=.80)

        ###################################################################

        self.root.mainloop()


view = View()
