#Los tipo de datos más comunes en python son:

# simples o primitivos
# int (entero)
# float (real)
# bool (logico)

#estructurados
# str (cadena)
# list (lista)
# tuple 
# dict (como un objeto)

#ejemplos de primitivos
entero=23
float=3.1416
logico=False

#estructurados
palabra="hola"
palabra2='@'
lista=[10,20,30,40]
lista2=[True,100,3.3,"Que tal",'9']
tuple=("Hola","que","tal")
dict={
    "nombre":"Daniel",
    "apellidos":"Hernandez Gomez",
    "edad":20,
    "estatura":1.7
}

#Mostrar el tipo de datos de cada identificador
print(type(entero))
print(type(float))
print(type(logico))
print(type(palabra))
print(type(palabra2))
print(type(list))
print(type(tuple))
print(type(dict))