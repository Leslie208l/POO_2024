import os
import math  # Import the math module for square root function

def solicitarNumeros():
    global n1, n2  
    n1 = float(input("Numero #1: "))  # Changed int to float to handle decimal division
    n2 = float(input("Numero #2: "))  # Changed int to float to handle decimal division
    return n1, n2

def operacionAritmetica(n1, n2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 == 0:
            return "No se puede dividir por cero."
        else:
            return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "POTENCIA":
        return f"{n1} ^ {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        if n1 < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return f"Raíz cuadrada de {n1} = {math.sqrt(n1)}"
    elif opcion == "7" or opcion.upper() == "SALIR":
        return "Salir"
    else:
        return "Opción no válida"

opcion = True
while opcion:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    print("\n\t..:: CALCULADORA BÁSICA ::..\n 1.- Suma \n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Potencia\n 6.- Raíz Cuadrada\n 7.- SALIR") 
    opcion = input("\tElige una opción: ").strip().upper()

    if opcion in ["1", "2", "3", "4", "5", "6"]:
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))
        input("Presiona Enter para continuar...")
    elif opcion == "7" or opcion.upper() == "SALIR":
        print("Terminaste la ejecución del programa.")
        opcion = False
    else:
        print("Opción no válida. Introduce un número del 1 al 7.")
        input("Presiona Enter para continuar...")










        import os
import math

def solicitarNumeros():
    global n1, n2  
    n1 = float(input("Numero #1: "))  
    n2 = float(input("Numero #2: ")) 
    return n1, n2

def operacionAritmetica(n1, n2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 == 0:
            return "No se puede dividir por cero."
        else:
            return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "POTENCIA":
        return f"{n1} ^ {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        if n1 < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return f"Raíz cuadrada de {n1} = {math.sqrt(n1)}"
    elif opcion == "7" or opcion.upper() == "SALIR":
        return "Salir"
    else:
        return "Opción no válida"

opcion = True
while opcion:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("\n\t..:: CALCULADORA BÁSICA ::..\n 1.- Suma \n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Potencia\n 6.- Raíz Cuadrada\n 7.- SALIR") 
    opcion = input("\tElige una opción: ").strip().upper()

    if opcion in ["1", "2", "3", "4", "5", "6"]:
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))
        input("Presiona Enter para continuar...")
    elif opcion == "7" or opcion.upper() == "SALIR":
        print("Terminaste la ejecución del programa.")
        opcion = False
    else:
        print("Opción no válida. Introduce un número del 1 al 7.")
        input("Presiona Enter para continuar...")