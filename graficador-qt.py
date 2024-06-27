import sys
import pandas as pd
from sqlalchemy import create_engine
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

# Conexión a la base de datos MySQL
engine = create_engine('mysql+pymysql://root:Bautista?2006@localhost/ejemplo_db')

# Consulta de datos
query = "SELECT * FROM ventas"
df = pd.read_sql(query, engine)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualización de Datos con PyQt")

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

        # Gráfico de barras
        ax1 = self.canvas.figure.add_subplot(211)
        sns.barplot(x='producto', y='cantidad', data=df, ax=ax1)
        ax1.set_title('Cantidad de Productos Vendidos')

        # Gráfico de líneas
        ax2 = self.canvas.figure.add_subplot(212)
        sns.lineplot(x='fecha', y='precio', data=df, marker='o', ax=ax2)
        ax2.set_title('Precio de Ventas por Fecha')

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
