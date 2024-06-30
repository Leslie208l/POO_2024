class Lectores:
    def __init__(self, nombre: str, direccion: str, telefono: int):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def reserva(self, item: str):
        print(f"{self.nombre} ha reservado {item}.")

    def entregar(self, item: str):
        print(f"{self.nombre} ha entregado {item}.")

class Estudiantes(Lectores):
    def __init__(self, nombre: str, direccion: str, telefono: int, carrera: str, matricula: int):
        super().__init__(nombre, direccion, telefono)
        self.carrera = carrera
        self.matricula = matricula

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Estudiante con matrícula {self.matricula} ha reservado {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Estudiante con matrícula {self.matricula} ha entregado {item}.")

class Docentes(Lectores):
    def __init__(self, nombre: str, direccion: str, telefono: int, modalidad: str, num_empleado: int):
        super().__init__(nombre, direccion, telefono)
        self.modalidad = modalidad
        self.num_empleado = num_empleado

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Docente con número de empleado {self.num_empleado} ha reservado {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Docente con número de empleado {self.num_empleado} ha entregado {item}.")
