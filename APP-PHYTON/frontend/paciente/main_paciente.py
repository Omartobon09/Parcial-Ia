from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QCheckBox, QGroupBox, QGridLayout, QMessageBox
)
import requests
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

        self.label_sintomas = QLabel("Describa sus síntomas:")
        self.input_sintomas = QTextEdit()
        layout.addWidget(self.label_sintomas)
        layout.addWidget(self.input_sintomas)

        self.group_sintomas = QGroupBox("Seleccione los síntomas:")
        grid_layout = QGridLayout()

        self.check_fiebre = QCheckBox("Fiebre")
        self.check_tos = QCheckBox("Tos")
        self.check_dolor_cabeza = QCheckBox("Dolor de cabeza")
        self.check_cansancio = QCheckBox("Cansancio")
        self.check_dolor_garganta = QCheckBox("Dolor de garganta")
        self.check_falta_aire = QCheckBox("Falta de aire")
        self.check_dolor_muscular = QCheckBox("Dolor muscular")
        self.check_nauseas = QCheckBox("Náuseas")
        self.check_perdida_olfato = QCheckBox("Pérdida del olfato")
        self.check_perdida_gusto = QCheckBox("Pérdida del gusto")
        self.check_congestion_nasal = QCheckBox("Congestión nasal")
        self.check_diarrhea = QCheckBox("Diarrea")
        self.check_dolor_pecho = QCheckBox("Dolor en el pecho")
        self.check_palpitaciones = QCheckBox("Palpitaciones")
        self.check_mareos = QCheckBox("Mareos")
        self.check_hinchazon_piernas = QCheckBox("Hinchazón de piernas")
        self.check_dificultad_respiratoria = QCheckBox(
            "Dificultad respiratoria")

        self.sintomas_checkboxes = [
            self.check_fiebre, self.check_tos, self.check_dolor_cabeza,
            self.check_cansancio, self.check_dolor_garganta, self.check_falta_aire,
            self.check_dolor_muscular, self.check_nauseas, self.check_perdida_olfato,
            self.check_perdida_gusto, self.check_congestion_nasal, self.check_diarrhea,
            self.check_dolor_pecho, self.check_palpitaciones, self.check_mareos,
            self.check_hinchazon_piernas, self.check_dificultad_respiratoria
        ]

        for i, checkbox in enumerate(self.sintomas_checkboxes):
            grid_layout.addWidget(checkbox, i // 2, i % 2)

        self.group_sintomas.setLayout(grid_layout)
        layout.addWidget(self.group_sintomas)

        self.boton_guardar = QPushButton("Generar Diagnóstico")
        self.boton_guardar.clicked.connect(self.generar_diagnostico)
        layout.addWidget(self.boton_guardar)

        self.boton_seguimiento = QPushButton("Seguimiento")
        self.boton_seguimiento.clicked.connect(self.abrir_seguimiento)
        layout.addWidget(self.boton_seguimiento)

        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.close)
        layout.addWidget(self.boton_salir)

        self.setLayout(layout)

    def apply_styles(self):
        frontend_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), ".."))
        style_path = os.path.join(frontend_dir, "styles.qss")

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")

    def generar_diagnostico(self):
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
        if self.check_dolor_muscular.isChecked():
            sintomas_seleccionados.append("Dolor muscular")
        if self.check_nauseas.isChecked():
            sintomas_seleccionados.append("Náuseas")
        if self.check_perdida_olfato.isChecked():
            sintomas_seleccionados.append("Pérdida del olfato")
        if self.check_perdida_gusto.isChecked():
            sintomas_seleccionados.append("Pérdida del gusto")
        if self.check_congestion_nasal.isChecked():
            sintomas_seleccionados.append("Congestión nasal")
        if self.check_diarrhea.isChecked():
            sintomas_seleccionados.append("Diarrea")
        if self.check_dolor_pecho.isChecked():
            sintomas_seleccionados.append("Dolor en el pecho")
        if self.check_palpitaciones.isChecked():
            sintomas_seleccionados.append("Palpitaciones")
        if self.check_mareos.isChecked():
            sintomas_seleccionados.append("Mareos")
        if self.check_hinchazon_piernas.isChecked():
            sintomas_seleccionados.append("Hinchazón de piernas")
        if self.check_dificultad_respiratoria.isChecked():
            sintomas_seleccionados.append("Dificultad respiratoria")

        if not sintomas_seleccionados:
            QMessageBox.warning(
                self, "Error", "Por favor, seleccione al menos un síntoma.")
            return

        sintomas_final = ", ".join(sintomas_seleccionados)
        if sintomas_texto:
            sintomas_final += f"\nDescripción adicional: {sintomas_texto}"

        diagnostico, recomendacion = self.realizar_diagnostico(
            sintomas_seleccionados)

        QMessageBox.information(
            self, "Diagnóstico", f"Diagnóstico: {diagnostico}\nRecomendación: {recomendacion}")

        self.enviar_diagnostico_api(sintomas_final, recomendacion)

        self.input_sintomas.clear()
        for checkbox in self.sintomas_checkboxes:
            checkbox.setChecked(False)

    def realizar_diagnostico(self, sintomas):
        # Aquí puedes definir las reglas para el diagnóstico
        if "Fiebre" in sintomas and "Tos" in sintomas and "Falta de aire" in sintomas:
            return "Posible COVID-19", "Consulte a un médico y realice una prueba de COVID-19"
        elif "Dolor de cabeza" in sintomas and "Cansancio" in sintomas and "Dolor muscular" in sintomas:
            return "Gripe", "Descanse, manténgase hidratado y tome medicamentos para el dolor según sea necesario"
        elif "Dolor de garganta" in sintomas and "Fiebre" in sintomas and "Dolor de cabeza" in sintomas:
            return "Infección de garganta", "Consulte a un médico y tome antibióticos si es necesario"
        elif "Náuseas" in sintomas and "Diarrea" in sintomas:
            return "Gastroenteritis", "Manténgase hidratado, evite alimentos sólidos y consulte a un médico si los síntomas persisten"
        elif "Pérdida del olfato" in sintomas and "Pérdida del gusto" in sintomas and "Congestión nasal" in sintomas:
            return "Resfriado común", "Descanse, manténgase hidratado y use descongestionantes si es necesario"
        elif "Dolor en el pecho" in sintomas and "Palpitaciones" in sintomas and "Mareos" in sintomas:
            return "Posible problema cardíaco", "Consulte a un cardiólogo lo antes posible"
        elif "Hinchazón de piernas" in sintomas and "Dificultad respiratoria" in sintomas:
            return "Posible insuficiencia cardíaca", "Consulte a un cardiólogo inmediatamente"
        else:
            return "Síntomas no concluyentes", "Consulte a un médico para un diagnóstico preciso"

    def enviar_diagnostico_api(self, descripcion, recomendacion):
        url = "http://localhost:5000/enviardiagnostico"
        data = {
            "descripcion": descripcion,
            "recomendacion": recomendacion
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print("Diagnóstico enviado correctamente")
            else:
                print(f"Error al enviar diagnóstico: {response.status_code}")
        except Exception as e:
            print(f"Error al enviar diagnóstico: {e}")

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
