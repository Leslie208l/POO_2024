#10.- Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron


def contar_aprobados_y_no_aprobados():
    aprobados = 0
    no_aprobados = 0

    for i in range(1, 16):
        try:
            calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
            if calificacion >= 5.0:
                aprobados += 1
            else:
                no_aprobados += 1
        except ValueError:
            print("Por favor, ingrese una calificación válida.")

    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos no aprobados: {no_aprobados}")

contar_aprobados_y_no_aprobados()
