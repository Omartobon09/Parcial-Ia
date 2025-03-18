import requests
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QCheckBox, QFormLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class LoginUser(QWidget):
    loginSuccess = pyqtSignal(str, int)  

    def __init__(self, on_login_success_callback):
        super().__init__()

        self.on_login_success = on_login_success_callback

        
        self.setWindowTitle("Inicio de Sesión")
        self.setMinimumSize(400, 450)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        
        logo_label = QLabel("SISTEMA MÉDICO")
        logo_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(logo_label)

        
        login_group = QGroupBox("Credenciales")
        login_layout = QFormLayout()
        login_group.setLayout(login_layout)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_layout.addRow(QLabel("Usuario:"), self.username_input)
        login_layout.addRow(QLabel("Contraseña:"), self.password_input)

        self.remember_checkbox = QCheckBox("Recordar credenciales")
        login_layout.addRow("", self.remember_checkbox)

        main_layout.addWidget(login_group)

        
        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.error_label)

        
        self.login_button = QPushButton("INICIAR SESIÓN")
        self.login_button.clicked.connect(self.validate_login)
        main_layout.addWidget(self.login_button)

        self.username_input.returnPressed.connect(self.validate_login)
        self.password_input.returnPressed.connect(self.validate_login)

    def validate_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            self.error_label.setText("Ingrese usuario y contraseña")
            return

    
        api_url = "http://localhost:5000/api/auth/login"
        data = {"usuario": username, "contrasena": password}

        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                result = response.json()
                user_data = result.get("user", {})  
                user_role = user_data.get("rol_id") 

                if user_role is not None:
                    self.error_label.setText("")
                    self.hide()
                    self.on_login_success(username, user_role)
                else:
                    self.error_label.setText("Error obteniendo rol del usuario")
            else:
                self.error_label.setText("Usuario o contraseña incorrectos")
        except requests.exceptions.RequestException:
            self.error_label.setText("Error de conexión con el servidor")
