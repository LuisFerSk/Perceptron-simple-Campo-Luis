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

        button_data = Button(frame_input_output, text="Cargar entradas", command=lambda:
                             viewControl.LoadData(entry_data, treeview_input_output))
        button_data.place(relx=.05, rely=.01, relwidth=.25, relheight=.30)

        entry_data = Entry(frame_input_output, width=50)
        entry_data.place(relx=.35, rely=.01, relwidth=.64, relheight=.30)

        ###################################################################

        frame_parametros = Frame(self.root)
        frame_parametros.place(
            relx=.01, rely=.12, relwidth=.33, relheight=.33)

        ###################################################################

        label_error_min = Label(
            frame_parametros, text="Error minimo")
        label_error_min.place(relx=.05, rely=.02, relwidth=.25, relheight=.10)

        entry_error_min = Entry(frame_parametros, width=50)
        entry_error_min.place(relx=.35, rely=.02, relwidth=.64, relheight=.10)

        ###################################################################
        label_rata = Label(
            frame_parametros, text="Rata de aprendizaje")
        label_rata.place(relx=.05, rely=.15, relwidth=.25, relheight=.10)

        entry_rata = Entry(frame_parametros, width=50)
        entry_rata.place(relx=.35, rely=.15, relwidth=.64, relheight=.10)

        ###################################################################
        label_iteraciones = Label(
            frame_parametros, text="Numero de iteraciones minimas")
        label_iteraciones.place(
            relx=.05, rely=.28, relwidth=.25, relheight=.10)

        entry_iteraciones = Entry(frame_parametros, width=50)
        entry_iteraciones.place(
            relx=.35, rely=.28, relwidth=.64, relheight=.10)

        ###################################################################

        label_funcion = Label(
            frame_parametros, text="Funcion")
        label_funcion.place(relx=.05, rely=.41, relwidth=.25, relheight=.10)

        combo = Combobox(frame_parametros)
        combo['values'] = ('Funcion Escalon',
                           'Funcion Lineal', 'Funcion Sigma')
        combo.current(0)
        combo.place(relx=.35, rely=.41, relwidth=.64, relheight=.10)

        ###################################################################

        button_entrenar = Button(frame_parametros, text="Entrenar", command=lambda:
                                 viewControl.Entrenar(combo.get()))
        button_entrenar.place(relx=.05, rely=.67, relwidth=.95, relheight=.15)

        button_entrenar = Button(frame_parametros, text="Simular", command=lambda:
                                 viewControl.Entrenar(combo.get()))
        button_entrenar.place(relx=.05, rely=.85, relwidth=.95, relheight=.15)

        ###################################################################

        frame_view_input_output = LabelFrame(
            self.root, text="Entradas y salidas")
        frame_view_input_output.place(
            relx=.01, rely=.47, relwidth=.33, relheight=.33)

        treeview_input_output = Treeview(frame_view_input_output)
        viewControl.CrearGrid(treeview_input_output, frame_view_input_output)

        ###################################################################

        frame_grafica_entrenamiento = LabelFrame(
            self.root, text="Grafica Salida esperada vs Salida resultante")
        frame_grafica_entrenamiento.place(
            relx=.36, rely=.01, relwidth=.60, relheight=.40)

        ###################################################################

        frame_grafica_simulacion = LabelFrame(
            self.root, text="Grafica simulación")
        frame_grafica_simulacion.place(
            relx=.36, rely=.45, relwidth=.60, relheight=.40)

        ###################################################################

        self.root.mainloop()


view = View()
