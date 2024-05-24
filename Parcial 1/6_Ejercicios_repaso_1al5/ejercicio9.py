#9.- Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa


def solicitar_numeros():
    print("Introduce números. Ingresa '111' para salir.")

    while True:
        try:
            numero = int(input("Ingresa un número: "))
            if numero == 111:
                print("Saliendo del programa...")
                break
        except ValueError:
            print("Por favor, ingresa solo números enteros.")

solicitar_numeros()
