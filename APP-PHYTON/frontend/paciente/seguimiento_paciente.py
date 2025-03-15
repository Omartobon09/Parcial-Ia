import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
)

class SeguimientoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_styles()
        self.cargar_historial()

    def initUI(self):
        self.setWindowTitle("Seguimiento del Paciente")
        self.setMinimumSize(500, 400)

        layout = QVBoxLayout()

        self.label_historial = QLabel("Historial del Paciente:")
        layout.addWidget(self.label_historial)

        self.texto_historial = QTextEdit()
        self.texto_historial.setReadOnly(True) 
        layout.addWidget(self.texto_historial)

        self.boton_cerrar = QPushButton("Cerrar")
        self.boton_cerrar.clicked.connect(self.close)
        layout.addWidget(self.boton_cerrar)

        self.setLayout(layout)

    def apply_styles(self):
        frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        style_path = os.path.join(frontend_dir, "styles.qss")

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())  
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")

    def cargar_historial(self):
        try:
            with open("historial.txt", "r") as file:
                historial_texto = file.read()
                if historial_texto.strip():
                    self.texto_historial.setPlainText(historial_texto)
                else:
                    self.texto_historial.setPlainText("No hay registros en el historial.")
        except FileNotFoundError:
            self.texto_historial.setPlainText("No se encontró el archivo de historial.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = SeguimientoApp()
    ventana.show()
    sys.exit(app.exec())
