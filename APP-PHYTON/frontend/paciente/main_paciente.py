from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QCheckBox, QGroupBox, QGridLayout
)
import os
from paciente.historial_paciente import HistorialApp
from paciente.seguimiento_paciente import SeguimientoApp

class PacienteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_styles()

    def initUI(self):
        self.setWindowTitle("Registro de Paciente")
        self.setMinimumSize(400, 400)

        layout = QVBoxLayout()
        
        self.label_nombre = QLabel("Nombre del paciente:")
        self.input_nombre = QLineEdit()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)

        self.group_sintomas = QGroupBox("Seleccione los síntomas:")
        grid_layout = QGridLayout()
        
        self.check_fiebre = QCheckBox("Fiebre")
        self.check_tos = QCheckBox("Tos")
        self.check_dolor_cabeza = QCheckBox("Dolor de cabeza")
        self.check_cansancio = QCheckBox("Cansancio")
        self.check_dolor_garganta = QCheckBox("Dolor de garganta")
        self.check_falta_aire = QCheckBox("Falta de aire")

        sintomas_checkboxes = [
            self.check_fiebre, self.check_tos, self.check_dolor_cabeza,
            self.check_cansancio, self.check_dolor_garganta, self.check_falta_aire
        ]
        
        for i, checkbox in enumerate(sintomas_checkboxes):
            grid_layout.addWidget(checkbox, i // 2, i % 2)

        self.group_sintomas.setLayout(grid_layout)
        layout.addWidget(self.group_sintomas)
        
        self.label_sintomas = QLabel("Describa sus síntomas:")
        self.input_sintomas = QTextEdit()
        layout.addWidget(self.label_sintomas)
        layout.addWidget(self.input_sintomas)

        self.boton_guardar = QPushButton("Guardar Historial")
        self.boton_guardar.clicked.connect(self.guardar_historial)
        layout.addWidget(self.boton_guardar)

        self.boton_historial = QPushButton("Llenar formulario")
        self.boton_historial.clicked.connect(self.abrir_historial)
        layout.addWidget(self.boton_historial)
        
        self.boton_seguimiento = QPushButton("Seguimiento")
        self.boton_seguimiento.clicked.connect(self.abrir_seguimiento)
        layout.addWidget(self.boton_seguimiento)

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

    def guardar_historial(self):
        nombre = self.input_nombre.text()
        sintomas_texto = self.input_sintomas.toPlainText()

        sintomas_seleccionados = []
        if self.check_fiebre.isChecked():
            sintomas_seleccionados.append("Fiebre")
        if self.check_tos.isChecked():
            sintomas_seleccionados.append("Tos")
        if self.check_dolor_cabeza.isChecked():
            sintomas_seleccionados.append("Dolor de cabeza")
        if self.check_cansancio.isChecked():
            sintomas_seleccionados.append("Cansancio")
        if self.check_dolor_garganta.isChecked():
            sintomas_seleccionados.append("Dolor de garganta")
        if self.check_falta_aire.isChecked():
            sintomas_seleccionados.append("Falta de aire")

        sintomas_final = ", ".join(sintomas_seleccionados)
        if sintomas_texto:
            sintomas_final += f"\nDescripción adicional: {sintomas_texto}"

        if nombre and sintomas_final:
            with open("historial.txt", "a") as file:
                file.write(f"Paciente: {nombre}\nSíntomas: {sintomas_final}\n{'-'*30}\n")
            self.input_nombre.clear()
            self.input_sintomas.clear()
            for checkbox in [self.check_fiebre, self.check_tos, self.check_dolor_cabeza, self.check_cansancio, self.check_dolor_garganta, self.check_falta_aire]:
                checkbox.setChecked(False)

    def abrir_historial(self):
        self.historial_window = HistorialApp()
        self.historial_window.show()
        
    def abrir_seguimiento(self):
        self.seguimiento_window = SeguimientoApp()
        self.seguimiento_window.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = PacienteApp()
    ventana.show()
    sys.exit(app.exec())
