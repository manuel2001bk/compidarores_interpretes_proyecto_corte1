from ventana_ui import *

import re
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ingreso_texto
        self.botton_ingresar.clicked.connect(self.actualizar)
        self.palabras = []
        self.data_tabla = []

    def fragmentar_lineas(self):
        manup = self.palabras.copy()
        self.palabras.clear()
        for i in manup:
            aux = i.split(" ")
            print(aux)
            for y in aux:
                self.palabras.append(y)

    def fragmentar_texto_lineas(self, manup):
        manup = manup.split("\n")
        for i in manup:
            print(i)
            aux = i.split("\t")
            if len(aux) == 1:
                self.palabras.append(aux[0])
            else:
                self.palabras.append(aux[1])
        self.fragmentar_lineas()
        print(self.palabras)

    def evaluar_palabras(self):
        for i in self.palabras:
            print(i)
            if i == "<":
                self.data_tabla.append([i, "Valido", "Delimitador"])
            elif i == "get_Data":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == ":":
                self.data_tabla.append([i, "Valido", "Delimitador"])
            elif i == "cpu":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == "ram":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == "disc":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == "battery":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == "gpu":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == "red":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == ",":
                self.data_tabla.append([i, "Valido", "Delimitador"])
            elif i == "fin":
                self.data_tabla.append([i, "Valido", "Palabra Reservada"])
            elif i == ">":
                self.data_tabla.append([i, "Valido", "Delimitador"])
            else:
                patron = re.compile('[0-9]+.[0-9]')
                if patron.match(i) != None:
                    self.data_tabla.append([i, "Valido", "Flotantes"])
                else:
                    self.data_tabla.append([i, "Invalido", "No pertenece"])

    def generar_tabla(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 1)
        column_labels = ["Palabra", "Estado", "Token"]
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=self.data_tabla, colLabels=column_labels,
                 rowLoc='center', loc="center", colColours=["yellow"] * 3,
                 )

        plt.show()

    def actualizar(self):
        print("Acabas de hacer click en el boton.")
        manup = self.ingreso_texto.toPlainText()
        self.fragmentar_texto_lineas(manup)
        self.evaluar_palabras()
        print(self.data_tabla)
        self.generar_tabla()
        self.palabras = []
        self.data_tabla = []


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
