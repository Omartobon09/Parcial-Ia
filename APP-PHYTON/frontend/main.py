from PyQt6.QtWidgets import QApplication
from login import LoginUser
from paciente.main_paciente import PacienteApp
from medico.main_medico import MedicoApp

def on_login_success(username):
    global ventana_principal

    if username == "pac":
        ventana_principal = PacienteApp()
    elif username == "doc":
        ventana_principal = MedicoApp()
    else:
        print("Usuario no válido") 
        return

    ventana_principal.show()

if __name__ == "__main__":
    app = QApplication([])

    login = LoginUser(on_login_success)
    login.show()

    app.exec()
