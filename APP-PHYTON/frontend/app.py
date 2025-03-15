import sys
import requests
import json
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QCheckBox, QTextEdit,
                             QGroupBox, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem,
                             QMessageBox, QDateEdit)
from PyQt6.QtCore import Qt, QDate


class SistemaCirculatorioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Diagnóstico Circulatorio")
        self.setMinimumSize(800, 600)

        self.api_url = "http://localhost:8000"

        self.initUI()

    def initUI(self):

        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: #4d4262")
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        formulario_widget = QWidget()
        formulario_layout = QVBoxLayout()
        formulario_widget.setLayout(formulario_layout)

        resultados_widget = QWidget()
        resultados_layout = QVBoxLayout()
        resultados_widget.setLayout(resultados_layout)

        datos_usuario_group = QGroupBox("Datos del Usuario")
        datos_usuario_layout = QFormLayout()

        self.nombre_input = QLineEdit()
        self.identificacion_input = QLineEdit()

        datos_usuario_layout.addRow("Nombre:", self.nombre_input)
        datos_usuario_layout.addRow(
            "Identificación:", self.identificacion_input)
        datos_usuario_group.setLayout(datos_usuario_layout)

        preguntas_group = QGroupBox("Síntomas")
        preguntas_layout = QVBoxLayout()

        self.preguntas = [
            "¿Tiene dolor en el pecho?",
            "¿Presenta dificultad para respirar?",
            "¿Experimenta mareos o desmayos?",
            "¿Tiene hinchazón en las piernas?",
            "¿Siente palpitaciones o latidos irregulares?"
        ]

        self.checkboxes = []
        for pregunta in self.preguntas:
            checkbox = QCheckBox(pregunta)
            self.checkboxes.append(checkbox)
            preguntas_layout.addWidget(checkbox)

        preguntas_layout.addStretch()
        preguntas_group.setLayout(preguntas_layout)

        botones_group = QGroupBox("Acciones")
        botones_layout = QHBoxLayout()

        self.diagnosticar_btn = QPushButton("Diagnosticar")
        self.diagnosticar_btn.clicked.connect(self.diagnosticar)
        self.limpiar_btn = QPushButton("Limpiar Formulario")
        self.limpiar_btn.clicked.connect(self.limpiar_formulario)

        botones_layout.addWidget(self.diagnosticar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        botones_group.setLayout(botones_layout)

        resultado_group = QGroupBox("Resultado del Diagnóstico")
        resultado_layout = QVBoxLayout()

        self.resultado_text = QTextEdit()
        self.resultado_text.setReadOnly(True)

        resultado_layout.addWidget(self.resultado_text)
        resultado_group.setLayout(resultado_layout)

        formulario_layout.addWidget(datos_usuario_group)
        formulario_layout.addWidget(preguntas_group)
        formulario_layout.addWidget(botones_group)
        formulario_layout.addWidget(resultado_group)

        consultas_group = QGroupBox("Consultar Diagnósticos")
        consultas_layout = QVBoxLayout()

        filtros_layout = QFormLayout()

        self.id_filtro = QLineEdit()
        self.fecha_inicio = QDateEdit()
        self.fecha_inicio.setDate(QDate.currentDate().addMonths(-1))
        self.fecha_fin = QDateEdit()
        self.fecha_fin.setDate(QDate.currentDate())

        filtros_layout.addRow("Identificación:", self.id_filtro)
        filtros_layout.addRow("Fecha Inicio:", self.fecha_inicio)
        filtros_layout.addRow("Fecha Fin:", self.fecha_fin)

        filtros_botones = QHBoxLayout()

        self.buscar_btn = QPushButton("Buscar")
        self.buscar_btn.clicked.connect(self.buscar_consultas)
        self.ver_todos_btn = QPushButton("Ver Todos")
        self.ver_todos_btn.clicked.connect(self.obtener_todas_consultas)

        filtros_botones.addWidget(self.buscar_btn)
        filtros_botones.addWidget(self.ver_todos_btn)

        self.resultados_tabla = QTableWidget()
        self.resultados_tabla.setColumnCount(5)
        self.resultados_tabla.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Identificación", "Fecha", "Diagnóstico"])
        self.resultados_tabla.horizontalHeader().setStretchLastSection(True)
        self.resultados_tabla.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows)
        self.resultados_tabla.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers)
        self.resultados_tabla.cellDoubleClicked.connect(
            self.mostrar_detalle_consulta)

        self.detalle_text = QTextEdit()
        self.detalle_text.setReadOnly(True)

        consultas_layout.addLayout(filtros_layout)
        consultas_layout.addLayout(filtros_botones)
        consultas_layout.addWidget(self.resultados_tabla)
        consultas_layout.addWidget(QLabel("Detalle de Consulta:"))
        consultas_layout.addWidget(self.detalle_text)

        consultas_group.setLayout(consultas_layout)
        resultados_layout.addWidget(consultas_group)

        main_layout.addWidget(formulario_widget, 1)
        main_layout.addWidget(resultados_widget, 1)

    def validar_formulario(self):
        if not self.nombre_input.text().strip():
            QMessageBox.warning(self, "Error", "El nombre es obligatorio")
            return False

        if not self.identificacion_input.text().strip():
            QMessageBox.warning(
                self, "Error", "La identificación es obligatoria")
            return False

        if not all(c.isdigit() for c in self.identificacion_input.text().strip()):
            QMessageBox.warning(
                self, "Error", "La identificación debe contener solo números")
            return False

        if not any(checkbox.isChecked() for checkbox in self.checkboxes):
            QMessageBox.warning(
                self, "Error", "Debe seleccionar al menos un síntoma")
            return False

        return True

    def limpiar_formulario(self):
        self.nombre_input.clear()
        self.identificacion_input.clear()
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)
        self.resultado_text.clear()

    def diagnosticar(self):
        if not self.validar_formulario():
            return

        try:
            usuario_data = {
                "nombre": self.nombre_input.text().strip(),
                "identificacion": self.identificacion_input.text().strip()
            }

            response = requests.post(
                f"{self.api_url}/usuarios/", json=usuario_data)
            response.raise_for_status()
            usuario_id = response.json()["id"]

            respuestas = []
            for i, checkbox in enumerate(self.checkboxes, 1):
                respuestas.append({
                    "pregunta_id": i,
                    "respuesta": checkbox.isChecked()
                })

            diagnostico_response = requests.post(
                f"{self.api_url}/diagnosticar/", json=respuestas)
            diagnostico_response.raise_for_status()
            diagnostico = diagnostico_response.json()["diagnostico"]

            consulta_data = {
                "usuario_id": usuario_id,
                "respuestas": respuestas,
                "diagnostico": diagnostico
            }

            consulta_response = requests.post(
                f"{self.api_url}/consultas/", json=consulta_data)
            consulta_response.raise_for_status()

            self.resultado_text.setHtml(f"""
                <h3>Diagnóstico</h3>
                <p><strong>{diagnostico}</strong></p>
                <p>Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>Paciente: {usuario_data['nombre']} ({usuario_data['identificacion']})</p>
                <h4>Síntomas reportados:</h4>
            """)

            for i, checkbox in enumerate(self.checkboxes):
                if checkbox.isChecked():
                    self.resultado_text.append(f"<li>{self.preguntas[i]}</li>")

            QMessageBox.information(
                self, "Éxito", "Diagnóstico realizado y guardado correctamente")

        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Error al procesar el diagnóstico: {str(e)}")

    def obtener_todas_consultas(self):
        try:
            response = requests.get(f"{self.api_url}/consultas/todas/")
            response.raise_for_status()
            consultas = response.json()

            self.actualizar_tabla_resultados(consultas)

        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Error al obtener consultas: {str(e)}")

    def buscar_consultas(self):
        try:
            params = {}

            if self.id_filtro.text().strip():
                params["identificacion"] = self.id_filtro.text().strip()

            fecha_inicio = self.fecha_inicio.date().toString("yyyy-MM-dd")
            fecha_fin = self.fecha_fin.date().toString("yyyy-MM-dd")

            params["fecha_inicio"] = f"{fecha_inicio} 00:00:00"
            params["fecha_fin"] = f"{fecha_fin} 23:59:59"

            response = requests.post(
                f"{self.api_url}/consultas/buscar/", json=params)
            response.raise_for_status()
            consultas = response.json()

            self.actualizar_tabla_resultados(consultas)

            if not consultas:
                QMessageBox.information(
                    self, "Información", "No se encontraron consultas con esos criterios")

        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"Error al buscar consultas: {str(e)}")

    def actualizar_tabla_resultados(self, consultas):
        self.resultados_tabla.setRowCount(0)

        for consulta in consultas:
            row_position = self.resultados_tabla.rowCount()
            self.resultados_tabla.insertRow(row_position)

            self.resultados_tabla.setItem(
                row_position, 0, QTableWidgetItem(str(consulta["id"])))
            self.resultados_tabla.setItem(
                row_position, 1, QTableWidgetItem(consulta["nombre"]))
            self.resultados_tabla.setItem(
                row_position, 2, QTableWidgetItem(consulta["identificacion"]))
            fecha = datetime.strptime(
                consulta["fecha_consulta"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M")
            self.resultados_tabla.setItem(
                row_position, 3, QTableWidgetItem(fecha))

            diagnostico_corto = consulta["diagnostico"]
            if len(diagnostico_corto) > 50:
                diagnostico_corto = diagnostico_corto[:47] + "..."
            self.resultados_tabla.setItem(
                row_position, 4, QTableWidgetItem(diagnostico_corto))

            self.resultados_tabla.item(row_position, 0).setData(
                Qt.ItemDataRole.UserRole, consulta)

        self.resultados_tabla.resizeColumnsToContents()

    def mostrar_detalle_consulta(self, row, column):
        item = self.resultados_tabla.item(row, 0)
        if item is not None:
            consulta = item.data(Qt.ItemDataRole.UserRole)
            if isinstance(consulta, dict):
                detalle_html = self.generar_html_detalle(consulta)
                self.detalle_text.setHtml(detalle_html)
            else:
                print(
                    f"Error: Se esperaba un diccionario, pero se recibió: {type(consulta)}")
                self.detalle_text.setHtml(
                    "<p>Error al mostrar la consulta.</p>")

    def generar_html_detalle(self, consulta):
        return f"""
        <p><strong>ID:</strong> {consulta["id"]}</p>
        <p><strong>Usuario ID:</strong> {consulta["usuario_id"]}</p>
        <p><strong>Fecha:</strong> {consulta["fecha_consulta"]}</p>
        <p><strong>Diagnóstico:</strong> {consulta["diagnostico"]}</p>
        <p><strong>Respuestas:</strong></p>
        <ul>
            {"".join(f'<li>Pregunta: {respuesta["texto_pregunta"]}, Respuesta: {respuesta["respuesta"]}</li>' for respuesta in consulta["respuestas"])}
        </ul>
        """


class SistemaCirculatorio:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = SistemaCirculatorioApp()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    sistema = SistemaCirculatorio()
    sistema.run()
