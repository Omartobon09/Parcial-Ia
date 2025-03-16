import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
)

class HistorialApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_styles()

    def initUI(self):
        self.setWindowTitle("Historial del Paciente")
        self.setMinimumSize(400, 400)

        layout = QVBoxLayout()

        self.label_avances = QLabel("Descripción de avances en su estado:")
        self.input_avances = QTextEdit()
        layout.addWidget(self.label_avances)
        layout.addWidget(self.input_avances)

        self.label_sintomas = QLabel("Síntomas actuales:")
        self.input_sintomas = QTextEdit()
        layout.addWidget(self.label_sintomas)
        layout.addWidget(self.input_sintomas)

        self.label_estado = QLabel("¿Cómo se siente hoy?")
        self.input_estado = QTextEdit()
        layout.addWidget(self.label_estado)
        layout.addWidget(self.input_estado)

        self.label_preguntas = QLabel("Preguntas o inquietudes:")
        self.input_preguntas = QTextEdit()
        layout.addWidget(self.label_preguntas)
        layout.addWidget(self.input_preguntas)

        self.boton_cerrar = QPushButton("Volver")
        self.boton_cerrar.clicked.connect(self.close)
        layout.addWidget(self.boton_cerrar)
      
        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def apply_styles(self):
        frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        style_path = os.path.join(frontend_dir, "styles.qss")

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())  
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")
            
    def guardar_datos(self):
        print("Datos guardados correctamente")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = HistorialApp()
    ventana.show()
    sys.exit(app.exec())
