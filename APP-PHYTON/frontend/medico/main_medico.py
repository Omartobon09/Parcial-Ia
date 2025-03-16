from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
)
from PyQt6.QtCore import Qt
from medico.reglas_medico import SistemaReglas
import os
from medico.seguimiento_medico import SeguimientoPacientes

class MedicoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_styles()
    
    def initUI(self):
        self.setWindowTitle("Panel del Médico")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.label_titulo = QLabel("Lista de Pacientes")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_titulo)

        self.lista_pacientes = QListWidget()
        self.cargar_pacientes()
        layout.addWidget(self.lista_pacientes)

        self.boton_seguimiento = QPushButton("Seguimiento de Pacientes")
        self.boton_seguimiento.clicked.connect(self.ver_seguimiento)
        layout.addWidget(self.boton_seguimiento)

        self.boton_reportes = QPushButton("Generar Reportes")
        self.boton_reportes.clicked.connect(self.generar_reportes)
        layout.addWidget(self.boton_reportes)

        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.close)
        layout.addWidget(self.boton_salir)

        self.setLayout(layout)

    def apply_styles(self):
        frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        style_path = os.path.join(frontend_dir, "styles.qss")

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())  
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")

    def cargar_pacientes(self):
        pacientes = ["Paciente 1", "Paciente 2", "Paciente 3"] 
        self.lista_pacientes.addItems(pacientes)

    def ver_seguimiento(self):
        self.seguimiento = SeguimientoPacientes()
        self.seguimiento.show()

    def generar_reportes(self):
        reglas = SistemaReglas()
        reglas.generar_reporte()
        print("Reporte generado exitosamente.")  
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = MedicoApp()
    ventana.show()
    sys.exit(app.exec())
