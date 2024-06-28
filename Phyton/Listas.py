#Una lista es una secuencia de datos ordenados, la posición importa,
#heterogénea, puede contener distintos tipos de datos y mutable
#podemos cambiar la secuencia, ya sea modificando eliminando o añadiendo elementos.
#Para crear una lista se usan corchetes

#Crear una lista llamada "numeros" que contengan los números 1, 2, y 3 (en ese orden). 
# Crea una lista llamada "cadenas" la cual contenga "hola" y "mundo" (en ese orden). 
# Intenta usar el método de "append" para agregar objetos.
numeros=[]
numeros.append(1)
numeros.append(2)
numeros.append(3)
print("Listas:",numeros)
cadenas=[]
cadenas.append("hola")
cadenas.append("mundo")
print("Listas:",cadenas)
#Entre ellos están el método "append", que nos permite agregar un elemento al final
#El método "count", que nos devuelve el número de veces que se repite un elemento
#El método "index", que nos devuelve la posición de la primera aparición de un elemento
#El método "remove" que elimina la primera aparición de un elemento.