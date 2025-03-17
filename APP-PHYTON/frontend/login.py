from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QGroupBox, QCheckBox,
                             QFormLayout, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont


class LoginUser(QWidget):
    loginSuccess = pyqtSignal(str)

    def __init__(self, on_login_success_callback):
        super().__init__()

        # Guardar el callback
        self.on_login_success = on_login_success_callback

        # Configurar la ventana
        self.setWindowTitle("Inicio de Sesión")
        self.setMinimumSize(400, 450)
        self.setObjectName("loginForm")

        # Cargar archivo de estilos
        with open("styles.qss", "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

        # Inicializar UI
        self.setup_ui()

    def setup_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(main_layout)

        # Logo (placeholder - reemplazar con tu logo)
        logo_layout = QHBoxLayout()
        logo_label = QLabel()
        # Si tienes un logo:
        # logo_pixmap = QPixmap("path/to/logo.png").scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        # logo_label.setPixmap(logo_pixmap)
        logo_label.setText("SISTEMA MÉDICO")
        logo_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_layout.addWidget(logo_label)
        main_layout.addLayout(logo_layout)

        # Espaciador
        main_layout.addSpacerItem(QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Grupo de inicio de sesión
        login_group = QGroupBox("Credenciales")
        login_layout = QFormLayout()
        login_group.setLayout(login_layout)

        # Campos de usuario y contraseña
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Agregar campos al formulario
        login_layout.addRow(QLabel("Usuario:"), self.username_input)
        login_layout.addRow(QLabel("Contraseña:"), self.password_input)

        # Agregar "Recordarme" checkbox
        self.remember_checkbox = QCheckBox("Recordar credenciales")
        login_layout.addRow("", self.remember_checkbox)

        main_layout.addWidget(login_group)

        # Mensaje de error
        self.error_label = QLabel("")
        self.error_label.setObjectName("errorLabel")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.error_label)

        # Botones
        button_layout = QHBoxLayout()

        # Botón de login
        self.login_button = QPushButton("INICIAR SESIÓN")
        self.login_button.setObjectName("loginButton")
        self.login_button.clicked.connect(self.validate_login)
        button_layout.addWidget(self.login_button)

        main_layout.addLayout(button_layout)

        # Conectar evento Enter para iniciar sesión
        self.username_input.returnPressed.connect(self.validate_login)
        self.password_input.returnPressed.connect(self.validate_login)

    def validate_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificar credenciales (esto es solo un ejemplo)
        valid_credentials = {
            "pac": "123",
            "doc": "123"
        }

        if username in valid_credentials and password == valid_credentials[username]:
            self.error_label.setText("")
            self.hide()
            self.on_login_success(username)
        else:
            self.error_label.setText("Usuario o contraseña incorrectos")
