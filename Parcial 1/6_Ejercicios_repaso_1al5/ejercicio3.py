#3.-  Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

numero = 1
while numero <= 60:
    cuadrado = numero ** 2
    print("El cuadrado de", numero, "es:", cuadrado)
    numero += 1
    
for numero in range(1, 61):
    cuadrado = numero ** 2
    print("El cuadrado de", numero, "es:", cuadrado)
