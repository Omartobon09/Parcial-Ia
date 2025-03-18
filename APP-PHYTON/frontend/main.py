from PyQt6.QtWidgets import QApplication
from login import LoginUser
from paciente.main_paciente import PacienteApp
from medico.main_medico import MedicoApp

def on_login_success(username, rol_id):
    global ventana_principal

    if rol_id == 2:  # Paciente
        ventana_principal = PacienteApp()
    elif rol_id == 1:  # Médico
        ventana_principal = MedicoApp()
    else:
        print("Rol no válido")
        return

    ventana_principal.show()

if __name__ == "__main__":
    app = QApplication([])

    login = LoginUser(on_login_success)
    login.show()

    app.exec()
