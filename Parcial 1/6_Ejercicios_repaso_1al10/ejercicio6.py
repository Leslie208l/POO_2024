#Mostrar todas las tablas del 1 al 10 mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


def mostrar_tablas():
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()

mostrar_tablas()
