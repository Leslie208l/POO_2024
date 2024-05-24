# 5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

# Solicitar al usuario que ingrese los dos números
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Verificar cuál número es mayor para establecer el rango adecuado
if inicio < fin:
    # Mostrar los números en orden ascendente
    print("Números entre", inicio, "y", fin, "en orden ascendente:")
    for numero in range(inicio + 1, fin):
        print(numero, end=" ")
elif inicio > fin:
    # Mostrar los números en orden descendente
    print("Números entre", inicio, "y", fin, "en orden descendente:")
    for numero in range(inicio - 1, fin, -1):
        print(numero, end=" ")
else:
    print("Los números son iguales, no hay números entre ellos.")
