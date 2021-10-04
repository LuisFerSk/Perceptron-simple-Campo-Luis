import numpy as np

from Entrenador import *


class Neurona:
    def __init__(self, ruta_dataSet, rata_aprendizaje=1, error=0.1, numero_iteraciones=1000):
        self.error = error
        self.num_iterate = 0
        self.errores_RMS = []
        self.ruta_dataSet = ruta_dataSet
        self.rata_aprendizaje = rata_aprendizaje
        self.entrenador = Entrenador(ruta_dataSet)
        self.numero_iteraciones = numero_iteraciones

        self.salidas = self.entrenador.GetSalidas()
        self.entradas = self.entrenador.GetEntradas()
        self.umbrales = self.entrenador.GenerarUmbrales(self.salidas)
        self.pesos = self.entrenador.GenerarPesos(self.salidas, self.entradas)

    def CalcularSalidaResultante(self, entrada, pesos, umbral):
        iterador = 0
        salida_resultante = []
        for peso in pesos:
            salida_resultante.append((entrada @ peso)-umbral[iterador])
            iterador += 1
        return salida_resultante

    def FuncionSoma(self, patron, salidas):
        salida = []
        for i in range(len(salidas)):
            for j in range(len(patron)):
                salida.append(
                    (patron[j] * self.pesos[i][j]) - self.umbrales[i]
                )
        return salida

    def FuncionEscalon(self, salida_resultante):
        salida = []
        for escalon in salida_resultante:
            salida.append(1 if escalon >= 0 else 0)
        return salida

    def FuncionSigmoide(self, salida_soma):
        salida_resultante = []
        for n in range(len(salida_soma)):
            salida_resultante.append(1 / (1 + np.exp(-salida_soma[n])))
        return salida_resultante

    def FuncionLineal(self, salida_soma):
        salida_resultante = salida_soma
        return salida_resultante

    def CalcularErrorLineal(self, salidas, salida, iterador):
        return np.subtract(salidas[iterador], salida)

    def CalcularErrorPatron(self, error_lineal):
        return abs(error_lineal).sum()/len(error_lineal)

    def NuevoPeso(self, entrada, pesos, rata, error_lineal):
        for j in range(len(pesos)):
            for i in range(len(pesos[0])):
                pesos[j][i] += rata * error_lineal[j] * entrada[i]

    def NuevoUmbral(self, umbral, rata, error_lineal):
        for j in range(len(umbral)):
            umbral[j] += rata * error_lineal[j]

    def CalcularErrorRMS(self, error_patron):
        return np.abs(error_patron).sum()/len(error_patron)

    def Entrenar(self, funcion):
        self.YR = []
        contador = 0
        self.error_patron = []

        for entrada in self.entradas:
            self.salida_resultante = self.CalcularSalidaResultante(
                entrada, self.pesos, self.umbrales)

            salida_patron = np.array([self.salidas[contador]]) if len(
                self.salidas) == 1 else (self.salidas[contador, :])

            if funcion == 'Funcion Escalon':
                self.salida_funcion = self.FuncionEscalon(
                    self.salida_resultante)

            elif funcion == 'Funcion Lineal':
                self.resultado_soma = self.FuncionSoma(entrada)
                self.salida_funcion = self.FuncionLineal(self.resultado_soma)

            elif funcion == 'Funcion Sigma':
                self.resultado_soma = self.FuncionSoma(entrada)
                self.salida_funcion = self.FuncionSigmoide(self.resultado_soma)

            self.YR.append(self.salida_funcion)

            self.error_lineal = self.CalcularErrorLineal(
                self.salidas, self.salida_funcion, contador)

            self.error_patron.append(
                self.CalcularErrorPatron(self.error_lineal))

            self.NuevoPeso(entrada, self.pesos,
                           self.rata_aprendizaje, self.error_lineal)

            self.NuevoUmbral(
                self.umbrales, self.rata_aprendizaje, self.error_lineal)

            self.error_RMS = self.CalcularErrorRMS(self.error_patron)

            self.errores_RMS.append(self.error_RMS)

            print(self.error_RMS)

            self.num_iterate += 1

            contador += 1
