class SeguimientoPacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, nombre):
        self.pacientes.append(nombre)

    def listar_pacientes(self):
        return self.pacientes
