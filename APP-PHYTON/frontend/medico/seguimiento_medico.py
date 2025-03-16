from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import os

class SeguimientoPacientes(QWidget):  
    def __init__(self):
        super().__init__()
        self.initUI()
        self.apply_styles()

    def initUI(self):
        self.setWindowTitle("Seguimiento de Pacientes")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("Aquí va el seguimiento de pacientes")
        layout.addWidget(label)

        self.setLayout(layout)

    def apply_styles(self):
        frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        style_path = os.path.join(frontend_dir, "styles.qss")

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read())  
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = SeguimientoPacientes()
    ventana.show()
    sys.exit(app.exec())
