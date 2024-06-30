from clases import *

# Ejemplos de objetos
estudiante1 = Estudiantes("Leslie joselin sosa villa", "Col.centro 1500 ote", 618123456, "TI", 2335678)
docente1 = Docentes("Dagoberto", "Fracc.D.Arrieta 1400 nte", 6183335678, "TI", 123)

# Mostrar la información de los objetos usando las propiedades
print(f"Nombre del estudiante: {estudiante1.nombre}, Carrera: {estudiante1.carrera}, Matrícula: {estudiante1.matricula}")
print(f"Nombre del docente: {docente1.nombre}, Modalidad: {docente1.modalidad}, Número de Empleado: {docente1.num_empleado}")

# Llamar a los métodos
estudiante1.reserva("Libro de Matemáticas")
estudiante1.entregar("Libro de Matemáticas")

docente1.reserva("Proyector")
docente1.entregar("Proyector")
