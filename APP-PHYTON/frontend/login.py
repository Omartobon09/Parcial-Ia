import os
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, 
    QMessageBox, QSpacerItem, QSizePolicy
)

class LoginUser(QWidget):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.setWindowTitle("Login")
        self.setMinimumSize(400, 300) 

        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        main_layout = QVBoxLayout() 
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        form_layout = QFormLayout()
        form_layout.setSpacing(10) 

        self.user_label = QLabel("Usuario:")
        self.user_input = QLineEdit()
        form_layout.addRow(self.user_label, self.user_input)

        self.pass_label = QLabel("Contraseña:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addRow(self.pass_label, self.pass_input)

        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.validate_login)
        form_layout.addRow(self.login_button)

        main_layout.addLayout(form_layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(main_layout)

    def apply_styles(self):
        style_path = os.path.join(os.path.dirname(__file__), "styles.qss") 

        try:
            with open(style_path, "r") as file:
                self.setStyleSheet(file.read()) 
        except Exception as e:
            print(f"Error al cargar los estilos: {e}")

    def validate_login(self):
        usuario = self.user_input.text()
        contraseña = self.pass_input.text()

        if (usuario == "pac" and contraseña == "1234") or (usuario == "doc" and contraseña == "1234"):
            self.on_login_success(usuario)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
