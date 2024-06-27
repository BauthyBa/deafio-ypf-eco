import sys
import pandas as pd
from sqlalchemy import create_engine
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

engine = create_engine('mysql+pymysql://user:password@localhost/(nombre de la base de datos)') # Esta linea la tienen que completar con sus datos.

query = "SELECT * FROM (nombre de la base de datos)" #Aca tambien tienen que cambiar el nombre de la base de datos.
df = pd.read_sql(query, engine)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizacion de Datos con PyQt")

        self.layout = QVBoxLayout()

        self.boton_graficar = QPushButton("Mostrar Gráficos")
        self.boton_graficar.clicked.connect(self.mostrar_graficos)
        self.layout.addWidget(self.boton_graficar)

        self.canvas = FigureCanvas(plt.figure())
        self.layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def mostrar_graficos(self):
        self.canvas.figure.clear()

        # Grafico de barras
        ax1 = self.canvas.figure.add_subplot(211)
        sns.barplot(x='velocidad', y='voltaje', data=df, ax=ax1)
        ax1.set_title('Ejemplo de grafico de barras')
                                                                        #En esatas dos formas de graficar cambien los datos segun su BD.
        # Grafico de lineas
        ax2 = self.canvas.figure.add_subplot(212)
        sns.lineplot(x='tiempo', y='fecha', data=df, marker='o', ax=ax2)
        ax2.set_title('Ejemplo de grafico de linea')

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
